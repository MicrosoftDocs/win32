---
description: The ReadXMLFile method loads an XML project file.
ms.assetid: 8269da74-fb33-42cf-ae8c-fe3d7db27aea
title: IXml2Dex::ReadXMLFile method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IXml2Dex.ReadXMLFile
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IXml2Dex::ReadXMLFile method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `ReadXMLFile` method loads an XML project file. This method creates instances of all the objects expressed in the XML file and inserts them into the timeline, as well as applying any attributes given for the timeline, such as frame rate or default effect.

## Syntax


```C++
HRESULT ReadXMLFile(
   IUnknown *pTimeline,
   BSTR     XMLName
);
```



## Parameters

<dl> <dt>

*pTimeline* 
</dt> <dd>

Pointer to a timeline object's **IUnknown** interface.

</dd> <dt>

*XMLName* 
</dt> <dd>

String that specifies the name of the file to load.

</dd> </dl>

## Return value

Returns an HRESULT value. Possible values include the following.



| Return code                                                                                                  | Description                    |
|--------------------------------------------------------------------------------------------------------------|--------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                         | Success<br/>             |
| <dl> <dt>**VFW\_E\_INVALID\_FILE\_FORMAT**</dt> </dl> | Invalid file format<br/> |



 

## Remarks

This method does not clear existing objects from the timeline before it inserts the new objects defined in the XML file. If you need to refresh an existing timeline, call [**IAMTimeline::ClearAllGroups**](iamtimeline-clearallgroups.md) first.

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

 

 




