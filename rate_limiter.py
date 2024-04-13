import datetime

class RateLimiter:
  def __init__(self, maxRequests, period):
      self.maxRequests = maxRequests 
      self.period = period 

  def addRequest(self, ip):
      currentTime = datetime.datetime.now()
      requests = self.requests.get(ip, []) 
      requests.append(currentTime)
      self.requests[ip] = requests
      print(self.requests)

  def hasExceededLimit(self, ip):
      periodStartTime = datetime.datetime.now() - datetime.timedelta(minutes=self.periodInMinutes)
      requests = self.requests.get(ip, [])
      requestCount = 0
      i = len(requests) - 1
      while (i >= 0 and requests[i] >= periodStartTime):
          i -= 1
          requestCount += 1
      return requestCount >= self.maxRequests

  requests = {}
  maxRequests = 100
  periodInMinutes = 60
