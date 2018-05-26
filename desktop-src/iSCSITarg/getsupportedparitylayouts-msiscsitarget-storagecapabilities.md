---
title: GetSupportedParityLayouts method of the MSISCSITARGET\_StorageCapabilities class
description: Retrieves the supported parity layouts for systems that support parity-based storage organizations for volume or pool creation.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e6f7edaf-258c-42ee-9ce8-eaae5def5b1c
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetSupportedParityLayouts method iSCSI Software Target API
- GetSupportedParityLayouts method iSCSI Software Target API , MSISCSITARGET_StorageCapabilities class
- MSISCSITARGET_StorageCapabilities class iSCSI Software Target API , GetSupportedParityLayouts method
topic_type:
- apiref
api_name:
- MSISCSITARGET_StorageCapabilities.GetSupportedParityLayouts
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetSupportedParityLayouts method of the MSISCSITARGET\_StorageCapabilities class

Retrieves the supported parity layouts for systems that support parity-based storage organizations for volume or pool creation.

This method is inherited from the **CIM\_StorageCapabilities** class.

## Syntax


```mof
uint32 GetSupportedParityLayouts(
  [out] uint16 ParityLayout[]
);
```



## Parameters

<dl> <dt>

*ParityLayout* \[out\]
</dt> <dd>

On return, contains a list of the types of parity that are supported when you create or modify a volume or pool.

The possible values are.

<dt>

<span id="Non-Rotated_Parity"></span><span id="non-rotated_parity"></span><span id="NON-ROTATED_PARITY"></span>

**Non-Rotated Parity** (2)


</dt> <dd></dd> <dt>

<span id="Rotated_Parity"></span><span id="rotated_parity"></span><span id="ROTATED_PARITY"></span>

**Rotated Parity** (3)


</dt> <dd></dd> </dl> </dd> </dl>

## Return value

<dl> <dt>

**Method completed OK** (0)
</dt> <dt>

**Method not supported** (1)
</dt> <dt>

**Choice not available for this capability** (2)
</dt> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>Smiscsitarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SmIScsiTargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSISCSITARGET\_StorageCapabilities**](msiscsitarget-storagecapabilities.md)
</dt> </dl>

 

 





