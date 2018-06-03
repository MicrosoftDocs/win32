---
Description: The IWiaPreview interface caches unfiltered images internally and passes them through image processing filters.
ms.assetid: 8a51c42b-aa1d-4df0-aba3-6aeb8e1ca2cf
title: IWiaPreview interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IWiaPreview interface

The **IWiaPreview** interface caches unfiltered images internally and passes them through image processing filters.

## Members

The **IWiaPreview** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/windows/desktop/33f1d79a-33fc-4ce5-a372-e08bda378332) interface. **IWiaPreview** also has these types of members:

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

The **IWiaPreview** interface, like all Component Object Model (COM) interfaces, inherits the [IUnknown](https://msdn.microsoft.com/windows/desktop/33f1d79a-33fc-4ce5-a372-e08bda378332) interface methods.



| IUnknown Methods                                        | Description                               |
|---------------------------------------------------------|-------------------------------------------|
| [IUnknown::QueryInterface](https://msdn.microsoft.com/windows/desktop/54d5ff80-18db-43f2-b636-f93ac053146d) | Returns pointers to supported interfaces. |
| [IUnknown::AddRef](https://msdn.microsoft.com/windows/desktop/b4316efd-73d4-4995-b898-8025a316ba63)                 | Increments reference count.               |
| [IUnknown::Release](https://msdn.microsoft.com/windows/desktop/4b494c6f-f0ee-4c35-ae45-ed956f40dc7a)               | Decrements reference count.               |



 

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wia.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wia.idl</dt> </dl> |



 

 




