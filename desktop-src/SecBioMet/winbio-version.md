---
title: WINBIO_VERSION structure (Winbio\_types.h)
description: Contains the software version number of a biometric service provider component.
ms.assetid: b9d08e10-00db-4f3f-9e27-6063aafa4151
keywords:
- WINBIO_VERSION structure Windows Biometric Framework API
- PWINBIO_VERSION structure pointer Windows Biometric Framework API
topic_type:
- apiref
api_name:
- WINBIO_VERSION
api_location:
- Winbio_types.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WINBIO\_VERSION structure

The **WINBIO\_VERSION** structure contains the software version number of a biometric service provider component.

## Syntax


```C++
typedef struct _WINBIO_VERSION {
  DWORD MajorVersion;
  DWORD MinorVersion;
} WINBIO_VERSION, *PWINBIO_VERSION;
```



## Members

<dl> <dt>

**MajorVersion**
</dt> <dd>

A **DWORD** that contains the major version number.

</dd> <dt>

**MinorVersion**
</dt> <dd>

A **DWORD** that contains the minor version number.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                                       |
| Header<br/>                   | <dl> <dt>Winbio\_types.h (include Winbio.h)</dt> </dl> |



## See also

<dl> <dt>

[Client Application Structures](client-application-structures.md)
</dt> <dt>

[**WINBIO\_BSP\_SCHEMA**](winbio-bsp-schema.md)
</dt> <dt>

[**WINBIO\_UNIT\_SCHEMA**](winbio-unit-schema.md)
</dt> </dl>

 

 





