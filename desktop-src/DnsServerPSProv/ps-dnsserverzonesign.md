---
title: PS\_DnsServerZoneSign class
description: DNS Server Zone Sign Task Definition.
audience: developer
ms.assetid: 'baf9db9e-1166-4a80-a397-18afef2f54a5'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["PS_DnsServerZoneSign class", "PS_DnsServerZoneSign class, described"]
topic_type:
- apiref
api_name:
- PS_DnsServerZoneSign
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
---

# PS\_DnsServerZoneSign class

DNS Server Zone Sign Task Definition.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class PS_DnsServerZoneSign
{
};
```

## Members

The **PS\_DnsServerZoneSign** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DnsServerZoneSign** class has these methods.



| Method                                        | Description                               |
|:----------------------------------------------|:------------------------------------------|
| [**Invoke**](invoke-ps-dnsserverzonesign.md) | Initiates signing on the zone.<br/> |



 

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

 

 





