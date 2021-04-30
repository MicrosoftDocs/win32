---
description: The WriteXMLFile method translates a timeline to XML and writes the XML data to a file.
ms.assetid: 0a269e3d-6ca3-401e-bc22-6b4e8aacdbc9
title: IXml2Dex::WriteXMLFile method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IXml2Dex.WriteXMLFile
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IXml2Dex::WriteXMLFile method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `WriteXMLFile` method translates a timeline to XML and writes the XML data to a file.

## Syntax


```C++
HRESULT WriteXMLFile(
   IUnknown *pTimeline,
   BSTR     FileName
);
```



## Parameters

<dl> <dt>

*pTimeline* 
</dt> <dd>

Pointer to the timeline object's **IUnknown** interface.

</dd> <dt>

*FileName* 
</dt> <dd>

String that specifies the name of the file to write.

</dd> </dl>

## Return value

Returns an **HRESULT** value that depends on the implementation of the interface. The **HRESULT** can include one of the following standard constants, or other values not listed.



| Return code                                                                                   | Description                     |
|-----------------------------------------------------------------------------------------------|---------------------------------|
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Argument is invalid.<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory.<br/> |
| <dl> <dt>**S\_OK**</dt> </dl>          | Success.<br/>             |



 

## Remarks

This method generates an XML file that represents all the components in the timeline.

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

 

 




