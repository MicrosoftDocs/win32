---
description: The Show method shows or hides the dialog box. This method implements the IPropertyPage::Show method.
ms.assetid: 03796779-ed41-4b68-852d-6b1849a9dc10
title: CBasePropertyPage.Show method (Cprop.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBasePropertyPage.Show
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBasePropertyPage.Show method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `Show` method shows or hides the dialog box. This method implements the [IPropertyPage::Show](/windows/win32/api/ocidl/nf-ocidl-ipropertypage-show) method.

## Syntax

```C++
HRESULT Show(
   UINT nCmdShow
);
```
## Parameters

*nCmdShow*

Type: **[UINT](../winprog/windows-data-types.md)**

Value that specifies whether to show or hide the window. For more information, see the [IPropertyPage::Show](/windows/win32/api/ocidl/nf-ocidl-ipropertypage-show) method.

## Return value

Returns an **HRESULT** value. Possible values include the following.

| Return code                                                                                  | Description                    |
|----------------------------------------------------------------------------------------------|--------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Success.<br/>            |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Invalid argument.<br/>   |
| <dl> <dt>**E\_UNEXPECTED**</dt> </dl> | Unexpected failure.<br/> |

## Requirements

| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header  | <dl> <dt>Cprop.h (include Streams.h)</dt> </dl>                                                                                     |
| Library | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |

## See also

[CBasePropertyPage Class](cbasepropertypage.md)
