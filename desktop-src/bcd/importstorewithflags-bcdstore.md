---
title: ImportStoreWithFlags method of the BcdStore class
description: Marks the specified store as the system store and optionally reinitializes boot entries in NVRAM on a computer with Unified Extensible Firmware Interface (UEFI) firmware.
ms.assetid: '2807eb0f-8d4b-4807-bb91-c527f0ff660f'
keywords: ["ImportStoreWithFlags method Boot Config", "ImportStoreWithFlags method Boot Config , BcdStore class", "BcdStore class Boot Config , ImportStoreWithFlags method"]
topic_type:
- apiref
api_name:
- BcdStore.ImportStoreWithFlags
api_location:
- Root\WMI
api_type:
- COM
---

# ImportStoreWithFlags method of the BcdStore class

Marks the specified store as the system store and optionally reinitializes boot entries in NVRAM on a computer with Unified Extensible Firmware Interface (UEFI) firmware.

## Syntax


```mof
boolean ImportStoreWithFlags(
  [in]           string File,
  [in, optional] uint32 Flags
);
```



## Parameters

<dl> <dt>

*File* \[in\]
</dt> <dd>

The full path to the store. The store could be created by the [**ExportStore**](exportstore-bcdstore.md) or [**CreateStore**](createstore-bcdstore.md) method or by the **BcdEdit /export** or **BcdEdit /createstore** command.

</dd> <dt>

*Flags* \[in, optional\]
</dt> <dd>

On computers with UEFI firmware, this parameter can be set with zero or the following value.



| Value                                                                                                                                                                                                                 | Meaning                                                                                                           |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| <span id="Clean"></span><span id="clean"></span><span id="CLEAN"></span><dl> <dt>**Clean**</dt> <dt>0x1</dt> </dl> | Deletes all boot entries in NVRAM and recreates them based on information in the supplied file store. <br/> |



 

On computers without UEFI firmware, the *Flags* parameter is ignored.

</dd> </dl>

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP1 \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Namespace<br/>                | Root\\WMI<br/>                                                               |
| MOF<br/>                      | <dl> <dt>Bcd.mof</dt> </dl> |



## See also

<dl> <dt>

[**BcdStore**](bcdstore.md)
</dt> <dt>

[**ExportStore**](exportstore-bcdstore.md)
</dt> <dt>

[**ImportStore**](importstore-bcdstore.md)
</dt> </dl>

 

 





