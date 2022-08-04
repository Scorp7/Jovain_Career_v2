from  sqlalchemy import create_engine, text

db_connection_string = "mysql+mysqldb://drar13f32dkt:pscale_pw_0CxMJxr4kubo445S9Q--9HWS8O03v7leFdoVFkJtuOw@cgykdct4ixka.us-east-3.psdb.cloud/joviancareers"

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


def load_job_from_db(id): 
  with engine.connect() as con:
    result = con.execute(text('SELECT * FROM jobs WHERE id = :var'),
    var = id )

    rows = result.all()
    if len(rows)==0:
      return None
    else:
      return dict(rows[0])
