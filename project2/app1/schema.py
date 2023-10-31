import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError
from .models import User, Vehicle, ParkingDetails, ParkingSpot,Ewallet,SavedParkinglot

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = "__all__"
        
class CarType(DjangoObjectType):
    class Meta:
        model = Vehicle
        fields = "__all__"
        
class ParkingdetailType(DjangoObjectType):
    class Meta:
        model = ParkingDetails
        fields = "__all__"
        
class ParkingspotType(DjangoObjectType):
    class Meta:
        model = ParkingSpot
        fields = "__all__"

class EwalletType(DjangoObjectType):
    class Meta:
        model = Ewallet
        fields = "__all__"
        
class SavedType(DjangoObjectType):
    class Meta:
        model = SavedParkinglot
        fields = "__all__"


class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    usersbyid = graphene.Field(UserType, id=graphene.ID(required=True))
    usersbyemail = graphene.Field(UserType, email=graphene.String(required=True))
    usersbyfireid = graphene.Field(UserType,fireid=graphene.String(required = True))

    
    vehicles = graphene.List(CarType)
    vehiclesbyid = graphene.Field(CarType, id=graphene.ID(required = True))
    vehiclesbyfireid = graphene.List(CarType, fireid=graphene.String(required = True))
    
    parkingdetail = graphene.List(ParkingdetailType)
    parkingdetailbyid = graphene.Field(ParkingdetailType, id=graphene.String(required = True))
    parkingdetailbymulti = graphene.List(ParkingdetailType, fireid=graphene.String(required = True),todaydate= graphene.String(required = True),parkingname = graphene.String(required = True))
    parkingdetailbyfireid = graphene.List(ParkingdetailType, fireid=graphene.String(required = True))
    
    parkingspot = graphene.List(ParkingspotType)
    parkingspotbyid = graphene.Field(ParkingspotType, id=graphene.ID(required = True))
    parkingspotbyname = graphene.Field(ParkingspotType, name=graphene.String(required = True))
    
    balance = graphene.List(EwalletType)
    balancebyfireid = graphene.Field(EwalletType,fireid = graphene.String(required = True))
    balancebyemail = graphene.Field(EwalletType, email=graphene.String(required=True))
    
    saved = graphene.List(SavedType)
    savedbyfireid = graphene.List(SavedType,fireid = graphene.String(required = True))
    
    
    #User Resolvers
    def resolve_users(self, info):
        return User.objects.all()

    def resolve_usersbyid(self, info, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            raise GraphQLError(f"User with ID {id} does not exist.")
        
    def resolve_usersbyemail(self, info, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            raise GraphQLError(f"User with ID {email} does not exist.")
        
    def resolve_usersbyfireid(self, info, fireid):
        try:
            return User.objects.get(fireid=fireid)
        except User.DoesNotExist:
            raise GraphQLError(f"User with ID {fireid} does not exist.")
    
    
    # vehicle Resolver    
    def resolve_vehicles(self, info):
        return Vehicle.objects.all()

    def resolve_vehiclesbyid(self, info, id):
        try:
            return Vehicle.objects.get(id=id)
        except Vehicle.DoesNotExist:
            raise GraphQLError(f"Car with ID {id} does not exist.")
        
    def resolve_vehiclesbyfireid(self, info, fireid):
        try:
            return Vehicle.objects.all().filter(fireid=fireid)
        except Vehicle.DoesNotExist:
            raise GraphQLError(f"Car with ID {fireid} does not exist.")
    
    
    #Parking Details resolver    
    def resolve_parkingdetail(self, info):
        return ParkingDetails.objects.all()

    def resolve_parkingdetailbyid(self, info, id):
        try:
            return ParkingDetails.objects.get(id=id)
        except ParkingDetails.DoesNotExist:
            raise GraphQLError(f"Parking Detail with ID {id} does not exist.")
        
    def resolve_parkingdetailbymulti(self, info, fireid,todaydate,parkingname):
        try:
            return ParkingDetails.objects.all().filter(fireid=fireid,todaydate=todaydate,parkingname=parkingname)
        except ParkingDetails.DoesNotExist:
            raise GraphQLError(f"Parking Detail with ID {fireid} does not exist.")
    
    def resolve_parkingdetailbyfireid(self, info, fireid):
        try:
            return ParkingDetails.objects.all().filter(fireid=fireid)
        except ParkingDetails.DoesNotExist:
            raise GraphQLError(f"Parking Detail with ID {fireid} does not exist.")
    
    #parking spot resolvers    
    def resolve_parkingspot(self, info):
        return ParkingSpot.objects.all()

    def resolve_parkingspotbyid(self, info, id):
        try:
            print(id)
            return ParkingSpot.objects.get(id=id)
        except ParkingSpot.DoesNotExist:
            raise GraphQLError(f"Parking Spot with ID {id} does not exist.")
    
    def resolve_parkingspotbyname(self, info, name):
        try:
            print(name)
            return ParkingSpot.objects.all().filter(name=name)
        except ParkingSpot.DoesNotExist:
            raise GraphQLError(f"Parking Spot with ID {name} does not exist.")
    
    # E-wallet resolvers    
    def resolve_balance(self, info):
        return Ewallet.objects.all()

    def resolve_balancebyfireid(self, info, fireid):
        try:
            return Ewallet.objects.get(fireid=fireid)
        except Ewallet.DoesNotExist:
            raise GraphQLError(f"Wallet with ID {fireid} does not exist.")
        
    def resolve_balancebyemail(self, info, email):
        try:
            return Ewallet.objects.get(email=email)
        except Ewallet.DoesNotExist:
            raise GraphQLError(f"User with ID {email} does not exist.")
        
    # Saved Resolvers
    def resolve_saved(self, info):
        return SavedParkinglot.objects.all()
    
    def resolve_savedbyfireid(self, info, fireid):
        try:
            return SavedParkinglot.objects.all().filter(fireid=fireid)
        except SavedParkinglot.DoesNotExist:
            raise GraphQLError(f"User with ID {fireid} does not exist.")

# Creating User        
class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        # username = graphene.String(required=True)
        # date = graphene.String(required=True)
        email = graphene.String(required=True)
        # phoneno = graphene.Float(required=True)
        # gender = graphene.String(required=True)


    def mutate(self, info,email):
        user = User(email =email)
        user.save()
        return CreateUser(user=user)

#Creating Vehicle
class CreateVehicle(graphene.Mutation):
    vehicle = graphene.Field(CarType)
    
    class Arguments:
        modelname = graphene.String(required=True)
        platenum =  graphene.String(required=True)
        fireid = graphene.String(required=True)
        
    def mutate(self, info,modelname,platenum,fireid):
        vehicle = Vehicle(modelname = modelname,platenum = platenum,fireid = fireid)
        vehicle.save()
        return CreateVehicle(vehicle = vehicle)
    
#Creating ParkingDetails    
class CreateParkingdetail(graphene.Mutation):
    parkingdetail = graphene.Field(ParkingdetailType)
    
    class Arguments:
        # selecteddate = graphene.String(required=True)
        # duration = graphene.String(required=True)
        # starthour = graphene.String(required=True)
        # endhour = graphene.String(required=True)
        # totalcost = graphene.Int(required=True)
        fireid = graphene.String(required=True)
        todaydate = graphene.String(required=True)
        parkingname = graphene.String(required=True)
        address = graphene.String(required=True)
        displayphoto = graphene.String(required=True)
        
    def mutate(self, info,fireid,todaydate,parkingname,address,displayphoto):
        parkingdetail = ParkingDetails(fireid = fireid,todaydate=todaydate,parkingname= parkingname,address=address,displayphoto=displayphoto)
        parkingdetail.save()
        return CreateParkingdetail(parkingdetail = parkingdetail)  
    

#Creating E-wallet
class CreateWallet(graphene.Mutation):
    walletname = graphene.Field(EwalletType)

    class Arguments:
        # username = graphene.String(required=True)
        # date = graphene.String(required=True)
        email = graphene.String(required=True)
        fireid = graphene.String(required=True)
        # phoneno = graphene.Float(required=True)
        # gender = graphene.String(required=True)


    def mutate(self, info,email,fireid):
        walletname = Ewallet(email =email,fireid =fireid)
        walletname.save()
        return CreateWallet(walletname=walletname)  

# Creating Saved
class CreateSaved(graphene.Mutation):
    save = graphene.Field(SavedType)

    class Arguments:
        fireid = graphene.String(required = True)
        spotname = graphene.String(required = True)
        spotaddress = graphene.String(required = True)
        displayphoto = graphene.String(required = True)
        parkid = graphene.String(required = True)



    def mutate(self, info,fireid,spotname,spotaddress,displayphoto,parkid):
        save = SavedParkinglot(fireid=fireid,spotname=spotname,spotaddress=spotaddress,displayphoto=displayphoto,parkid=parkid)
        save.save()
        return CreateSaved(save=save) 
    

# class UpdateUser(graphene.Mutation):
#     user = graphene.Field(UserType)

#     class Arguments:
#         id = graphene.ID(required=True)
#         username = graphene.String()
#         date = graphene.String()
#         phoneno = graphene.Float()
#         gender  = graphene.String()
#         # email = graphene.String()

#     def mutate(self, info, id, **kwargs):
#         user = User.objects.get(id=id)
#         for field, value in kwargs.items():
#             if value is not None:
#                 setattr(user, field, value)
#         user.save()
#         return UpdateUser(user=user)

class UpdateUserInput(graphene.InputObjectType):
    user_id = graphene.ID()
    username = graphene.String()
    date = graphene.String()
    phoneno = graphene.String()
    gender = graphene.String()
    email = graphene.String()
    fireid = graphene.String()




#Updation using DjangoID
class UpdateUserMutation(graphene.Mutation):
    class Arguments:
        input_data = UpdateUserInput(required=True)

    user = graphene.Field(UserType)

    def mutate(self, info, input_data):
        user_id = input_data.get('user_id')
        username = input_data.get('username')
        email = input_data.get('email')
        date = input_data.get('date')
        phoneno = input_data.get('phoneno')
        gender = input_data.get('gender')
        fireid = input_data.get('fireid')

        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise Exception(f"User with ID {user_id} does not exist")

        if username is not None:
            user.username = username
        
        if date is not None:
            user.date = date
            
        if phoneno is not None:
            user.phoneno = phoneno
            
        if gender is not None:
            user.gender = gender


        if email is not None:
            user.email = email
            
        if fireid is not None:
            user.fireid = fireid

        user.save()

        return UpdateUserMutation(user=user)
    
#Updation using Firebase ID
class UpdateUserFireMutation(graphene.Mutation):
    class Arguments:
        input_data = UpdateUserInput(required=True)

    user = graphene.Field(UserType)

    def mutate(self, info, input_data):
        user_id = input_data.get('user_id')
        username = input_data.get('username')
        email = input_data.get('email')
        date = input_data.get('date')
        phoneno = input_data.get('phoneno')
        gender = input_data.get('gender')
        fireid = input_data.get('fireid')

        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise Exception(f"User with ID {user_id} does not exist")

        if username is not None:
            user.username = username
        
        if date is not None:
            user.date = date
            
        if phoneno is not None:
            user.phoneno = phoneno
            
        if gender is not None:
            user.gender = gender


        if email is not None:
            user.email = email
            
        if fireid is not None:
            user.fireid = fireid

        user.save()

        return UpdateUserFireMutation(user=user)
    
#Updation on E- wallet
class EwalletInput(graphene.InputObjectType):
    balancename_id = graphene.ID()
    email = graphene.String()
    # useridval = graphene.String()
    fireid = graphene.String()
    balance = graphene.String()



# Balance Updation
class EwalletMutation(graphene.Mutation):
    class Arguments:
        input_data = EwalletInput(required=True)

    balancename = graphene.Field(EwalletType)

    def mutate(self, info, input_data):
        balancename_id = input_data.get('balancename_id')
        # useridval = input_data.get('useridval')
        email = input_data.get('email')
        balance = input_data.get('balance')
        fireid = input_data.get('fireid')


        try:
            balancename = Ewallet.objects.get(pk=balancename_id)
        except Ewallet.DoesNotExist:
            raise Exception(f"Wallet with ID {balancename_id} does not exist")

        if balance is not None:
            balancename.balance = balance
            
        if fireid is not None:
            balancename.fireid = fireid
            
        if email is not None:
            balancename.email = email
        

            


        balancename.save()

        return EwalletMutation(balancename=balancename)
    
    
# Updating ParkingDetails using id
class UpdateParkingdetailInput(graphene.InputObjectType):
    detail_id = graphene.ID()
    username = graphene.String()
    phoneno = graphene.String()
    vehiclename = graphene.String()
    vehiclenum = graphene.String()
    selecteddate = graphene.String()
    duration = graphene.String()
    starthour = graphene.String()
    endhour = graphene.String()
    totalcost = graphene.String()
    floornum = graphene.String()
    spotnum = graphene.String()


class UpdateParkingdetailMutation(graphene.Mutation):
    class Arguments:
        input_data = UpdateParkingdetailInput(required=True)

    detail = graphene.Field(ParkingdetailType)

    def mutate(self, info, input_data):
        detail_id = input_data.get('detail_id')
        username = input_data.get('username')
        phoneno = input_data.get('phoneno')
        vehiclename = input_data.get('vehiclename')
        vehiclenum = input_data.get('vehiclenum')
        selecteddate = input_data.get('selecteddate')
        duration = input_data.get('duration')
        starthour = input_data.get('starthour')
        endhour = input_data.get('endhour')
        totalcost = input_data.get('totalcost')
        floornum = input_data.get('floornum')
        spotnum = input_data.get('spotnum')

        try:
            detail = ParkingDetails.objects.get(pk=detail_id)
        except ParkingDetails.DoesNotExist:
            raise Exception(f"User with ID {detail_id} does not exist")

        if username is not None:
            detail.username = username
            
        if phoneno is not None:
            detail.phoneno = phoneno
        
        if vehiclename is not None:
            detail.vehiclename = vehiclename
            
            
        if vehiclenum is not None:
            detail.vehiclenum = vehiclenum


        if selecteddate is not None:
            detail.selecteddate = selecteddate
            
        if duration is not None:
            detail.duration = duration
            
        if starthour is not None:
            detail.starthour = starthour
            
        if endhour is not None:
            detail.endhour = endhour
            
        if totalcost is not None:
            detail.totalcost = totalcost
            
        if floornum is not None:
            detail.floornum = floornum
            
        if spotnum is not None:
            detail.spotnum = spotnum

        detail.save()

        return UpdateParkingdetailMutation(detail=detail)
    
# Delete Saved Mutation
class DeleteSaved(graphene.Mutation):
    id = graphene.ID()
    success = graphene.Boolean()

    class Arguments:
        id = graphene.ID(required=True)

    def mutate(self, info, id):
        try:
            save = SavedParkinglot.objects.get(id=id)
            save.delete()
            return DeleteSaved(id=id, success=True)
        except SavedParkinglot.DoesNotExist:
            return DeleteSaved(id=None, success=False)

# Deleting PArking Detail

class DeleteParkingdetail(graphene.Mutation):
    id = graphene.ID()
    success = graphene.Boolean()

    class Arguments:
        id = graphene.ID(required=True)

    def mutate(self, info, id):
        try:
            save = ParkingDetails.objects.get(id=id)
            save.delete()
            return DeleteParkingdetail(id=id, success=True)
        except ParkingDetails.DoesNotExist:
            return DeleteParkingdetail(id=None, success=False)

    
class Mutation(graphene.ObjectType):
    
    #Creation
    create_user = CreateUser.Field()
    create_vehicle = CreateVehicle.Field()
    create_parkingdetail = CreateParkingdetail.Field()
    create_wallet = CreateWallet.Field()
    create_saved = CreateSaved.Field()
    
    #Upadation
    update_user = UpdateUserMutation.Field()
    update_fireuser = UpdateUserFireMutation.Field()
    update_wallet = EwalletMutation.Field()
    update_parkdetails = UpdateParkingdetailMutation.Field()
    
    #deletion
    delete_saved = DeleteSaved.Field()
    delete_detail = DeleteParkingdetail.Field()


        
schema = graphene.Schema(query=Query, mutation=Mutation)