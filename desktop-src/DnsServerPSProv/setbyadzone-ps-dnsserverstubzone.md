---
title: SetByADZone method of the PS\_DnsServerStubZone class
description: Overwrites settings of DNS server stub zone. If none exists exit with terminating error.
audience: developer
ms.assetid: 84709178-8d01-46b7-9e53-80e64634cecb
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetByADZone method
- SetByADZone method, PS_DnsServerStubZone class
- PS_DnsServerStubZone class, SetByADZone method
topic_type:
- apiref
api_name:
- PS_DnsServerStubZone.SetByADZone
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetByADZone method of the PS\_DnsServerStubZone class

Overwrites settings of DNS server stub zone. If none exists exit with terminating error.

## Syntax


```mof
uint32 SetByADZone(
  [in]  string            DirectoryPartitionName,
  [in]  string            Name,
  [in]  string            ComputerName,
  [in]  string            ReplicationScope,
  [in]  boolean           PassThru,
  [out] DnsServerStubZone cmdletOutput
);
```



## Parameters

<dl> <dt>

*DirectoryPartitionName* \[in\]
</dt> <dd>

Specifies the directory partition on which to store the zone. FQDN: Specifies fully qualified domain name of the directory partition. domain: Stores the zone on the domain directory partition. enterprise: Stores the zone on the enterprise directory partition. legacy: Stores the zone on a legacy directory partition. Parameter valid only if it is AD based.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Specifies the name of the zone.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command

</dd> <dt>

*ReplicationScope* \[in\]
</dt> <dd>

Specifies the directory partition on which to store the zone. Parameter valid only if it is AD based.

The possible values are.

<dt>

<span id="Forest"></span><span id="forest"></span><span id="FOREST"></span>

<span id="Forest"></span><span id="forest"></span><span id="FOREST"></span>**Forest** ("Forest")


</dt> <dd>

Stores the zone on the enterprise directory partition.

</dd> <dt>

<span id="Domain"></span><span id="domain"></span><span id="DOMAIN"></span>

<span id="Domain"></span><span id="domain"></span><span id="DOMAIN"></span>**Domain** ("Domain")


</dt> <dd>

Specifies fully qualified domain name of the directory partition.

</dd> <dt>

<span id="Legacy"></span><span id="legacy"></span><span id="LEGACY"></span>

<span id="Legacy"></span><span id="legacy"></span><span id="LEGACY"></span>**Legacy** ("Legacy")


</dt> <dd>

Stores the zone on a legacy directory partition.

</dd> <dt>

<span id="Custom"></span><span id="custom"></span><span id="CUSTOM"></span>

<span id="Custom"></span><span id="custom"></span><span id="CUSTOM"></span>**Custom** ("Custom")


</dt> <dd>

Specifies fully qualified domain name of the directory partition.

</dd> </dl> </dd> <dt>

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
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsServerStubZone**](ps-dnsserverstubzone.md)
</dt> </dl>

 

 





