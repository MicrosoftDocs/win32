---
title: PS\_BgpStatistics class
description: Retrieves Border Gateway Protocol (BGP) message and route statistics.
audience: developer
ms.assetid: b9d00b81-8a2a-4969-aa5f-94c87bf438ed
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_BgpStatistics class
- PS_BgpStatistics class, described
topic_type:
- apiref
api_name:
- PS_BgpStatistics
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PS\_BgpStatistics class

Retrieves Border Gateway Protocol (BGP) message and route statistics.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class PS_BgpStatistics
{
};
```

## Members

The **PS\_BgpStatistics** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_BgpStatistics** class has these methods.



| Method                              | Description                                                                                         |
|:------------------------------------|:----------------------------------------------------------------------------------------------------|
| [**Get**](get-ps-bgpstatistics.md) | Retrieves the BGP peering message and route advertisement statistics for a set of peers.<br/> |



 

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                               |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





