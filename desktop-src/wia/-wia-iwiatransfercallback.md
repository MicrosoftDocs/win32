---
Description: The IWiaTransferCallback interface receives callbacks during a data transfer.
ms.assetid: 8fcaccf5-4d7b-4984-97ec-ec8c838a8360
title: IWiaTransferCallback interface (Wia.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWiaTransferCallback
api_type: 
- COM
api_location: 
- Wiaguid.lib
- Wiaguid.dll
---

# IWiaTransferCallback interface

The **IWiaTransferCallback** interface receives callbacks during a data transfer.

## Members

The **IWiaTransferCallback** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/en-us/library/ms680509(v=VS.85).aspx) interface. **IWiaTransferCallback** also has these types of members:

-   [Methods](#methods)

### Methods

The **IWiaTransferCallback** interface has these methods.



| Method                                                                 | Description                                                              |
|:-----------------------------------------------------------------------|:-------------------------------------------------------------------------|
| [**GetNextStream**](-wia-iwiatransfercallback-getnextstream.md)       | Gets a new stream for the specified item. <br/>                    |
| [**TransferCallback**](-wia-iwiatransfercallback-transfercallback.md) | Provides progress and other notifications during a transfer. <br/> |



 

## Remarks

Image processing filter developers should implement this interface and the [**IWiaImageFilter**](-wia-iwiaimagefilter.md) interface.

The **IWiaTransferCallback** interface, like all Component Object Model (COM) interfaces, inherits the [IUnknown](https://msdn.microsoft.com/en-us/library/ms680509(v=VS.85).aspx) interface methods.



| IUnknown Methods                                        | Description                               |
|---------------------------------------------------------|-------------------------------------------|
| [IUnknown::QueryInterface](https://msdn.microsoft.com/en-us/library/ms682521(v=VS.85).aspx) | Returns pointers to supported interfaces. |
| [IUnknown::AddRef](https://msdn.microsoft.com/en-us/library/ms691379(v=VS.85).aspx)                 | Increments reference count.               |
| [IUnknown::Release](https://msdn.microsoft.com/en-us/library/ms682317(v=VS.85).aspx)               | Decrements reference count.               |



 

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                   |
| Header<br/>                   | <dl> <dt>Wia.h</dt> </dl>       |
| IDL<br/>                      | <dl> <dt>Wia.idl</dt> </dl>     |
| Library<br/>                  | <dl> <dt>Wiaguid.lib</dt> </dl> |



 

 




