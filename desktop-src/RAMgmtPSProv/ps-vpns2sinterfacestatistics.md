---
title: PS\_VpnS2SInterfaceStatistics class
description: Refers to statistics of an IKEv2 S2S connection.
audience: developer
ms.assetid: 02de13ea-c66c-463f-a54e-e6ae3188a13b
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_VpnS2SInterfaceStatistics class
- PS_VpnS2SInterfaceStatistics class, described
topic_type:
- apiref
api_name:
- PS_VpnS2SInterfaceStatistics
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PS\_VpnS2SInterfaceStatistics class

Refers to statistics of an IKEv2 S2S connection.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class PS_VpnS2SInterfaceStatistics
{
};
```

## Members

The **PS\_VpnS2SInterfaceStatistics** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_VpnS2SInterfaceStatistics** class has these methods.



| Method                                                    | Description                                                                                                                                                                  |
|:----------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Clear**](clear-ps-vpns2sinterfacestatistics.md)       | Resets the statistics of an S2S interface.<br/>                                                                                                                        |
| [**Get**](get-ps-vpns2sinterfacestatistics.md)           | Retrieves statistics of an S2S interface for the specified VPN connection.<br/>                                                                                        |
| [**GetByAll**](getbyall-ps-vpns2sinterfacestatistics.md) | Retrieves statistics of an S2S interface for all VPN connections.<br/> **Windows Server 2012:** This method is not available before Windows Server 2012 R2.<br/> |



 

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





