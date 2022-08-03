from  sqlalchemy import create_engine, text

db_connection_string = "mysql+mysqldb://hvmrn158mty9:pscale_pw_G6vypY6vHxDLH1ulHldbwspseXd3lgOr7EhY2m02gWY@cgykdct4ixka.us-east-3.psdb.cloud/joviancareers"

engine = create_engine(db_connection_string,
                    connect_args={   "ssl": {
                                        "ssl_ca": "/etc/ssl/cert.pem"
                                    }
                                }
                    )


def load_jobs_from_db():
  with engine.connect() as con:
    result = con.execute('SELECT * FROM jobs')
  
    jobs = []
    for row in result.all():
      jobs.append(dict(row))
  return jobs


# with engine.connect() as con:
#   result = con.execute('SELECT * FROM jobs')
  
#   row_dict = []
#   for row in result.all():
#     row_dict.append(dict(row))

# print(row_dict)