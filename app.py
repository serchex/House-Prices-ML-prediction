import streamlit as st
import pandas as pd
import joblib
import nominal as nom


model = joblib.load('models/catboost_model.pkl')
order = joblib.load('models/feature_order.pkl')

st.title('Houses Price Prediction')

#
mssubclass = st.selectbox('Building class (MSSubClass)', [20, 30, 40, 45, 50, 60, 70, 75, 80, 85, 90, 120, 150, 160, 180, 190])
zones = {'Agriculture':'A','Commercial':'C (all)','Floating Village Residential':'FV','Industrial':'I',
         'Residential High Density':'RH','Residential Low Density':'RL','Residential Low Density Park':'RP',
         'Residential Medium Density':'RM'}
mszoning = st.selectbox('General zoning  classification (MSZoning):', zones.keys())
key_zone = zones[mszoning]
lotfrontage = st.slider('Linear feet of street connected to property',21,313)
lotarea = st.slider('Lot size in square feet', 1300, 215245)
street_ = {'Gravel': 'Grvl','Paved':'Pave'}
street = st.selectbox('Type of road access to property',street_.keys())
key_street = street_[street]
alley_ = {'Gravel':'Grvl','Paved':'Pave','No alley access':'NA'}
alley = st.selectbox('Type of alley access to property',alley_.keys())
key_alley = alley_[alley]
lotshape_ = {'Regular':'Reg','Slightly irregular':'IR1','Moderately Irregular':'IR2','Irregular':'IR3'}
lotshape = st.selectbox('General shape of property',lotshape_.keys())
key_lotshape = lotshape_[lotshape]
landcontour_ = {'Near Flat/Level':'Lvl','Banked - Quick and significant rise from street grade to building':'Bnk',\
                'Hillside - Significant slope from side to side':'HLS','Depression':'Low'}
landcontour = st.selectbox('Flatness of the property', landcontour_.keys())
key_landcontour = landcontour_[landcontour]
utilities_ = {'All public Utilities (E,G,W,& S)':'AllPub','Electricity, Gas, and Water (Septic Tank)':'NoSewr',\
              'Electricity and Gas Only':'NoSeWa','Electricity only':'ELO'}
utilities = st.selectbox('Type of utilities available',utilities_.keys())
key_utilities = utilities_[utilities]
lotconfig_ = {'Inside lot':'Inside','Corner lot':'Corner','Cul-de-sac':'CulDSac','Frontage on 2 sides of property':'FR2',\
              'Frontage on 3 sides of property':'FR3'}
