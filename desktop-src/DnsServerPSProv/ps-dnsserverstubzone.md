---
title: PS\_DnsServerStubZone class
description: DNS Server Stub Zone definition.
audience: developer
ms.assetid: '903abf0d-06a0-45cd-94ea-d00af191405f'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["PS_DnsServerStubZone class", "PS_DnsServerStubZone class, described"]
topic_type:
- apiref
api_name:
- PS_DnsServerStubZone
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
---

# PS\_DnsServerStubZone class

DNS Server Stub Zone definition.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class PS_DnsServerStubZone
{
};
```

## Members

The **PS\_DnsServerStubZone** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DnsServerStubZone** class has these methods.



| Method                                                                                | Description                                                                                        |
|:--------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------|
| [**AddByADForwardLookupZone**](addbyadforwardlookupzone-ps-dnsserverstubzone.md)     | Adds stub zone<br/>                                                                          |
| [**AddByADReverseLookupZone**](addbyadreverselookupzone-ps-dnsserverstubzone.md)     | Adds stub zone<br/>                                                                          |
| [**AddByFileForwardLookupZone**](addbyfileforwardlookupzone-ps-dnsserverstubzone.md) | Adds stub zone<br/>                                                                          |
| [**AddByFileReverseLookupZone**](addbyfilereverselookupzone-ps-dnsserverstubzone.md) | Adds stub zone<br/>                                                                          |
| [**SetByADZone**](setbyadzone-ps-dnsserverstubzone.md)                               | Overwrites settings of DNS server stub zone. If none exists exit with terminating error<br/> |
| [**SetByParameter**](setbyparameter-ps-dnsserverstubzone.md)                         | Overwrites settings of DNS server stub zone. If none exists exit with terminating error<br/> |



 

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

 

 





