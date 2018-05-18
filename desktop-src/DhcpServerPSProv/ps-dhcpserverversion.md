---
title: PS\_DhcpServerVersion class
description: Returns the software version of the DHCP Server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '206ddc2d-d892-4edd-ad40-81fff222fe28'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["PS_DhcpServerVersion class", "PS_DhcpServerVersion class, described"]
topic_type:
- apiref
api_name:
- PS_DhcpServerVersion
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
---

# PS\_DhcpServerVersion class

Returns the software version of the DHCP Server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class PS_DhcpServerVersion
{
};
```

## Members

The **PS\_DhcpServerVersion** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DhcpServerVersion** class has these methods.



| Method                                  | Description                                     |
|:----------------------------------------|:------------------------------------------------|
| [**Get**](get-ps-dhcpserverversion.md) | Gets the version of the DHCP server.<br/> |



 

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





