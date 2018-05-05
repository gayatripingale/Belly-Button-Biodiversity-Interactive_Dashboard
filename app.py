# dependencies

# Flask( Server)
from flask import Flas,jsonify,render_template,request,flash,redirect

# SQL ALchemy (ORM)
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine,func,desc,select
import pandas as pd
import numpy as np

# database setup

engine = create_engine("sqlite:///DataSets/belly_button_biodiversity.sqlite")

# reflect an exisiting database into a new model
Base = automap()

#reflect tables
Base.prepare(engine,reflect=True)

#save referances to the table
OTU = Base.classes.otu
Samples_Metadata = Base.classes.Samples_Metadata

# Create session(link from Python to # DB)
session = Session(engine)

# Flask setup
app = Flask(__name__)

# Flask Routes

# Returns the dashboard homepage
@app.route("/")
def index():
    return render_template("index.html")

# Returns a list of sample names

@app.route('/names')
def names():
    # Return list of sample names

    #Use Pandas to perform the sql query

    stmt = session.querry(Samples).statement
    df = pd.read_sql_query(stmt,session.bind)
    df.set_index('otu_id',inplace=True)

    # Return a list of the colum names(samle names)

    return jsonify(list(df.columns))

    # Returns a list of OTU description
    @app.route('/otu'):
    def otu():
        results = session.querry(OTU.lowsest_taxonomic_unit_found).all()

        # Use numpy ravel to extract list o ftuples into lis of OTU descriptions
        otu_list = list(np.ravel(results))
        return jsonify(otu_list)

        # Returns a json dictionary of sample Samples_Metadata

        #MetaData for a given sample.

        @app.route('/metadatq/<sample>')
        def sample_metadata(sample):
            sel = [Samples_Metadata.SAMPLEID, Samples_Meatadata.Ethnicity, Samples_Metadata.GENDER, Samples_Metadat.AGE, Samoles_Metadata.BBTYPE]

            #
