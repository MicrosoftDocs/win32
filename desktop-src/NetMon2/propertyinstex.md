---
description: The PROPERTYINSTEX structure defines a freeform, extended property instance.
ms.assetid: a2316baf-07e2-4617-bb35-e20cfb11fbcb
title: PROPERTYINSTEX structure (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PROPERTYINSTEX
api_type: 
- HeaderDef
api_location: 
- Netmon.h
---

# PROPERTYINSTEX structure

The **PROPERTYINSTEX** structure defines a freeform, extended property instance.

## Syntax


```C++
typedef struct _PROPERTYINSTEX {
  WORD    Length;
  WORD    LengthEx;
  ULPVOID lpData;
  union {
    BYTE          Byte[];
    WORD          Word[];
    DWORD         Dword[];
    LARGE_INTEGER LargeInt[];
    SYSTEMTIME    SysTime[];
    TYPED_STRING  TypedString;
  };
} PROPERTYINSTEX;
```



## Members

<dl> <dt>

**Length**
</dt> <dd>

Length of the data in Bytes.

</dd> <dt>

**LengthEx**
</dt> <dd>

Length of the extended data.

</dd> <dt>

**lpData**
</dt> <dd>

Pointer to the extended data.

</dd> <dt>

**Byte**
</dt> <dd>

Pointer to the **BYTE** data.

</dd> <dt>

**Word**
</dt> <dd>

Pointer to the **WORD** data.

</dd> <dt>

**Dword**
</dt> <dd>

Pointer to the **DWORD** data.

</dd> <dt>

**LargeInt**
</dt> <dd>

Pointer to the **LARGEINT** data.

</dd> <dt>

**SysTime**
</dt> <dd>

Pointer to the **SYSTEMTIME** data.

</dd> <dt>

**TypedString**
</dt> <dd>

A typed string that may have extended data.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



 

 




