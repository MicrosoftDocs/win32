---
title: About CD Burning
description: About CD Burning
ms.assetid: '1ecc73ed-c49d-4190-baa9-93162f075a4c'
keywords: ["Windows Media Player,CD burning", "Windows Media Player object model,CD burning", "object model,CD burning", "Windows Media Player ActiveX control,CD burning", "ActiveX control,CD burning", "Windows Media Player Mobile ActiveX control,CD burning", "Windows Media Player Mobile,CD burning", "CD burning,about", "burning CDs,about"]
---

# About CD Burning

The Windows Media Player 11 SDK introduces new functionality for creating CDs. This process is called *burning*.

To enumerate the CD drives on the user's computer, use the **IWMPCdromCollection** interface. You retrieve a pointer to this interface by calling [IWMPCore::get\_cdromCollection](iwmpcore-get-cdromcollection.md). By using the **count** and **item** methods, you can iterate the collection to retrieve an **IWMPCdrom** interface pointer for each CD drive on the user's computer. The **IWMPCdrom** interface represents an individual CD drive.

Before you begin burning a CD, you must first call **QueryInterface** through an **IWMPCdrom** pointer to retrieve a pointer to the **IWMPCdromBurn** interface. By using the **isAvailable** method, you can determine whether a particular CD drive can burn CDs, whether there is a CD in the drive, and how the CD can be used.

To specify the items to burn to CD, you must create a playlist. Windows Media Player represents playlists by using the **IWMPPlaylist** interface. You can create this playlist any way you like. For example, you might simply retrieve a playlist from the library by calling [IWMPMediaCollection::getByAlbum](iwmpmediacollection-getbyalbum.md). After you create the playlist that you want to burn to CD, you must call the [IWMPCdromBurn::put\_burnPlaylist](iwmpcdromburn-put-burnplaylist.md) method and pass the playlist pointer as an argument. This sets your playlist as the one that Windows Media Player will copy to the CD.

If you retrieve a playlist from the library, any changes you make to the playlist will be reflected in the user's library. To avoid this, call [IWMPPlaylist::setItemInfo](iwmpplaylist-setiteminfo.md), passing the attribute name "Temporary" and the value "true". This converts your playlist instance to a temporary playlist, which can be edited without changing the original playlist.

Each time you set a new playlist for burning, or make changes to an existing burn playlist, you must call [IWMPCdromBurn::refreshStatus](iwmpcdromburn-refreshstatus.md) to update the status information. This ensures that Windows Media Player does the processing necessary to provide you with accurate status information for the CD burning operation.

To specify the type of CD to burn, call [IWMPCdromBurn::put\_burnFormat](iwmpcdromburn-put-burnformat.md). Windows Media Player enables you to burn two types of CDs: audio CDs and data CDs. The [WMPBurnFormat](wmpburnformat.md) enumeration defines the CD types.

You can specify a volume label for the CD by calling [IWMPCdromBurn::put\_label](iwmpcdromburn-put-label.md).

When you are ready to begin burning the CD, call [IWMPCdromBurn::startBurn](iwmpcdromburn-startburn.md). You can monitor the progress of the burning operation by periodically calling [IWMPCdromBurn::get\_burnProgress](iwmpcdromburn-get-burnprogress.md). This method retrieves a progress value for the entire burning operation. The value retrieved is a number that represents the percentage of burning completed. You can monitor the state of the burning operation by handling the [IWMPEvents3::CdromBurnStateChange](iwmpevents3-iwmpevents3--cdromburnstatechange.md) event, which uses the [WMPBurnState](wmpburnstate.md) enumeration to indicate the current state. You should be careful to compare the **IWMPCdromBurn** pointer (provided by the event) to the pointer that represents your burning operation to ensure that the event was raised by your operation. You can stop the burning operation by calling [IWMPCdromBurn::stopBurn](iwmpcdromburn-stopburn.md).

There are two events that you can handle to receive error notifications about your burning operation. The [IWMPEvents3::CdromBurnError](iwmpevents3-iwmpevents3--cdromburnerror.md) event is raised when a generic error occurs. [IWMPEvents3::CdromBurnMediaError](iwmpevents3-iwmpevents3--cdromburnmediaerror.md) is raised when a particular media item causes an error during burning. Like the **CdromBurnStateChange** event, each of these events provides an **IWMPCdromBurn** pointer that represents the burning operation that raised the event. The **CdromBurnMediaError** event provides an **IDispatch** pointer that represents the media item that raised the event. You can call **QueryInterface** through this pointer to retrieve an **IWMPMedia** pointer.

## Related topics

<dl> <dt>

[**About the Player Object Model**](about-the-player-object-model.md)
</dt> <dt>

[**IWMPCdrom Interface**](iwmpcdrom.md)
</dt> <dt>

[**IWMPCdromBurn Interface**](iwmpcdromburn.md)
</dt> <dt>

[**IWMPCdromCollection Interface**](iwmpcdromcollection.md)
</dt> <dt>

[**IWMPEvents3 Interface**](iwmpevents3.md)
</dt> <dt>

[**IWMPMedia Interface**](iwmpmedia.md)
</dt> <dt>

[**IWMPPlaylist Interface**](iwmpplaylist.md)
</dt> <dt>

[**Temporary Attribute**](temporary-attribute.md)
</dt> </dl>

 

 




