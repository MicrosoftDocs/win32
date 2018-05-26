---
title: PS\_DhcpServerDnsCredential class
description: PS\_DhcpServerDnsCredential class.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: fbfaf29f-b44d-46d4-ae5d-f8f4fc841c66
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DhcpServerDnsCredential class
- PS_DhcpServerDnsCredential class, described
topic_type:
- apiref
api_name:
- PS_DhcpServerDnsCredential
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PS\_DhcpServerDnsCredential class

PS\_DhcpServerDnsCredential class.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class PS_DhcpServerDnsCredential
{
};
```

## Members

The **PS\_DhcpServerDnsCredential** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DhcpServerDnsCredential** class has these methods.



| Method                                              | Description                                                                                                                    |
|:----------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------|
| [**Get**](get-ps-dhcpserverdnscredential.md)       | Gets the user account used by the DHCP server for registering or de-registering client records with DNS server<br/>      |
| [**Remove**](remove-ps-dhcpserverdnscredential.md) | Removes DNS credentials to be used by the DHCP server for registering leases with DNS server<br/>                        |
| [**Set**](set-ps-dhcpserverdnscredential.md)       | Sets DNS credentials to be used by the DHCP server for registering or de-registering client records with DNS server<br/> |



 

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





