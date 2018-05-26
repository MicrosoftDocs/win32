---
title: Whats New in Windows Media Player 12
description: This topic lists features that are new in Windows Media Player 12.
ms.assetid: 17f76963-c96d-46c9-82c0-3ed2d8a4e892
keywords:
- Windows Media Player,whats new
- Windows Media Player,new features
- software development kit (SDK),Windows Media Player 12
- SDK (software development kit),Windows Media Player 12
- documentation,Windows Media Player 12 SDK
- whats new,Windows Media Player 12
- new features,Windows Media Player 12
- interfaces,new features in Windows Media Player 12
- attributes,new features in Windows Media Player 12
- metadata,new features in Windows Media Player 12
- enumerations,new features in Windows Media Player 12
- flags,new features in Windows Media Player 12
- interfaces,deprecated in Windows Media Player 12
- methods,deprecated in Windows Media Player 11 and not 12
- versions of Windows Media Player,new features in version 12
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# What's New in Windows Media Player 12

This topic lists features that are new in Windows Media Player 12.

## New Interfaces

-   [**IWMPAudioRenderConfig**](/windows/win32/wmprealestate/nn-wmprealestate-iwmpaudiorenderconfig?branch=master)
-   [**IWMPEvents4**](/windows/win32/wmp/nn-wmp-iwmpevents4?branch=master)
-   [**IWMPLibrary2**](/windows/win32/wmp/nn-wmp-iwmplibrary2?branch=master)
-   [**IWMPSyncDevice3**](/windows/win32/wmp/nn-wmp-iwmpsyncdevice3?branch=master)

## New Attributes

The following new attributes for media items are available through the [**IWMPMedia**](/windows/win32/wmp/nn-wmp-iwmpmedia?branch=master) and [**IWMPMedia3**](/windows/win32/wmp/nn-wmp-iwmpmedia3?branch=master) interfaces.

-   [**AlbumCoverURL**](wm-albumcoverurl-attribute.md)
-   [**AlternateSourceURL**](alternatesourceurl-attribute.md)
-   [**DLNASourceURI**](dlnasourceuri-attribute.md)
-   [**DLNAServerUDN**](dlnaserverudn-attribute.md)
-   [**DTCPIPHost**](dtcpiphost-attribute.md)
-   [**DTCPIPPort**](dtcpipport-attribute.md)
-   [**LibraryID**](libraryid-attribute.md)
-   [**LibraryName**](libraryname-attribute.md)

## New Device Metadata

The following new device metadata items can be retrieved by calling [**IWMPSyncDevice::getItemInfo**](/windows/win32/wmp/nf-wmp-iwmpsyncdevice-getiteminfo?branch=master).

-   **BackgroundSyncState**
-   **SkippedFiles**
-   **SyncFilter**

The following new device metadata items can be set by calling [**IWMPSyncDevice2::setItemInfo**](/windows/win32/wmp/nf-wmp-iwmpsyncdevice2-setiteminfo?branch=master).

-   **AutoSyncDefaultRules**
-   **BackgroundSyncState**
-   **IncludeSkippedFiles**
-   **SyncFilter**
-   **SyncOnConnect**

## New Enumeration Member

The [**WMPSyncState**](https://msdn.microsoft.com/library/windows/desktop/dd564891) enumeration has the following new member.

-   **wmpssEstimating**

## New Flag

The [**IWMPGraphCreation::GetGraphCreationFlags**](/windows/win32/wmpservices/nf-wmpservices-iwmpgraphcreation-getgraphcreationflags?branch=master) method supports the following new flag.

-   **WMPGC\_FLAGS\_USE\_CUSTOM\_GRAPH**

## Deprecated Interface

The following interface is deprecated.

-   [**IWMPFolderMonitorServices**](/windows/win32/wmp/nn-wmp-iwmpfoldermonitorservices?branch=master)

## Methods That Are No Longer Deprecated

The following methods were deprecated in Windows Media Player 11 SDK, but are no longer deprecated.

-   [**IWMPGraphCreation::GraphCreationPreRender**](/windows/win32/wmpservices/nf-wmpservices-iwmpgraphcreation-graphcreationprerender?branch=master)
-   [**IWMPGraphCreation::GraphCreationPostRender**](/windows/win32/wmpservices/nf-wmpservices-iwmpgraphcreation-graphcreationpostrender?branch=master)

## Related topics

<dl> <dt>

[About the Windows Media Player SDK](about-the-windows-media-player-sdk.md)
</dt> </dl>

 

 




