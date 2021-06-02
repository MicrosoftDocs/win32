---
description: After an image has been selected, an application uses the IWiaDataTransfer interface (for applications running in Windows XP or earlier) or the IWiaTransfer interface (for applications running in Windows Vista or later) to transfer image data from imaging devices. See either Transfering Image Data in WIA 1.0 or Transferring Image Data in WIA 2.0 for details.
ms.assetid: cf76e526-d63b-4ee5-ba3c-871f2051a82c
title: Acquiring Images
ms.topic: article
ms.date: 05/31/2018
---

# Acquiring Images

After an image has been selected, an application uses the [**IWiaDataTransfer**](/windows/desktop/api/wia_xp/nn-wia_xp-iwiadatatransfer) interface (for applications running in Windows XP or earlier) or the [**IWiaTransfer**](-wia-iwiatransfer.md) interface (for applications running in Windows Vista or later) to transfer image data from imaging devices. See either [Transfering Image Data in WIA 1.0](-wia-transferring-image-data.md) or [Transferring Image Data in WIA 2.0](-wia-transferring-image-data-in-wia2.md) for details.

After a device has been selected, an application uses the [**IWiaItem::DeviceDlg**](/windows/desktop/api/wia_xp/nf-wia_xp-iwiaitem-devicedlg) method of the [**IWiaItem**](/windows/desktop/api/wia_xp/nn-wia_xp-iwiaitem) or [**IWiaItem2**](-wia-iwiaitem2.md) interface of the device (the root item) to select an image from a specified Windows Image Acquisition (WIA) device. The [**IWiaDevMgr::GetImageDlg**](/windows/desktop/api/wia_xp/nf-wia_xp-iwiadevmgr-getimagedlg) method displays a dialog box that allows a user to select an image from a specified device, and transfers the image to a file name selected by the user. It also allows the user to specify a device if necessary. For more information, see [Selecting a Device](-wia-selecting-a-device.md)

Note that it is not necessary for a user to select an image using the above method. An application can obtain a pointer to an image item directly from a device's item tree. For instructions, see [Navigating an Item Tree](-wia-navigating-an-item-tree.md).

Once the WIA item that represents the desired image has been selected, an application running on Windows XP or earlier queries the [**IWiaItem**](/windows/desktop/api/wia_xp/nn-wia_xp-iwiaitem) interface of that item for a pointer to its [**IWiaDataTransfer**](/windows/desktop/api/wia_xp/nn-wia_xp-iwiadatatransfer) interface. An application running on Windows Vista or later queries the [**IWiaItem2**](-wia-iwiaitem2.md) interface for a pointer to its [**IWiaTransfer**](-wia-iwiatransfer.md) interface.

The application can then uses the methods of the [**IWiaDataTransfer**](/windows/desktop/api/wia_xp/nn-wia_xp-iwiadatatransfer) (or [**IWiaTransfer**](-wia-iwiatransfer.md)) interface to transfer the image data to the application.

If the imaging device is a scanner, [**IWiaDataTransfer::idtGetData**](/windows/desktop/api/wia_xp/nf-wia_xp-iwiadatatransfer-idtgetdata), or other methods of the [**IWiaDataTransfer**](/windows/desktop/api/wia_xp/nn-wia_xp-iwiadatatransfer) interface, triggers a scan operation, and then transfers the resulting image data. If the device is a camera, the image data is simply transferred from the camera to the application.

 

 



