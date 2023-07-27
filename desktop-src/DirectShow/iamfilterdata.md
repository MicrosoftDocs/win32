---
description: Learn about the IAMFilterData interface, which converts filter information to packed binary data. This interface has been deprecated.
ms.assetid: d9800850-b0ee-44f7-bcb4-f2bac8d17693
title: IAMFilterData interface (Fil\_data.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMFilterData
api_type: 
- COM
api_location: 
- fil_data.h
ms.custom: UpdateFrequency5
---

# IAMFilterData interface

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This interface has been deprecated. New applications should use the [**IFilterMapper2**](/windows/desktop/api/Strmif/nn-strmif-ifiltermapper2) interface instead.

 

The `IAMFilterData` interface converts filter information to packed binary data, which can be stored in the registry. The Filter Mapper object exposes this interface.

## Members

The **IAMFilterData** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IAMFilterData** also has these types of members:

-   [Methods](#methods)

### Methods

The **IAMFilterData** interface has these methods.



| Method                                                     | Description                                               |
|:-----------------------------------------------------------|:----------------------------------------------------------|
| [**CreateFilterData**](iamfilterdata-createfilterdata.md) | Creates binary registry data for a filter.<br/>     |
| [**ParseFilterData**](iamfilterdata-parsefilterdata.md)   | Unpacks the binary registry data for a filter.<br/> |



 

## Remarks

> [!Note]  
> The header Fil\_data.h is located in the [Mapper Sample](mapper-sample.md) directory in the Windows SDK.

 

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Fil\_data.h</dt> </dl> |



## See also

<dl> <dt>

[Deprecated Interfaces](deprecated-interfaces.md)
</dt> </dl>

 

 
