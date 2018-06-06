---
Description: The IWiaTransferCallback interface receives callbacks during a data transfer.
ms.assetid: 8fcaccf5-4d7b-4984-97ec-ec8c838a8360
title: IWiaTransferCallback interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IWiaTransferCallback interface

The **IWiaTransferCallback** interface receives callbacks during a data transfer.

## Members

The **IWiaTransferCallback** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/33f1d79a-33fc-4ce5-a372-e08bda378332) interface. **IWiaTransferCallback** also has these types of members:

-   [Methods](#methods)

### Methods

The **IWiaTransferCallback** interface has these methods.



| Method                                                                 | Description                                                              |
|:-----------------------------------------------------------------------|:-------------------------------------------------------------------------|
| [**GetNextStream**](-wia-iwiatransfercallback-getnextstream.md)       | Gets a new stream for the specified item. <br/>                    |
| [**TransferCallback**](-wia-iwiatransfercallback-transfercallback.md) | Provides progress and other notifications during a transfer. <br/> |



 

## Remarks

Image processing filter developers should implement this interface and the [**IWiaImageFilter**](-wia-iwiaimagefilter.md) interface.

The **IWiaTransferCallback** interface, like all Component Object Model (COM) interfaces, inherits the [IUnknown](https://msdn.microsoft.com/33f1d79a-33fc-4ce5-a372-e08bda378332) interface methods.



| IUnknown Methods                                        | Description                               |
|---------------------------------------------------------|-------------------------------------------|
| [IUnknown::QueryInterface](https://msdn.microsoft.com/54d5ff80-18db-43f2-b636-f93ac053146d) | Returns pointers to supported interfaces. |
| [IUnknown::AddRef](https://msdn.microsoft.com/b4316efd-73d4-4995-b898-8025a316ba63)                 | Increments reference count.               |
| [IUnknown::Release](https://msdn.microsoft.com/4b494c6f-f0ee-4c35-ae45-ed956f40dc7a)               | Decrements reference count.               |



 

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                   |
| Header<br/>                   | <dl> <dt>Wia.h</dt> </dl>       |
| IDL<br/>                      | <dl> <dt>Wia.idl</dt> </dl>     |
| Library<br/>                  | <dl> <dt>Wiaguid.lib</dt> </dl> |



 

 