lotconfig = st.selectbox('Lot configuration',lotconfig_.keys())
key_lotconfig = lotconfig_[lotconfig]
landslope_ = {'Gentle slope':'Gtl','Moderate Slope':'Mod','Severe Slope':'Sev'}
landslope = st.selectbox('Slope of property',landslope_.keys())
key_landslope = landslope_[landslope]
neighborhood_ = {'Bloomington Heights':'Blmngtn','Bluestem':'Blueste','Briardale':'BrDale','Brookside':'BrkSide','Clear Creek':'ClearCr',\
                 'College Creek':'CollgCr','Crawford':'Crawfor','Edwards':'Edwards','Gilbert':'Gilbert','Iowa DOT and Rail Road':'IDOTRR',
                 'Meadow Village':'MeadowV','Mitchell':'Mitchel','North Ames':'Names','Northridge':'NoRidge','Northpark Villa':'NPkVill',
                 'Northridge Heights':'NridgHt','Northwest Ames':'NWAmes','Old Town':'OldTown','South & West of Iowa State University':'SWISU',
                 'Sawyer':'Sawyer','Sawyer West':'SawyerW','Somerset':'Somerst','Stone Brook':'StoneBr','Timberland':'Timber','Veenker':'Veenker'
}
neighborhood = st.selectbox('Physical locations within Ames city limits (Neighborhood)',neighborhood_.keys())
key_neighborhood = neighborhood_[neighborhood]
condition1_ = {'Adjacent to arterial street':'Artery','Adjacent to feeder street':'Feedr','Normal':'Norm',\
               '''Within 200' of North-South Railroad''':'RRNn','Adjacent to North-South Railroad':'RRAn',\
                'Near positive off-site feature--park, greenbelt, etc.':'PosN','Adjacent to postive off-site feature':'PosA',\
                '''Within 200' of East-West Railroad''':'RRNe','Adjacent to East-West Railroad':'RRAe'
}
condition1 = st.selectbox('Proximity to various conditions',condition1_.keys())
key_condition1 = condition1_[condition1]
condition2_ = {'Adjacent to arterial street':'Artery','Adjacent to feeder street':'Feedr','Normal':'Norm',\
               '''Within 200' of North-South Railroad''':'RRNn','Adjacent to North-South Railroad':'RRAN',\
               'Near positive off-site feature--park, greenbelt, etc.':'POSN','Adjacent to postive off-site feature':'POSA',\
                '''Within 200' of East-West Railroad''':'RRNe','Adjacent to East-West Railroad':'RRAe'
}
condition2 = st.selectbox('Proximity to various conditions (if more than one is present)',condition2_.keys())
key_condition2 = condition2_[condition2]
bldgtype_ = {'Single-family Detached':'1Fam','Two-family Conversion; originally built as one-family dwelling':'2FmCon',\
             'Duplex':'Duplx','Townhouse End Unit':'TwnhsE','Townhouse Inside Unit':'TwnhsI'
}
bldgtype = st.selectbox('Type of dwelling',bldgtype_.keys())
key_bldgtype = bldgtype_[bldgtype]
housestyle_ = {'One story':'1Story','One and one-half story: 2nd level finished':'1.5Fin','One and one-half story: 2nd level unfinished':'1.5Unf',\
               'Two story':'2Story','Two and one-half story: 2nd level finished':'2.5Fin','Two and one-half story: 2nd level unfinished':'2.5Unf',\
               'Split Foyer':'SFoyer','Split Level':'SLv1'
}
housestyle = st.selectbox('Style of dwelling',housestyle_.keys())
key_housestyle = housestyle_[housestyle]
overallqual_ = {'Very Excellent':10,'Excellent':9,'Very Good':8,'Good':7,'Above Average':6,'Average':5,'Below Average':4,'Fair':3,\
                'Poor':2,'Very Poor':1
}
overallqual = st.selectbox('Rates the overall material and finish of the house',overallqual_.keys())
key_overallqual = overallqual_[overallqual]
overallcond_ = {'Very Excellent':10,'Excellent':9,'Very Good':8,'Good':7,'Above Average':6,'Average':5,'Below Average':4,'Fair':3,\
                'Poor':2,'Very Poor':1
}
overallcond = st.selectbox('Rates the overall condition of the house', overallcond_.keys())
key_overallcond = overallcond_[overallcond]
yearbuilt = st.slider('Original construction date',1872,2025)
yearremodadd = st.slider('Remodel date (same as construction date if no remodeling or additions)',1950,2010)
roofstyle_ = {'Flat':'Flat','Gable':'Gable','Gabrel (Barn)':'Gambrel','Hip':'Hip','Mansard':'Mansard','Shed':'Shed'}
roofstyle = st.selectbox('Type of roof',roofstyle_.keys())
key_roofstyle = roofstyle_[roofstyle]
roofmatl_ = {'ClyTile Clay or Tile':'ClyTile','Standard (Composite) Shingle':'CompShg','Membrane':'Membran','Metal':'Metal','Roll':'Roll',
            'Gravel & Tar':'Tar&Grv','Wood Shakes':'WdShake','Wood Shingles':'WdShngl'
} 
roofmatl = st.selectbox('Roof material',roofmatl_.keys())
key_roofmatl = roofmatl_[roofmatl]
exterior1st_ = {'AsbShng Asbestos Shingles':'AsbShng','Asphalt Shingles':'AsphShn','Brick Common':'BrkComm','Brick Face':'BrkFace',\
                'Cinder Block':'CBlock','Cement Board':'CemntBd','Hard Board':'HdBoard','Imitation Stucco':'ImStucc','Metal Siding':'MetalSd',\
                'Other':'Other','Plywood':'Plywood','PreCast':'PreCast','Stone':'Stone','Stucco':'Stucco','Vinyl Siding':'VinylSd',\
                'WdShing Wood Shingles':'Wd Sdng','Wood Siding':'WdShing' 
}
exterior1st = st.selectbox('Exterior covering on house',exterior1st_.keys())
key_exterior1st = exterior1st_[exterior1st]
exterior2nd_ = {'AsbShng Asbestos Shingles':'AsbShng','Asphalt Shingles':'AsphShn','Brick Common':'BrkComm','Brick Face':'BrkFace',\
                'Cinder Block':'CBlock','Cement Board':'CemntBd','Hard Board':'HdBoard','Imitation Stucco':'ImStucc','Metal Siding':'MetalSd',\
                'Other':'Other','Plywood':'Plywood','PreCast':'PreCast','Stone':'Stone','Stucco':'Stucco','Vinyl Siding':'VinylSd',\
                'WdShing Wood Shingles':'Wd Sdng','Wood Siding':'WdShing'}
