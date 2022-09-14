---
title: The FORMATETC Structure
description: The FORMATETC structure is a generalized clipboard format, enhanced to encompass a target device, an aspect or view of the data, and a storage medium.
ms.assetid: 46d8988a-4b97-4c86-8b1b-db87044a7e01
ms.topic: article
ms.date: 05/31/2018
---

# The FORMATETC Structure

The FORMATETC structure is a generalized clipboard format, enhanced to encompass a target device, an *aspect* or view of the data, and a storage medium. A data consumer, such as an OLE container application, passes the [**FORMATETC**](/windows/win32/api/objidl/ns-objidl-formatetc) structure as an argument in calls to [**IDataObject**](/windows/desktop/api/ObjIdl/nn-objidl-idataobject) to indicate the type of data it wants from a data source, such as a compound document object. The source uses the **FORMATETC** structure to describe what formats it can provide.

[**FORMATETC**](/windows/win32/api/objidl/ns-objidl-formatetc) can describe virtually any data, including other objects such as monikers. A container can ask one of its embedded objects to list its data formats by calling [**IDataObject::EnumFormatEtc**](/windows/desktop/api/ObjIdl/nf-objidl-idataobject-enumformatetc), which returns an enumerator object that implements the [**IEnumFORMATETC**](/windows/desktop/api/ObjIdl/nn-objidl-ienumformatetc) interface. Instead of replying merely that it has "text and a bitmap," the object can provide a detailed description of the data, including the device (normally screen or printer) for which it is rendered, the aspect to be presented to the user (full contents, thumbnail, icon, or formatted for printing), and the storage medium containing the data (global memory, disk file, storage object, or stream). This ability to tightly describe data will, in time, result in higher quality printer and screen output as well as more efficiency in data browsing, where a thumbnail sketch is much faster to retrieve and display than a fully detailed rendering.

The following table lists fields of the [**FORMATETC**](/windows/win32/api/objidl/ns-objidl-formatetc) data structure and the information that they specify.



| Field                   | Specifies                                                                                                                                                                                                                                                                    |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **cfFormat**<br/> | The format in which the data is to be rendered, which can be a standard clipboard format, a proprietary format, or an OLE format. For more information on OLE formats, see [Compound Documents](compound-documents.md).<br/>                                          |
| **ptd**<br/>      | A [**DVTARGETDEVICE**](/windows/win32/api/objidl/ns-objidl-dvtargetdevice) structure, which contains enough information about a Windows target device, such as a screen or printer, so that a handle to its device context (hDC) can be created using the [**CreateDC**](/windows/desktop/api/wingdi/nf-wingdi-createdca) function. <br/> |
| **dwAspect**<br/> | The aspect or view of the data to be rendered; can be the full contents, a thumbnail sketch, an icon, or formatted for printing.<br/>                                                                                                                                  |
| **lindex**<br/>   | The part of the aspect that is of interest; for the present, the value must be -1, indicating that the entire view is of interest.<br/>                                                                                                                                |
| **tymed**<br/>    | The data's storage medium, which can be global memory, disk file, or an instance of one of COM's structured-storage interfaces.<br/>                                                                                                                                   |



 

## Related topics

<dl> <dt>

[Data Formats and Transfer Media](data-formats-and-transfer-media.md)
</dt> </dl>

 

