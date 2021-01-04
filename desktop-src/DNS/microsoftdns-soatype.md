---
title: MicrosoftDNS_SOAType class
description: The subclass of MicrosoftDNS\_ResourceRecord that represents a Start Of Authority (SOA) record.
ms.assetid: a5e6b6d3-7f5d-42e2-b3ed-2786f7aafb14
keywords:
- MicrosoftDNS_SOAType class DNS
- MicrosoftDNS_SOAType class DNS , described
topic_type:
- apiref
api_name:
- MicrosoftDNS_SOAType
- MicrosoftDNS_SOAType.Modify
- MicrosoftDNS_SOAType.SerialNumber
- MicrosoftDNS_SOAType.PrimaryServer
- MicrosoftDNS_SOAType.ResponsibleParty
- MicrosoftDNS_SOAType.RefreshInterval
- MicrosoftDNS_SOAType.RetryDelay
- MicrosoftDNS_SOAType.ExpireLimit
- MicrosoftDNS_SOAType.MinimumTTL
api_location:
- Root\MicrosoftDNS
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# MicrosoftDNS\_SOAType class

The subclass of [**MicrosoftDNS\_ResourceRecord**](microsoftdns-resourcerecord.md) that represents a Start Of Authority (SOA) record.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
class MicrosoftDNS_SOAType : MicrosoftDNS_ResourceRecord
{
  uint32 SerialNumber;
  string PrimaryServer;
  string ResponsibleParty;
  uint32 RefreshInterval;
  uint32 RetryDelay;
  uint32 ExpireLimit;
  uint32 MinimumTTL;
};
```

## Members

The **MicrosoftDNS\_SOAType** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MicrosoftDNS\_SOAType** class has these methods.



| Method     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|:-----------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Modify** | Updates the TTL, SOA Serial Number, Primary Server, Responsible Party, Refresh Interval, Retry Delay, Expire Limit and Minimum TTL (for the zone) to the values specified as the input parameters of this method. If a new value for a parameter is not specified, then the current value for the parameter is not changed. The method returns a reference to the modified object as an output parameter. <br/> Qualifiers: Implemented<br/> |



 

### Properties

The **MicrosoftDNS\_SOAType** class has these properties.

<dl> <dt>

**ExpireLimit**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Time, in seconds, before an unresponsive zone is no longer authoritative.

</dd> <dt>

**MinimumTTL**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Lower limit on the time, in seconds, that a DNS Server or Caching resolver are allowed to cache any resource record from the zone to which this record belongs.

</dd> <dt>

**PrimaryServer**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Authoritative DNS Server for the zone to which the record belongs.

</dd> <dt>

**RefreshInterval**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Time, in seconds, before the zone containing this record should be refreshed.

</dd> <dt>

**ResponsibleParty**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the responsible party for the zone to which the record belongs.

</dd> <dt>

**RetryDelay**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Time, in seconds, before retrying a failed refresh of the zone to which this record belongs.

</dd> <dt>

**SerialNumber**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Serial number of the SOA record.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| Namespace<br/>                | Root\\MicrosoftDNS<br/>                                                          |
| MOF<br/>                      | <dl> <dt>Dnsprov.mof</dt> </dl> |



## See also

<dl> <dt>

[**MicrosoftDNS\_ResourceRecord**](microsoftdns-resourcerecord.md)
</dt> <dt>

[**Modify Method of the MicrosoftDNS\_SOAType Class**](microsoftdns-soatype-modify.md)
</dt> </dl>

 

 





