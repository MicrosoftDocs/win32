---
title: Set method of the PS\_DnsServerEDns class
description: Sets DNS server EDns settings.
audience: developer
ms.assetid: 'fe890e40-db85-4c2a-b2eb-f369f958bbe5'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Set method", "Set method, PS_DnsServerEDns class", "PS_DnsServerEDns class, Set method"]
topic_type:
- apiref
api_name:
- PS_DnsServerEDns.Set
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# Set method of the PS\_DnsServerEDns class

Sets DNS server EDns settings.

## Syntax


```mof
uint32 Set(
  [in]  datetime      CacheTimeout,
  [in]  boolean       EnableProbes,
  [in]  boolean       EnableReception,
  [in]  string        ComputerName,
  [in]  boolean       PassThru,
  [out] DnsServerEDns cmdletOutput
);
```



## Parameters

<dl> <dt>

*CacheTimeout* \[in\]
</dt> <dd>

Specifies the number of seconds that EDns information is cached. The default value is 604,800 seconds (one week). Range = 10 to 86400.

</dd> <dt>

*EnableProbes* \[in\]
</dt> <dd>

Enables or disables EDnsProbes.

<dt>

0
</dt> <dd>

Disables active support for EDnsProbes.

</dd> <dt>

1
</dt> <dd>

Enables active support for EDnsProbes.

</dd> </dl> </dd> <dt>

*EnableReception* \[in\]
</dt> <dd>

**true** to enable EDNS reception; **false** to disable reception.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**true** to return the current instance in the *CmdletOutput* parameter. The default is **false**.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

On return, contains an instance of the current object. This parameter returns a value only if *PassThru* is set to **true.**

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsServerEDns**](ps-dnsserveredns.md)
</dt> </dl>

 

 





