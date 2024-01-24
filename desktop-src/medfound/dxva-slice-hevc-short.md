---
description: Specifies slice control data.
ms.assetid: ae3399e9-b78c-473d-8ed5-e570dfb676aa
title: DXVA_Slice_HEVC_Short structure (Dxva.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DXVA_Slice_HEVC_Short
api_type: 
- HeaderDef
api_location: 
- dxva.h
---

# DXVA\_Slice\_HEVC\_Short structure

Specifies slice control data.

## Syntax


```C++
typedef struct _DXVA_Slice_HEVC_Short {
  UINT   BSNALunitDataLocation;
  UINT   SliceBytesInBuffer;
  USHORT wBadSliceChopping;
} DXVA_Slice_HEVC_Short, *LPDXVA_Slice_HEVC_Short;
```



## Members

<dl> <dt>

**BSNALunitDataLocation**
</dt> <dd>

Specifies the location of the NAL unit.

</dd> <dt>

**SliceBytesInBuffer**
</dt> <dd>

The number of bytes in the bitstream data buffer that are associated with this slice control data structure.

</dd> <dt>

**wBadSliceChopping**
</dt> <dd>

If off-host bitstream parsing is used, this value indicates the bad slice chopping and contains one of the following values:



| Requirement | Value |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Value | Description                                                                                                                                                                                                                                             |
| 0     | All bits for the slice are located within the corresponding bitstream data buffer.                                                                                                                                                                      |
| 1     | The bitstream data buffer contains the start of the slice, but not the entire slice, because the buffer is full.                                                                                                                                        |
| 2     | The bitstream data buffer contains the end of the slice. It does not contain the start of the slice, because the start of the slice was located in the previous bitstream data buffer.                                                                  |
| 3     | The bitstream data buffer does not contain the start of the slice because the start of the slice was located in the previous bitstream data buffer and it does not contain the end of the slice becuase the current bitstream data buffer is also full. |



 

</dd> </dl>

## Remarks

**DXVA\_Slice\_HEVC\_Short** contains slice control data which is passed to the hardware accelerator from the host software decoder.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                           |
| Header<br/>                   | <dl> <dt>Dxva.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Structures](media-foundation-structures.md)
</dt> </dl>

 

 




