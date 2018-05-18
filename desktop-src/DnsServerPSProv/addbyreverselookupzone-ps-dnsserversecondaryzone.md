---
title: AddByReverseLookupZone method of the PS\_DnsServerSecondaryZone class
description: Creates a standard secondary zone.
audience: developer
ms.assetid: '354a76a2-ce7d-4089-ab5a-6f46a2b6ab73'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["AddByReverseLookupZone method", "AddByReverseLookupZone method, PS_DnsServerSecondaryZone class", "PS_DnsServerSecondaryZone class, AddByReverseLookupZone method"]
topic_type:
- apiref
api_name:
- PS_DnsServerSecondaryZone.AddByReverseLookupZone
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# AddByReverseLookupZone method of the PS\_DnsServerSecondaryZone class

Creates a standard secondary zone.

## Syntax


```mof
uint32 AddByReverseLookupZone(
  [in]  boolean                LoadExisting,
  [in]  string                 MasterServers[],
  [in]  string                 NetworkId,
  [in]  string                 ZoneFile,
  [in]  string                 ComputerName,
  [in]  boolean                PassThru,
  [out] DnsServerSecondaryZone cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*LoadExisting* \[in\]
</dt> <dd>

Loads existing zone

</dd> <dt>

*MasterServers* \[in\]
</dt> <dd>

Specifies IP addresses of the master DNS servers for this zone.

</dd> <dt>

*NetworkId* \[in\]
</dt> <dd>

Specifies the IP subnet and range of the zone to be created. IP address with prefix length, for example: 11.1.1/24 , 1234::/64

</dd> <dt>

*ZoneFile* \[in\]
</dt> <dd>

Specifies name of the zone file. This parameter is only relevant for file-backed zones.

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

Receives and embedded instance of the [**DnsServerSecondaryZone**](dnsserversecondaryzone.md) class.

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

[**PS\_DnsServerSecondaryZone**](ps-dnsserversecondaryzone.md)
</dt> </dl>

 

 





