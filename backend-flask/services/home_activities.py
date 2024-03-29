from datetime import datetime, timedelta, timezone
from opentelemetry import trace

from lib.db import pool

tracer = trace.get_tracer("home.activities")

class HomeActivities:
  def run(logger):
    logger.info("HomeActivities")
    with tracer.start_as_current_span("home-activities-mock-data"):
      span = trace.get_current_span()
      now = datetime.now(timezone.utc).astimezone()
      span.set_attribute("app.now", now.isoformat())
      

      sql = """
      SELECT * FROM activities
      """
      with pool.connection() as conn:
        with conn.cursor() as cur:
          cur.execute(sql)
          # this will return a tuple
          # the first field being the data
          json = cur.fetchone()
      return json[0]    
      return results