from  sqlalchemy import create_engine, text

db_connection_string = "mysql+mysqldb://iwoick8e8o9j:pscale_pw_J9cSS6_UbfomNGYlrG2D0BLfzzSDmRP4v4zqRXM2WQ0@cgykdct4ixka.us-east-3.psdb.cloud/joviancareers"

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
