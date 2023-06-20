---
description: The WriteXML method translates a timeline to an XML string.
ms.assetid: 1039c6fc-b2ba-4052-90b6-b7468b94c071
title: IXml2Dex::WriteXML method (Qedit.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IXml2Dex.WriteXML
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
ms.custom: UpdateFrequency5
---

# IXml2Dex::WriteXML method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `WriteXML` method translates a timeline to an XML string.

## Syntax


```C++
HRESULT WriteXML(
   IUnknown *pTimeline,
   BSTR     *pbstrXML
);
```



## Parameters

<dl> <dt>

*pTimeline* 
</dt> <dd>

Pointer to the timeline object's **IUnknown** interface.

</dd> <dt>

*pbstrXML* 
</dt> <dd>

Pointer to a variable of type BSTR that receives the XML string describing the timeline.

</dd> </dl>

## Return value

Returns S\_OK if successful. If there is insufficient memory for the conversion, returns E\_OUTOFMEMORY. Otherwise, returns another error code.

## Remarks

The method allocates memory for the string. The application must call **SysFreeString** to free the memory.

> [!Note]  
> The header file Qedit.h is not compatible with Direct3D headers later than version 7.

 

> [!Note]  
> To obtain Qedit.h, download the [Microsoft Windows SDK Update for Windows Vista and .NET Framework 3.0](https://msdn.microsoft.com/windowsvista/bb980924.aspx). Qedit.h is not available in the Microsoft Windows SDK for Windows 7 and .NET Framework 3.5 Service Pack 1.

 

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Version<br/> | Internet Explorer 4.0 or later<br/>                                               |
| Header<br/>  | <dl> <dt>Qedit.h</dt> </dl>      |
| Library<br/> | <dl> <dt>Strmiids.lib</dt> </dl> |



## See also

<dl> <dt>

[**IXml2Dex Interface**](ixml2dex.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




