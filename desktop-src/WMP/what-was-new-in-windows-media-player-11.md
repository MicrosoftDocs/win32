---
title: What Was New in Windows Media Player 11
description: This topic lists features that were new in Windows Media Player 11 and the Windows Media Player 11 SDK.
ms.assetid: d2a6b6ce-a924-4b55-9dc7-68cc57e5651f
keywords:
- Windows Media Player,what's new
- Windows Media Player,new features
- software development kit (SDK),Windows Media Player 11
- SDK (software development kit),Windows Media Player 11
- documentation,Windows Media Player 11 SDK
- what's new,Windows Media Player 11
- new features,Windows Media Player 11
- interfaces,new features in Windows Media Player 11
- attributes,new features in Windows Media Player 11
- Windows Media Player ActiveX control,new features in version 11
- ActiveX control,new features in version 11
- skins,new features in Windows Media Player 11
- Windows Media Player skins,new features in version 11
- plug-ins,new features in Windows Media Player 11
- Windows Media Player plug-ins,new features in version 11
- online stores,new features in Windows Media Player 11
- Windows Media Player online stores,new features in version 11
- samples,new features in Windows Media Player 11
- versions of Windows Media Player,new features in version 11
ms.topic: article
ms.date: 05/31/2018
---

# What Was New in Windows Media Player 11

This topic lists features that were new in Windows Media Player 11 and the Windows Media Player 11 SDK.

## Windows Media Player Control

The following interfaces were new in the Windows Media Player 11 ActiveX control.

-   [**IWMPLibrary Interface**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmplibrary)
-   [**IWMPLibraryServices Interface**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmplibraryservices)
-   [**IWMPLibrarySharingServices Interface**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmplibrarysharingservices)
-   [**IWMPMediaCollection2 Interface**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpmediacollection2)
-   [**IWMPQuery Interface**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpquery)
-   [**IWMPStringCollection2 Interface**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpstringcollection2)
-   [**MediaCollection Object**](mediacollection-object.md)
-   [**Query Object**](query-object.md)
-   [**StringCollection Object**](stringcollection-object.md)
-   [**IWMPCdromRip Interface**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpcdromrip)
-   [**IWMPCdromBurn Interface**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpcdromburn)
-   [**IWMPFolderMonitorServices Interface**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpfoldermonitorservices)
-   [**IWMPSyncDevice2 Interface**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpsyncdevice2)
-   [**IWMPVideoRenderConfig Interface**](/previous-versions/windows/desktop/api/wmprealestate/nn-wmprealestate-iwmpvideorenderconfig)
-   [**IWMPUserEventSink**](/previous-versions/windows/desktop/api/wmpservices/nn-wmpservices-iwmpusereventsink)
-   [**IWMPEvents3 Interface**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpevents3)

## Windows Media Player Skins

The following skin features were new in Windows Media Player 11.

-   New attributes for positioning controls. See [**AmbientAttributes.right**](ambientattributes-right.md) and [**AmbientAttributes.bottom**](ambientattributes-bottom.md).
-   New attributes for moving and sizing controls. See [**AmbientAttributes.moveSizeTo**](ambientattributes-movesizeto.md) and [**AmbientAttributes.slideTo**](ambientattributes-slideto.md).
-   A new attribute for specifying image resizing behavior. See [**AmbientAttributes.resizeImages**](ambientattributes-resizeimages.md).
-   A new attribute for specifying non-uniform scaling of a skin element. See [**AmbientAttributes.nineGridMargins**](ambientattributes-ninegridmargins.md).

## Windows Media Player Plug-ins

The Windows Media Player 11 SDK introduced a new type of plug-in for converting digital media file formats. See [Windows Media Player Conversion Plug-ins](windows-media-player-conversion-plug-ins.md).

DSP Plug-ins created before the release of the Windows Media Player 11 SDK must be updated to work with Windows Media Player 11. See [Updating Existing DSP Plug-ins](updating-existing-dsp-plug-ins.md).

The Windows Media Player plug-in wizard was updated to create DSP plug-ins that work in Windows Media Player 11. For details, see [Updates to the DSP Plug-in Wizard for Windows Media Player 11](updates-to-the-dsp-plug-in-wizard-for-windows-media-player-11.md).

## Windows Media Player Online Stores

Windows Media Player 11 introduced a new model for integrating online store catalogs into the Windows Media Player library feature. See [Type 1 Online Stores](type-1-online-stores.md).

## Windows Media Player

The following features were new in Windows Media Player 11.

-   [Device Extensions for Reporting Acquired Content](device-extensions-for-reporting-acquired-content.md)
-   [Device Extensions for Playlist Object Preferences](device-extensions-for-playlist-object-preferences.md)

## Windows Media Player SDK Samples

The C# sample named SchemaReader was new in the Windows Media Player 11 SDK. The sample creates a tool that uses the Windows Media Player object model to retrieve and display information about metadata in the Windows Media Player library or in a digital media file. The tool can save the results to a text file. The tool enumerates the metadata attribute names stored in the library for each supported schema (audio, video, playlist, photo, and other). The tool can also provide information about available attributes for playlists in the playlist collection, CD tracks, CD table of contents, DVD titles, DVD chapters, DVD table of contents, and individual media files.

The C++ sample named WMPML was updated in the Windows Media Player 11 SDK to demonstrate the following features:

-   Using the new [**IWMPStringCollection2**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpstringcollection2) interface to create a user interface similar to the Windows Media Player library feature.
-   Using the [**IWMPQuery**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpquery) and [**IWMPMediaCollection2**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpmediacollection2) interfaces to create compound queries and display the results.

 

 




