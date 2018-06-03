---
title: ImportByDSSet method of the PS\_DnsServerTrustAnchor class
description: Imports a DNS server Trust anchor from a specified file.
audience: developer
ms.assetid: 33e26aa9-c571-43c8-9130-e883de4d2cc7
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ImportByDSSet method
- ImportByDSSet method, PS_DnsServerTrustAnchor class
- PS_DnsServerTrustAnchor class, ImportByDSSet method
topic_type:
- apiref
api_name:
- PS_DnsServerTrustAnchor.ImportByDSSet
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ImportByDSSet method of the PS\_DnsServerTrustAnchor class

Imports a DNS server Trust anchor from a specified file.

## Syntax


```mof
uint32 ImportByDSSet(
  [in]  string               ComputerName,
  [in]  string               DSSetFile,
  [in]  boolean              PassThru,
  [out] DnsServerTrustAnchor cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

An optional DNS server name. The acceptable values for this parameter are: an IP address or any value that resolves to an IP address, such as a fully qualified domain name (FQDN), host name, or NETBIOS name.

</dd> <dt>

*DSSetFile* \[in\]
</dt> <dd>

File path of the DSset file.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**True** to return the object that was modified by the method. By default, this method does not generate any output.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

Receives and embedded instance of the [**DnsServerTrustAnchor**](dnsservertrustanchor.md) class.

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

 

 





