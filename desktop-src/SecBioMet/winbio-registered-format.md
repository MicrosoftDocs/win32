---
title: WINBIO_REGISTERED_FORMAT structure (Winbio\_types.h)
description: Specifies a registered data format as an owner/format pair.
ms.assetid: a178840e-81cc-4dd3-9d80-a181fa7fa888
keywords:
- WINBIO_REGISTERED_FORMAT structure Windows Biometric Framework API
- PWINBIO_REGISTERED_FORMAT structure pointer Windows Biometric Framework API
topic_type:
- apiref
api_name:
- WINBIO_REGISTERED_FORMAT
api_location:
- Winbio_types.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WINBIO\_REGISTERED\_FORMAT structure

The **WINBIO\_REGISTERED\_FORMAT** structure specifies a registered data format as an owner/format pair.

## Syntax


```C++
typedef struct _WINBIO_REGISTERED_FORMAT {
  USHORT Owner;
  USHORT Type;
} WINBIO_REGISTERED_FORMAT, *PWINBIO_REGISTERED_FORMAT;
```



## Members

<dl> <dt>

**Owner**
</dt> <dd>

An IBIA (International Biometric Industry Association) assigned owner value.

</dd> <dt>

**Type**
</dt> <dd>

An owner assigned format.

</dd> </dl>

## Remarks

Because Windows currently supports only fingerprint readers, the following values should be used in the **WINBIO\_REGISTERED\_FORMAT** structure.



| Constant                                    | Meaning                                                                                                               |
|---------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| WINBIO\_ANSI\_381\_FORMAT\_OWNER<br/> | InterNational Committee for Information Technology Standards (INCITS) technical committee M1 (biometrics).<br/> |
| WINBIO\_ANSI\_381\_FORMAT\_TYPE<br/>  | ANSI INCITS 381 finger image based data interchange format.<br/>                                                |



 

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

[**WINBIO\_ANSI\_381\_FORMAT Constants**](winbio-ansi-381-format-constants.md)
</dt> <dt>

[**WINBIO\_BDB\_ANSI\_381\_HEADER**](winbio-bdb-ansi-381-header.md)
</dt> <dt>

[**WINBIO\_BIR\_HEADER**](winbio-bir-header.md)
</dt> </dl>

 

 





