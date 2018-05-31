---
Description: Interfaces
ms.assetid: f58529da-f419-445a-879a-2c087b770f0f
title: Interfaces
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Interfaces

The Picture Acquisition application programming interface (API) exposes the following interfaces.



| Interface                                                                        | Description                                                                                         |
|----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| [**IPhotoAcquire**](/windows/desktop/api/photoacquire/nn-photoacquire-iphotoacquire)                                           | Provides methods for acquiring photos from a device.                                                |
| [**IPhotoAcquireDeviceSelectionDialog**](/windows/desktop/api/photoacquire/nn-photoacquire-iphotoacquiredeviceselectiondialog) | Provides a dialog box for selecting the device to acquire images from.                              |
| [**IPhotoAcquireItem**](/windows/desktop/api/photoacquire/nn-photoacquire-iphotoacquireitem)                                   | Provides methods for working with items as they are acquired from a device.                         |
| [**IPhotoAcquireOptionsDialog**](/windows/desktop/api/photoacquire/nn-photoacquire-iphotoacquireoptionsdialog)                 | Used to display an options dialog box in which the user can select photo acquisition settings.      |
| [**IPhotoAcquireProgressCB**](/windows/desktop/api/photoacquire/nn-photoacquire-iphotoacquireprogresscb)                       | May be implemented if you wish to do extra processing at various stages in the acquisition process. |
| [**IPhotoAcquireSettings**](/windows/desktop/api/photoacquire/nn-photoacquire-iphotoacquiresettings)                           | Used to work with image acquisition settings, such as file name format.                             |
| [**IPhotoAcquireSource**](/windows/desktop/api/photoacquire/nn-photoacquire-iphotoacquiresource)                               | Used for acquisition of items from a device.                                                        |
| [**IPhotoProgressDialog**](/windows/desktop/api/photoacquire/nn-photoacquire-iphotoprogressdialog)                             | Provides the progress dialog box that may be displayed when enumerating or importing images.        |
| [**IUserInputString**](/windows/desktop/api/photoacquire/nn-photoacquire-iuserinputstring)                                     | Represents the object created when asking the user for a string.                                    |



 

## Related topics

<dl> <dt>

[**Programming Reference**](programming-reference.md)
</dt> </dl>

 

 



