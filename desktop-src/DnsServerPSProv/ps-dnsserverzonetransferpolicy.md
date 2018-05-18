---
title: PS\_DnsServerZoneTransferPolicy class
description: DNS Server zone transfer policy.
audience: developer
ms.assetid: 'bf6ce530-699a-489c-84c9-a479c88672f9'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["PS_DnsServerZoneTransferPolicy class", "PS_DnsServerZoneTransferPolicy class, described"]
topic_type:
- apiref
api_name:
- PS_DnsServerZoneTransferPolicy
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
---

# PS\_DnsServerZoneTransferPolicy class

DNS Server zone transfer policy.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class PS_DnsServerZoneTransferPolicy
{
};
```

## Members

The **PS\_DnsServerZoneTransferPolicy** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DnsServerZoneTransferPolicy** class has these methods.



| Method                                                                      | Description                                                  |
|:----------------------------------------------------------------------------|:-------------------------------------------------------------|
| [**AddByInputObject**](addbyinputobject-ps-dnsserverzonetransferpolicy.md) | Adds a new zone transfer policy by input object.<br/>  |
| [**AddByServer**](addbyserver-ps-dnsserverzonetransferpolicy.md)           | Adds a new zone transfer policy by server.<br/>        |
| [**AddByZone**](addbyzone-ps-dnsserverzonetransferpolicy.md)               | Adds a new zone transfer policy by zone.<br/>          |
| [**GetByServer**](getbyserver-ps-dnsserverzonetransferpolicy.md)           | Enumerates the zone transfer policy by server.<br/>    |
| [**GetByZone**](getbyzone-ps-dnsserverzonetransferpolicy.md)               | Enumerates the zone transfer policy by zone.<br/>      |
| [**RemoveByServer**](removebyserver-ps-dnsserverzonetransferpolicy.md)     | Removes a zone transfer policy by server.<br/>         |
| [**RemoveByZone**](removebyzone-ps-dnsserverzonetransferpolicy.md)         | Removes a zone transfer policy by zone.<br/>           |
| [**SetByInputObject**](setbyinputobject-ps-dnsserverzonetransferpolicy.md) | Edits a new zone transfer policy by input object.<br/> |
| [**SetByServer**](setbyserver-ps-dnsserverzonetransferpolicy.md)           | Edits a new zone transfer policy by server.<br/>       |
| [**SetByZone**](setbyzone-ps-dnsserverzonetransferpolicy.md)               | Edits a new zone transfer policy by zone.<br/>         |



 

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[DnsServerPSProvider Provider](dns-server-classes.md)
</dt> </dl>

 

 





