---
title: PLA Interfaces
description: Performance Logs and Alerts (PLA) provides interfaces that you use to configure data collector objects and group them into a data collector set, which you can then schedule to run locally or on a remote computer.
ms.assetid: add9f413-f720-4429-9830-854aafd05065
keywords:
- Performance Logs and Alerts PLA , interfaces
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PLA Interfaces

Performance Logs and Alerts (PLA) provides interfaces that you use to configure data collector objects and group them into a data collector set, which you can then schedule to run locally or on a remote computer.

The following is the list of interfaces that you use to create and manage the data collector set:

-   [**IAlertDataCollector**](/previous-versions/windows/desktop/api/Pla/nn-pla-ialertdatacollector)
-   [**IApiTracingDataCollector**](/previous-versions/windows/desktop/api/Pla/nn-pla-iapitracingdatacollector)
-   [**IConfigurationDataCollector**](/previous-versions/windows/desktop/api/Pla/nn-pla-iconfigurationdatacollector)
-   [**IDataCollector**](/previous-versions/windows/desktop/api/Pla/nn-pla-idatacollector)
-   [**IDataCollectorCollection**](/previous-versions/windows/desktop/api/Pla/nn-pla-idatacollectorcollection)
-   [**IDataCollectorSet**](/previous-versions/windows/desktop/api/Pla/nn-pla-idatacollectorset)
-   [**IDataCollectorSetCollection**](/previous-versions/windows/desktop/api/Pla/nn-pla-idatacollectorsetcollection)
-   [**IDataManager**](/previous-versions/windows/desktop/api/Pla/nn-pla-idatamanager)
-   [**IFolderAction**](/previous-versions/windows/desktop/api/Pla/nn-pla-ifolderaction)
-   [**IFolderActionCollection**](/previous-versions/windows/desktop/api/Pla/nn-pla-ifolderactioncollection)
-   [**IPerformanceCounterDataCollector**](/previous-versions/windows/desktop/api/Pla/nn-pla-iperformancecounterdatacollector)
-   [**ISchedule**](/previous-versions/windows/desktop/api/Pla/nn-pla-ischedule)
-   [**IScheduleCollection**](/previous-versions/windows/desktop/api/Pla/nn-pla-ischedulecollection)
-   [**ITraceDataCollector**](/previous-versions/windows/desktop/api/Pla/nn-pla-itracedatacollector)
-   [**ITraceDataProvider**](/previous-versions/windows/desktop/api/Pla/nn-pla-itracedataprovider)
-   [**ITraceDataProviderCollection**](/previous-versions/windows/desktop/api/Pla/nn-pla-itracedataprovidercollection)
-   [**IValueMap**](/previous-versions/windows/desktop/api/Pla/nn-pla-ivaluemap)
-   [**IValueMapItem**](/previous-versions/windows/desktop/api/Pla/nn-pla-ivaluemapitem)

The [**IDataCollectorSet**](/previous-versions/windows/desktop/api/Pla/nn-pla-idatacollectorset) interface is the primary interface that you use to manage the configuration information that is common to all data collector objects.

To use PLA, the client computer must run in an elevated state or the user must be in the Performance Log Users group.

When calling the **CoCreateInstance** function to create an instance of an object, specify the **CLSCTX\_SERVER** context.

 

 




