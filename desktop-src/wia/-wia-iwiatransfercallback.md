---
Description: 'The IWiaTransferCallback interface receives callbacks during a data transfer.'
ms.assetid: '8fcaccf5-4d7b-4984-97ec-ec8c838a8360'
title: IWiaTransferCallback interface
---

# IWiaTransferCallback interface

The **IWiaTransferCallback** interface receives callbacks during a data transfer.

## Members

The **IWiaTransferCallback** interface inherits from the [**IUnknown**](com.iunknown) interface. **IWiaTransferCallback** also has these types of members:

-   [Methods](#methods)

### Methods

The **IWiaTransferCallback** interface has these methods.



| Method                                                                 | Description                                                              |
|:-----------------------------------------------------------------------|:-------------------------------------------------------------------------|
| [**GetNextStream**](-wia-iwiatransfercallback-getnextstream.md)       | Gets a new stream for the specified item. <br/>                    |
| [**TransferCallback**](-wia-iwiatransfercallback-transfercallback.md) | Provides progress and other notifications during a transfer. <br/> |



 

## Remarks

Image processing filter developers should implement this interface and the [**IWiaImageFilter**](-wia-iwiaimagefilter.md) interface.

The **IWiaTransferCallback** interface, like all Component Object Model (COM) interfaces, inherits the [IUnknown](com.iunknown) interface methods.



| IUnknown Methods                                        | Description                               |
|---------------------------------------------------------|-------------------------------------------|
| [IUnknown::QueryInterface](com.iunknown_queryinterface) | Returns pointers to supported interfaces. |
| [IUnknown::AddRef](com.iunknown_addref)                 | Increments reference count.               |
| [IUnknown::Release](com.iunknown_release)               | Decrements reference count.               |



 

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                   |
| Header<br/>                   | <dl> <dt>Wia.h</dt> </dl>       |
| IDL<br/>                      | <dl> <dt>Wia.idl</dt> </dl>     |
| Library<br/>                  | <dl> <dt>Wiaguid.lib</dt> </dl> |



 

 




