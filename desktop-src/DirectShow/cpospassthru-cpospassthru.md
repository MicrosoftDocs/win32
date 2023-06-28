---
description: CPosPassThru.CPosPassThru constructor - Constructor method.
ms.assetid: b258401c-158b-4eb8-8736-1e1ad9a8403a
title: CPosPassThru.CPosPassThru constructor
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CPosPassThru.CPosPassThru
api_type: 
- COM
api_location: 
ms.custom: UpdateFrequency5
---

# CPosPassThru.CPosPassThru constructor

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Constructor method.

## Syntax


```C++
CPosPassThru(
   const TCHAR     *pName,
         LPUNKNOWN pUnk,
         HRESULT   *phr,
         IPin      *pPin,
                   
);
```



## Parameters

<dl> <dt>

*pName* 
</dt> <dd>

Pointer to the name of the object, for debugging purposes. Allocate this parameter in static memory.

</dd> <dt>

*pUnk* 
</dt> <dd>

Pointer to the owner of this object. If the object is aggregated, pass a pointer to the aggregating object's **IUnknown** interface. Otherwise, set this parameter to **NULL**.

</dd> <dt>

*phr* 
</dt> <dd>

Pointer to an **HRESULT** value. Ignored.

</dd> <dt>

*pPin* 
</dt> <dd>

Pointer to the [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin) interface of the filter's input pin.

</dd> <dt>

 
</dt> <dd></dd> </dl>

 

 



