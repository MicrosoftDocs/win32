---
description: Contains extended module information.
ms.assetid: 705769de-0aeb-4a28-b174-8620efa74baf
title: AUX_MODULE_EXTENDED_INFO structure (Aux\_klib.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- AUX_MODULE_EXTENDED_INFO
api_type: 
- HeaderDef
api_location: 
- Aux_klib.h
---

# AUX\_MODULE\_EXTENDED\_INFO structure

Contains extended module information.

## Syntax


```C++
typedef struct _AUX_MODULE_EXTENDED_INFO {
  AUX_MODULE_BASIC_INFO BasicInfo;
  ULONG                 ImageSize;
  USHORT                FileNameOffset;
  UCHAR                 FullPathName[AUX_KLIB_MODULE_PATH_LEN];
} AUX_MODULE_EXTENDED_INFO, *PAUX_MODULE_EXTENDED_INFO;
```



## Members

<dl> <dt>

**BasicInfo**
</dt> <dd>

An [**AUX\_MODULE\_BASIC\_INFO**](aux-module-basic-info-struct.md) structure.

</dd> <dt>

**ImageSize**
</dt> <dd>

The size, in bytes, of the loaded module.

</dd> <dt>

**FileNameOffset**
</dt> <dd>

The offset of the file name within the **FullPathName** buffer.

</dd> <dt>

**FullPathName**
</dt> <dd>

The full path of the module.

</dd> </dl>

## Remarks

The object library that implements this API can be downloaded from [here](https://www.microsoft.com/?ref=go).

## Requirements



| Requirement | Value |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | Windows Auxiliary API library version 1.0 or later<br/>                          |
| Header<br/>          | <dl> <dt>Aux\_klib.h</dt> </dl> |



## See also

<dl> <dt>

[**AuxKlibQueryModuleInformation**](auxklibquerymoduleinformation-func.md)
</dt> <dt>

[**AUX\_MODULE\_BASIC\_INFO**](aux-module-basic-info-struct.md)
</dt> </dl>

 

 




