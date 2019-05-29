import graphene
from graphene.relay import Node
from graphql import GraphQLError
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from models import Gig as GigModel
from mongoengine import *

class Gig(MongoengineObjectType):
    """
        Get all Gigs
    """
    class Meta:
        model = GigModel
        interfaces = (Node,)

class CreateGig(graphene.Mutation):
    """
        Creates a new gig
    """
    class Arguments:
        title = graphene.String()
        price = graphene.String()
        description = graphene.String()
        contact_phone = graphene.String()
        contact_email = graphene.String()
        contact_name = graphene.String()
    
    gig = graphene.Field(Gig)

    def mutate(self, info, **kwargs):
        gig = GigModel(
            title=kwargs['title'],
            price=kwargs['price'],
            description=kwargs['description'],
            contact_phone=kwargs['contact_phone'],
            contact_email=kwargs['contact_email'],
            contact_name=kwargs['contact_name'],
        )
        gig.save()
        if gig:
            return CreateGig(gig=gig)
        return GraphQLError("Action Failed")


class Query(graphene.ObjectType):
    get_all_gigs = MongoengineConnectionField(Gig)


class Mutation(graphene.ObjectType):
    create_gig = CreateGig.Field(
        description="Creates a new gig and takes the arguments\
            \n- title: title of the gig\
            \n- price: Price of the gig\
            \n- desription: description of the gig\
            \n- contact_email: email of creator\
            \n- contact_name: name of creator\
            \n- contact_phone: phone number of creator")


schema = graphene.Schema(query=Query, mutation=Mutation)
