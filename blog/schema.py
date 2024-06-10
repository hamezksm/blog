import graphene
import app.schema
import authentication.schema

# Schema to combine all schemas from different apps


class Query(app.schema.Query,authentication.schema.Query ,graphene.ObjectType):
    # Combine the queries from different apps
    pass


class Mutation(app.schema.Mutation, authentication.schema.Mutation,graphene.ObjectType):
    # Combine the mutations from different apps
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
