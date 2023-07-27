---
description: The LoadXML method loads property data expressed in Extensible Markup Language (XML).
ms.assetid: cc67e7e0-a6e0-43d1-b35d-5d64caf24e6e
title: IPropertySetter::LoadXML method (Qedit.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IPropertySetter.LoadXML
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
ms.custom: UpdateFrequency5
---

# IPropertySetter::LoadXML method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `LoadXML` method loads property data expressed in Extensible Markup Language (XML).

## Syntax


```C++
HRESULT LoadXML(
  [in] IUnknown *pxml
);
```



## Parameters

<dl> <dt>

*pxml* \[in\]
</dt> <dd>

Pointer to the **IUnknown** interface of an XML element created by the Microsoft XML parser.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include the following.



| Return code                                                                                                  | Description                     |
|--------------------------------------------------------------------------------------------------------------|---------------------------------|
| <dl> <dt>**S\_FALSE**</dt> </dl>                      | No property data.<br/>    |
| <dl> <dt>**S\_OK**</dt> </dl>                         | Success.<br/>             |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>                | Insufficient memory.<br/> |
| <dl> <dt>**VFW\_E\_INVALID\_FILE\_FORMAT**</dt> </dl> | Invalid format.<br/>      |



 

## Remarks

Typically, applications will not need to use this method. DES uses it internally to load properties from XTL files.

To use this method, create an **IXMLDocument** object and use it to parse an XML file. Then use the **IXMLDocument** object to retrieve **IXMLElement** objects. If the object has properties, you can pass the **IXMLElement** pointer to the **LoadXML** method. The method loads the properties into the property setter.

> [!Note]  
> The **IXMLDocument** and **IXMLElement** interfaces are implemented in Microsoft XML Core Services (MSXML) version 1.0, but are not implemented in more recent versions of MSXML.

 

> [!Note]  
> The header file Qedit.h is not compatible with Direct3D headers later than version 7.

 

> [!Note]  
> To obtain Qedit.h, download the [Microsoft Windows SDK Update for Windows Vista and .NET Framework 3.0](https://msdn.microsoft.com/windowsvista/bb980924.aspx). Qedit.h is not available in the Microsoft Windows SDK for Windows 7 and .NET Framework 3.5 Service Pack 1.

 

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Qedit.h</dt> </dl>      |
| Library<br/> | <dl> <dt>Strmiids.lib</dt> </dl> |



## See also

<dl> <dt>

[**IPropertySetter Interface**](ipropertysetter.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




