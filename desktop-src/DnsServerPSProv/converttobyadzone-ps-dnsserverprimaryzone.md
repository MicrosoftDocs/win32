---
title: ConvertToByADZone method of the PS\_DnsServerPrimaryZone class
description: Converts a zone to DNS server primary zone.
audience: developer
ms.assetid: dadd4c83-3e3a-4bb5-a1f9-9972810ae6dd
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ConvertToByADZone method
- ConvertToByADZone method, PS_DnsServerPrimaryZone class
- PS_DnsServerPrimaryZone class, ConvertToByADZone method
topic_type:
- apiref
api_name:
- PS_DnsServerPrimaryZone.ConvertToByADZone
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ConvertToByADZone method of the PS\_DnsServerPrimaryZone class

Converts a zone to DNS server primary zone.

## Syntax


```mof
uint32 ConvertToByADZone(
  [in]  string               ComputerName,
  [in]  string               Name,
  [in]  string               ReplicationScope,
  [in]  boolean              LoadExisting,
  [in]  boolean              PassThru,
  [in]  string               DirectoryPartitionName,
  [in]  boolean              Force,
  [out] DnsServerPrimaryZone cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Specifies name of the zone

</dd> <dt>

*ReplicationScope* \[in\]
</dt> <dd>

Specifies the directory partition on which to store the zone. FQDN: Specifies fully qualified domain name of the directory partition. domain: Stores the zone on the domain directory partition. enterprise: Stores the zone on the enterprise directory partition. legacy: Stores the zone on a legacy directory partition. Parameter valid only if it is AD based.

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

*LoadExisting* \[in\]
</dt> <dd>

Specifies existing file to be used while loading the zone

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**True** to return the object that was modified by the method. By default, this method does not generate any output.

</dd> <dt>

*DirectoryPartitionName* \[in\]
</dt> <dd>

Specifies the directory partition on which to store the zone.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Converts a zone without prompting you for confirmation. By default, the method prompts you for confirmation before it proceeds.

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

 

 





