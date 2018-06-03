---
title: Restore method of the PS\_DnsServerSecondaryZone class
description: Forces a secondary DNS zone to update from the master zone.
audience: developer
ms.assetid: 2890d237-d21e-4f02-8aac-43e66515ca57
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Restore method
- Restore method, PS_DnsServerSecondaryZone class
- PS_DnsServerSecondaryZone class, Restore method
topic_type:
- apiref
api_name:
- PS_DnsServerSecondaryZone.Restore
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Restore method of the PS\_DnsServerSecondaryZone class

Forces a secondary DNS zone to update from the master zone.

## Syntax


```mof
uint32 Restore(
  [in]  string                 Name,
  [in]  string                 ComputerName,
  [in]  boolean                PassThru,
  [in]  boolean                Force,
  [out] DnsServerSecondaryZone cmdletOutput
);
```



## Parameters

<dl> <dt>

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

**True** to return the object that was modified by the method. By default, this method does not generate any output.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Updates the DNS zone without prompting you for confirmation. By default, the method prompts you for confirmation before it proceeds.

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

 

 





