---
title: PS\_DnsServerZoneTransfer class
description: DNS Server Zone Transfer definition.
audience: developer
ms.assetid: 'e6f91dae-32eb-4b3f-bfdf-d2fbd12ba0bf'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["PS_DnsServerZoneTransfer class", "PS_DnsServerZoneTransfer class, described"]
topic_type:
- apiref
api_name:
- PS_DnsServerZoneTransfer
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
---

# PS\_DnsServerZoneTransfer class

DNS Server Zone Transfer definition.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class PS_DnsServerZoneTransfer
{
};
```

## Members

The **PS\_DnsServerZoneTransfer** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DnsServerZoneTransfer** class has these methods.



| Method                                          | Description                                                   |
|:------------------------------------------------|:--------------------------------------------------------------|
| [**Start**](start-ps-dnsserverzonetransfer.md) | Starts DNS Zone transfer from Primary to Secondary<br/> |



 

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[DnsServerPSProvider Provider](dns-server-classes.md)
</dt> </dl>

 

 





