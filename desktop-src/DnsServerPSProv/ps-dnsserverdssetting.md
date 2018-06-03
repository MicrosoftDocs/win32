---
title: PS\_DnsServerDsSetting class
description: DNS Server DS Setting definition.
audience: developer
ms.assetid: 2e3d3fd9-2120-45ae-a77d-b17f05e70c7a
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DnsServerDsSetting class
- PS_DnsServerDsSetting class, described
topic_type:
- apiref
api_name:
- PS_DnsServerDsSetting
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PS\_DnsServerDsSetting class

DNS Server DS Setting definition.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class PS_DnsServerDsSetting
{
};
```

## Members

The **PS\_DnsServerDsSetting** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DnsServerDsSetting** class has these methods.



| Method                                   | Description                                |
|:-----------------------------------------|:-------------------------------------------|
| [**Get**](get-ps-dnsserverdssetting.md) | Retrieve DNS Server AD Settings<br/> |
| [**Set**](set-ps-dnsserverdssetting.md) | Set Active Directory Settings<br/>   |



 

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[DnsServerPSProvider Provider](dns-server-classes.md)
</dt> </dl>

 

 





