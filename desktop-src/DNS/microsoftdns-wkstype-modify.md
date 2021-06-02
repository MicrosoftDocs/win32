---
title: Modify method of the MicrosoftDNS_WKSType class
description: The Modify method updates a Well-Known Services (WKS) Resource Record.
ms.assetid: 3a9100eb-dc90-45bb-9739-14026da100fd
keywords:
- Modify method DNS
- Modify method DNS , MicrosoftDNS_WKSType class
- MicrosoftDNS_WKSType class DNS , Modify method
topic_type:
- apiref
api_name:
- MicrosoftDNS_WKSType.Modify
api_location:
- Root\MicrosoftDNS
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Modify method of the MicrosoftDNS\_WKSType class

The **Modify** method updates a Well-Known Services (WKS) Resource Record.

## Syntax


```mof
void Modify(
  [in, optional] uint32               TTL,
  [in, optional] uint32               InternetAddress,
  [in, optional] uint8                IPProtocol,
  [in, optional] uint8                Services,
  [out, ref]     MicrosoftDNS_WKSType &RR
);
```



## Parameters

<dl> <dt>

*TTL* \[in, optional\]
</dt> <dd>

Time, in seconds, that the RR can be cached by a DNS resolver.

</dd> <dt>

*InternetAddress* \[in, optional\]
</dt> <dd>

Internet IP address for the record's owner.

</dd> <dt>

*IPProtocol* \[in, optional\]
</dt> <dd>

String representing the IP protocol for this record. Valid values are UDP or TCP.

</dd> <dt>

*Services* \[in, optional\]
</dt> <dd>

String containing all services used by the Well Known Service (WKS) record.

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

[**MicrosoftDNS\_WKSType**](microsoftdns-wkstype.md)
</dt> <dt>

[**CreateInstanceFromPropertyData Method of the MicrosoftDNS\_WKSType Class**](microsoftdns-wkstype-createinstancefrompropertydata.md)
</dt> <dt>

[**MicrosoftDNS\_ResourceRecord**](microsoftdns-resourcerecord.md)
</dt> </dl>

 

 





