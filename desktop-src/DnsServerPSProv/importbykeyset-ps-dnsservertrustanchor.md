---
title: ImportByKeySet method of the PS\_DnsServerTrustAnchor class
description: Imports DNS server Trust anchors from specified files.
audience: developer
ms.assetid: 1ec5a3e6-9a5d-4e52-a14a-0224e579be4e
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ImportByKeySet method
- ImportByKeySet method, PS_DnsServerTrustAnchor class
- PS_DnsServerTrustAnchor class, ImportByKeySet method
topic_type:
- apiref
api_name:
- PS_DnsServerTrustAnchor.ImportByKeySet
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ImportByKeySet method of the PS\_DnsServerTrustAnchor class

Imports DNS server Trust anchors from specified files.

## Syntax


```mof
uint32 ImportByKeySet(
  [in]  string               ComputerName,
  [in]  string               KeySetFile,
  [in]  boolean              PassThru,
  [out] DnsServerTrustAnchor cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

Optional DNS server name. The acceptable values for this parameter are: an IP address or any value that resolves to an IP address, such as a fully qualified domain name (FQDN), host name, or NETBIOS name.

</dd> <dt>

*KeySetFile* \[in\]
</dt> <dd>

File path of the keyset file.

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

 

 





