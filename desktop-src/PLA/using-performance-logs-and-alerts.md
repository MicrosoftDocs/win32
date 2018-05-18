---
title: Using PLA
description: Performance Logs and Alerts (PLA) provides the ability to generate alert notifications based on performance counter thresholds.
ms.assetid: '5d854513-13cb-47dd-a74a-cc746191cb44'
keywords: ["Performance Logs and Alerts PLA , using"]
---

# Using PLA

Performance Logs and Alerts (PLA) provides the ability to generate alert notifications based on performance counter thresholds. You can also use PLA to query performance data, create event tracing sessions, capture a computer's configuration, and trace API calls in some Win32 system DLLs.

The data collector set is the primary entity used in PLA. The data collector set defines where the logs are written, when the set runs and for how long, and the credentials used to run the set. PLA uses data collectors to collect data. You can add one or more of the following data collectors to a data collector set:

-   [Alert](ialertdatacollector.md)
-   [API Tracing](iapitracingdatacollector.md)
-   [Configuration](iconfigurationdatacollector.md)
-   [Performance Counter](iperformancecounterdatacollector.md)
-   [Event Tracing](itracedatacollector.md)

This section describes:

-   [Creating a Data Collector Set](creating-a-data-collector-set.md)
-   [Adding a Data Collector to a Data Collector Set](adding-a-data-collector-to-a-data-collector-set.md)
-   [Running a Data Collector Set](running-a-data-collector-set.md)
-   [Managing the Data of a Data Collector Set](managing-the-data-of-a-data-collector-set.md)
-   [Committing a Data Collector Set](committing-a-data-collector-set.md)
-   [Querying Data Collector Sets](querying-data-collector-sets.md)

 

 




