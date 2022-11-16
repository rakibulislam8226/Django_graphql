from graphql_auth.schema import UserQuery, MeQuery
import graphene


class Query(UserQuery, MeQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
