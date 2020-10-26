---
title: Scenario 3 Performance Counters
description: Performance counters measure quantities of information or data, according to the number, size, duration, and rate of data being requested or received.
ms.assetid: 1b264144-7600-402e-86f8-674a2d02f9f9
ms.topic: article
ms.date: 05/31/2018
---

# Scenario 3: Performance Counters

Performance counters measure quantities of information or data, according to the number, size, duration, and rate of data being requested or received. You should not expect to get a list of details from a counter, such as a list of error messages. Instead, use performance counters to get quantities, such as the number of error message since startup or the rate at which error messages are being generated.

## Performance Counters for HTTP.sys

Starting with Windows Vista and Windows Server 2008, HTTP.sys has the following performance metric counters to help you with monitoring, diagnosing, and capacity planning for Web servers: The HTTP Server API component has the following performance counters to help you with monitoring, diagnosing, and capacity planning for Web servers:

- HTTP Service Counters:
  - Number of URIs in the cache, added since startup, deleted since startup, and number of cache flushes
  - Cache hits/second and Cache misses/second
- HTTP Service URL Groups:
  - Data send rate, data receive rate, bytes transferred (sent and received)
  - Maximum number of connections, connection attempts rate, rate for GET and HEAD requests, and total number of requests
- HTTP Service Request Queues:
  - Number of requests in queue, age of oldest requests in queue (age of the last request in the queue)
  - Rate of request arrivals into the queue, rate of rejection, total number of rejected requests, rate of cache hits

**Accessing Performance Counters**

1.  Type **perfmon** at the command prompt to start the Performance Diagnostic Console.
2.  Select **Performance Monitor** in the tree control and then open the **Add Counters** by clicking **+**.
3.  From **Add Counters** select from the three Performance Counters sets: **HTTP Service**, **HTTP Service Request Queues** , or **HTTP Service Url Groups**.
4.  To view counters from the **HTTP Service Request Queues** and **HTTP Service Url Groups** counter sets, select **instance(s)** and click **Add**, and then click **OK**. To view the HTTP Service counters, select the counter set in the left pane and click **Add**.

> [!Note]  
> Only one instance of the HTTP Server API counters exists per machine, as these counters represent the component-wide state. With instances of Url Group performance counters, the instance ID (for the performance counter) will match the Url Group ID. The Url Group ID can be viewed by running **netsh http show servicestate**. With instances of Request Queues performance counters, the instance name corresponds to Request Queue Name. The Request Queue Name (if one exists) can be shown by the same **netsh http show servicestate**. However, some server applications may have unnamed Request Queues that cannot be matched to a performance counter instance ID.

 

 

 




