---
title: PS\_RemoteAccessConnectionStatisticsSummary class
description: Refers to the summary of active (real-time) and accounting statistics for connections.
audience: developer
ms.assetid: aa6ff523-7951-4b02-a9f5-eadd872c7289
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_RemoteAccessConnectionStatisticsSummary class
- PS_RemoteAccessConnectionStatisticsSummary class, described
topic_type:
- apiref
api_name:
- PS_RemoteAccessConnectionStatisticsSummary
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PS\_RemoteAccessConnectionStatisticsSummary class

Refers to the summary of active (real-time) and accounting statistics for connections.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class PS_RemoteAccessConnectionStatisticsSummary
{
};
```

## Members

The **PS\_RemoteAccessConnectionStatisticsSummary** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_RemoteAccessConnectionStatisticsSummary** class has these methods.



| Method                                                                                                    | Description                                                                                                                                                                                                                         |
|:----------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetByAccountingStatistics**](getbyaccountingstatistics-ps-remoteaccessconnectionstatisticssummary.md) | This cmdlet displays the following1. Summary statistics of current (real-time) active DirectAccess and VPN connections2. Summary statistics of DirectAccess and VPN historical connections for a specified time duration<br/> |
| [**GetByActiveStatistics**](getbyactivestatistics-ps-remoteaccessconnectionstatisticssummary.md)         | This cmdlet displays the following1. Summary statistics of current (real-time) active DirectAccess and VPN connections2. Summary statistics of DirectAccess and VPN historical connections for a specified time duration<br/> |



 

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





