---
description: The KSMULTIPLE\_ITEM structure describes the size and count of variable-length properties on kernel-mode pins.
ms.assetid: aedbf7bc-393d-4ab5-afcd-d8822b925f07
title: KSMULTIPLE_ITEM structure (Ks.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- KSMULTIPLE_ITEM
api_type: 
- HeaderDef
api_location: 
- ks.h
---

# KSMULTIPLE\_ITEM structure

The `KSMULTIPLE_ITEM` structure describes the size and count of variable-length properties on kernel-mode pins.

## Syntax


```C++
typedef struct {
  ULONG Size;
  ULONG Count;
} KSMULTIPLE_ITEM, *PKSMULTIPLE_ITEM;
```



## Members

<dl> <dt>

**Size**
</dt> <dd>

Size of the returned memory block, in bytes. The size includes the **KSMULTIPLE\_ITEM** structure and the items that follow it.

</dd> <dt>

**Count**
</dt> <dd>

Specifies the total number of items that follow this structure.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ks.h</dt> </dl> |



## See also

<dl> <dt>

[DirectShow Structures](directshow-structures.md)
</dt> <dt>

[**IKsPin::KsQueryMediums**](ikspin-ksquerymediums.md)
</dt> <dt>

[**REGPINMEDIUM**](/windows/desktop/api/strmif/ns-strmif-regpinmedium)
</dt> </dl>

 

 




