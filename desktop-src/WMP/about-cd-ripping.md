---
title: About CD Ripping
description: About CD Ripping
ms.assetid: 1a179284-2909-4fc0-82be-996794ee4f31
keywords:
- Windows Media Player,CD ripping
- Windows Media Player object model,CD ripping
- object model,CD ripping
- Windows Media Player ActiveX control,CD ripping
- ActiveX control,CD ripping
- Windows Media Player Mobile ActiveX control,CD ripping
- Windows Media Player Mobile,CD ripping
- CD ripping,about
- ripping CDs,about
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# About CD Ripping

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The Windows Media Player 11 SDK introduces new functionality for copying audio tracks from CDs to the user's computer. This process is called *ripping*.

When you rip audio tracks by using the Windows Media Player SDK interfaces, the resulting music tracks are created by using the settings that the user defined in the Windows Media Player **Options** dialog box.

To enumerate the CD drives on the user's computer, use the **IWMPCdromCollection** interface. You retrieve a pointer to this interface by calling [IWMPCore::get\_cdromCollection](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpcore-get_cdromcollection). By using the **count** and **item** methods, you can iterate the collection to retrieve an **IWMPCdrom** interface pointer for each CD drive on the user's computer. The **IWMPCdrom** interface represents an individual CD drive. Before you begin ripping a CD, you must first call **QueryInterface** through an **IWMPCdrom** pointer to retrieve a pointer to the **IWMPCdromRip** interface.

To start the ripping operation, simply call [IWMPCdromRip::startRip](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpcdromrip-startrip). You can monitor the progress of the ripping operation by periodically calling [IWMPCdromRip::get\_ripProgress](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpcdromrip-get_ripprogress). This method retrieves a progress value for the entire ripping operation. The value retrieved is a number that represents the percentage of ripping completed. You can monitor the state of the ripping operation by periodically calling [IWMPCdromRip::get\_ripState](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpcdromrip-get_ripstate). This method retrieves a [WMPRipState](/previous-versions/windows/desktop/api/wmp/ne-wmp-wmpripstate) enumeration value that indicates whether the operation is in progress or stopped. You can also monitor the state of the ripping operation by handling the [IWMPEvents3::CdromRipStateChange](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpevents3-cdromripstatechange) event. You should be careful to compare the **IWMPCdromRip** pointer (provided by the event) to the pointer that represents your ripping operation to ensure that the event was raised by your operation. You can stop the ripping operation by calling [IWMPCdromRip::stopRip](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpcdromrip-stoprip).

To receive error notifications about a ripping operation, you can handle the [IWMPEvents3::CdromRipMediaError](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpevents3-cdromripmediaerror) event. Like **CdromRipStateChange**, this event provides an **IWMPCdromRip** interface pointer that represents the ripping operation that raised the event. The event also provides an **IDispatch** pointer that represents the media item that raised the event. You can call **QueryInterface** through this pointer to retrieve an **IWMPMedia** pointer.

## Related topics

<dl> <dt>

[**About the Player Object Model**](about-the-player-object-model.md)
</dt> </dl>

 

 




