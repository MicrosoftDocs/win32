---
description: The Init method initializes the object.
ms.assetid: a919adfa-0ffb-4241-b709-ad0e8d55476a
title: CSeekingPassThru.Init method (Seekpt.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CSeekingPassThru.Init
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CSeekingPassThru.Init method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `Init` method initializes the object.

## Syntax


```C++
HRESULT Init(
  [in] BOOL bSupportRendering,
       IPin *pPin
);
```



## Parameters

<dl> <dt>

*bSupportRendering* \[in\]
</dt> <dd>

Boolean value that specifies whether the filter is a renderer. Use the value **TRUE** if the filter is a renderer, or **FALSE** otherwise.

</dd> <dt>

*pPin* 
</dt> <dd>

Pointer to the [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin) interface on the filter's input pin.

</dd> </dl>

## Return value

Returns one of the **HRESULT** values shown in the following table.



| Return code                                                                                   | Description                                        |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Success.<br/>                                |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Object was already initialized.<br/>         |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Not enough memory to create the object.<br/> |



 

## Remarks

If the value of *bSupportRendering* is **TRUE**, this method creates an instance of the [**CRendererPosPassThru**](crendererpospassthru.md) class. Otherwise, it creates an instance of the [**CPosPassThru**](cpospassthru.md) class.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Seekpt.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CSeekingPassThru Class**](cseekingpassthru.md)
</dt> </dl>

 

 




