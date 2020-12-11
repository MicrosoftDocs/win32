---
title: STOWED_EXCEPTION_INFORMATION_HEADER structure
description: Contains info that identifies the parent structure.
ms.assetid: 0BC1FDAA-C750-4DEC-AF6A-B2CB3240B67C
keywords:
- STOWED_EXCEPTION_INFORMATION_HEADER structure Windows Error Reporting
- PSTOWED_EXCEPTION_INFORMATION_HEADER structure pointer Windows Error Reporting
topic_type:
- apiref
api_name:
- STOWED_EXCEPTION_INFORMATION_HEADER
api_location:
- none
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# STOWED\_EXCEPTION\_INFORMATION\_HEADER structure

Contains info that identifies the parent structure.

## Syntax


```C++
typedef struct _STOWED_EXCEPTION_INFORMATION_HEADER {
  ULONG Size;
  ULONG Signature;
} STOWED_EXCEPTION_INFORMATION_HEADER, *PSTOWED_EXCEPTION_INFORMATION_HEADER;
```



## Members

<dl> <dt>

**Size**
</dt> <dd>

Type: **[**ULONG**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Size, in bytes, of the parent structure.

</dd> <dt>

**Signature**
</dt> <dd>

Type: **[**ULONG**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

A 32-bit value that specifies the signature of the parent structure.



| Value                                                                                                                                                                                                                                                                                                            | Meaning                                                                                                                                       |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="STOWED_EXCEPTION_INFORMATION_V1_SIGNATURE"></span><span id="stowed_exception_information_v1_signature"></span><dl> <dt>**STOWED\_EXCEPTION\_INFORMATION\_V1\_SIGNATURE**</dt> <dt>'SE01'</dt> </dl> | This value indicates that the parent is a **STOWED\_EXCEPTION\_INFORMATION\_V1** structure.<br/>                                        |
| <span id="STOWED_EXCEPTION_INFORMATION_V2_SIGNATURE"></span><span id="stowed_exception_information_v2_signature"></span><dl> <dt>**STOWED\_EXCEPTION\_INFORMATION\_V2\_SIGNATURE**</dt> <dt>'SE02'</dt> </dl> | This value indicates that the parent is a [**STOWED\_EXCEPTION\_INFORMATION\_V2**](stowed-exception-information-v2.md) structure.<br/> |



 

</dd> </dl>

## Remarks

[**STOWED\_EXCEPTION\_INFORMATION\_V2**](stowed-exception-information-v2.md) and **STOWED\_EXCEPTION\_INFORMATION\_HEADER** currently aren't defined in a header that is publicly available so you need to define them in your source code before you use them.

The **STOWED\_EXCEPTION\_INFORMATION\_V1** structure is identical to this structure except it doesn't contain the **NestedExceptionType** and **NestedException** members.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                            |
| Header<br/>                   | <dl> <dt>None</dt> </dl> |



## See also

<dl> <dt>

[**STOWED\_EXCEPTION\_INFORMATION\_V2**](stowed-exception-information-v2.md)
</dt> </dl>

 

