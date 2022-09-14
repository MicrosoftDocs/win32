---
description: The IWiaImageFilter interface is an extension interface implemented by image processing filter developers and called by Windows Image Acquisition (WIA) 2.0.
ms.assetid: 2abe913b-bb2b-486d-a3f4-d5932433fc82
title: IWiaImageFilter interface (Wia.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWiaImageFilter
api_type: 
- COM
api_location: 
- Wia.h
---

# IWiaImageFilter interface

The **IWiaImageFilter** interface is an extension interface implemented by image processing filter developers and called by Windows Image Acquisition (WIA) 2.0.

## Members

The **IWiaImageFilter** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IWiaImageFilter** also has these types of members:

-   [Methods](#methods)

### Methods

The **IWiaImageFilter** interface has these methods.



| Method                                                                | Description                                                                                             |
|:----------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------|
| [**ApplyProperties**](-wia-iwiaimagefilter-applyproperties.md)       | Enables the image processing filter to write properties back to the driver (and device).<br/>     |
| [**FilterPreviewImage**](-wia-iwiaimagefilter-filterpreviewimage.md) | Filters the preview image.<br/>                                                                   |
| [**InitializeFilter**](-wia-iwiaimagefilter-initializefilter.md)     | Initializes the filter. Called by WIA 2.0 before each image download. <br/>                       |
| [**SetNewCallback**](-wia-iwiaimagefilter-setnewcallback.md)         | Sets a new application callback for the image processing filter to use for forwarding calls.<br/> |



 

## Remarks

Image processing filter developers should implement this interface and the [**IWiaTransferCallback**](-wia-iwiatransfercallback.md) interface.

WIA 2.0 calls filter methods. They are never called directly from an application.

Microsoft supplies the WIA 2.0 Preview Component, which caches the original, unfiltered preview image that is acquired from the scanner. An application uses [CoCreateInstance](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance) to co-create an instance of the WIA 2.0 Preview Component (CLSID\_WiaPreview), which loads the filter using [**IWiaItem2::GetExtension**](-wia-iwiaitem2-getextension.md). The filter is called automatically when the application calls [**IWiaTransfer::Download**](-wia-iwiatransfer-download.md).

The image processing filter is always executed when an image is scanned. An application cannot acquire an image from the scanner without having the imaging filter applied first.

A filter must implement brightness and contrast at a minimum. The common UI, which provides brightness and contrast controls to the user, can display accurate previews to the user.

An image processing filter should never modify the *lMessage* member of the [**WiaTransferParams**](-wia-wiatransferparams.md) structure.

To read the required properties the image processing filter should call [**IWiaPropertyStorage::GetPropertyStream**](/windows/desktop/api/wia_xp/nf-wia_xp-iwiapropertystorage-getpropertystream) on the [**IWiaPropertyStorage**](/windows/desktop/api/wia_xp/nn-wia_xp-iwiapropertystorage) interface that it gets from the item by calling [IWiaImageFilter::QueryInterface](/windows/win32/api/unknwn/nf-unknwn-iunknown-queryinterface(q)). The filter can then instantiate an [IPropertyStorage](/windows/win32/api/propidlbase/nn-propidlbase-ipropertystorage) instance on this stream to read the items properties. The image processing filter should not call [IWiaPropertyStorage::ReadMultiple](/windows/win32/api/propidlbase/nf-propidlbase-ipropertystorage-readmultiple) directly because this method calls into the driver's `drvReadItemProperties`, but the WIA 2.0 service has already locked the driver in the `drvAcquireItemData` call so this call will timeout and fail.

The properties that the filter is interested in could for example be the brightness and contrast settings. The filter typically also needs to read the image format as well as the preview property, [**WIA\_DPS\_PREVIEW**](-wia-wiaitempropscannerdevice.md), from *pWiaItem2*. These properties are all used in the filtering process.

The WIA 2.0 components always writes unfiltered data into the image processing filter. The image processing algorithm implemented by the filter's stream can filter the data more than once and does not have to be concerned with producing the same results as filtering the data once.

The filter must pay attention to the [**WIA\_DPS\_PREVIEW**](-wia-wiaitempropscannerdevice.md) property, especially if some filter related tasks are handled in hardware. For example, a certain driver can change the brightness of the lamp in the scanner hardware depending on how the application has set the brightness into a WIA 2.0 item. During the final scan (when the application calls [**IWiaTransfer::Download**](-wia-iwiatransfer-download.md)) the driver would typically modify the physical lamp of the scanner. In this case the image processing filter may not have to perform any brightness processing at all. During a preview scan, however, the driver should not modify the brightness of the lamp—instead this should be taken care of solely in the image processing filter. It is important that the WIA 2.0 Preview Component and the image processing filter return accurate images based on the properties set into the item.

An image processing filter must support all image formats that the driver supports.

The image processing filter is always given an image corresponding to the selection area set into the item for which we are acquiring the image. Note, however, that the image may have been rotated by the driver in case it supports the [**WIA\_IPS\_ROTATION**](-wia-wiaitempropscanneritem.md) property.

The image processing filter is created through [**IWiaItem2::GetExtension**](-wia-iwiaitem2-getextension.md), typically not by the application but by WIA 2.0 components when an application calls [**IWiaPreview::GetNewPreview**](-wia-iwiapreview-getnewpreview.md) or [**IWiaTransfer::Download**](-wia-iwiatransfer-download.md).

The **IWiaImageFilter** interface, like all Component Object Model (COM) interfaces, inherits the [IUnknown](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface methods.



| IUnknown Methods                                        | Description                               |
|---------------------------------------------------------|-------------------------------------------|
| [IUnknown::QueryInterface](/windows/win32/api/unknwn/nf-unknwn-iunknown-queryinterface(q)) | Returns pointers to supported interfaces. |
| [IUnknown::AddRef](/windows/win32/api/unknwn/nf-unknwn-iunknown-addref)                 | Increments reference count.               |
| [IUnknown::Release](/windows/win32/api/unknwn/nf-unknwn-iunknown-release)               | Decrements reference count.               |



 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wia.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wia.idl</dt> </dl> |



 

 
