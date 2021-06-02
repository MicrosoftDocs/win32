---
description: Contains format information for smart recompression.
ms.assetid: 471a7b4a-e639-443b-a30e-870b747e072c
title: SCompFmt0 structure (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SCompFmt0
api_type: 
- HeaderDef
api_location: 
- Qedit.h
---

# SCompFmt0 structure

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

Contains format information for smart recompression.

## Syntax


```C++
typedef struct _SCompFmt0 {
  long          nFormatId;
  AM_MEDIA_TYPE MediaType;
} SCompFmt0;
```



## Members

<dl> <dt>

**nFormatId**
</dt> <dd>

Reserved; must be zero.

</dd> <dt>

**MediaType**
</dt> <dd>

[**AM\_MEDIA\_TYPE**](/windows/win32/api/strmif/ns-strmif-am_media_type) structure that describes the compression format.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Qedit.h</dt> </dl> |



## See also

<dl> <dt>

[**IAMTimelineGroup::GetSmartRecompressFormat**](iamtimelinegroup-getsmartrecompressformat.md)
</dt> <dt>

[**IAMTimelineGroup::SetSmartRecompressFormat**](iamtimelinegroup-setsmartrecompressformat.md)
</dt> </dl>

 

 




