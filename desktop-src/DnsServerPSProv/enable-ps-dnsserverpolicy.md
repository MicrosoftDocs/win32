---
title: Enable method of the PS\_DNSServerPolicy class
description: Enables a DNS server policy.
audience: developer
ms.assetid: 89956216-64f0-4a31-95eb-1e9324bc354c
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Enable method
- Enable method, PS_DNSServerPolicy class
- PS_DNSServerPolicy class, Enable method
topic_type:
- apiref
api_name:
- PS_DNSServerPolicy.Enable
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Enable method of the PS\_DNSServerPolicy class

Enables a DNS server policy.

## Syntax


```mof
uint32 Enable(
  [in] string  Level,
  [in] string  Name,
  [in] string  ComputerName,
  [in] string  ZoneName,
  [in] boolean Force
);
```



## Parameters

<dl> <dt>

*Level* \[in\]
</dt> <dd>

The level of the policy.

<dt>

Server
</dt> <dd>

The policy applies to a single server.

</dd> <dt>

Zone
</dt> <dd>

The policy applies to a zone.

</dd> </dl> </dd> <dt>

*Name* \[in\]
</dt> <dd>

Name of the policy.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Optional DNS server name.

</dd> <dt>

*ZoneName* \[in\]
</dt> <dd>

The name of the zone.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

If specified, overrides the default confirmation before performing the operation.

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

[**PS\_DNSServerPolicy**](ps-dnsserverpolicy.md)
</dt> </dl>

 

 





