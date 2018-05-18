---
title: Sync method of the PS\_DnsServerZone class
description: Write back all zone or roothint datafile(s) for the specified zone.
audience: developer
ms.assetid: 'd4a50e50-cc71-4d06-9024-8e74e36e86e3'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Sync method", "Sync method, PS_DnsServerZone class", "PS_DnsServerZone class, Sync method"]
topic_type:
- apiref
api_name:
- PS_DnsServerZone.Sync
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# Sync method of the PS\_DnsServerZone class

Write back all zone or roothint datafile(s) for the specified zone.

## Syntax


```mof
uint32 Sync(
  [in]  string        Name,
  [in]  string        ComputerName,
  [in]  boolean       PassThru,
  [out] DnsServerZone cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

Specifies the name of the zone, otherwise applies for all zones on the server

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

On return, contains an instance of the current object. This parameter returns a value only if *PassThru* is set to **true.**

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| Header<br/>                   | <dl> <dt>Mlang.h</dt> </dl>                 |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsServerZone**](ps-dnsserverzone.md)
</dt> </dl>

 

 





