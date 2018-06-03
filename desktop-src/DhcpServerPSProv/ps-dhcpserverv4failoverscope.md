---
title: PS\_DhcpServerv4FailoverScope class
description: Dhcp Server v4Failover Scope.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b4f02d07-0ada-4b85-b9bc-3b1775ea5df3
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DhcpServerv4FailoverScope class
- PS_DhcpServerv4FailoverScope class, described
topic_type:
- apiref
api_name:
- PS_DhcpServerv4FailoverScope
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PS\_DhcpServerv4FailoverScope class

Dhcp Server v4Failover Scope.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class PS_DhcpServerv4FailoverScope
{
};
```

## Members

The **PS\_DhcpServerv4FailoverScope** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DhcpServerv4FailoverScope** class has these methods.



| Method                                                | Description                                                                                                                                                                                                                                                                                               |
|:------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Add**](add-ps-dhcpserverv4failoverscope.md)       | Adds the specified scope(s) to the failover relationship.<br/>                                                                                                                                                                                                                                      |
| [**Remove**](remove-ps-dhcpserverv4failoverscope.md) | Removes the specified scopes from the failover relationship. For any specified scope which is not part of the specified failover relationship or which do not exist, a NTE will be returned. This processing will be done upfront before adding the valid scopes to the failover relationship.<br/> |



 

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





