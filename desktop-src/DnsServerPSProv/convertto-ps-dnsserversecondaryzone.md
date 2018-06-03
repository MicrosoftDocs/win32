---
title: ConvertTo method of the PS\_DnsServerSecondaryZone class
description: Converts a primary zone to a secondary zone. .
audience: developer
ms.assetid: 4efe979c-dc6a-4e8c-b5fe-4ee93b6c4386
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ConvertTo method
- ConvertTo method, PS_DnsServerSecondaryZone class
- PS_DnsServerSecondaryZone class, ConvertTo method
topic_type:
- apiref
api_name:
- PS_DnsServerSecondaryZone.ConvertTo
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ConvertTo method of the PS\_DnsServerSecondaryZone class

Converts a primary zone to a secondary zone. .

## Syntax


```mof
uint32 ConvertTo(
  [in]  string                 ZoneFile,
  [in]  string                 MasterServers[],
  [in]  string                 Name,
  [in]  string                 ComputerName,
  [in]  boolean                PassThru,
  [in]  boolean                Force,
  [out] DnsServerSecondaryZone cmdletOutput
);
```



## Parameters

<dl> <dt>

*ZoneFile* \[in\]
</dt> <dd>

Specifies zone file path

</dd> <dt>

*MasterServers* \[in\]
</dt> <dd>

Specifies a list of IPv4/v6 addresses of primary DNS servers for this zone

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Specifies the name of the zone.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**true** to return the current instance in the *CmdletOutput* parameter. The default is **false**.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

If specified, overrides the default confirmation before performing the operation.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

On return, contains an embedded instance of [**DnsServerSecondaryZone**](dnsserversecondaryzone.md).

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

 

 





