---
title: AddByDS method of the PS\_DnsServerTrustAnchor class
description: Adds a trust anchor DNSKEY record. If there is no trust anchor zone present, the cmdlet should create one. If neither SecureEntryPoint nor ZoneSigningKey are specified, then the cmdlet creates a trust anchor with SEP bit set.
audience: developer
ms.assetid: 64167ef7-6e71-4e77-8e79-a300e381e992
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AddByDS method
- AddByDS method, PS_DnsServerTrustAnchor class
- PS_DnsServerTrustAnchor class, AddByDS method
topic_type:
- apiref
api_name:
- PS_DnsServerTrustAnchor.AddByDS
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AddByDS method of the PS\_DnsServerTrustAnchor class

Adds a trust anchor DNSKEY record. If there is no trust anchor zone present, the cmdlet should create one. If neither SecureEntryPoint nor ZoneSigningKey are specified, then the cmdlet creates a trust anchor with SEP bit set.

## Syntax


```mof
uint32 AddByDS(
  [in]  string               Name,
  [in]  string               ComputerName,
  [in]  uint16               KeyTag,
  [in]  string               DigestType,
  [in]  string               Digest,
  [in]  string               CryptoAlgorithm,
  [in]  boolean              PassThru,
  [out] DnsServerTrustAnchor cmdletOutput
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

Name of the trust anchor.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Optional DNS server name.

</dd> <dt>

*KeyTag* \[in\]
</dt> <dd>

Specifies the unique key tag that the DNS server uses to identify a key.

</dd> <dt>

*DigestType* \[in\]
</dt> <dd>

Specifies the type of algorithm that the zone signing key uses to create the DS record. Valid values are one or more of the following: Sha1, Sha256, or Sha384.

</dd> <dt>

*Digest* \[in\]
</dt> <dd>

The DS digest data.

</dd> <dt>

*CryptoAlgorithm* \[in\]
</dt> <dd>

Cryptographic algorithm used for key generation.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**True** to return the object that was modified by the method. By default, this method does not generate any output.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

Receives an embedded instance of the [**DnsServerTrustAnchor**](dnsservertrustanchor.md) class.

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

[**PS\_DnsServerTrustAnchor**](ps-dnsservertrustanchor.md)
</dt> </dl>

 

 





