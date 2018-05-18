---
title: AddByFileForwardLookupZone method of the PS\_DnsServerConditionalForwarder class
description: Adds a DNS conditional forwarder zone.
audience: developer
ms.assetid: 'd1c70915-3f4e-43a1-ba86-7609b2615a4d'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["AddByFileForwardLookupZone method", "AddByFileForwardLookupZone method, PS_DnsServerConditionalForwarder class", "PS_DnsServerConditionalForwarder class, AddByFileForwardLookupZone method"]
topic_type:
- apiref
api_name:
- PS_DnsServerConditionalForwarder.AddByFileForwardLookupZone
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# AddByFileForwardLookupZone method of the PS\_DnsServerConditionalForwarder class

Adds a DNS conditional forwarder zone.

## Syntax


```mof
uint32 AddByFileForwardLookupZone(
  [in]  boolean                           LoadExisting,
  [in]  string                            MasterServers[],
  [in]  string                            ComputerName,
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

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command.

</dd> <dt>

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

 

 





