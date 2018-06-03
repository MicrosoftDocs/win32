---
title: PS\_DhcpServerv6DnsSetting class
description: DhcpServer v6DnsSetting.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: db6be670-c083-42e4-91cc-f5ef7a88655b
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DhcpServerv6DnsSetting class
- PS_DhcpServerv6DnsSetting class, described
topic_type:
- apiref
api_name:
- PS_DhcpServerv6DnsSetting
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PS\_DhcpServerv6DnsSetting class

DhcpServer v6DnsSetting

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class PS_DhcpServerv6DnsSetting
{
};
```

## Members

The **PS\_DhcpServerv6DnsSetting** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DhcpServerv6DnsSetting** class has these methods.



| Method                                       | Description                                                                                                               |
|:---------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------|
| [**Get**](get-ps-dhcpserverv6dnssetting.md) | Gets the DNS Update settings configured on the DHCP Server for a specific scope or reservation or server wide.<br/> |
| [**Set**](set-ps-dhcpserverv6dnssetting.md) | Configures how the DNS server should be updated by the DHCP server with client-related information.<br/>            |



 

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





