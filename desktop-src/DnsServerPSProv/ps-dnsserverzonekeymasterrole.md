---
title: PS\_DnsServerZoneKeyMasterRole class
description: DNS Server Zone Key Master Server Task Definition.
audience: developer
ms.assetid: '7dd411b4-1884-4ebd-8b35-459c20b25a27'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["PS_DnsServerZoneKeyMasterRole class", "PS_DnsServerZoneKeyMasterRole class, described"]
topic_type:
- apiref
api_name:
- PS_DnsServerZoneKeyMasterRole
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
---

# PS\_DnsServerZoneKeyMasterRole class

DNS Server Zone Key Master Server Task Definition.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class PS_DnsServerZoneKeyMasterRole
{
};
```

## Members

The **PS\_DnsServerZoneKeyMasterRole** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DnsServerZoneKeyMasterRole** class has these methods.



| Method                                               | Description                                                               |
|:-----------------------------------------------------|:--------------------------------------------------------------------------|
| [**Reset**](reset-ps-dnsserverzonekeymasterrole.md) | Performs a key master role transfer for an AD integrated zone.<br/> |



 

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

 

 





