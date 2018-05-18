---
title: Data Transfer Interfaces
description: Data Transfer Interfaces
ms.assetid: 'c42e65a4-7b77-4f39-8323-04fa60c5b140'
---

# Data Transfer Interfaces

The [**IDataObject**](idataobject.md) interface provides consumers of data with methods for getting and setting an object's data, determining which formats the object supports, and registering for and receiving notifications when data in the object changes. When obtaining data, a caller can specify the format in which it wants to render the data. The source of the data, however, determines the storage medium, which it returns in an out parameter provided by the caller.

By itself, [**IDataObject**](idataobject.md) supplies all the tools you need to implement Windows clipboard transfers or compound document transfers in your applications. If you also want to support drag and drop transfers, you need to implement the [**IDropSource**](idropsource.md) and [**IDropTarget**](idroptarget.md) interfaces along with **IDataObject**.

The [**IDataObject**](idataobject.md) interface combined with OLE clipboard APIs provide all the capabilities of the Windows clipboard APIs. It is not generally necessary to use both clipboard APIs. Data suppliers that support either drag and drop transfers or OLE compound documents must implement the **IDataObject** interface. If your application supports only clipboard transfers now, but you intend to add drag and drop or compound documents in later releases, you may want to implement **IDataObject** and the OLE clipboard APIs now in order to minimize the amount of time spent recoding and debugging later. You may also want to implement **IDataObject** in order to utilize transfer media other than global memory.

The following table summarizes which ones to use, depending on what types of data transfer you want to support:



| To support                                                                       | Use                                                                                                                                                                         |
|----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Compound documents<br/>                                                    | [**IDataObject**](idataobject.md)<br/>                                                                                                                               |
| Drag and drop transfers<br/>                                               | [**IDataObject**](idataobject.md), [**IDropSource**](idropsource.md), [**IDropTarget**](idroptarget.md), [**DoDragDrop**](dodragdrop.md) (or the equivalent)<br/> |
| Clipboard transfers using global memory exclusively<br/>                   | [Clipboard API](_win32_Clipboard_cpp)<br/>                                                                                                                            |
| Clipboard transfers using exchange mediums other than global memory.<br/>  | [**IDataObject**](idataobject.md)<br/>                                                                                                                               |
| Clipboard transfers now but drag and drop or compound documents later<br/> | [**IDataObject**](idataobject.md) and the interfaces and function listed above for "Drag and drop transfers"<br/>                                                    |



 

When a user initiates a data transfer operation, the source application creates an instance of [**IDataObject**](idataobject.md) and through it makes the data available in one or more formats. In a clipboard transfer, the application calls the [**OleSetClipboard**](olesetclipboard.md) function to pass a data-object pointer to OLE. (**OleSetClipboard** also offers standard clipboard data formats for both OLE version 1 and non-OLE applications.) In a drag and drop transfer, the application calls the [**DoDragDrop**](dodragdrop.md) function instead.

On the receiving side of the transfer, the destination receives the [**IDataObject**](idataobject.md) pointer either as an argument to an invocation of [**IDropTarget::Drop**](idroptarget-drop.md) or by calling the [**OleSetClipboard**](olesetclipboard.md) function, depending on whether the transfer is by means of drag and drop or the clipboard. Having obtained this pointer, the destination calls [**IDataObject::EnumFormatEtc**](idataobject-enumformatetc.md) to learn what formats are available for retrieval and on what types of media they can be obtained. Armed with this information, the receiving application requests the data with a call to [**IDataObject::GetData**](idataobject-getdata.md).

## Related topics

<dl> <dt>

[Data Transfer](data-transfer.md)
</dt> </dl>

 

 





