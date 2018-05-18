---
title: PS\_DhcpServerv4IPRecord class
description: Dhcp Server v4 IP Record class.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'bb9656a4-b50d-4e12-aedd-02b0f9f81504'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["PS_DhcpServerv4IPRecord class", "PS_DhcpServerv4IPRecord class, described"]
topic_type:
- apiref
api_name:
- PS_DhcpServerv4IPRecord
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
---

# PS\_DhcpServerv4IPRecord class

Dhcp Server v4 IP Record class.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class PS_DhcpServerv4IPRecord
{
};
```

## Members

The **PS\_DhcpServerv4IPRecord** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DhcpServerv4IPRecord** class has these methods.



| Method                                           | Description                                                          |
|:-------------------------------------------------|:---------------------------------------------------------------------|
| [**Repair**](repair-ps-dhcpserverv4iprecord.md) | Reconciles DHCP server database for the specified scopes.<br/> |



 

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





