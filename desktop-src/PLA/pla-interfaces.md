---
title: PLA Interfaces
description: Performance Logs and Alerts (PLA) provides interfaces that you use to configure data collector objects and group them into a data collector set, which you can then schedule to run locally or on a remote computer.
ms.assetid: add9f413-f720-4429-9830-854aafd05065
keywords:
- Performance Logs and Alerts PLA , interfaces
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# PLA Interfaces

Performance Logs and Alerts (PLA) provides interfaces that you use to configure data collector objects and group them into a data collector set, which you can then schedule to run locally or on a remote computer.

The following is the list of interfaces that you use to create and manage the data collector set:

-   [**IAlertDataCollector**](/windows/previous-versions/Pla/nn-pla-ialertdatacollector?branch=master)
-   [**IApiTracingDataCollector**](/windows/previous-versions/Pla/nn-pla-iapitracingdatacollector?branch=master)
-   [**IConfigurationDataCollector**](/windows/previous-versions/Pla/nn-pla-iconfigurationdatacollector?branch=master)
-   [**IDataCollector**](/windows/previous-versions/Pla/nn-pla-idatacollector?branch=master)
-   [**IDataCollectorCollection**](/windows/previous-versions/Pla/nn-pla-idatacollectorcollection?branch=master)
-   [**IDataCollectorSet**](/windows/previous-versions/Pla/nn-pla-idatacollectorset?branch=master)
-   [**IDataCollectorSetCollection**](/windows/previous-versions/Pla/nn-pla-idatacollectorsetcollection?branch=master)
-   [**IDataManager**](/windows/previous-versions/Pla/nn-pla-idatamanager?branch=master)
-   [**IFolderAction**](/windows/previous-versions/Pla/nn-pla-ifolderaction?branch=master)
-   [**IFolderActionCollection**](/windows/previous-versions/Pla/nn-pla-ifolderactioncollection?branch=master)
-   [**IPerformanceCounterDataCollector**](/windows/previous-versions/Pla/nn-pla-iperformancecounterdatacollector?branch=master)
-   [**ISchedule**](/windows/previous-versions/Pla/nn-pla-ischedule?branch=master)
-   [**IScheduleCollection**](/windows/previous-versions/Pla/nn-pla-ischedulecollection?branch=master)
-   [**ITraceDataCollector**](/windows/previous-versions/Pla/nn-pla-itracedatacollector?branch=master)
-   [**ITraceDataProvider**](/windows/previous-versions/Pla/nn-pla-itracedataprovider?branch=master)
-   [**ITraceDataProviderCollection**](/windows/previous-versions/Pla/nn-pla-itracedataprovidercollection?branch=master)
-   [**IValueMap**](/windows/previous-versions/Pla/nn-pla-ivaluemap?branch=master)
-   [**IValueMapItem**](/windows/previous-versions/Pla/nn-pla-ivaluemapitem?branch=master)

The [**IDataCollectorSet**](/windows/previous-versions/Pla/nn-pla-idatacollectorset?branch=master) interface is the primary interface that you use to manage the configuration information that is common to all data collector objects.

To use PLA, the client computer must run in an elevated state or the user must be in the Performance Log Users group.

When calling the **CoCreateInstance** function to create an instance of an object, specify the **CLSCTX\_SERVER** context.

 

 




