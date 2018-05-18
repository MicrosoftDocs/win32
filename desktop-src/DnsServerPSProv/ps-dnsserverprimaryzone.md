---
title: PS\_DnsServerPrimaryZone class
description: DNS Server Primary Zone definition.
audience: developer
ms.assetid: '94c84eed-1872-46a4-b7aa-f40a82faf6b7'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["PS_DnsServerPrimaryZone class", "PS_DnsServerPrimaryZone class, described"]
topic_type:
- apiref
api_name:
- PS_DnsServerPrimaryZone
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
---

# PS\_DnsServerPrimaryZone class

DNS Server Primary Zone definition.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class PS_DnsServerPrimaryZone
{
};
```

## Members

The **PS\_DnsServerPrimaryZone** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DnsServerPrimaryZone** class has these methods.



| Method                                                                                   | Description                                                |
|:-----------------------------------------------------------------------------------------|:-----------------------------------------------------------|
| [**AddByADForwardLookupZone**](addbyadforwardlookupzone-ps-dnsserverprimaryzone.md)     | Adss Primary zone on DNS server<br/>                 |
| [**AddByADReverseLookupZone**](addbyadreverselookupzone-ps-dnsserverprimaryzone.md)     | Adds Primary zone on DNS server<br/>                 |
| [**AddByFileForwardLookupZone**](addbyfileforwardlookupzone-ps-dnsserverprimaryzone.md) | Adss Primary zone on DNS server<br/>                 |
| [**AddByFileReverseLookupZone**](addbyfilereverselookupzone-ps-dnsserverprimaryzone.md) | Adss Primary zone on DNS server<br/>                 |
| [**ConvertToByADZone**](converttobyadzone-ps-dnsserverprimaryzone.md)                   | Converts a zone to DNS server primary zone<br/>      |
| [**ConvertToByFileZone**](converttobyfilezone-ps-dnsserverprimaryzone.md)               | Converts a zone to DNS server primary zone<br/>      |
| [**Restore**](restore-ps-dnsserverprimaryzone.md)                                       | Copies zone information from its source.<br/>        |
| [**SetByADZone**](setbyadzone-ps-dnsserverprimaryzone.md)                               | Overwrites settings of DNS server primary zone.<br/> |
| [**SetByFileZone**](setbyfilezone-ps-dnsserverprimaryzone.md)                           | Overwrites settings of DNS server primary zone.<br/> |
| [**SetByParameters**](setbyparameters-ps-dnsserverprimaryzone.md)                       | Overwrites settings of DNS server primary zone.<br/> |



 

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

 

 





