---
title: PLA Interfaces
description: Performance Logs and Alerts (PLA) provides interfaces that you use to configure data collector objects and group them into a data collector set, which you can then schedule to run locally or on a remote computer.
ms.assetid: 'add9f413-f720-4429-9830-854aafd05065'
keywords: ["Performance Logs and Alerts PLA , interfaces"]
---

# PLA Interfaces

Performance Logs and Alerts (PLA) provides interfaces that you use to configure data collector objects and group them into a data collector set, which you can then schedule to run locally or on a remote computer.

The following is the list of interfaces that you use to create and manage the data collector set:

-   [**IAlertDataCollector**](ialertdatacollector.md)
-   [**IApiTracingDataCollector**](iapitracingdatacollector.md)
-   [**IConfigurationDataCollector**](iconfigurationdatacollector.md)
-   [**IDataCollector**](idatacollector.md)
-   [**IDataCollectorCollection**](idatacollectorcollection.md)
-   [**IDataCollectorSet**](idatacollectorset.md)
-   [**IDataCollectorSetCollection**](idatacollectorsetcollection.md)
-   [**IDataManager**](idatamanager.md)
-   [**IFolderAction**](ifolderaction.md)
-   [**IFolderActionCollection**](ifolderactioncollection.md)
-   [**IPerformanceCounterDataCollector**](iperformancecounterdatacollector.md)
-   [**ISchedule**](ischedule.md)
-   [**IScheduleCollection**](ischedulecollection.md)
-   [**ITraceDataCollector**](itracedatacollector.md)
-   [**ITraceDataProvider**](itracedataprovider.md)
-   [**ITraceDataProviderCollection**](itracedataprovidercollection.md)
-   [**IValueMap**](ivaluemap.md)
-   [**IValueMapItem**](ivaluemapitem.md)

The [**IDataCollectorSet**](idatacollectorset.md) interface is the primary interface that you use to manage the configuration information that is common to all data collector objects.

To use PLA, the client computer must run in an elevated state or the user must be in the Performance Log Users group.

When calling the **CoCreateInstance** function to create an instance of an object, specify the **CLSCTX\_SERVER** context.

 

 




