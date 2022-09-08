from graphql_auth.schema import UserQuery,MeQuery
import graphene
import graphql_jwt
from graphene_django import DjangoObjectType
from postCreate.models import Book,Category
from graphql_auth import mutations

  
class BookType(DjangoObjectType):
    class Meta: 
        model = Book
        fields = (
            'id',
            'title',
            'author',
            'isbn',
            'pages', 
            'price',
            'quantity', 
            'description',
            'status',
            'date_created',
        )  
        
class CategoryType(DjangoObjectType):
    class Meta: 
        model = Category
        fields = ('id','name')  


class Query(UserQuery,MeQuery,graphene.ObjectType):
    books = graphene.Field(BookType,id=graphene.Int())
    category = graphene.List(CategoryType)

    # @graphene.resolve_only_args
    def resolve_books(root,info,id):
        return Book.objects.get(pk=id)
    
    def resolve_category(root,info):
        return Category.objects.all()
    
########## CRUD ############
#-------------- create start------------------- #
class CategoryMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info,name):
        category=Category(name=name)
        category.save()
        return CategoryMutation(category=category)
#------------- create end --------------------#

#---------- update start-------------- #
# class UpdateCategory(graphene.Mutation):
#     class Arguments:
#         id=graphene.ID()
#         name = graphene.String(required=True)

#     category = graphene.Field(CategoryType)

#     @classmethod
#     def mutate(cls, root, info,name,id):
#         category=Category.objects.get(id=id)
#         category.name = name
#         category.save()
#         return UpdateCategory(category=category)
#--------------- update end----------------- #

#--------------- delete start------------------ #
# class DeleteCategory(graphene.Mutation):
#     class Arguments:
#         id = graphene.ID()

#     category = graphene.Field(CategoryType)

#     @classmethod
#     def mutate(cls, root, info,id):
#         category=Category(id=id)
#         category.delete()
#         return DeleteCategory(category=category)
#------------------ delete start -------------------#

# class Mutation(graphene.ObjectType):
#     update_category = CategoryMutation.Field()    #for create
    # update_category = DeleteCategory.Field()     #for delete
    # update_category = UpdateCategory.Field()     #for delete

    # no need 
    # token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    # verify_token = graphql_jwt.Verify.Field()
    # refresh_token = graphql_jwt.Refresh.Field()
############# CRUD #############

class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    resend_activation_email = mutations.ResendActivationEmail.Field()
    send_password_reset_email = mutations.SendPasswordResetEmail.Field()
    password_reset = mutations.PasswordReset.Field()
    password_set = mutations.PasswordSet.Field() # For passwordless registration
    password_change = mutations.PasswordChange.Field()
    update_account = mutations.UpdateAccount.Field()
    archive_account = mutations.ArchiveAccount.Field()
    delete_account = mutations.DeleteAccount.Field()
    send_secondary_email_activation =  mutations.SendSecondaryEmailActivation.Field()
    verify_secondary_email = mutations.VerifySecondaryEmail.Field()
    swap_emails = mutations.SwapEmails.Field()
    remove_secondary_email = mutations.RemoveSecondaryEmail.Field()

    # django-graphql-jwt inheritances
    token_auth = mutations.ObtainJSONWebToken.Field()
    verify_token = mutations.VerifyToken.Field()
    refresh_token = mutations.RefreshToken.Field()
    revoke_token = mutations.RevokeToken.Field()
class Mutation(AuthMutation, graphene.ObjectType):
    update_category = CategoryMutation.Field()     # for create
    # update_category = DeleteCategory.Field()     #for delete
    # update_category = UpdateCategory.Field()     #for delete
    pass
    
schema = graphene.Schema(query=Query, mutation=Mutation)