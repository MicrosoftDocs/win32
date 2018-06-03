---
title: GetSupportedParityLayouts method of the CIM\_StorageCapabilities class
description: For systems that support Parity-based storage organizations for volume or pool creation, this method can be used to the supported parity layouts.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7edc7508-e98e-464d-8213-792e23b704a4
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetSupportedParityLayouts method iSCSI Software Target API
- GetSupportedParityLayouts method iSCSI Software Target API , CIM_StorageCapabilities class
- CIM_StorageCapabilities class iSCSI Software Target API , GetSupportedParityLayouts method
topic_type:
- apiref
api_name:
- CIM_StorageCapabilities.GetSupportedParityLayouts
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetSupportedParityLayouts method of the CIM\_StorageCapabilities class

For systems that support Parity-based storage organizations for volume or pool creation, this method can be used to the supported parity layouts.

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

List of supported Parity for a Volume/Pool creation or modification.

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

**Choice not aavailable for this capability** (2)
</dt> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_StorageCapabilities**](cim-storagecapabilities.md)
</dt> </dl>

 

 





