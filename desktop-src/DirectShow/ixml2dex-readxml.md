---
description: IXml2Dex::ReadXML method - Not implemented.
ms.assetid: f75ee69d-2778-4c3c-a810-6708b1669541
title: IXml2Dex::ReadXML method
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IXml2Dex.ReadXML
api_type: 
- COM
api_location: 
ms.custom: UpdateFrequency5
---

# IXml2Dex::ReadXML method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

Not implemented.

## Syntax


```C++
HRESULT ReadXML(
   IUnknown *pTimeline,
   IUnknown *pXML
);
```



## Parameters

<dl> <dt>

*pTimeline* 
</dt> <dd>

Reserved.

</dd> <dt>

*pXML* 
</dt> <dd>

Reserved.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

> [!Note]  
> The header file Qedit.h is not compatible with Direct3D headers later than version 7.

 

> [!Note]  
> To obtain Qedit.h, download the [Microsoft Windows SDK Update for Windows Vista and .NET Framework 3.0](https://msdn.microsoft.com/windowsvista/bb980924.aspx). Qedit.h is not available in the Microsoft Windows SDK for Windows 7 and .NET Framework 3.5 Service Pack 1.

 

## See also

<dl> <dt>

[**IXml2Dex Interface**](ixml2dex.md)
</dt> </dl>

 

 



