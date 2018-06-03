---
title: PS\_DnsServerSecondaryZone class
description: DNS Server Secondary Zone definition.
audience: developer
ms.assetid: f4a753e7-0b32-4622-9214-7d6823e1738a
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DnsServerSecondaryZone class
- PS_DnsServerSecondaryZone class, described
topic_type:
- apiref
api_name:
- PS_DnsServerSecondaryZone
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PS\_DnsServerSecondaryZone class

DNS Server Secondary Zone definition.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class PS_DnsServerSecondaryZone
{
};
```

## Members

The **PS\_DnsServerSecondaryZone** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DnsServerSecondaryZone** class has these methods.



| Method                                                                             | Description                                                            |
|:-----------------------------------------------------------------------------------|:-----------------------------------------------------------------------|
| [**AddByForwardLookupZone**](addbyforwardlookupzone-ps-dnsserversecondaryzone.md) | Creates a standard secondary zone.<br/>                          |
| [**AddByReverseLookupZone**](addbyreverselookupzone-ps-dnsserversecondaryzone.md) | Creates a standard secondary zone.<br/>                          |
| [**ConvertTo**](convertto-ps-dnsserversecondaryzone.md)                           | Converts a primary zone to a secondary zone.<br/>                |
| [**Restore**](restore-ps-dnsserversecondaryzone.md)                               | Forces a secondary DNS zone to update from the master zone.<br/> |
| [**Set**](set-ps-dnsserversecondaryzone.md)                                       | Overwrites settings of DNS server secondary zone.<br/>           |



 

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

 

 





