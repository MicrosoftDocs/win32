---
title: PS\_RemoteAccessConnectionStatisticsLocal class
description: Refers to the real-time connection stats and stats based on accounting data.
audience: developer
ms.assetid: 2f979ade-8385-4582-95aa-cc0218136d9a
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_RemoteAccessConnectionStatisticsLocal class
- PS_RemoteAccessConnectionStatisticsLocal class, described
topic_type:
- apiref
api_name:
- PS_RemoteAccessConnectionStatisticsLocal
api_location:
- RAServerPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PS\_RemoteAccessConnectionStatisticsLocal class

Refers to the real-time connection stats and stats based on accounting data.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAServerPSProvider"), AMENDMENT]
class PS_RemoteAccessConnectionStatisticsLocal
{
};
```

## Members

The **PS\_RemoteAccessConnectionStatisticsLocal** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_RemoteAccessConnectionStatisticsLocal** class has these methods.



| Method                                                                                                  | Description                                                                                                                                                                                                                        |
|:--------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetByAccountingStatistics**](getbyaccountingstatistics-ps-remoteaccessconnectionstatisticslocal.md) | This cmdlet displays the following1. Statistics of current (real-time) active DirectAccess and VPN connections2. Statistics of DirectAccess and VPN connections for a specified time duration, based on accounting data<br/> |
| [**GetByActiveStatistics**](getbyactivestatistics-ps-remoteaccessconnectionstatisticslocal.md)         | This cmdlet displays the following1. Statistics of current (real-time) active DirectAccess and VPN connections2. Statistics of DirectAccess and VPN connections for a specified time duration, based on accounting data<br/> |



 

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                    |
| Namespace<br/>                | Root\\microsoft\\windows\\remoteaccess\\server<br/>                                         |
| MOF<br/>                      | <dl> <dt>RAServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAServerPSProvider.dll</dt> </dl> |



 

 





