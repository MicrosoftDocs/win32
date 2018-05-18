---
title: SetByParameters method of the PS\_DnsServerConditionalForwarder class
description: Sets DNS server Conditional Forwarder settings.
audience: developer
ms.assetid: '871a9afe-f950-4113-ae7e-5b9fcb77b101'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["SetByParameters method", "SetByParameters method, PS_DnsServerConditionalForwarder class", "PS_DnsServerConditionalForwarder class, SetByParameters method"]
topic_type:
- apiref
api_name:
- PS_DnsServerConditionalForwarder.SetByParameters
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# SetByParameters method of the PS\_DnsServerConditionalForwarder class

Sets DNS server Conditional Forwarder settings.

## Syntax


```mof
uint32 SetByParameters(
  [in]  boolean                           UseRecursion,
  [in]  string                            MasterServers[],
  [in]  uint32                            ForwarderTimeout,
  [in]  string                            Name,
  [in]  string                            ComputerName,
  [in]  boolean                           PassThru,
  [out] DnsServerConditionalForwarderZone cmdletOutput
);
```



## Parameters

<dl> <dt>

*UseRecursion* \[in\]
</dt> <dd>

Overrides the DNS server UseRecursion setting.

</dd> <dt>

*MasterServers* \[in\]
</dt> <dd>

Specifies the addresses of the master servers.

</dd> <dt>

*ForwarderTimeout* \[in\]
</dt> <dd>

Indicates the time, in seconds, a DNS server forwarding a query for the name under the forward zone waits for resolution from the forwarder before attempting to resolve the query itself. This parameter is applicable to the Forward zones only. Range = 0 to 15.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Specifies the name of the zone.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**True** to return the object that was modified by the method. By default, this method does not generate any output.

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

[**PS\_DnsServerConditionalForwarder**](ps-dnsserverconditionalforwarder.md)
</dt> </dl>

 

 





