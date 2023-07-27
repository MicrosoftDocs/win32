---
description: Learn about the IAMFilterData::ParseFilterData method, unpacks the binary registry data for a filter. This interface has been deprecated.
ms.assetid: 86095fcf-3364-42a0-95db-08223fa3cc20
title: IAMFilterData::ParseFilterData method (Fil\_data.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMFilterData.ParseFilterData
api_type: 
- COM
api_location: 
- Quartz.dll
ms.custom: UpdateFrequency5
---

# IAMFilterData::ParseFilterData method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This interface has been deprecated. New applications should not use it.

 

The `ParseFilterData` method unpacks the binary registry data for a filter.

There is typically no reason for an application to call this method. The [**IFilterMapper2::EnumMatchingFilters**](/windows/desktop/api/Strmif/nf-strmif-ifiltermapper2-enummatchingfilters) method provides a more convenient way to access the filter registry data.

## Syntax


```C++
HRESULT ParseFilterData(
  [in]  BYTE  *rgbFilterData,
  [in]  ULONG cb,
  [out] BYTE  **prgbRegFilter2
);
```



## Parameters

<dl> <dt>

*rgbFilterData* \[in\]
</dt> <dd>

Pointer to the binary registry data. You can get this data by retrieving the "FilterData" property from the filter moniker. The data is stored as a **SAFEARRAY** of bytes (VT\_UI1 \| VT\_ARRAY).

</dd> <dt>

*cb* \[in\]
</dt> <dd>

Specifies the size of the binary data, in bytes.

</dd> <dt>

*prgbRegFilter2* \[out\]
</dt> <dd>

Address of a variable that receives a pointer to the unpacked data. When the method returns, cast this pointer to a [**REGFILTER2**](/windows/desktop/api/strmif/ns-strmif-regfilter2) type to access the filter data. The caller must release the memory by calling the **CoTaskMemFree** method.

</dd> </dl>

## Return value

If the method succeeds, it returns S\_OK. If it fails, it returns an error code.

## Remarks

> [!Note]  
> The header Fil\_data.h is located in the [Mapper Sample](mapper-sample.md) directory in the Windows SDK.

 

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Fil\_data.h</dt> </dl> |
| DLL<br/>    | <dl> <dt>Quartz.dll</dt> </dl>  |



## See also

<dl> <dt>

[**IAMFilterData Interface**](iamfilterdata.md)
</dt> </dl>

 

 




