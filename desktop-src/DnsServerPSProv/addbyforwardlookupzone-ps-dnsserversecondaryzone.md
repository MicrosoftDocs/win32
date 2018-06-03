---
title: AddByForwardLookupZone method of the PS\_DnsServerSecondaryZone class
description: Creates a standard secondary zone.
audience: developer
ms.assetid: f4a753e7-0b32-4622-9214-7d6823e1738a
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AddByForwardLookupZone method
- AddByForwardLookupZone method, PS_DnsServerSecondaryZone class
- PS_DnsServerSecondaryZone class, AddByForwardLookupZone method
topic_type:
- apiref
api_name:
- PS_DnsServerSecondaryZone.AddByForwardLookupZone
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AddByForwardLookupZone method of the PS\_DnsServerSecondaryZone class

Creates a standard secondary zone.

## Syntax


```mof
uint32 AddByForwardLookupZone(
  [in]  boolean                LoadExisting,
  [in]  string                 MasterServers[],
  [in]  string                 Name,
  [in]  string                 ZoneFile,
  [in]  string                 ComputerName,
  [in]  boolean                PassThru,
  [out] DnsServerSecondaryZone cmdletOutput
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

*Name* \[in\]
</dt> <dd>

Specifies the name of the zone.

</dd> <dt>

*ZoneFile* \[in\]
</dt> <dd>

Specifies zone file path

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
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsServerSecondaryZone**](ps-dnsserversecondaryzone.md)
</dt> </dl>

 

 





