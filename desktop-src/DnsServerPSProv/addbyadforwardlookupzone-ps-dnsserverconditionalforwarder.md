---
title: AddByADForwardLookupZone method of the PS\_DnsServerConditionalForwarder class
description: Adds a DNS conditional forwarder zone.
audience: developer
ms.assetid: 'fa1b42eb-dab7-446f-9d6d-caf89a8e778d'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["AddByADForwardLookupZone method", "AddByADForwardLookupZone method, PS_DnsServerConditionalForwarder class", "PS_DnsServerConditionalForwarder class, AddByADForwardLookupZone method"]
topic_type:
- apiref
api_name:
- PS_DnsServerConditionalForwarder.AddByADForwardLookupZone
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# AddByADForwardLookupZone method of the PS\_DnsServerConditionalForwarder class

Adds a DNS conditional forwarder zone.

## Syntax


```mof
uint32 AddByADForwardLookupZone(
  [in]  boolean                           LoadExisting,
  [in]  string                            MasterServers[],
  [in]  string                            DirectoryPartitionName,
  [in]  string                            ComputerName,
  [in]  string                            ReplicationScope,
  [in]  boolean                           UseRecursion,
  [in]  string                            Name,
  [in]  uint32                            ForwarderTimeout,
  [in]  boolean                           PassThru,
  [out] DnsServerConditionalForwarderZone cmdletOutput
);
```



## Parameters

<dl> <dt>

*LoadExisting* \[in\]
</dt> <dd>

Specifies Loading of existing zone.

</dd> <dt>

*MasterServers* \[in\]
</dt> <dd>

Specifies the IP addresses of the master servers of the zone.

</dd> <dt>

*DirectoryPartitionName* \[in\]
</dt> <dd>

Specifies the directory partition on which to store the zone.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command.

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

*UseRecursion* \[in\]
</dt> <dd>

Overrides DNS server's Use Recursion setting.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Specifies the name of the zone.

</dd> <dt>

*ForwarderTimeout* \[in\]
</dt> <dd>

Indicates the time, in seconds, a DNS server forwarding a query for the name under the forward zone waits for resolution from the forwarder before attempting to resolve the query itself. This parameter is applicable to the Forward zones only. Range = 0 to 15

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**True** to return the object that was modified by the method. By default, this method does not generate any output.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

Receives an embedded instance of the [**DnsServerConditionalForwarder**](dnsserverconditionalforwarderzone.md) class.

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

 

 





