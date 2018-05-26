---
title: Data Transfer Interfaces
description: Data Transfer Interfaces
ms.assetid: c42e65a4-7b77-4f39-8323-04fa60c5b140
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Data Transfer Interfaces

The [**IDataObject**](/windows/win32/ObjIdl/nn-objidl-idataobject?branch=master) interface provides consumers of data with methods for getting and setting an object's data, determining which formats the object supports, and registering for and receiving notifications when data in the object changes. When obtaining data, a caller can specify the format in which it wants to render the data. The source of the data, however, determines the storage medium, which it returns in an out parameter provided by the caller.

By itself, [**IDataObject**](/windows/win32/ObjIdl/nn-objidl-idataobject?branch=master) supplies all the tools you need to implement Windows clipboard transfers or compound document transfers in your applications. If you also want to support drag and drop transfers, you need to implement the [**IDropSource**](/windows/win32/OleIdl/nn-oleidl-idropsource?branch=master) and [**IDropTarget**](/windows/win32/OleIdl/nn-oleidl-idroptarget?branch=master) interfaces along with **IDataObject**.

The [**IDataObject**](/windows/win32/ObjIdl/nn-objidl-idataobject?branch=master) interface combined with OLE clipboard APIs provide all the capabilities of the Windows clipboard APIs. It is not generally necessary to use both clipboard APIs. Data suppliers that support either drag and drop transfers or OLE compound documents must implement the **IDataObject** interface. If your application supports only clipboard transfers now, but you intend to add drag and drop or compound documents in later releases, you may want to implement **IDataObject** and the OLE clipboard APIs now in order to minimize the amount of time spent recoding and debugging later. You may also want to implement **IDataObject** in order to utilize transfer media other than global memory.

The following table summarizes which ones to use, depending on what types of data transfer you want to support:



| To support                                                                       | Use                                                                                                                                                                         |
|----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Compound documents<br/>                                                    | [**IDataObject**](/windows/win32/ObjIdl/nn-objidl-idataobject?branch=master)<br/>                                                                                                                               |
| Drag and drop transfers<br/>                                               | [**IDataObject**](/windows/win32/ObjIdl/nn-objidl-idataobject?branch=master), [**IDropSource**](/windows/win32/OleIdl/nn-oleidl-idropsource?branch=master), [**IDropTarget**](/windows/win32/OleIdl/nn-oleidl-idroptarget?branch=master), [**DoDragDrop**](/windows/win32/Ole2/nf-ole2-dodragdrop?branch=master) (or the equivalent)<br/> |
| Clipboard transfers using global memory exclusively<br/>                   | [Clipboard API](_win32_Clipboard_cpp)<br/>                                                                                                                            |
| Clipboard transfers using exchange mediums other than global memory.<br/>  | [**IDataObject**](/windows/win32/ObjIdl/nn-objidl-idataobject?branch=master)<br/>                                                                                                                               |
| Clipboard transfers now but drag and drop or compound documents later<br/> | [**IDataObject**](/windows/win32/ObjIdl/nn-objidl-idataobject?branch=master) and the interfaces and function listed above for "Drag and drop transfers"<br/>                                                    |



 

When a user initiates a data transfer operation, the source application creates an instance of [**IDataObject**](/windows/win32/ObjIdl/nn-objidl-idataobject?branch=master) and through it makes the data available in one or more formats. In a clipboard transfer, the application calls the [**OleSetClipboard**](/windows/win32/Ole2/nf-ole2-olesetclipboard?branch=master) function to pass a data-object pointer to OLE. (**OleSetClipboard** also offers standard clipboard data formats for both OLE version 1 and non-OLE applications.) In a drag and drop transfer, the application calls the [**DoDragDrop**](/windows/win32/Ole2/nf-ole2-dodragdrop?branch=master) function instead.

On the receiving side of the transfer, the destination receives the [**IDataObject**](/windows/win32/ObjIdl/nn-objidl-idataobject?branch=master) pointer either as an argument to an invocation of [**IDropTarget::Drop**](/windows/win32/OleIdl/nf-oleidl-idroptarget-drop?branch=master) or by calling the [**OleSetClipboard**](/windows/win32/Ole2/nf-ole2-olesetclipboard?branch=master) function, depending on whether the transfer is by means of drag and drop or the clipboard. Having obtained this pointer, the destination calls [**IDataObject::EnumFormatEtc**](/windows/win32/ObjIdl/nf-objidl-idataobject-enumformatetc?branch=master) to learn what formats are available for retrieval and on what types of media they can be obtained. Armed with this information, the receiving application requests the data with a call to [**IDataObject::GetData**](/windows/win32/ObjIdl/nf-objidl-idataobject-getdata?branch=master).

## Related topics

<dl> <dt>

[Data Transfer](data-transfer.md)
</dt> </dl>

 

 





