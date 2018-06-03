---
title: GetByServer method of the PS\_DnsServerZoneTransferPolicy class
description: Enumerates a zone transfer policy by server.
audience: developer
ms.assetid: 841f3b02-ca70-45b6-af92-54e1f78e684b
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetByServer method
- GetByServer method, PS_DnsServerZoneTransferPolicy class
- PS_DnsServerZoneTransferPolicy class, GetByServer method
topic_type:
- apiref
api_name:
- PS_DnsServerZoneTransferPolicy.GetByServer
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetByServer method of the PS\_DnsServerZoneTransferPolicy class

Enumerates a zone transfer policy by server.

## Syntax


```mof
uint32 GetByServer(
  [in]  string          Name,
  [in]  string          ComputerName,
  [out] DnsServerPolicy cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

Name of the policy to retrieve.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Optional DNS server name.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

On return, contains an array of [**DnsServerPolicy**](dnsserverpolicy.md). This parameter returns a value only if *PassThru* is set to **true.**

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsServerZoneTransferPolicy**](ps-dnsserverzonetransferpolicy.md)
</dt> </dl>

 

 





