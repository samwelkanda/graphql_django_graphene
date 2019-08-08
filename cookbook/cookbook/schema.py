import graphene

from cookbook.ingredients import schema

class Query(cookbook.ingredients.schema.Query, graphene.ObjectType):
    # Will inherit from multiple queries as we begin to add apps to 
    # our project
    pass

schema = graphene.Schema(query=Query)