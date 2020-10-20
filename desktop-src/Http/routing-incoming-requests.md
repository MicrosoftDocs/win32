---
title: Routing Incoming Requests
description: The HTTP Server API maintains a routing database to determine which application receives an incoming request.
ms.assetid: 7c613137-66bd-4375-93cb-b5562823bc12
ms.topic: article
ms.date: 05/31/2018
---

# Routing Incoming Requests

The HTTP Server API maintains a routing database to determine which application receives an incoming request. The routing table is built from the reservation database and contains reservation entries as well as current registrations. When a registration or reservation is made, it is placed into the routing database bucket that corresponds to the host type as follows:

-   \+ : port registrations are placed in the "Strong Wildcard" bucket

-   host : port registrations are placed in the "Explicit" bucket

-   IP : port registrations are placed in the "IP-bound Weak Wildcard" bucket

-   \* : port registrations are placed in the "Weak Wildcard" bucket

These steps also refer to the order incoming HTTP requests are processed. The strong wildcard reservations first, then the explicit reservation are checked followed by the IP-bound weak wildcard and weak wildcard. The search stops when a match is found so that registrations in any of the remaining buckets are not found.

The HTTP Server API routing algorithm locates the best match for the [UrlPrefix](urlprefix-strings.md) by searching both the registration entries and the reservation entries of the routing database, starting with the strong wildcard bucket and ending with the weak wildcard bucket. The best match, within a bucket, is the longest match in the relative URI portion of the UrlPrefix (assuming an exact match for the host, port and scheme portions of the URL). After a match is found in a bucket, the routing algorithm stops its search and skips all lower priority buckets.

For example, consider the following registrations (listed in descending order of priority based on bucket types:

-   Registration: `https://+:80/vroot/` is registered by application 1

-   Registration: `https://adatum.com:80/` is registered by application 2

-   Registration: `https://\*:80/` is registered by application 3

An incoming request for `https://adatum.com:80/vroot/subdir/file.htm/` is delivered to application 1. An incoming request for `https://adatum.com:80/default.htm/` is delivered to application 2. An incoming request for `https://otheradatum.com:80/file.htm/` is delivered to application 3.

If the best match is a reservation entry, this means that the application that should receive the request is not running. For example, consider the following registration and reservation:

-   Registration: `https://\*:80/vroot/` is registered by application 1, user A

-   Reservation: `https://adatum.com:80/` has been reserved for user B

An incoming request for `https://adatum.com:80/vroot/file.htm/` is not delivered to application 1 because the best match leads to the reservation entry for user B. The precedence rules are applied in this case to the reservation which has a higher priority. If no process is active that is authorized and registered to service requests for the URL received, the request is rejected with a 400 status code (Bad Request).

 

 




