---
Description: The IWiaPreview interface caches unfiltered images internally and passes them through image processing filters.
ms.assetid: 8a51c42b-aa1d-4df0-aba3-6aeb8e1ca2cf
title: IWiaPreview interface (Wia.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWiaPreview
api_type: 
- COM
api_location: 
- Wia.h
---

# IWiaPreview interface

The **IWiaPreview** interface caches unfiltered images internally and passes them through image processing filters.

## Members

The **IWiaPreview** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/ms680509(v=VS.85).aspx) interface. **IWiaPreview** also has these types of members:

-   [Methods](#methods)

### Methods

The **IWiaPreview** interface has these methods.



| Method                                                  | Description                                                                                                                                                                                 |
|:--------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Clear**](-wia-iwiapreview-clear.md)                 | Releases the unfiltered image cached by the [**IWiaPreview::GetNewPreview**](-wia-iwiapreview-getnewpreview.md) method. It also releases the image processing filter. <br/>          |
| [**DetectRegions**](-wia-iwiapreview-detectregions.md) | Invokes the driver segmentation filter and passes the unfiltered image cached by the [**IWiaPreview::GetNewPreview**](-wia-iwiapreview-getnewpreview.md) method to the filter. <br/> |
| [**GetNewPreview**](-wia-iwiapreview-getnewpreview.md) | Caches internally the unfiltered image returned from the driver. <br/>                                                                                                                |
| [**UpdatePreview**](-wia-iwiapreview-updatepreview.md) | Gets the unfiltered image cached by the [**IWiaPreview::GetNewPreview**](-wia-iwiapreview-getnewpreview.md) method. <br/>                                                            |



 

## Remarks

This filter is called automatically by the [**IWiaTransfer::Download**](-wia-iwiatransfer-download.md) method.

The **IWiaPreview** interface, like all Component Object Model (COM) interfaces, inherits the [IUnknown](https://msdn.microsoft.com/library/ms680509(v=VS.85).aspx) interface methods.



| IUnknown Methods                                        | Description                               |
|---------------------------------------------------------|-------------------------------------------|
| [IUnknown::QueryInterface](https://msdn.microsoft.com/library/ms682521(v=VS.85).aspx) | Returns pointers to supported interfaces. |
| [IUnknown::AddRef](https://msdn.microsoft.com/library/ms691379(v=VS.85).aspx)                 | Increments reference count.               |
| [IUnknown::Release](https://msdn.microsoft.com/library/ms682317(v=VS.85).aspx)               | Decrements reference count.               |



 

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wia.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wia.idl</dt> </dl> |



 

 




