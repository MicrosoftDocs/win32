---
title: Optimize method of the MSFT\_Volume class
description: Optimizes the volume.
ms.assetid: ef56d743-1b6b-421c-8ffc-82c08cc9dee1
keywords:
- Optimize method Windows Storage Management API
- Optimize method Windows Storage Management API , MSFT_Volume class
- MSFT_Volume class Windows Storage Management API , Optimize method
topic_type:
- apiref
api_name:
- MSFT_Volume.Optimize
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Optimize method of the MSFT\_Volume class

Optimizes the volume.

## Syntax


```mof
UInt32 Optimize(
  [in]  Boolean ReTrim,
  [in]  Boolean Analyze,
  [in]  Boolean Defrag,
  [in]  Boolean SlabConsolidate,
  [in]  Boolean TierOptimize,
  [out] String  ExtendedStatus
);
```



## Parameters

<dl> <dt>

*ReTrim* \[in\]
</dt> <dd>

Set to TRUE to retrim the volume.

</dd> <dt>

*Analyze* \[in\]
</dt> <dd>

Set to TRUE to analyze the volume.

</dd> <dt>

*Defrag* \[in\]
</dt> <dd>

Set to TRUE to defragment the volume.

</dd> <dt>

*SlabConsolidate* \[in\]
</dt> <dd>

Set to TRUE to slab-consolidate the volume.

</dd> <dt>

*TierOptimize* \[in\]
</dt> <dd>

Set to TRUE to optimize the volume tiers.

</dd> <dt>

*ExtendedStatus* \[out\]
</dt> <dd>

A string that contains an embedded [**MSFT\_StorageExtendedStatus**](msft-storageextendedstatus.md) object.

This parameter allows the storage provider to return extended (implementation-specific) error information.

</dd> </dl>

## Return value

<dl> <dt>

**Success** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Unspecified Error** (2)
</dt> <dt>

**Timeout** (3)
</dt> <dt>

**Failed** (4)
</dt> <dt>

**Invalid Parameter** (5)
</dt> <dt>

**This command is not supported on x86 running in x64 environment.** (7)
</dt> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_Volume**](msft-volume.md)
</dt> </dl>

 

 





