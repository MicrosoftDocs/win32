---
description: The IXml2Dex interface saves and loads DirectShow Editing Services (DES) project files in Extensible Markup Language (XML). This interface also provides methods for reading and writing DirectShow graph (.grf) files.
ms.assetid: a07b0cbe-1f1d-4ccd-a994-9bb1a49c78d8
title: IXml2Dex interface (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IXml2Dex
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IXml2Dex interface

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `IXml2Dex` interface saves and loads [DirectShow Editing Services](directshow-editing-services.md) (DES) project files in Extensible Markup Language (XML). This interface also provides methods for reading and writing DirectShow graph (.grf) files.

## Members

The **IXml2Dex** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IXml2Dex** also has these types of members:

-   [Methods](#methods)

### Methods

The **IXml2Dex** interface has these methods.



| Method                                                      | Description                                                                |
|:------------------------------------------------------------|:---------------------------------------------------------------------------|
| [**CopyXML**](ixml2dex-copyxml.md)                         | Not implemented.<br/>                                                |
| [**CreateGraphFromFile**](ixml2dex-creategraphfromfile.md) | Not implemented.<br/>                                                |
| [**Delete**](ixml2dex-delete.md)                           | Not implemented.<br/>                                                |
| [**PasteXML**](ixml2dex-pastexml.md)                       | Not implemented.<br/>                                                |
| [**PasteXMLFile**](ixml2dex-pastexmlfile.md)               | Not implemented.<br/>                                                |
| [**ReadXML**](ixml2dex-readxml.md)                         | Not implemented.<br/>                                                |
| [**ReadXMLFile**](ixml2dex-readxmlfile.md)                 | Loads an XML project file.<br/>                                      |
| [**Reset**](ixml2dex-reset.md)                             | Not implemented.<br/>                                                |
| [**WriteGrfFile**](ixml2dex-writegrffile.md)               | Writes a filter graph to a file in .grf format.<br/>                 |
| [**WriteXML**](ixml2dex-writexml.md)                       | Translates a timeline to an XML string.<br/>                         |
| [**WriteXMLFile**](ixml2dex-writexmlfile.md)               | Translates a timeline to XML and writes the XML data to a file.<br/> |
| [**WriteXMLPart**](ixml2dex-writexmlpart.md)               | Not implemented.<br/>                                                |



 

## Remarks

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



 

 