exterior2nd = st.selectbox('Exterior covering on house (if more than one material)',exterior2nd_.keys())
key_exterior2nd = exterior2nd_[exterior2nd]
masvnrtype_ = {'Brick Common':'BrkCmn','Brick Face':'BrkFace','Cinder Block':'CBlock','None':'None','Stone':'Stone'}
masvnrtype = st.selectbox('Masonry veneer type',masvnrtype_.keys())
key_masvnrtype = masvnrtype_[masvnrtype]
masvnrarea = st.slider('Masonry veneer area in square feet',0,1600)
exterqual_ = {'Excellent':'EX','Good':'Gd','Average/Typical':'TA','Fair':'Fa','Poor':'Po'}
exterqual = st.selectbox('Evaluates the quality of the material on the exterior',exterqual_.keys())
key_exterqual = exterqual_[exterqual]
extercond_ = {'Excellent':'EX','Good':'Gd','Average/Typical':'TA','Fair':'Fa','Poor':'Po'}
extercond = st.selectbox('Evaluates the present condition of the material on the exterior',extercond_.keys())
key_extercond = extercond_[extercond]
foundation_ = {'Brick & Tile':'BrkTil','Cinder Block':'CBlock','Poured Contrete':'PConc','Slab':'Slab','Stone':'Stone','Wood':'Wood'}
foundation = st.selectbox('Type of foundation',foundation_.keys())
key_foundation = foundation_[foundation]
bsmtqual_ = {'Excellent (100+ inches)':'Ex','Good (90-99 inches)':'Gd','Typical (80-89 inches)':'TA','Fair (70-79 inches)':'Fa',\
             'Poor (<70 inches':'Po','No Basement':'NA'
}
bsmtqual = st.selectbox('Evaluates the height of the basement',bsmtqual_.keys())
key_bmstqual = bsmtqual_[bsmtqual]
bsmtcond_ = {'Excellent':'Ex','Good':'Gd','Typical - slight dampness allowed':'TA','Fair - dampness or some cracking or settling':'Fa',\
             'Poor - Severe cracking, settling, or wetness':'Po','No Basement':'NA'
}
bsmtcond = st.selectbox('Evaluates the general condition of the basement',bsmtcond_.keys())
key_bsmtcond = bsmtcond_[bsmtcond]
bsmtexposure_ = {'Good Exposure':'Gd','Average Exposure (split levels or foyers typically score average or above)':'Av',\
                'Mimimum Exposure':'Mn','No Exposure':'No','No Basement':'NA'
}
bsmtexposure = st.selectbox('Refers to walkout or garden level walls',bsmtexposure_.keys())
key_bsmtexposure = bsmtexposure_[bsmtexposure]
bsmtfintype1_ = {'Good Living Quarters':'GLQ','Average Living Quarters':'ALQ','Below Average Living Quarters':'BLQ','Average Rec Room':'Rec',
                 'Low Quality':'LwQ','Unfinshed':'Unf','No Basement':'NA'
}
bsmtfintype1 = st.selectbox('Rating of basement finished area',bsmtfintype1_.keys())
key_bsmtfintype1 = bsmtfintype1_[bsmtfintype1]
bsmtfinsf1 = st.slider('Type 1 finished square feet',0,5644)
bsmtfintype2_ = {'Good Living Quarters':'GLQ','Average Living Quarters':'ALQ','Below Average Living Quarters':'BLQ','Average Rec Room':'Rec',\
                 'Low Quality':'LwQ','Unfinshed':'Unf','No Basement':'NA'
}
bsmtfintype2 = st.selectbox('Rating of basement finished area (if multiple types)', bsmtfintype2_.keys())
key_bsmtfintype2 = bsmtfintype2_[bsmtfintype2]
bsmtfinsf2 = st.slider('Type 2 finished square feet',0,1474)
bsmtunfsf = st.slider('Unfinished square feet of basement area',0,2336)
totalbsmtsf = st.slider('Total square feet of basement area',0,6110)
heating_ = {'Floor Furnace':'Floor','Gas forced warm air furnace':'GasA','Gas hot water or steam heat':'GasW','Gravity furnace':'Grav',\
            'Hot water or steam heat other than gas':'OthW','Wall furnace':'Wall'
}
heating = st.selectbox('Type of heating', heating_.keys())
key_heating = heating_[heating]
heatingqc_ = {'Excellent':'EX','Good':'Gd','Average/Typical':'TA','Fair':'Fa','Poor':'Po'}
heatingqc = st.selectbox('Heating quality and condition',heatingqc_.keys())
key_heatingqc = heatingqc_[heatingqc]
centralair_ = {'No':'N','Yes':'Y'}
centralair = st.selectbox('Central air conditioning',centralair_.keys())
key_centralair = centralair_[centralair]
electrical_ = {'Standard Circuit Breakers & Romex':'SBrkr','Fuse Box over 60 AMP and all Romex wiring (Average)':'FuseA',\
               '60 AMP Fuse Box and mostly Romex wiring (Fair)':'FuseF',\
               '60 AMP Fuse Box and mostly knob & tube wiring (poor)':'FuseP','Mixed':'Mix'
}
electrical = st.selectbox('Electrical system',electrical_.keys())
key_electrical = electrical_[electrical]
fstflrsf = st.slider('First Floor square feet',334,4692) 
sndflrsf = st.slider('Second floor square feet',0,2065)
lowqualfinsf = st.slider('Low quality finished square feet (all floors)',0,572)
grlivarea = st.slider('Above grade (ground) living area square feet',334,5642)
bsmtfullbath = st.slider('Basement full bathrooms',0,3)
bsmthalfbath = st.slider('Basement half bathrooms',0,2)
fullbath = st.slider('Full bathrooms above grade',0,3)
halfbath = st.slider('Half baths above grade',0,2)
bedroomabvgr = st.slider('Bedrooms above grade (does NOT include basement bedrooms)',0,8)
kitchenabvgr = st.slider('Kitchens above grade',0,3)
kitchenqual_ = {'Excellent':'Ex','Good':'Gd','Typical/Average':'TA','Fair':'Fa','Poor':'Po'}
kitchenqual = st.selectbox('Kitchen quality',kitchenqual_.keys())
key_kitchenqual = kitchenqual_[kitchenqual]
totrmsabvgrd = st.slider('Total rooms above grade (does not include bathrooms)',2,14)
functional_ = {'Typical Functionality':'Typ','Minor Deductions 1':'Min1','Minor Deductions 2':'Min2','Moderate Deductions':'Mod',\
               'Major Deductions 1':'Maj1','Major Deductions 2':'Maj2','Severely Damaged':'Sev','Salvage only':'Sal'
}
functional = st.selectbox('Home functionality (Assume typical unless deductions are warranted)',functional_.keys())
key_functional = functional_[functional]
fireplaces = st.slider('Number of fireplaces',0,3)
fireplacequ_ = {'Excellent - Exceptional Masonry Fireplace':'Ex','Good - Masonry Fireplace in main level':'Gd',\
                'Average - Prefabricated Fireplace in main living area or Masonry Fireplace in basement':'TA',\
                'Fair - Prefabricated Fireplace in basement':'Fa','Poor - Ben Franklin Stove':'Po','No Fireplace':'NA'
}
fireplacequ = st.selectbox('Fireplace quality', fireplacequ_.keys())
key_fireplacequ = fireplacequ_[fireplacequ]
garagetype_ = {'More than one type of garage':'2Types','Attached to home':'Attchd','Basement Garage':'Basment',\
               'Built-In (Garage part of house - typically has room above garage)':'BuiltIn','Car Port':'CarPort',\
               'Detached from home':'Detchd','No Garage':'NA'
}
garagetype = st.selectbox('Garage location',garagetype_.keys())
key_garagetype = garagetype_[garagetype]
garageyrblt = st.slider('Year garage was built',1900,2025)
garagefinish_ = {'Finished':'Fin','Rough Finished':'RFn','Unfinished':'Unf','No Garage':'NA'}
key_garagefinish = st.selectbox('Interior finish of the garage', garagefinish_.keys())
garagecars = st.slider('Size of garage in car capacity',0,4)
garagearea = st.slider('Size of garage in square feet',0,1418)
garagequal_ = {'Excellent':'Ex','Good':'Gd','Typical/Average':'TA','Fair':'Fa','Poor':'Po','No Garage':'NA'}
garagequal = st.selectbox('Garage quality',garagequal_.keys())
key_garagequal = garagequal_[garagequal]
garagecond_ = {'Excellent':'Ex','Good':'Gd','Typical/Average':'TA','Fair':'Fa','Poor':'Po','No Garage':'NA'}
garagecond = st.selectbox('Garage condition',garagecond_.keys())
paveddrive_ = {'Paved':'Y','Partial Pavement':'P','Dirt/Gravel':'N'}
paveddrive = st.selectbox('Paved driveway',paveddrive_.keys())
key_paveddrive = paveddrive_[paveddrive]
wooddecksf = st.slider('Wood deck area in square feet',0,857)
openporchsf = st.slider('Open porch area in square feet',0,547)
enclosedporch = st.slider('Enclosed porch area in square feet',0,552)
tssnporch = st.slider(' Three season porch area in square feet',0,508) 
screenporch = st.slider('Screen porch area in square feet',0,480)
poolarea = st.slider('Pool area in square feet',0,738)
poolqc_ = {'Excellent':'Ex','Good':'Gd','Average/Typical':'TA','Fair':'Fa','No Pool':'NA'}
poolqc = st.selectbox('Pool quality', poolqc_.keys())
key_poolqc = poolqc_[poolqc]
fence_ = {'Good Privacy':'GdPrv','Minimum Privacy':'MnPrv','Good Wood':'GdWo','Minimum Wood/Wire':'MnWw','No Fence':'NA'}
fence = st.selectbox('Fence quality', fence_.keys())
key_fence = fence_[fence]
miscfeature_ = {'Elevator':'Elev','2nd Garage (if not described in garage section)':'Gar2','Other':'Othr','Shed (over 100 SF)':'Shed',\
                'Tennis Court':'TenC','None':'NA'
}
miscfeature = st.selectbox('Miscellaneous feature not covered in other categories',miscfeature_.keys())
key_miscfeature = miscfeature_[miscfeature]
miscval = st.slider('$Value of miscellaneous feature',0,15500)
mosold = st.slider('Month Sold (MM)',1,12)
yrsold = st.slider('Year Sold (YYYY)',2006,2025)
saletype_ = {'Warranty Deed - Conventional':'WD','Warranty Deed - Cash':'CWD','Warranty Deed - VA Loan':'VWD',\
             'Home just constructed and sold':'New','Court Officer Deed/Estate':'COD','Contract 15% Down payment regular terms':'Con',\
             'Contract Low Down payment and low interest':'ConLw','Contract Low Interest':'ConLI','Contract Low Down':'ConLD',\
             'Other':'Oth'
}
saletype = st.selectbox('Type of sale', saletype_.keys())
key_saletype = saletype_[saletype]
salecondition_ = {'Normal Sale':'Normal','Abnormal Sale -  trade, foreclosure, short sale':'Abnorml',\
                  'Adjoining Land Purchase':'AdjLand',\
                  'Allocation - two linked properties with separate deeds, typically condo with a garage unit':'Alloca',\
                  'Sale between family members':'Family','Home was not completed when last assessed (associated with New Homes)':'Partial'
}
salecondition = st.selectbox('Condition of sale',salecondition_.keys())
key_salecondition = salecondition_[salecondition]

