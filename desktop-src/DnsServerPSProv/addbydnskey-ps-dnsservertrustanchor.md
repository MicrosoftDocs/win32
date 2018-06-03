---
title: AddByDnsKey method of the PS\_DnsServerTrustAnchor class
description: Adds a trust anchor with the specified key information to a DNS server.
audience: developer
ms.assetid: 646e0b50-8322-4ec0-88b3-68e6cfb6c581
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AddByDnsKey method
- AddByDnsKey method, PS_DnsServerTrustAnchor class
- PS_DnsServerTrustAnchor class, AddByDnsKey method
topic_type:
- apiref
api_name:
- PS_DnsServerTrustAnchor.AddByDnsKey
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AddByDnsKey method of the PS\_DnsServerTrustAnchor class

Adds a trust anchor with the specified key information to a DNS server.

## Syntax


```mof
uint32 AddByDnsKey(
  [in]  string               Name,
  [in]  string               KeyProtocol,
  [in]  string               Base64Data,
  [in]  string               ComputerName,
  [in]  string               CryptoAlgorithm,
  [in]  boolean              PassThru,
  [out] DnsServerTrustAnchor cmdletOutput
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The name of the trust anchor.

</dd> <dt>

*KeyProtocol* \[in\]
</dt> <dd>

The protocol name. The default value is DNSSEC.

</dd> <dt>

*Base64Data* \[in\]
</dt> <dd>

The key data.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Optional DNS server name.

</dd> <dt>

*CryptoAlgorithm* \[in\]
</dt> <dd>

Cryptographic algorithm to use for key generation.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Returns an object representing the item with which you are working. By default, this method does not generate any output.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The output type is the type of the objects that the method emits.

Microsoft.Management.Infrastructure.CimInstance\#DnsServerTrustAnchor

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

 

 





