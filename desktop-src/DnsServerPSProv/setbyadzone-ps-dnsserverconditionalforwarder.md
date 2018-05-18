---
title: SetByADZone method of the PS\_DnsServerConditionalForwarder class
description: Sets DNS server Conditional Forwarder settings.
audience: developer
ms.assetid: 'dc022c49-2284-4534-8bd8-939613a9ca2f'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["SetByADZone method", "SetByADZone method, PS_DnsServerConditionalForwarder class", "PS_DnsServerConditionalForwarder class, SetByADZone method"]
topic_type:
- apiref
api_name:
- PS_DnsServerConditionalForwarder.SetByADZone
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# SetByADZone method of the PS\_DnsServerConditionalForwarder class

Sets DNS server Conditional Forwarder settings.

## Syntax


```mof
uint32 SetByADZone(
  [in]  string                            DirectoryPartitionName,
  [in]  string                            ReplicationScope,
  [in]  string                            Name,
  [in]  string                            ComputerName,
  [in]  boolean                           PassThru,
  [out] DnsServerConditionalForwarderZone cmdletOutput
);
```



## Parameters

<dl> <dt>

*DirectoryPartitionName* \[in\]
</dt> <dd>

Specifies the name of the directory partition.

</dd> <dt>

*ReplicationScope* \[in\]
</dt> <dd>

The replication scope.

The possible values are.

<dt>

<span id="Forest"></span><span id="forest"></span><span id="FOREST"></span>

**Forest** ("Forest")


</dt> <dd></dd> <dt>

<span id="Domain"></span><span id="domain"></span><span id="DOMAIN"></span>

**Domain** ("Domain")


</dt> <dd></dd> <dt>

<span id="Legacy"></span><span id="legacy"></span><span id="LEGACY"></span>

**Legacy** ("Legacy")


</dt> <dd></dd> <dt>

<span id="Custom"></span><span id="custom"></span><span id="CUSTOM"></span>

**Custom** ("Custom")


</dt> <dd></dd> </dl> </dd> <dt>

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

 

 





