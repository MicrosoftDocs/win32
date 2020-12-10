---
title: MicrosoftDNS_WINSType class
description: The subclass of MicrosoftDNS\_ResourceRecord that represents a Windows Internet Name Service (WINS) record.
ms.assetid: 8f891d80-ee4d-4641-8a6c-159c78e5cf86
keywords:
- MicrosoftDNS_WINSType class DNS
- MicrosoftDNS_WINSType class DNS , described
topic_type:
- apiref
api_name:
- MicrosoftDNS_WINSType
- MicrosoftDNS_WINSType.CreateInstanceFromPropertyData
- MicrosoftDNS_WINSType.Modify
- MicrosoftDNS_WINSType.MappingFlag
- MicrosoftDNS_WINSType.LookupTimeout
- MicrosoftDNS_WINSType.CacheTimeout
- MicrosoftDNS_WINSType.WinsServers
api_location:
- Root\MicrosoftDNS
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# MicrosoftDNS\_WINSType class

The subclass of [**MicrosoftDNS\_ResourceRecord**](microsoftdns-resourcerecord.md) that represents a Windows Internet Name Service (WINS) record.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
class MicrosoftDNS_WINSType : MicrosoftDNS_ResourceRecord
{
  uint32 MappingFlag;
  uint32 LookupTimeout;
  uint32 CacheTimeout;
  string WinsServers;
};
```

## Members

The **MicrosoftDNS\_WINSType** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MicrosoftDNS\_WINSType** class has these methods.



| Method                             | Description                                                                                                                                                                                                                                                                                                                                                                                                  |
|:-----------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **CreateInstanceFromPropertyData** | Instantiates a WINS Type of RR based on the data in the method's input parameters: the record's DNS Server Name, Container Name, Owner Name, class (default = IN), time-to-live value, and WINS mapping flag, look-up time out, cache time out and list of IP addresses for look up. It returns a reference to the new object as an output parameter. <br/> Qualifiers: Implemented, static<br/> |
| **Modify**                         | Updates the TTL, Mapping Flag, Look-up Time out, Cache Time out and Wins Servers to the values specified as the input parameters of this method. If a new value for a parameter is not specified, then the current value for the parameter is not changed. The method returns a reference to the modified object as an output parameter. <br/> Qualifiers: Implemented<br/>                      |



 

### Properties

The **MicrosoftDNS\_WINSType** class has these properties.

<dl> <dt>

**CacheTimeout**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Time, in seconds, that a DNS Server using WINS Look up may cache the WINS server's response.

</dd> <dt>

**LookupTimeout**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Time, in seconds, that a DNS Server attempts resolution using WINS Look up.

</dd> <dt>

**MappingFlag**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

WINS mapping flag that specifies whether the record must be included into the zone replication. It may have only two values: 0x80000000 and 0x00010000 corresponding to the replication and no-replication (local record) flags, respectively. The following values are valid.



| Value                                                                                                                                               | Meaning                                       |
|-----------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| <span id="0x80000000"></span><span id="0X80000000"></span><dl> <dt>**0x80000000**</dt> </dl> | Replication flag<br/>                   |
| <span id="0x00010000"></span><span id="0X00010000"></span><dl> <dt>**0x00010000**</dt> </dl> | No-replication (local record) flag<br/> |



 

</dd> <dt>

**WinsServers**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

List of comma-separated IP addresses of WINS servers used in WINS Look ups.

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

[**CreateInstanceFromPropertyData Method of the MicrosoftDNS\_WINSType Class**](microsoftdns-winstype-createinstancefrompropertydata.md)
</dt> <dt>

[**Modify Method of the MicrosoftDNS\_WINSType Class**](microsoftdns-winstype-modify.md)
</dt> <dt>

[**MicrosoftDNS\_ResourceRecord**](microsoftdns-resourcerecord.md)
</dt> </dl>

 

 





