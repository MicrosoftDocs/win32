---
Description: The IWiaPreview interface caches unfiltered images internally and passes them through image processing filters.
ms.assetid: 8a51c42b-aa1d-4df0-aba3-6aeb8e1ca2cf
title: IWiaPreview interface
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IWiaPreview interface

The **IWiaPreview** interface caches unfiltered images internally and passes them through image processing filters.

## Members

The **IWiaPreview** interface inherits from the [**IUnknown**](com.iunknown) interface. **IWiaPreview** also has these types of members:

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

The **IWiaPreview** interface, like all Component Object Model (COM) interfaces, inherits the [IUnknown](com.iunknown) interface methods.



| IUnknown Methods                                        | Description                               |
|---------------------------------------------------------|-------------------------------------------|
| [IUnknown::QueryInterface](com.iunknown_queryinterface) | Returns pointers to supported interfaces. |
| [IUnknown::AddRef](com.iunknown_addref)                 | Increments reference count.               |
| [IUnknown::Release](com.iunknown_release)               | Decrements reference count.               |



 

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wia.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wia.idl</dt> </dl> |



 

 




