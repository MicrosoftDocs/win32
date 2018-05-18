---
title: Start method of the PS\_DnsServerZoneTransfer class
description: Starts DNS Zone transfer from Primary to Secondary.
audience: developer
ms.assetid: '42be02a4-4c0f-4711-b428-b8d924642843'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Start method", "Start method, PS_DnsServerZoneTransfer class", "PS_DnsServerZoneTransfer class, Start method"]
topic_type:
- apiref
api_name:
- PS_DnsServerZoneTransfer.Start
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# Start method of the PS\_DnsServerZoneTransfer class

Starts DNS Zone transfer from Primary to Secondary.

## Syntax


```mof
uint32 Start(
  [in]  string        ComputerName,
  [in]  string        Name,
  [in]  boolean       FullTransfer,
  [in]  boolean       PassThru,
  [out] DnsServerZone cmdletOutput
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

Specifies the name of the zone.

</dd> <dt>

*FullTransfer* \[in\]
</dt> <dd>

Performs full transfer. If not specified, by default does only incremental transfer.

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

[**PS\_DnsServerZoneTransfer**](ps-dnsserverzonetransfer.md)
</dt> </dl>

 

 





