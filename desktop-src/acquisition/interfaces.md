---
Description: Interfaces
ms.assetid: f58529da-f419-445a-879a-2c087b770f0f
title: Interfaces
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Interfaces

The Picture Acquisition application programming interface (API) exposes the following interfaces.



| Interface                                                                        | Description                                                                                         |
|----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| [**IPhotoAcquire**](/windows/win32/photoacquire/nn-photoacquire-iphotoacquire?branch=master)                                           | Provides methods for acquiring photos from a device.                                                |
| [**IPhotoAcquireDeviceSelectionDialog**](/windows/win32/photoacquire/nn-photoacquire-iphotoacquiredeviceselectiondialog?branch=master) | Provides a dialog box for selecting the device to acquire images from.                              |
| [**IPhotoAcquireItem**](/windows/win32/photoacquire/nn-photoacquire-iphotoacquireitem?branch=master)                                   | Provides methods for working with items as they are acquired from a device.                         |
| [**IPhotoAcquireOptionsDialog**](/windows/win32/photoacquire/nn-photoacquire-iphotoacquireoptionsdialog?branch=master)                 | Used to display an options dialog box in which the user can select photo acquisition settings.      |
| [**IPhotoAcquireProgressCB**](/windows/win32/photoacquire/nn-photoacquire-iphotoacquireprogresscb?branch=master)                       | May be implemented if you wish to do extra processing at various stages in the acquisition process. |
| [**IPhotoAcquireSettings**](/windows/win32/photoacquire/nn-photoacquire-iphotoacquiresettings?branch=master)                           | Used to work with image acquisition settings, such as file name format.                             |
| [**IPhotoAcquireSource**](/windows/win32/photoacquire/nn-photoacquire-iphotoacquiresource?branch=master)                               | Used for acquisition of items from a device.                                                        |
| [**IPhotoProgressDialog**](/windows/win32/photoacquire/nn-photoacquire-iphotoprogressdialog?branch=master)                             | Provides the progress dialog box that may be displayed when enumerating or importing images.        |
| [**IUserInputString**](/windows/win32/photoacquire/nn-photoacquire-iuserinputstring?branch=master)                                     | Represents the object created when asking the user for a string.                                    |



 

## Related topics

<dl> <dt>

[**Programming Reference**](programming-reference.md)
</dt> </dl>

 

 



