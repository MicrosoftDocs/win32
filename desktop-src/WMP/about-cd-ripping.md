---
title: About CD Ripping
description: About CD Ripping
ms.assetid: '1a179284-2909-4fc0-82be-996794ee4f31'
keywords: ["Windows Media Player,CD ripping", "Windows Media Player object model,CD ripping", "object model,CD ripping", "Windows Media Player ActiveX control,CD ripping", "ActiveX control,CD ripping", "Windows Media Player Mobile ActiveX control,CD ripping", "Windows Media Player Mobile,CD ripping", "CD ripping,about", "ripping CDs,about"]
---

# About CD Ripping

The Windows Media Player 11 SDK introduces new functionality for copying audio tracks from CDs to the user's computer. This process is called *ripping*.

When you rip audio tracks by using the Windows Media Player SDK interfaces, the resulting music tracks are created by using the settings that the user defined in the Windows Media Player **Options** dialog box.

To enumerate the CD drives on the user's computer, use the **IWMPCdromCollection** interface. You retrieve a pointer to this interface by calling [IWMPCore::get\_cdromCollection](iwmpcore-get-cdromcollection.md). By using the **count** and **item** methods, you can iterate the collection to retrieve an **IWMPCdrom** interface pointer for each CD drive on the user's computer. The **IWMPCdrom** interface represents an individual CD drive. Before you begin ripping a CD, you must first call **QueryInterface** through an **IWMPCdrom** pointer to retrieve a pointer to the **IWMPCdromRip** interface.

To start the ripping operation, simply call [IWMPCdromRip::startRip](iwmpcdromrip-startrip.md). You can monitor the progress of the ripping operation by periodically calling [IWMPCdromRip::get\_ripProgress](iwmpcdromrip-get-ripprogress.md). This method retrieves a progress value for the entire ripping operation. The value retrieved is a number that represents the percentage of ripping completed. You can monitor the state of the ripping operation by periodically calling [IWMPCdromRip::get\_ripState](iwmpcdromrip-get-ripstate.md). This method retrieves a [WMPRipState](wmpripstate.md) enumeration value that indicates whether the operation is in progress or stopped. You can also monitor the state of the ripping operation by handling the [IWMPEvents3::CdromRipStateChange](iwmpevents3-iwmpevents3--cdromripstatechange.md) event. You should be careful to compare the **IWMPCdromRip** pointer (provided by the event) to the pointer that represents your ripping operation to ensure that the event was raised by your operation. You can stop the ripping operation by calling [IWMPCdromRip::stopRip](iwmpcdromrip-stoprip.md).

To receive error notifications about a ripping operation, you can handle the [IWMPEvents3::CdromRipMediaError](iwmpevents3-iwmpevents3--cdromripmediaerror.md) event. Like **CdromRipStateChange**, this event provides an **IWMPCdromRip** interface pointer that represents the ripping operation that raised the event. The event also provides an **IDispatch** pointer that represents the media item that raised the event. You can call **QueryInterface** through this pointer to retrieve an **IWMPMedia** pointer.

## Related topics

<dl> <dt>

[**About the Player Object Model**](about-the-player-object-model.md)
</dt> </dl>

 

 




