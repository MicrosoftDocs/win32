---
Description: Acquiring Images
ms.assetid: ac583847-2af3-4d4d-ac55-ac26d702f16a
title: Acquiring Images
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Acquiring Images

The Picture Acquisition APIs are used to add image acquisition functionality to an application. The first step in an acquisition experience is generally to select a device to acquire images from. The [**IPhotoAcquireDeviceSelectionDialog**](/windows/desktop/api/photoacquire/nn-photoacquire-iphotoacquiredeviceselectiondialog) interface provides a dialog box that enables users to choose a device to acquire images from.

At the start of an acquisition session, an application may also need to select settings such as file name formats, as well as whether to rotate images, to prompt for tags, or to erase photos from the camera after importing them. The [**IPhotoAcquireOptionsDialog**](/windows/desktop/api/photoacquire/nn-photoacquire-iphotoacquireoptionsdialog) interface provides a dialog box to obtain acquisition settings from the user. The [**IPhotoAcquireSettings**](/windows/desktop/api/photoacquire/nn-photoacquire-iphotoacquiresettings) interface is used to programmatically select the acquisition settings.

Once a device has been selected, an application uses the [**CreatePhotoSource**](/windows/desktop/api/PhotoAcquire/nf-photoacquire-iphotoacquire-createphotosource) method of the [**IPhotoAcquire**](/windows/desktop/api/photoacquire/nn-photoacquire-iphotoacquire) interface to initialize an [**IPhotoAcquireSource**](/windows/desktop/api/photoacquire/nn-photoacquire-iphotoacquiresource) object representing the image source. At this point, the application may choose to use the methods of the **IPhotoAcquireSource** interface to manage the list of items to acquire, or to access device-specific properties and acquisition settings.

To acquire items from a device, an application uses the [**IPhotoAcquire::Acquire**](/windows/desktop/api/PhotoAcquire/nf-photoacquire-iphotoacquire-acquire) method.

To work with individual items either before or during transfer, an application may use the [**IPhotoAcquireItem**](/windows/desktop/api/photoacquire/nn-photoacquire-iphotoacquireitem) interface.

The [**IPhotoAcquireProgressCB**](/windows/desktop/api/photoacquire/nn-photoacquire-iphotoacquireprogresscb) interface enables the application to override the default behavior or supply additional functionality in response to various acquisition events, such as the end of an item transfer or the start of item deletion. When extended functionality is desired, the application supplies a custom implementation of the **IPhotoAcquireProgressCB**, in which the methods corresponding to the acquisition events to handle are implemented. These methods are implemented in addition to the methods inherited from **IUnknown**. Then the application passes the object that implements **IPhotoAcquireProgressCB** to [**IPhotoAcquire::Acquire**](/windows/desktop/api/PhotoAcquire/nf-photoacquire-iphotoacquire-acquire) (to handle events during photo acquisition) or [**IPhotoAcquireSource::InitializeItemList**](/windows/desktop/api/PhotoAcquire/nf-photoacquire-iphotoacquiresource-initializeitemlist) (to handle events during photo enumeration).

During either enumeration or acquisition of items from the photo source, the [**IPhotoProgressDialog**](/windows/desktop/api/photoacquire/nn-photoacquire-iphotoprogressdialog) interface may be used to indicate progress.

 

 



