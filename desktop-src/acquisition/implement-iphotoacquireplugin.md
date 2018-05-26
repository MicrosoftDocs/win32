---
Description: Implement IPhotoAcquirePlugin
ms.assetid: 3c4f82ab-d7af-4af3-b2cc-4279c8e567da
title: Implement IPhotoAcquirePlugin
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Implement IPhotoAcquirePlugin

Your plug-in extends the Windows Vista acquisition experience by implementing the [**IPhotoAcquirePlugin**](/windows/win32/photoacquire/nn-photoacquire-iphotoacquireplugin?branch=master) interface. These methods are implemented in addition to the methods inherited from [IUnknown](https://msdn.microsoft.com/library/windows/desktop/ms680509).

Implement the [**IPhotoAcquirePlugin::Initialize**](/windows/win32/PhotoAcquire/nf-photoacquire-iphotoacquireplugin-initialize?branch=master) method to perform actions during initialization of the acquisition experience. The **IPhotoAcquirePlugin::Initialize** method provides access to the [**IPhotoAcquireSource**](/windows/win32/photoacquire/nn-photoacquire-iphotoacquiresource?branch=master) that represents the device, and the [**IPhotoAcquireProgressCB**](/windows/win32/photoacquire/nn-photoacquire-iphotoacquireprogresscb?branch=master) that provides callback functions during acquisition.

Implement the [**IPhotoAcquirePlugin::ProcessItem**](/windows/win32/PhotoAcquire/nf-photoacquire-iphotoacquireplugin-processitem?branch=master) method to provide additional functionality each time an item is acquired. **IPhotoAcquirePlugin::ProcessItem** is called both before and after an item is saved, and provides access to the underlying file stream and an [**IPhotoAcquireItem**](/windows/win32/photoacquire/nn-photoacquire-iphotoacquireitem?branch=master) object representing the item being transferred.

Implement [**IPhotoAcquirePlugin::DisplayConfigureDialog**](/windows/win32/PhotoAcquire/nf-photoacquire-iphotoacquireplugin-displayconfiguredialog?branch=master) to perform actions when the configuration dialog is displayed.

[**IPhotoAcquirePlugin::TransferComplete**](/windows/win32/PhotoAcquire/nf-photoacquire-iphotoacquireplugin-transfercomplete?branch=master) may be implemented for additional functionality when a transfer session completes.

## Related topics

<dl> <dt>

[**Programming Guide**](programming-guide.md)
</dt> </dl>

 

 



