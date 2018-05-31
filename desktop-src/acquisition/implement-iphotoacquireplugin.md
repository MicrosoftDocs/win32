---
Description: Implement IPhotoAcquirePlugin
ms.assetid: 3c4f82ab-d7af-4af3-b2cc-4279c8e567da
title: Implement IPhotoAcquirePlugin
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Implement IPhotoAcquirePlugin

Your plug-in extends the Windows Vista acquisition experience by implementing the [**IPhotoAcquirePlugin**](/windows/desktop/api/photoacquire/nn-photoacquire-iphotoacquireplugin) interface. These methods are implemented in addition to the methods inherited from [IUnknown](https://msdn.microsoft.com/library/windows/desktop/ms680509).

Implement the [**IPhotoAcquirePlugin::Initialize**](/windows/desktop/api/PhotoAcquire/nf-photoacquire-iphotoacquireplugin-initialize) method to perform actions during initialization of the acquisition experience. The **IPhotoAcquirePlugin::Initialize** method provides access to the [**IPhotoAcquireSource**](/windows/desktop/api/photoacquire/nn-photoacquire-iphotoacquiresource) that represents the device, and the [**IPhotoAcquireProgressCB**](/windows/desktop/api/photoacquire/nn-photoacquire-iphotoacquireprogresscb) that provides callback functions during acquisition.

Implement the [**IPhotoAcquirePlugin::ProcessItem**](/windows/desktop/api/PhotoAcquire/nf-photoacquire-iphotoacquireplugin-processitem) method to provide additional functionality each time an item is acquired. **IPhotoAcquirePlugin::ProcessItem** is called both before and after an item is saved, and provides access to the underlying file stream and an [**IPhotoAcquireItem**](/windows/desktop/api/photoacquire/nn-photoacquire-iphotoacquireitem) object representing the item being transferred.

Implement [**IPhotoAcquirePlugin::DisplayConfigureDialog**](/windows/desktop/api/PhotoAcquire/nf-photoacquire-iphotoacquireplugin-displayconfiguredialog) to perform actions when the configuration dialog is displayed.

[**IPhotoAcquirePlugin::TransferComplete**](/windows/desktop/api/PhotoAcquire/nf-photoacquire-iphotoacquireplugin-transfercomplete) may be implemented for additional functionality when a transfer session completes.

## Related topics

<dl> <dt>

[**Programming Guide**](programming-guide.md)
</dt> </dl>

 

 



