# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AgriculturalOfficer(models.Model):
    aid = models.OneToOneField('User', models.DO_NOTHING, db_column='AID', primary_key=True)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'agricultural_officer'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Batch(models.Model):
    b_number = models.AutoField(db_column='B_Number', primary_key=True)  # Field name made lowercase.
    location = models.ForeignKey('Location', models.DO_NOTHING, db_column='Location_ID', blank=True, null=True)  # Field name made lowercase.
    market = models.ForeignKey('MarketPlace', models.DO_NOTHING, db_column='MARKET_ID', blank=True, null=True)  # Field name made lowercase.
    product_amount = models.DecimalField(db_column='Product_Amount', max_digits=10, decimal_places=2)  # Field name made lowercase.
    optimum_temperature_to_store = models.DecimalField(db_column='Optimum_temperature_to_store', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    optimum_humidity_to_store = models.DecimalField(db_column='Optimum_humidity_to_store', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    product_unit_price = models.DecimalField(db_column='Product_Unit_price', max_digits=10, decimal_places=2)  # Field name made lowercase.
    kg = models.CharField(db_column='KG', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ton = models.CharField(db_column='TON', max_length=3, blank=True, null=True)  # Field name made lowercase.
    mon = models.CharField(db_column='MON', max_length=3, blank=True, null=True)  # Field name made lowercase.
    batch_description = models.TextField(db_column='Batch_Description', blank=True, null=True)  # Field name made lowercase.
    date_time_batch_created = models.DateTimeField(db_column='Date_Time_Batch_Created')  # Field name made lowercase.
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='User_ID', blank=True, null=True)  # Field name made lowercase.
    product = models.ForeignKey('Product', models.DO_NOTHING, db_column='PRODUCT_ID', blank=True, null=True)  # Field name made lowercase.
    hid = models.ForeignKey('Harvest', models.DO_NOTHING, db_column='HID', blank=True, null=True)  # Field name made lowercase.
    sell = models.IntegerField(db_column='SELL')  # Field name made lowercase.
    store = models.IntegerField(db_column='STORE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'batch'


class BatchPurchaseRequest(models.Model):
    pid = models.OneToOneField('PurchaseRequest', models.DO_NOTHING, db_column='PID', primary_key=True)  # Field name made lowercase. The composite primary key (PID, B_Number) found, that is not supported. The first column is selected.
    b_number = models.ForeignKey(Batch, models.DO_NOTHING, db_column='B_Number')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'batch_purchase_request'
        unique_together = (('pid', 'b_number'),)


class Customer(models.Model):
    cid = models.OneToOneField('User', models.DO_NOTHING, db_column='CID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customer'


class CustomerReqVisitToFarmer(models.Model):
    fid = models.OneToOneField('Farmer', models.DO_NOTHING, db_column='FID', primary_key=True)  # Field name made lowercase. The composite primary key (FID, CID, Visit_Date, Time_Slot) found, that is not supported. The first column is selected.
    cid = models.ForeignKey(Customer, models.DO_NOTHING, db_column='CID')  # Field name made lowercase.
    visit_date = models.DateField(db_column='Visit_Date')  # Field name made lowercase.
    time_slot = models.CharField(db_column='Time_Slot', max_length=100)  # Field name made lowercase.
    person_in_visit = models.CharField(db_column='Person_In_Visit', max_length=255, blank=True, null=True)  # Field name made lowercase.
    visit_charge_set_by_farmer = models.DecimalField(db_column='Visit_Charge_Set_By_Farmer', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customer_req_visit_to_farmer'
        unique_together = (('fid', 'cid', 'visit_date', 'time_slot'),)


class Delivery(models.Model):
    pid = models.OneToOneField('PurchaseRequest', models.DO_NOTHING, db_column='PID', primary_key=True)  # Field name made lowercase. The composite primary key (PID, D_Time_DATE) found, that is not supported. The first column is selected.
    d_time_date = models.DateTimeField(db_column='D_Time_DATE')  # Field name made lowercase.
    delivery_status = models.CharField(db_column='Delivery_Status', max_length=50)  # Field name made lowercase.
    delivered_by = models.CharField(db_column='Delivered_By', max_length=255, blank=True, null=True)  # Field name made lowercase.
    is_pickedup = models.IntegerField(db_column='IS_PickedUp', blank=True, null=True)  # Field name made lowercase.
    is_on_the_way = models.IntegerField(db_column='IS_on_the_Way', blank=True, null=True)  # Field name made lowercase.
    fromwherepickup_loc = models.CharField(db_column='FromWherePickup_Loc', max_length=255, blank=True, null=True)  # Field name made lowercase.
    delivery_address = models.CharField(db_column='Delivery_Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    is_satisfy_customer = models.IntegerField(db_column='IS_satisfy_Customer', blank=True, null=True)  # Field name made lowercase.
    delivery_method = models.CharField(db_column='Delivery_Method', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'delivery'
        unique_together = (('pid', 'd_time_date'),)


class DistributorCompany(models.Model):
    did = models.OneToOneField('User', models.DO_NOTHING, db_column='DID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'distributor_company'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Farmer(models.Model):
    fid = models.OneToOneField('User', models.DO_NOTHING, db_column='FID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'farmer'


class FarmerSeedDemand(models.Model):
    fid = models.OneToOneField(Farmer, models.DO_NOTHING, db_column='FID', primary_key=True)  # Field name made lowercase. The composite primary key (FID, SEED_ID) found, that is not supported. The first column is selected.
    seed = models.ForeignKey('Seed', models.DO_NOTHING, db_column='SEED_ID')  # Field name made lowercase.
    quantity = models.IntegerField(db_column='QUANTITY')  # Field name made lowercase.
    urgent_need = models.IntegerField(db_column='URGENT_NEED', blank=True, null=True)  # Field name made lowercase.
    delivery_soon = models.IntegerField(db_column='DELIVERY_SOON', blank=True, null=True)  # Field name made lowercase.
    high_demand = models.IntegerField(db_column='HIGH_DEMAND', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'farmer_seed_demand'
        unique_together = (('fid', 'seed'),)


class FarmerSeedStock(models.Model):
    fid = models.OneToOneField(Farmer, models.DO_NOTHING, db_column='FID', primary_key=True)  # Field name made lowercase. The composite primary key (FID, SEED_STOCK_ID) found, that is not supported. The first column is selected.
    seed_stock = models.ForeignKey('SeedStock', models.DO_NOTHING, db_column='SEED_STOCK_ID')  # Field name made lowercase.
    quantity = models.IntegerField(db_column='QUANTITY')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'farmer_seed_stock'
        unique_together = (('fid', 'seed_stock'),)


class FinancialsupportCustomerToFarmer(models.Model):
    fid = models.OneToOneField(Farmer, models.DO_NOTHING, db_column='FID', primary_key=True)  # Field name made lowercase. The composite primary key (FID, CID) found, that is not supported. The first column is selected.
    cid = models.ForeignKey(Customer, models.DO_NOTHING, db_column='CID')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    donate = models.IntegerField(db_column='Donate', blank=True, null=True)  # Field name made lowercase.
    loan = models.IntegerField(db_column='Loan', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'financialsupport_customer_to_farmer'
        unique_together = (('fid', 'cid'),)


class Harvest(models.Model):
    hid = models.AutoField(db_column='HID', primary_key=True)  # Field name made lowercase.
    season = models.CharField(db_column='SEASON', max_length=50)  # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase.
    product = models.ForeignKey('Product', models.DO_NOTHING, db_column='Product_ID', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='USERID', blank=True, null=True)  # Field name made lowercase.
    qualitygrade = models.DecimalField(db_column='QualityGrade', max_digits=3, decimal_places=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'harvest'


class HarvestFields(models.Model):
    fields_id = models.AutoField(db_column='FIELDS_ID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='USERID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'harvest_fields'


class HarvestFieldsCropsType(models.Model):
    fields = models.OneToOneField(HarvestFields, models.DO_NOTHING, db_column='FIELDS_ID', primary_key=True)  # Field name made lowercase. The composite primary key (FIELDS_ID, CROP_TYPE) found, that is not supported. The first column is selected.
    crop_type = models.CharField(db_column='CROP_TYPE', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'harvest_fields_crops_type'
        unique_together = (('fields', 'crop_type'),)


class HarvestFieldsSoilType(models.Model):
    fields = models.OneToOneField(HarvestFields, models.DO_NOTHING, db_column='FIELDS_ID', primary_key=True)  # Field name made lowercase. The composite primary key (FIELDS_ID, SOIL_TYPE) found, that is not supported. The first column is selected.
    soil_type = models.CharField(db_column='SOIL_TYPE', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'harvest_fields_soil_type'
        unique_together = (('fields', 'soil_type'),)


class HarvestHarvestFields(models.Model):
    hid = models.OneToOneField(Harvest, models.DO_NOTHING, db_column='HID', primary_key=True)  # Field name made lowercase. The composite primary key (HID, FIELDS_ID) found, that is not supported. The first column is selected.
    fields = models.ForeignKey(HarvestFields, models.DO_NOTHING, db_column='FIELDS_ID')  # Field name made lowercase.
    time_date_of_harvest_from_fields = models.DateTimeField(db_column='TIME_DATE_OF_Harvest_From_Fields')  # Field name made lowercase.
    quantity = models.DecimalField(db_column='Quantity', max_digits=10, decimal_places=2)  # Field name made lowercase.
    unitofmeasure = models.CharField(db_column='UnitOfMeasure', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'harvest_harvest_fields'
        unique_together = (('hid', 'fields'),)


class HomeLocation(models.Model):
    location_id = models.AutoField(db_column='Location_ID', primary_key=True)  # Field name made lowercase.
    latitude = models.DecimalField(db_column='Latitude', max_digits=9, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    longitude = models.DecimalField(db_column='Longitude', max_digits=9, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    street = models.CharField(db_column='Street', max_length=255, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=100, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=100, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=100, blank=True, null=True)  # Field name made lowercase.
    postalcode = models.CharField(db_column='PostalCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    altitude = models.IntegerField(db_column='Altitude', blank=True, null=True)  # Field name made lowercase.
    timezone = models.CharField(db_column='Timezone', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'home_location'


class LiveTemperatureHumidityMonitoringOfProductBatches(models.Model):
    humidity = models.DecimalField(db_column='Humidity', max_digits=5, decimal_places=2)  # Field name made lowercase.
    temperature = models.DecimalField(db_column='Temperature', max_digits=5, decimal_places=2)  # Field name made lowercase.
    sid = models.OneToOneField('Sensor', models.DO_NOTHING, db_column='SID', primary_key=True)  # Field name made lowercase. The composite primary key (SID, Recorded_Time) found, that is not supported. The first column is selected.
    recorded_time = models.DateTimeField(db_column='Recorded_Time')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'live_temperature_humidity_monitoring_of_product_batches'
        unique_together = (('sid', 'recorded_time'),)


class Loan(models.Model):
    lid = models.AutoField(db_column='LID', primary_key=True)  # Field name made lowercase.
    v_yes = models.IntegerField(db_column='V_YES', blank=True, null=True)  # Field name made lowercase.
    v_no = models.IntegerField(db_column='V_NO', blank=True, null=True)  # Field name made lowercase.
    why_loan_need = models.TextField(db_column='WHY_LOAN_NEED', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='AMOUNT', max_digits=10, decimal_places=2)  # Field name made lowercase.
    video_link = models.CharField(db_column='Video_Link', max_length=2083, blank=True, null=True)  # Field name made lowercase.
    fid = models.ForeignKey(Farmer, models.DO_NOTHING, db_column='FID', blank=True, null=True)  # Field name made lowercase.
    aid = models.ForeignKey(AgriculturalOfficer, models.DO_NOTHING, db_column='AID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'loan'


class Loan20(models.Model):
    aid = models.OneToOneField(AgriculturalOfficer, models.DO_NOTHING, db_column='AID', primary_key=True)  # Field name made lowercase. The composite primary key (AID, LID, TIMEDATE) found, that is not supported. The first column is selected.
    lid = models.ForeignKey(Loan, models.DO_NOTHING, db_column='LID')  # Field name made lowercase.
    timedate = models.DateTimeField(db_column='TIMEDATE')  # Field name made lowercase.
    notes = models.TextField(db_column='NOTES', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'loan2_0'
        unique_together = (('aid', 'lid', 'timedate'),)


class Location(models.Model):
    location_id = models.AutoField(db_column='Location_ID', primary_key=True)  # Field name made lowercase.
    latitude = models.DecimalField(db_column='Latitude', max_digits=9, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    longitude = models.DecimalField(db_column='Longitude', max_digits=9, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    street = models.CharField(db_column='Street', max_length=255, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=100, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=100, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=100, blank=True, null=True)  # Field name made lowercase.
    postalcode = models.CharField(db_column='PostalCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    altitude = models.IntegerField(db_column='Altitude', blank=True, null=True)  # Field name made lowercase.
    timezone = models.CharField(db_column='Timezone', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'location'


class MarketPlace(models.Model):
    market_id = models.AutoField(db_column='MARKET_ID', primary_key=True)  # Field name made lowercase.
    location = models.ForeignKey(Location, models.DO_NOTHING, db_column='Location_ID', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    traditional = models.IntegerField(db_column='Traditional', blank=True, null=True)  # Field name made lowercase.
    wholeseller = models.IntegerField(db_column='Wholeseller', blank=True, null=True)  # Field name made lowercase.
    starttime = models.TimeField(db_column='StartTime')  # Field name made lowercase.
    endtime = models.TimeField(db_column='EndTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'market_place'


class MarketPlaceProductSold(models.Model):
    market = models.OneToOneField(MarketPlace, models.DO_NOTHING, db_column='MARKET_ID', primary_key=True)  # Field name made lowercase. The composite primary key (MARKET_ID, Products_Sold) found, that is not supported. The first column is selected.
    products_sold = models.CharField(db_column='Products_Sold', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'market_place_product_sold'
        unique_together = (('market', 'products_sold'),)


class Nutritionists(models.Model):
    nid = models.OneToOneField('User', models.DO_NOTHING, db_column='NID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nutritionists'


class PDemand(models.Model):
    product = models.ForeignKey('Product', models.DO_NOTHING, blank=True, null=True)
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userid', blank=True, null=True)
    locationid = models.ForeignKey(Location, models.DO_NOTHING, db_column='locationid', blank=True, null=True)
    p_demand_id = models.AutoField(primary_key=True)
    demandamount = models.DecimalField(db_column='DemandAmount', max_digits=10, decimal_places=2)  # Field name made lowercase.
    demand_date_time = models.DateTimeField(db_column='Demand_Date_Time')  # Field name made lowercase.
    state = models.CharField(db_column='STATE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    area = models.CharField(db_column='AREA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    season = models.CharField(db_column='SEASON', max_length=50, blank=True, null=True)  # Field name made lowercase.
    price_should_be = models.DecimalField(db_column='Price_Should_be', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    comments = models.TextField(db_column='Comments', blank=True, null=True)  # Field name made lowercase.
    mon = models.IntegerField(db_column='MON', blank=True, null=True)  # Field name made lowercase.
    kg = models.IntegerField(db_column='KG', blank=True, null=True)  # Field name made lowercase.
    ton = models.IntegerField(db_column='TON', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'p_demand'


class Product(models.Model):
    product_id = models.AutoField(db_column='Product_ID', primary_key=True)  # Field name made lowercase.
    product_name = models.CharField(db_column='Product_Name', max_length=255)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'product'


class PurchaseRequest(models.Model):
    pid = models.AutoField(db_column='PID', primary_key=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=10, decimal_places=2)  # Field name made lowercase.
    p_date = models.DateField(db_column='P_Date')  # Field name made lowercase.
    payment_status = models.CharField(db_column='Payment_Status', max_length=50)  # Field name made lowercase.
    rid = models.ForeignKey('Retailer', models.DO_NOTHING, db_column='RID', blank=True, null=True)  # Field name made lowercase.
    did = models.ForeignKey(DistributorCompany, models.DO_NOTHING, db_column='DID', blank=True, null=True)  # Field name made lowercase.
    cid = models.ForeignKey(Customer, models.DO_NOTHING, db_column='CID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'purchase_request'


class Retailer(models.Model):
    rid = models.OneToOneField('User', models.DO_NOTHING, db_column='RID', primary_key=True)  # Field name made lowercase.
    storename = models.CharField(db_column='StoreName', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'retailer'


class SampleResult(models.Model):
    certifications_id = models.AutoField(db_column='CERTIFICATIONS_ID', primary_key=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50)  # Field name made lowercase.
    certification_details = models.TextField(db_column='Certification_Details', blank=True, null=True)  # Field name made lowercase.
    b_number = models.ForeignKey(Batch, models.DO_NOTHING, db_column='B_Number', blank=True, null=True)  # Field name made lowercase.
    nid = models.ForeignKey(Nutritionists, models.DO_NOTHING, db_column='NID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sample_result'


class Seed(models.Model):
    seed_id = models.AutoField(db_column='SEED_ID', primary_key=True)  # Field name made lowercase.
    type_of_seed_name = models.CharField(db_column='Type_of_Seed_name', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'seed'


class SeedStock(models.Model):
    seed_stock_id = models.AutoField(db_column='Seed_Stock_id', primary_key=True)  # Field name made lowercase.
    stock_seed_expirydate = models.DateField(db_column='Stock_Seed_ExpiryDate', blank=True, null=True)  # Field name made lowercase.
    stock_quantity_total = models.IntegerField(db_column='Stock_Quantity_Total', blank=True, null=True)  # Field name made lowercase.
    seed = models.ForeignKey(Seed, models.DO_NOTHING, db_column='Seed_ID', blank=True, null=True)  # Field name made lowercase.
    aid = models.ForeignKey(AgriculturalOfficer, models.DO_NOTHING, db_column='AID', blank=True, null=True)  # Field name made lowercase.
    warehouse = models.ForeignKey('Wirehouse', models.DO_NOTHING, db_column='Warehouse_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'seed_stock'


class SeedStock20(models.Model):
    aid = models.OneToOneField(AgriculturalOfficer, models.DO_NOTHING, db_column='AID', primary_key=True)  # Field name made lowercase. The composite primary key (AID, Seed_Stock_id) found, that is not supported. The first column is selected.
    seed_stock = models.ForeignKey(SeedStock, models.DO_NOTHING, db_column='Seed_Stock_id')  # Field name made lowercase.
    distributed_date_time = models.DateTimeField(db_column='DISTRIBUTED_DATE_Time')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'seed_stock_2_0'
        unique_together = (('aid', 'seed_stock'),)


class Sensor(models.Model):
    sensorid = models.AutoField(db_column='SensorID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    nextservingdate = models.DateField(db_column='NextServingDate', blank=True, null=True)  # Field name made lowercase.
    lastphysicalcheckeddate = models.DateField(db_column='LastPhysicalCheckedDate', blank=True, null=True)  # Field name made lowercase.
    b_number = models.ForeignKey(Batch, models.DO_NOTHING, db_column='B_NUMBER', blank=True, null=True)  # Field name made lowercase.
    wirehouse = models.ForeignKey('Wirehouse', models.DO_NOTHING, db_column='WIREHOUSE_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sensor'


class Supplier(models.Model):
    sid = models.OneToOneField('User', models.DO_NOTHING, db_column='SID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'supplier'


class User(models.Model):
    userid = models.AutoField(db_column='USERID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=255)
    email = models.CharField(db_column='Email', max_length=255)  # Field name made lowercase.
    password = models.CharField(max_length=255)
    location = models.ForeignKey(Location, models.DO_NOTHING, db_column='Location_ID', blank=True, null=True)  # Field name made lowercase.
    usercontactnumber = models.CharField(max_length=15, blank=True, null=True)
    usertype = models.CharField(db_column='userType', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'


class Vendor(models.Model):
    vid = models.OneToOneField(User, models.DO_NOTHING, db_column='VID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vendor'


class Wirehouse(models.Model):
    warehousehouseid = models.AutoField(db_column='WarehouseHouseID', primary_key=True)  # Field name made lowercase.
    warehousename = models.CharField(db_column='WarehouseName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    warehousenumber = models.CharField(db_column='WarehouseNumber', max_length=100, blank=True, null=True)  # Field name made lowercase.
    location = models.ForeignKey(Location, models.DO_NOTHING, db_column='LOCATION_ID', blank=True, null=True)  # Field name made lowercase.
    wid = models.ForeignKey('WirehouseManager', models.DO_NOTHING, db_column='WID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wirehouse'


class WirehouseManager(models.Model):
    wid = models.OneToOneField(User, models.DO_NOTHING, db_column='WID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wirehouse_manager'
