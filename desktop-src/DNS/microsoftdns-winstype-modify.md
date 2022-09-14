---
title: Modify method of the MicrosoftDNS_WINSType class
description: The Modify method updates a Windows Internet Name Service (WINS) Resource Record.
ms.assetid: b61c429a-6b01-4b17-9312-bc5b69d1e76a
keywords:
- Modify method DNS
- Modify method DNS , MicrosoftDNS_WINSType class
- MicrosoftDNS_WINSType class DNS , Modify method
topic_type:
- apiref
api_name:
- MicrosoftDNS_WINSType.Modify
api_location:
- Root\MicrosoftDNS
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Modify method of the MicrosoftDNS\_WINSType class

The **Modify** method updates a Windows Internet Name Service (WINS) Resource Record.

## Syntax


```mof
void Modify(
  [in, optional] uint32                TTL,
  [in, optional] uint32                MappingFlag,
  [in, optional] uint32                LookupTimeout,
  [in, optional] uint32                CacheTimeout,
  [in, optional] string                WinsServers,
  [out, ref]     MicrosoftDNS_WINSType &RR
);
```



## Parameters

<dl> <dt>

*TTL* \[in, optional\]
</dt> <dd>

Time, in seconds, that the RR can be cached by a DNS resolver.

</dd> <dt>

*MappingFlag* \[in, optional\]
</dt> <dd>

WINS mapping flag that specifies whether the record must be included into the zone replication. It may have only two values: 0x80000000 and 0x00010000 corresponding to the replication and no-replication (local record) flags, respectively. The following values are valid.



| Value                                                                                                                                               | Meaning                                       |
|-----------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| <span id="0x80000000"></span><span id="0X80000000"></span><dl> <dt>**0x80000000**</dt> </dl> | Replication flag<br/>                   |
| <span id="0x00010000"></span><span id="0X00010000"></span><dl> <dt>**0x00010000**</dt> </dl> | No-replication (local record) flag<br/> |



 

</dd> <dt>

*LookupTimeout* \[in, optional\]
</dt> <dd>

Time, in seconds, that a DNS Server attempts resolution using WINS Look up.

</dd> <dt>

*CacheTimeout* \[in, optional\]
</dt> <dd>

Time, in seconds, that a DNS Server using WINS Look up may cache the WINS server's response.

</dd> <dt>

*WinsServers* \[in, optional\]
</dt> <dd>

List of comma-separated IP addresses of WINS servers used in WINS Look ups.

</dd> <dt>

*RR* \[out, ref\]
</dt> <dd>

Reference to the new object.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

Any parameter not specified is left unchanged in the modified record.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| Namespace<br/>                | Root\\MicrosoftDNS<br/>                                                          |
| MOF<br/>                      | <dl> <dt>Dnsprov.mof</dt> </dl> |



## See also

<dl> <dt>

[**MicrosoftDNS\_WINSType**](microsoftdns-winstype.md)
</dt> <dt>

[**CreateInstanceFromPropertyData Method of the MicrosoftDNS\_WINSType Class**](microsoftdns-winstype-createinstancefrompropertydata.md)
</dt> <dt>

[**MicrosoftDNS\_ResourceRecord**](microsoftdns-resourcerecord.md)
</dt> </dl>

 

 