input_dict = {
    #'Id':1,
    'MSSubClass': mssubclass,
    'MSZoning': key_zone,
    'LotFrontage': lotfrontage,
    'LotArea':lotarea,
    'Street':key_street,
    'Alley':key_alley,
    'LotShape':key_lotshape,
    'LandContour':key_landcontour,
    'Utilities':key_utilities,
    'LotConfig':key_lotconfig,
    'LandSlope':key_landslope,
    'Neighborhood':key_neighborhood,
    'Condition1':key_condition1,
    'Condition2':key_condition2,
    'BldgType':key_bldgtype,
    'HouseStyle':key_housestyle,
    'OverallQual':key_overallqual,
    'OverallCond':key_overallcond,
    'YearBuilt':yearbuilt,
    'YearRemodAdd':yearremodadd,
    'RoofStyle':key_roofstyle,
    'RoofMatl':key_roofmatl,
    'Exterior1st':key_exterior1st,
    'Exterior2nd':key_exterior2nd,
    'MasVnrType':key_masvnrtype,
    'MasVnrArea':masvnrarea,
    'ExterQual':key_exterqual,
    'ExterCond':key_extercond,
    'Foundation':key_foundation,
    'BsmtQual':key_bmstqual,
    'BsmtCond':key_bsmtcond,
    'BsmtExposure':key_bsmtexposure,
    'BsmtFinType1':key_bsmtfintype1,
    'BsmtFinSF1': bsmtfinsf1,
    'BsmtFinType2':key_bsmtfintype2,
    'BsmtFinSF2':bsmtfinsf2,
    'BsmtUnfSF':bsmtunfsf,
    'TotalBsmtSF':totalbsmtsf,
    'Heating':key_heating,
    'HeatingQC':key_heatingqc,
    'CentralAir':key_centralair,
    'Electrical':key_electrical,
    '1stFlrSF':fstflrsf,
    '2ndFlrSF':sndflrsf,
    'LowQualFinSF':lowqualfinsf,
    'GrLivArea':grlivarea,
    'BsmtFullBath':bsmtfullbath,
    'BsmtHalfBath':bsmthalfbath,
    'FullBath':fullbath,
    'HalfBath':halfbath,
    'BedroomAbvGr':bedroomabvgr,
    'KitchenAbvGr':kitchenabvgr,
    'KitchenQual':key_kitchenqual,
    'TotRmsAbvGrd':totrmsabvgrd,
    'Functional':functional,
    'Fireplaces':fireplaces,
    'FireplaceQu':fireplacequ,
    'GarageType':garagetype,
    'GarageYrBlt':garageyrblt,
    'GarageFinish':key_garagefinish,
    'GarageCars':garagecars,
    'GarageArea':garagearea,
    'GarageQual':garagequal,
    'GarageCond':garagecond,
    'PavedDrive':key_paveddrive,
    'WoodDeckSF':wooddecksf,
    'OpenPorchSF':openporchsf,
    'EnclosedPorch':enclosedporch,
    '3SsnPorch':tssnporch,
    'ScreenPorch':screenporch,
    'PoolArea':poolarea,
    'PoolQC':key_poolqc,
    'Fence':key_fence,
    'MiscFeature':key_miscfeature,
    'MiscVal':miscval,
    'MoSold':mosold,
    'YrSold':yrsold,
    'SaleType':key_saletype,
    'SaleCondition':key_salecondition
    # otros campos necesarios...
}
#st.write(input_dict)
if st.button('Predict price'):
    df = pd.DataFrame({k: [v] for k,v in input_dict.items()})
    missing_cols = []
    for col in order:
        if col not in df.columns:
            missing_cols.append(col)

    if missing_cols:
        st.error(f"missing columns in input_dict: {missing_cols}")
    prepro = nom.preprocess_data(df)
    pred = model.predict(prepro)
    st.success(f'Estimated price: ${pred[0]:,.2f}')
