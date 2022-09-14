---
title: GetObjectByTextRepresentation method of the MicrosoftDNS_ResourceRecord class
description: The GetObjectByTextRepresentation method retrieves an existing instance of the MicrosoftDNS\_ResourceRecord class.
ms.assetid: d25e10de-81fa-4220-b2b8-d9a65298b629
keywords:
- GetObjectByTextRepresentation method DNS
- GetObjectByTextRepresentation method DNS , MicrosoftDNS_ResourceRecord class
- MicrosoftDNS_ResourceRecord class DNS , GetObjectByTextRepresentation method
topic_type:
- apiref
api_name:
- MicrosoftDNS_ResourceRecord.GetObjectByTextRepresentation
api_location:
- Root\MicrosoftDNS
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# GetObjectByTextRepresentation method of the MicrosoftDNS\_ResourceRecord class

The **GetObjectByTextRepresentation** method retrieves an existing instance of the [**MicrosoftDNS\_ResourceRecord**](microsoftdns-resourcerecord.md) class.

## Syntax


```mof
void GetObjectByTextRepresentation(
  [in]  string                      DnsServerName,
  [in]  string                      ContainerName,
  [in]  string                      TextRepresentation,
  [out] MicrosoftDns_ResourceRecord RR
);
```



## Parameters

<dl> <dt>

*DnsServerName* \[in\]
</dt> <dd>

Name of the DNS Server from which the RR should be retrieved.

</dd> <dt>

*ContainerName* \[in\]
</dt> <dd>

Name of the container from which the RR should be obtained.

</dd> <dt>

*TextRepresentation* \[in\]
</dt> <dd>

Text representation of the RR to be retrieved.

</dd> <dt>

*RR* \[out\]
</dt> <dd>

Reference to the instantiated RR.

</dd> </dl>

## Return value

This method does not return a value.

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

[**CreateInstanceFromTextRepresentation Method of the MicrosoftDNS\_ResourceRecord Class**](microsoftdns-resourcerecord-createinstancefromtextrepresentation.md)
</dt> </dl>

 

 





