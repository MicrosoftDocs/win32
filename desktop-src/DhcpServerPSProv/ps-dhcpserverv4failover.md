---
title: PS\_DhcpServerv4Failover class
description: DhcpServer v4Failover.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0356dcd8-8d2c-4fe7-a3d2-9cbef9b0a869
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DhcpServerv4Failover class
- PS_DhcpServerv4Failover class, described
topic_type:
- apiref
api_name:
- PS_DhcpServerv4Failover
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PS\_DhcpServerv4Failover class

DhcpServer v4Failover.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class PS_DhcpServerv4Failover
{
};
```

## Members

The **PS\_DhcpServerv4Failover** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DhcpServerv4Failover** class has these methods.



| Method                                                               | Description                                                                                                                                                                   |
|:---------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddByHotStandby**](addbyhotstandby-ps-dhcpserverv4failover.md)   | Adds a new IPv4 failover relationship on the server.<br/>                                                                                                               |
| [**AddByLoadBalance**](addbyloadbalance-ps-dhcpserverv4failover.md) | Adds a new IPv4 failover relationship on the server.<br/>                                                                                                               |
| [**GetByName**](getbyname-ps-dhcpserverv4failover.md)               | Gets the failover relationships configured on the server for the specific failover relationship name.<br/>                                                              |
| [**GetByScopeId**](getbyscopeid-ps-dhcpserverv4failover.md)         | Gets the failover relationships configured on the server for the specific failover relationship name.<br/>                                                              |
| [**Remove**](remove-ps-dhcpserverv4failover.md)                     | Removes the specified failover relationship(s). The failover relationship will be removed from both the DHCP servers which are part of this failover relationship.<br/> |
| [**Set**](set-ps-dhcpserverv4failover.md)                           | Modifies the properties of an existing failover relationship.<br/>                                                                                                      |



 

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





