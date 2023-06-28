---
description: These functions provide support for implementing the IUnknown interface in DirectShow.
ms.assetid: 991e4c69-7d30-4ecf-9ccf-4920452c21d6
title: COM Helper Functions (Combase.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- COM
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# COM Helper Functions

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

These functions provide support for implementing the **IUnknown** interface in DirectShow.



| Function                                               | Description                                                           |
|--------------------------------------------------------|-----------------------------------------------------------------------|
| [**DECLARE\_IUNKNOWN**](declare-iunknown.md)          | Declares the three methods of the base interface for a new interface. |
| [**GetInterface**](getinterface.md)                   | Retrieves an interface pointer to the requested client.               |
| [**INonDelegatingUnknown**](inondelegatingunknown.md) | Nondelegating version of the **IUnknown** interface.                  |
| [**LoadOLEAut32**](loadoleaut32.md)                   | Loads the Automation DLL (OleAut32.dll).                              |



 

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Combase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[Utility Functions](utility-functions.md)
</dt> </dl>

 

 




