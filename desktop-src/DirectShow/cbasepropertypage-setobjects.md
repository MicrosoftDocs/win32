---
description: The SetObjects method provides IUnknown pointers for the objects associated with the property page. This method implements the IPropertyPage::SetObjects method.
ms.assetid: 11ca1e70-772c-414e-9647-7e4c4084c0d3
title: CBasePropertyPage.SetObjects method (Cprop.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBasePropertyPage.SetObjects
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBasePropertyPage.SetObjects method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `SetObjects` method provides **IUnknown** pointers for the objects associated with the property page. This method implements the **IPropertyPage::SetObjects** method.

## Syntax


```C++
HRESULT SetObjects(
   ULONG     cObjects,
   LPUNKNOWN *ppUnk
);
```



## Parameters

<dl> <dt>

*cObjects* 
</dt> <dd>

Specifies the number of **IUnknown** pointers in the array specified by *ppUnk*.

</dd> <dt>

*ppUnk* 
</dt> <dd>

Specifies an array of **IUnknown** pointers.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include the following.



| Return code                                                                                  | Description                           |
|----------------------------------------------------------------------------------------------|---------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Success.<br/>                   |
| <dl> <dt>**E\_POINTER**</dt> </dl>    | **NULL** pointer argument.<br/> |
| <dl> <dt>**E\_UNEXPECTED**</dt> </dl> | Unexpected failure.<br/>        |



 

## Remarks

Although *ppUnk* specifies an array of **IUnknown** pointers, the **CBasePropertyPage** class is designed only to support one associated object. If *cObjects* is greater than 1, the method returns E\_UNEXPECTED.

If *cObjects* equals 1, this method calls the [**CBasePropertyPage::OnConnect**](cbasepropertypage-onconnect.md) method. If *cObjects* equals 0, this method calls the [**CBasePropertyPage::OnDisconnect**](cbasepropertypage-ondisconnect.md) method. The derived class should override both of those methods; for details, see the remarks for those methods.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Cprop.h (include Streams.h)</dt> </dl>                                                                                     |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePropertyPage Class**](cbasepropertypage.md)
</dt> </dl>

 

 




