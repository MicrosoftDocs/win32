---
title: SetByADZone method of the PS\_DnsServerPrimaryZone class
description: Overwrites settings of DNS server primary zone.
audience: developer
ms.assetid: 247def2e-c1a0-4e14-92a1-a854b7c49e6f
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetByADZone method
- SetByADZone method, PS_DnsServerPrimaryZone class
- PS_DnsServerPrimaryZone class, SetByADZone method
topic_type:
- apiref
api_name:
- PS_DnsServerPrimaryZone.SetByADZone
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SetByADZone method of the PS\_DnsServerPrimaryZone class

Overwrites settings of DNS server primary zone.

## Syntax


```mof
uint32 SetByADZone(
  [in]  string               Name,
  [in]  string               ReplicationScope,
  [in]  string               DirectoryPartitionName,
  [in]  string               ComputerName,
  [in]  boolean              PassThru,
  [out] DnsServerPrimaryZone cmdletOutput
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

Specifies the name of the zone.

</dd> <dt>

*ReplicationScope* \[in\]
</dt> <dd>

Specifies the directory partition on which to store the zone. FQDN: Specifies fully qualified domain name of the directory partition. domain: Stores the zone on the domain directory partition. enterprise: Stores the zone on the enterprise directory partition. legacy: Stores the zone on a legacy directory partition. Parameter valid only if it is AD based. In case of file, this is the file path.

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

*DirectoryPartitionName* \[in\]
</dt> <dd>

Specifies the directory partition on which to store the zone.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**True** to return the object that was modified by the method. By default, this method does not generate any output.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

Receives an embedded instance of the [**DnsServerPrimaryZone**](dnsserverprimaryzone.md) class.

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

[**PS\_DnsServerPrimaryZone**](ps-dnsserverprimaryzone.md)
</dt> </dl>

 

 





