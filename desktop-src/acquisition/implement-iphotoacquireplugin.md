---
Description: Implement IPhotoAcquirePlugin
ms.assetid: '3c4f82ab-d7af-4af3-b2cc-4279c8e567da'
title: Implement IPhotoAcquirePlugin
---

# Implement IPhotoAcquirePlugin

Your plug-in extends the Windows Vista acquisition experience by implementing the [**IPhotoAcquirePlugin**](iphotoacquireplugin.md) interface. These methods are implemented in addition to the methods inherited from [IUnknown](https://msdn.microsoft.com/library/windows/desktop/ms680509).

Implement the [**IPhotoAcquirePlugin::Initialize**](iphotoacquireplugin-initialize.md) method to perform actions during initialization of the acquisition experience. The **IPhotoAcquirePlugin::Initialize** method provides access to the [**IPhotoAcquireSource**](iphotoacquiresource.md) that represents the device, and the [**IPhotoAcquireProgressCB**](iphotoacquireprogresscb.md) that provides callback functions during acquisition.

Implement the [**IPhotoAcquirePlugin::ProcessItem**](iphotoacquireplugin-processitem.md) method to provide additional functionality each time an item is acquired. **IPhotoAcquirePlugin::ProcessItem** is called both before and after an item is saved, and provides access to the underlying file stream and an [**IPhotoAcquireItem**](iphotoacquireitem.md) object representing the item being transferred.

Implement [**IPhotoAcquirePlugin::DisplayConfigureDialog**](iphotoacquireplugin-displayconfiguredialog.md) to perform actions when the configuration dialog is displayed.

[**IPhotoAcquirePlugin::TransferComplete**](iphotoacquireplugin-transfercomplete.md) may be implemented for additional functionality when a transfer session completes.

## Related topics

<dl> <dt>

[**Programming Guide**](programming-guide.md)
</dt> </dl>

 

 



