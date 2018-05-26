---
title: AddByRoot method of the PS\_DnsServerTrustAnchor class
description: Adds a trust anchor DNSKEY record.
audience: developer
ms.assetid: ba8c686d-fd08-487f-b997-6d5d48f68e8a
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AddByRoot method
- AddByRoot method, PS_DnsServerTrustAnchor class
- PS_DnsServerTrustAnchor class, AddByRoot method
topic_type:
- apiref
api_name:
- PS_DnsServerTrustAnchor.AddByRoot
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# AddByRoot method of the PS\_DnsServerTrustAnchor class

Adds a trust anchor DNSKEY record. If there is no trust anchor zone present, the cmdlet should create one. If neither SecureEntryPoint nor ZoneSigningKey are specified, then the cmdlet creates a trust anchor with SEP bit set.

## Syntax


```mof
uint32 AddByRoot(
  [in]  string               ComputerName,
  [in]  boolean              PassThru,
  [in]  boolean              Root,
  [out] DnsServerTrustAnchor cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

Optional DNS server name.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If specified, returns the object or objects on which the operation was done.

</dd> <dt>

*Root* \[in\]
</dt> <dd>

The root.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DnsServerTrustAnchor**](dnsservertrustanchor.md) class.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsServerTrustAnchor**](ps-dnsservertrustanchor.md)
</dt> </dl>

 

 





