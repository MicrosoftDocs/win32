---
title: Disable method of the PS\_DNSServerPolicy class
description: Disables a DNS server policy.
audience: developer
ms.assetid: 'f7441c92-0645-4f96-8c9a-7b60c8e2374f'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Disable method", "Disable method, PS_DNSServerPolicy class", "PS_DNSServerPolicy class, Disable method"]
topic_type:
- apiref
api_name:
- PS_DNSServerPolicy.Disable
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# Disable method of the PS\_DNSServerPolicy class

Disables a DNS server policy.

## Syntax


```mof
uint32 Disable(
  [in] string  Level,
  [in] string  Name,
  [in] string  ComputerName,
  [in] boolean Force,
  [in] string  ZoneName
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

*Force* \[in\]
</dt> <dd>

If specified, overrides the default confirmation before performing the operation.

</dd> <dt>

*ZoneName* \[in\]
</dt> <dd>

Name of the zone.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DNSServerPolicy**](ps-dnsserverpolicy.md)
</dt> </dl>

 

 





