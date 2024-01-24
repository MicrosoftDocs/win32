---
title: What's New in Windows Media Player 12
description: This topic lists features that are new in Windows Media Player 12.
ms.assetid: 17f76963-c96d-46c9-82c0-3ed2d8a4e892
keywords:
- Windows Media Player,what's new
- Windows Media Player,new features
- software development kit (SDK),Windows Media Player 12
- SDK (software development kit),Windows Media Player 12
- documentation,Windows Media Player 12 SDK
- what's new,Windows Media Player 12
- new features,Windows Media Player 12
- interfaces,new features in Windows Media Player 12
- attributes,new features in Windows Media Player 12
- metadata,new features in Windows Media Player 12
- enumerations,new features in Windows Media Player 12
- flags,new features in Windows Media Player 12
- interfaces,deprecated in Windows Media Player 12
- methods,deprecated in Windows Media Player 11 and not 12
- versions of Windows Media Player,new features in version 12
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# What's New in Windows Media Player 12

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This topic lists features that are new in Windows Media Player 12.

## New Interfaces

-   [**IWMPAudioRenderConfig**](/previous-versions/windows/desktop/api/wmprealestate/nn-wmprealestate-iwmpaudiorenderconfig)
-   [**IWMPEvents4**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpevents4)
-   [**IWMPLibrary2**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmplibrary2)
-   [**IWMPSyncDevice3**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpsyncdevice3)

## New Attributes

The following new attributes for media items are available through the [**IWMPMedia**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpmedia) and [**IWMPMedia3**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpmedia3) interfaces.

-   [**AlbumCoverURL**](wm-albumcoverurl-attribute.md)
-   [**AlternateSourceURL**](alternatesourceurl-attribute.md)
-   [**DLNASourceURI**](dlnasourceuri-attribute.md)
-   [**DLNAServerUDN**](dlnaserverudn-attribute.md)
-   [**DTCPIPHost**](dtcpiphost-attribute.md)
-   [**DTCPIPPort**](dtcpipport-attribute.md)
-   [**LibraryID**](libraryid-attribute.md)
-   [**LibraryName**](libraryname-attribute.md)

## New Device Metadata

The following new device metadata items can be retrieved by calling [**IWMPSyncDevice::getItemInfo**](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpsyncdevice-getiteminfo).

-   **BackgroundSyncState**
-   **SkippedFiles**
-   **SyncFilter**

The following new device metadata items can be set by calling [**IWMPSyncDevice2::setItemInfo**](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpsyncdevice2-setiteminfo).

-   **AutoSyncDefaultRules**
-   **BackgroundSyncState**
-   **IncludeSkippedFiles**
-   **SyncFilter**
-   **SyncOnConnect**

## New Enumeration Member

The [**WMPSyncState**](/previous-versions/windows/desktop/api/wmp/ne-wmp-wmpsyncstate) enumeration has the following new member.

-   **wmpssEstimating**

## New Flag

The [**IWMPGraphCreation::GetGraphCreationFlags**](/previous-versions/windows/desktop/api/wmpservices/nf-wmpservices-iwmpgraphcreation-getgraphcreationflags) method supports the following new flag.

-   **WMPGC\_FLAGS\_USE\_CUSTOM\_GRAPH**

## Deprecated Interface

The following interface is deprecated.

-   [**IWMPFolderMonitorServices**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpfoldermonitorservices)

## Methods That Are No Longer Deprecated

The following methods were deprecated in Windows Media Player 11 SDK, but are no longer deprecated.

-   [**IWMPGraphCreation::GraphCreationPreRender**](/previous-versions/windows/desktop/api/wmpservices/nf-wmpservices-iwmpgraphcreation-graphcreationprerender)
-   [**IWMPGraphCreation::GraphCreationPostRender**](/previous-versions/windows/desktop/api/wmpservices/nf-wmpservices-iwmpgraphcreation-graphcreationpostrender)

## Related topics

<dl> <dt>

[About the Windows Media Player SDK](about-the-windows-media-player-sdk.md)
</dt> </dl>

 

 




