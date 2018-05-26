---
title: MSFT\_ServerManagerTasks class
description: Class that exposes Multi Machine Server Manager tasks.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c01d835e-8e88-43f4-8802-46c14fdcf4d9
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_ServerManagerTasks class
- MSFT_ServerManagerTasks class, described
topic_type:
- apiref
api_name:
- MSFT_ServerManagerTasks
api_location:
- MgmtProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_ServerManagerTasks class

Class that exposes Multi Machine Server Manager tasks.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("mgmtprovider"), AMENDMENT]
class MSFT_ServerManagerTasks
{
};
```

## Members

The **MSFT\_ServerManagerTasks** class has these types of members:

-   [Methods](#methods)

### Methods

The **MSFT\_ServerManagerTasks** class has these methods.



| Method                                                                                       | Description                                                                                                                                                                                                          |
|:---------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetCounterSamplesAtTime**](getcountersamplesattime-msft-servermanagertasks.md)           | Retrieves the performance counter samples logged by a Data Collector Set at the specified time stamps.<br/>                                                                                                    |
| [**GetCounterSamplesInTimeRange**](getcountersamplesintimerange-msft-servermanagertasks.md) | Retrieves the performance counter samples logged by a Data Collector Set in a particular time range.<br/>                                                                                                      |
| [**GetPerformanceCollectorState**](getperformancecollectorstate-msft-servermanagertasks.md) | Retrieves the state of a Data Collector Set in Performance Logs & Alerts.<br/>                                                                                                                                 |
| [**GetServerBpaResult**](getserverbparesult-msft-servermanagertasks.md)                     | Retrieves the BPA model results from the server.<br/>                                                                                                                                                          |
| [**GetServerClusterName**](getserverclustername-msft-servermanagertasks.md)                 | Retrieves the access names and name of all the nodes in the cluster.<br/>                                                                                                                                      |
| [**GetServerEventDetail**](getservereventdetail-msft-servermanagertasks.md)                 | Retrieves the details of events generated in an event log by a particular source.<br/>                                                                                                                         |
| [**GetServerEventDetailEx**](getservereventdetailex-msft-servermanagertasks.md)             | Retrieves the details of events generated in an event log by a particular source.<br/> **Windows Server 2012 R2 and Windows Server 2012:** This method is not available before Windows Server 2016.<br/> |
| [**GetServerFeature**](getserverfeature-msft-servermanagertasks.md)                         | Gets the server features on the managed node.<br/>                                                                                                                                                             |
| [**GetServerInventory**](getserverinventory-msft-servermanagertasks.md)                     | Retrieves the basic inventory information of the server.<br/>                                                                                                                                                  |
| [**GetServerServiceDetail**](getserverservicedetail-msft-servermanagertasks.md)             | Retrieves the details of the specified Win32 services on the managed node.<br/>                                                                                                                                |
| [**RemoveServerPerformanceLog**](removeserverperformancelog-msft-servermanagertasks.md)     | Remove the log file for a data collector set that are older than a given threshold.<br/>                                                                                                                       |
| [**SetPerformanceCollectorState**](setperformancecollectorstate-msft-servermanagertasks.md) | Configures the state of a Data Collector Set in Performance Logs & Alerts.<br/>                                                                                                                                |



 

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                              |
| Namespace<br/>                | Root\\Windows\\ServerManager<br/>                                                     |
| MOF<br/>                      | <dl> <dt>MgmtProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MgmtProvider.dll</dt> </dl> |



 

 





