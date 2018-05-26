---
title: Add method of the PS\_DnsServerResourceRecordDnsKey class
description: Adds a DNSKEY record.
audience: developer
ms.assetid: dfec3ba3-1f58-475d-92c4-217a9c0f9cad
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Add method
- Add method, PS_DnsServerResourceRecordDnsKey class
- PS_DnsServerResourceRecordDnsKey class, Add method
topic_type:
- apiref
api_name:
- PS_DnsServerResourceRecordDnsKey.Add
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Add method of the PS\_DnsServerResourceRecordDnsKey class

Adds a DNSKEY record.

## Syntax


```mof
uint32 Add(
  [in]  string                  Name,
  [in]  string                  CryptoAlgorithm,
  [in]  string                  ZoneName,
  [in]  datetime                TimeToLive,
  [in]  boolean                 AgeRecord,
  [in]  string                  Base64Data,
  [in]  string                  KeyProtocol,
  [in]  string                  ComputerName,
  [in]  boolean                 SecureEntryPoint,
  [in]  boolean                 ZoneKey,
  [in]  boolean                 PassThru,
  [in]  string                  ZoneScope,
  [out] DnsServerResourceRecord cmdletOutput
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The name of the resource record.

</dd> <dt>

*CryptoAlgorithm* \[in\]
</dt> <dd>

Cryptographic algorithm used for key generation.

</dd> <dt>

*ZoneName* \[in\]
</dt> <dd>

Name of the DNS zone where the record is added.

</dd> <dt>

*TimeToLive* \[in\]
</dt> <dd>

Specifies the life time of the record in DNS cache.

</dd> <dt>

*AgeRecord* \[in\]
</dt> <dd>

When specified creates a record with aging set.

</dd> <dt>

*Base64Data* \[in\]
</dt> <dd>

Specifies key data for this resource record.

</dd> <dt>

*KeyProtocol* \[in\]
</dt> <dd>

Specifies the key protocol for this resource record. The only value for this parameter is DnsSec.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies a DNS server. If you do not specify this parameter, the command runs on the local system. You can specify an IP address or any value that resolves to an IP address, such as a fully qualified domain name (FQDN), host name, or NETBIOS name.

</dd> <dt>

*SecureEntryPoint* \[in\]
</dt> <dd>

Specifies whether the key is a Secure entry point key or not as per RFC 3757.

</dd> <dt>

*ZoneKey* \[in\]
</dt> <dd>

Specifies whether this key will be used to sign the zone( either KSK or ZSK).

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**true** to return the object that was modified by the method. By default, this method does not generate any output.

</dd> <dt>

*ZoneScope* \[in\]
</dt> <dd>

Name of the zone scope.

**Windows Server 2012:** Not supported.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

Receives and embedded instance of the [**DnsServerResourceRecordDnsKey**](dnsserverresourcerecorddnskey.md) class.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsServerResourceRecordDnsKey**](ps-dnsserverresourcerecorddnskey.md)
</dt> </dl>

 

 





