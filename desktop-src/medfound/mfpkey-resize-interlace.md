---
description: MFPKEY_RESIZE_INTERLACE Property - Specifies whether the input stream is interlaced.
ms.assetid: 01ee0766-06ed-4255-9057-2fe033a772cd
title: MFPKEY_RESIZE_INTERLACE Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_RESIZE\_INTERLACE Property

Specifies whether the input stream is interlaced.

## Constant for IPropertyBag

Available only by using [**IPropertyStore**](/windows/win32/api/propsys/nn-propsys-ipropertystore).

## Data Type

VT\_BOOL

## Applies To

-   [Video Resizer DSP](videoresizer.md)

## Remarks

Use one of the following values:



| Value     | Description |
|-----------|-------------|
| VT\_FALSE | Progressive |
| VT\_TRUE  | Interlaced  |



 

If this property is not set, the DSP uses the input media type to determine whether the video is interlaced. You can set this property to override the media type setting.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Wmcodecdsp.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> </dl>

 

 
