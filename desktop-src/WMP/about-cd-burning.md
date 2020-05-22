---
title: About CD Burning
description: About CD Burning
ms.assetid: 1ecc73ed-c49d-4190-baa9-93162f075a4c
keywords:
- Windows Media Player,CD burning
- Windows Media Player object model,CD burning
- object model,CD burning
- Windows Media Player ActiveX control,CD burning
- ActiveX control,CD burning
- Windows Media Player Mobile ActiveX control,CD burning
- Windows Media Player Mobile,CD burning
- CD burning,about
- burning CDs,about
ms.topic: article
ms.date: 05/31/2018
---

# About CD Burning

The Windows Media Player 11 SDK introduces new functionality for creating CDs. This process is called *burning*.

To enumerate the CD drives on the user's computer, use the **IWMPCdromCollection** interface. You retrieve a pointer to this interface by calling [IWMPCore::get\_cdromCollection](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpcore-get_cdromcollection). By using the **count** and **item** methods, you can iterate the collection to retrieve an **IWMPCdrom** interface pointer for each CD drive on the user's computer. The **IWMPCdrom** interface represents an individual CD drive.

Before you begin burning a CD, you must first call **QueryInterface** through an **IWMPCdrom** pointer to retrieve a pointer to the **IWMPCdromBurn** interface. By using the **isAvailable** method, you can determine whether a particular CD drive can burn CDs, whether there is a CD in the drive, and how the CD can be used.

To specify the items to burn to CD, you must create a playlist. Windows Media Player represents playlists by using the **IWMPPlaylist** interface. You can create this playlist any way you like. For example, you might simply retrieve a playlist from the library by calling [IWMPMediaCollection::getByAlbum](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpmediacollection-getbyalbum). After you create the playlist that you want to burn to CD, you must call the [IWMPCdromBurn::put\_burnPlaylist](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpcdromburn-put_burnplaylist) method and pass the playlist pointer as an argument. This sets your playlist as the one that Windows Media Player will copy to the CD.

If you retrieve a playlist from the library, any changes you make to the playlist will be reflected in the user's library. To avoid this, call [IWMPPlaylist::setItemInfo](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpplaylist-setiteminfo), passing the attribute name "Temporary" and the value "true". This converts your playlist instance to a temporary playlist, which can be edited without changing the original playlist.

Each time you set a new playlist for burning, or make changes to an existing burn playlist, you must call [IWMPCdromBurn::refreshStatus](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpcdromburn-refreshstatus) to update the status information. This ensures that Windows Media Player does the processing necessary to provide you with accurate status information for the CD burning operation.

To specify the type of CD to burn, call [IWMPCdromBurn::put\_burnFormat](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpcdromburn-put_burnformat). Windows Media Player enables you to burn two types of CDs: audio CDs and data CDs. The [WMPBurnFormat](/previous-versions/windows/desktop/api/wmp/ne-wmp-wmpburnformat) enumeration defines the CD types.

You can specify a volume label for the CD by calling [IWMPCdromBurn::put\_label](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpcdromburn-put_label).

When you are ready to begin burning the CD, call [IWMPCdromBurn::startBurn](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpcdromburn-startburn). You can monitor the progress of the burning operation by periodically calling [IWMPCdromBurn::get\_burnProgress](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpcdromburn-get_burnprogress). This method retrieves a progress value for the entire burning operation. The value retrieved is a number that represents the percentage of burning completed. You can monitor the state of the burning operation by handling the [IWMPEvents3::CdromBurnStateChange](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpevents3-cdromburnstatechange) event, which uses the [WMPBurnState](/previous-versions/windows/desktop/api/wmp/ne-wmp-wmpburnstate) enumeration to indicate the current state. You should be careful to compare the **IWMPCdromBurn** pointer (provided by the event) to the pointer that represents your burning operation to ensure that the event was raised by your operation. You can stop the burning operation by calling [IWMPCdromBurn::stopBurn](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpcdromburn-stopburn).

There are two events that you can handle to receive error notifications about your burning operation. The [IWMPEvents3::CdromBurnError](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpevents3-cdromburnerror) event is raised when a generic error occurs. [IWMPEvents3::CdromBurnMediaError](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpevents3-cdromburnmediaerror) is raised when a particular media item causes an error during burning. Like the **CdromBurnStateChange** event, each of these events provides an **IWMPCdromBurn** pointer that represents the burning operation that raised the event. The **CdromBurnMediaError** event provides an **IDispatch** pointer that represents the media item that raised the event. You can call **QueryInterface** through this pointer to retrieve an **IWMPMedia** pointer.

## Related topics

<dl> <dt>

[**About the Player Object Model**](about-the-player-object-model.md)
</dt> <dt>

[**IWMPCdrom Interface**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpcdrom)
</dt> <dt>

[**IWMPCdromBurn Interface**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpcdromburn)
</dt> <dt>

[**IWMPCdromCollection Interface**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpcdromcollection)
</dt> <dt>

[**IWMPEvents3 Interface**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpevents3)
</dt> <dt>

[**IWMPMedia Interface**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpmedia)
</dt> <dt>

[**IWMPPlaylist Interface**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpplaylist)
</dt> <dt>

[**Temporary Attribute**](temporary-attribute.md)
</dt> </dl>

 

 




