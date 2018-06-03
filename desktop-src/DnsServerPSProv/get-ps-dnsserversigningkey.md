---
title: Get method of the PS\_DnsServerSigningKey class
description: Retrieves Zone signing key.
audience: developer
ms.assetid: f38053c0-c19d-465c-8f7d-6cb0a5a352a9
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_DnsServerSigningKey class
- PS_DnsServerSigningKey class, Get method
topic_type:
- apiref
api_name:
- PS_DnsServerSigningKey.Get
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Get method of the PS\_DnsServerSigningKey class

Retrieves Zone signing key.

## Syntax


```mof
uint32 Get(
  [in]  string              ZoneName,
  [in]  string              KeyId[],
  [in]  string              ComputerName,
  [out] DnsServerSigningKey cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ZoneName* \[in\]
</dt> <dd>

Name of the zone on which DnsSec operations are performed.

</dd> <dt>

*KeyId* \[in\]
</dt> <dd>

Uniquely identifies the key.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Optional DNS server name.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DnsServerSigningKey**](dnsserversigningkey.md) class.

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

[**PS\_DnsServerSigningKey**](ps-dnsserversigningkey.md)
</dt> </dl>

 

 





