---
title: Export method of the PS\_DnsServerZone class
description: Exports Zone information.
audience: developer
ms.assetid: 'b591b20f-15b6-4787-b94e-b6206db4a956'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Export method", "Export method, PS_DnsServerZone class", "PS_DnsServerZone class, Export method"]
topic_type:
- apiref
api_name:
- PS_DnsServerZone.Export
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# Export method of the PS\_DnsServerZone class

Exports Zone information.

## Syntax


```mof
uint32 Export(
  [in]  string        FileName,
  [in]  string        Name,
  [in]  string        ComputerName,
  [in]  boolean       PassThru,
  [out] DnsServerZone cmdletOutput
);
```



## Parameters

<dl> <dt>

*FileName* \[in\]
</dt> <dd>

File name and Path can be remote (need to check feasibility).

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Specifies the name of the zone.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**True** to return the object that was modified by the method. By default, this method does not generate any output.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

Receives and embedded instance of the [**DnsServerZone**](dnsserverzone.md) class.

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

[**PS\_DnsServerZone**](ps-dnsserverzone.md)
</dt> </dl>

 

 





