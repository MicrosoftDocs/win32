---
title: Update method of the PS\_DnsServerTrustPoint class
description: Initiates active refresh of all trust points in the trust anchor zone.
audience: developer
ms.assetid: f47896eb-55bb-48e0-877c-36dd859ab15b
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Update method
- Update method, PS_DnsServerTrustPoint class
- PS_DnsServerTrustPoint class, Update method
topic_type:
- apiref
api_name:
- PS_DnsServerTrustPoint.Update
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Update method of the PS\_DnsServerTrustPoint class

Initiates active refresh of all trust points in the trust anchor zone.

## Syntax


```mof
uint32 Update(
  [in] boolean Force,
  [in] string  ComputerName
);
```



## Parameters

<dl> <dt>

*Force* \[in\]
</dt> <dd>

If specified, overrides the default confirmation request before proceeding with active refresh of trust points.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Optional DNS server name.

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

[**PS\_DnsServerTrustPoint**](ps-dnsservertrustpoint.md)
</dt> </dl>

 

 





