---
title: What's New in Windows Media Player 12
description: This topic lists features that are new in Windows Media Player 12.
ms.assetid: '17f76963-c96d-46c9-82c0-3ed2d8a4e892'
keywords: ["Windows Media Player,what's new", "Windows Media Player,new features", "software development kit (SDK),Windows Media Player 12", "SDK (software development kit),Windows Media Player 12", "documentation,Windows Media Player 12 SDK", "what's new,Windows Media Player 12", "new features,Windows Media Player 12", "interfaces,new features in Windows Media Player 12", "attributes,new features in Windows Media Player 12", "metadata,new features in Windows Media Player 12", "enumerations,new features in Windows Media Player 12", "flags,new features in Windows Media Player 12", "interfaces,deprecated in Windows Media Player 12", "methods,deprecated in Windows Media Player 11 and not 12", "versions of Windows Media Player,new features in version 12"]
---

# What's New in Windows Media Player 12

This topic lists features that are new in Windows Media Player 12.

## New Interfaces

-   [**IWMPAudioRenderConfig**](iwmpaudiorenderconfig.md)
-   [**IWMPEvents4**](iwmpevents4.md)
-   [**IWMPLibrary2**](iwmplibrary2.md)
-   [**IWMPSyncDevice3**](iwmpsyncdevice3.md)

## New Attributes

The following new attributes for media items are available through the [**IWMPMedia**](iwmpmedia.md) and [**IWMPMedia3**](iwmpmedia3.md) interfaces.

-   [**AlbumCoverURL**](wm-albumcoverurl-attribute.md)
-   [**AlternateSourceURL**](alternatesourceurl-attribute.md)
-   [**DLNASourceURI**](dlnasourceuri-attribute.md)
-   [**DLNAServerUDN**](dlnaserverudn-attribute.md)
-   [**DTCPIPHost**](dtcpiphost-attribute.md)
-   [**DTCPIPPort**](dtcpipport-attribute.md)
-   [**LibraryID**](libraryid-attribute.md)
-   [**LibraryName**](libraryname-attribute.md)

## New Device Metadata

The following new device metadata items can be retrieved by calling [**IWMPSyncDevice::getItemInfo**](iwmpsyncdevice-getiteminfo.md).

-   **BackgroundSyncState**
-   **SkippedFiles**
-   **SyncFilter**

The following new device metadata items can be set by calling [**IWMPSyncDevice2::setItemInfo**](iwmpsyncdevice2-setiteminfo.md).

-   **AutoSyncDefaultRules**
-   **BackgroundSyncState**
-   **IncludeSkippedFiles**
-   **SyncFilter**
-   **SyncOnConnect**

## New Enumeration Member

The [**WMPSyncState**](https://msdn.microsoft.com/library/windows/desktop/dd564891) enumeration has the following new member.

-   **wmpssEstimating**

## New Flag

The [**IWMPGraphCreation::GetGraphCreationFlags**](iwmpgraphcreation-getgraphcreationflags.md) method supports the following new flag.

-   **WMPGC\_FLAGS\_USE\_CUSTOM\_GRAPH**

## Deprecated Interface

The following interface is deprecated.

-   [**IWMPFolderMonitorServices**](iwmpfoldermonitorservices.md)

## Methods That Are No Longer Deprecated

The following methods were deprecated in Windows Media Player 11 SDK, but are no longer deprecated.

-   [**IWMPGraphCreation::GraphCreationPreRender**](iwmpgraphcreation-graphcreationprerender.md)
-   [**IWMPGraphCreation::GraphCreationPostRender**](iwmpgraphcreation-graphcreationpostrender.md)

## Related topics

<dl> <dt>

[About the Windows Media Player SDK](about-the-windows-media-player-sdk.md)
</dt> </dl>

 

 




