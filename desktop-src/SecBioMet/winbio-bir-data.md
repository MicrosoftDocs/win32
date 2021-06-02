---
title: WINBIO_BIR_DATA structure (Winbio\_types.h)
description: Specifies the size, in bytes, and the offset of a block of biometric information.
ms.assetid: 2f73eb1f-f1a1-4831-a8f7-eec28aa51645
keywords:
- WINBIO_BIR_DATA structure Windows Biometric Framework API
topic_type:
- apiref
api_name:
- WINBIO_BIR_DATA
api_location:
- Winbio_types.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WINBIO\_BIR\_DATA structure

The **WINBIO\_BIR\_DATA** structure specifies the size, in bytes, and the offset of a block of biometric information. This structure is used by the [**WINBIO\_BIR**](winbio-bir.md) structure to specify where the various parts of a biometric information record are located.

## Syntax


```C++
typedef struct _WINBIO_BIR_DATA {
  ULONG Size;
  ULONG Offset;
} WINBIO_BIR_DATA;
```



## Members

<dl> <dt>

**Size**
</dt> <dd>

Size, in bytes, of the biometric information.

</dd> <dt>

**Offset**
</dt> <dd>

Offset, in bytes from the beginning of the [**WINBIO\_BIR**](winbio-bir.md) structure, of the biometric information.

</dd> </dl>

## Remarks

The use of offsets rather than pointers allows for easy serialization of the BIR and for less complicated translation between 32 and 64-bit environments or between user and kernel mode.

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

[**WINBIO\_BIR**](winbio-bir.md)
</dt> <dt>

[**WINBIO\_BIR\_HEADER**](winbio-bir-header.md)
</dt> </dl>

 

 





