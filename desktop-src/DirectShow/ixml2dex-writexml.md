---
description: The WriteXML method translates a timeline to an XML string.
ms.assetid: 1039c6fc-b2ba-4052-90b6-b7468b94c071
title: IXml2Dex::WriteXML method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
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
---

# IXml2Dex::WriteXML method

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

 

 




