---
description: The PID\_MAP structure contains identifies the contents of an MPEG-2 transport stream packet ID.
ms.assetid: c247ec75-483d-4587-a82f-07bbf6d277b4
title: PID_MAP structure (Bdatypes.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PID_MAP
api_type: 
- HeaderDef
api_location: 
- bdatypes.h
---

# PID\_MAP structure

The `PID_MAP` structure contains identifies the contents of an MPEG-2 transport stream packet ID.

## Syntax


```C++
typedef struct {
  ULONG                ulPID;
  MEDIA_SAMPLE_CONTENT MediaSampleContent;
} PID_MAP;
```



## Members

<dl> <dt>

**ulPID**
</dt> <dd>

Specifies the packet ID (PID)

</dd> <dt>

**MediaSampleContent**
</dt> <dd>

Specifies the contents of the packet payload, as a [**MEDIA\_SAMPLE\_CONTENT**](media-sample-content.md) enumeration type.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Bdatypes.h (include Bdaiface.h)</dt> </dl> |



## See also

<dl> <dt>

[DirectShow Structures](directshow-structures.md)
</dt> <dt>

[**IEnumPIDMap Interface**](/previous-versions/windows/desktop/api/Bdaiface/nn-bdaiface-ienumpidmap)
</dt> </dl>

 

 




