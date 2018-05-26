---
title: About the Object Model Versions
description: About the Object Model Versions
ms.assetid: 20bb1681-9079-4f8c-bb5e-5c98e3bdc76a
keywords:
- Windows Media Player,versions
- Windows Media Player object model,versions
- object model,versions
- Windows Media Player ActiveX control,versions for object model
- ActiveX control,versions for object model
- Windows Media Player Mobile ActiveX control,versions for object model
- Windows Media Player Mobile,versions for object model
- versions of Windows Media Player,object model
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# About the Object Model Versions

Windows Media Player 7.0 introduced a new object model. This object model has been extended with Windows Media Player 7.1, Windows Media Player for Windows XP, Windows Media Player 9 Series, Windows Media Player 10, Windows Media Player 11, and Windows Media Player 12. Each topic in the Object Model Reference includes a Requirements section that details the minimum requirement for the individual property, method, or event. The following lists detail the new objects, methods, properties, and events that have been added for each version since version 7.0. These lists also include new C++ interfaces, methods, and events.

Where a new or updated interface is also exposed as an object, only the object is listed. To locate the interface, refer to the [Object Model Reference for C++](object-model-reference-for-c.md). Usually, you will simply need to add the IWMP prefix to the object name. If a new interface extends an existing one, you may need to look for the latest version number. For example, Windows Media Player 9 Series introduced new properties and methods available from the [**Settings**](settings-object.md) object. In C++, these are available through the [**IWMPSettings2**](/windows/win32/wmp/nn-wmp-iwmpsettings2?branch=master) interface, which extends [**IWMPSettings**](/windows/win32/wmp/nn-wmp-iwmpsettings?branch=master).

## Added for Windows Media Player 7.1

-   [**Player.stretchToFit Property**](player-stretchtofit.md)

## Added for Windows Media Player for Windows XP

-   [**Controls.step Method**](controls-step.md)
-   [**DVD Object**](dvd-object.md)
-   [**Media.error Property**](media-error.md)
-   [**Player.DomainChange Event**](player-player-domainchange.md)
-   [**Player.MediaError Event**](player-player-mediaerror.md)
-   [**Player.OpenPlaylistSwitch Event**](player-player-openplaylistswitch.md)
-   [**Player.windowlessVideo Property**](player-windowlessvideo.md)

## Added for Windows Media Player 9 Series

-   [**ClosedCaption.getSAMILangID Method**](closedcaption-getsamilangid.md)
-   [**ClosedCaption.getSAMILangName Method**](closedcaption-getsamilangname.md)
-   [**ClosedCaption.getSAMIStyleName Method**](closedcaption-getsamistylename.md)
-   [**ClosedCaption.SAMILangCount Property**](closedcaption-samilangcount.md)
-   [**ClosedCaption.SAMIStyleCount Property**](closedcaption-samistylecount.md)
-   [**Controls.audioLanguageCount Property**](controls-audiolanguagecount.md)
-   [**Controls.currentAudioLanguage Property**](controls-currentaudiolanguage.md)
-   [**Controls.currentAudioLanguageIndex Property**](controls-currentaudiolanguageindex.md)
-   [**Controls.currentPositionTimecode Property**](controls-currentpositiontimecode.md)
-   [**Controls.getAudioLanguageDescription Method**](controls-getaudiolanguagedescription.md)
-   [**Controls.getAudioLanguageID Method**](controls-getaudiolanguageid.md)
-   [**Controls.getLanguageName Method**](controls-getlanguagename.md)
-   [**ErrorItem.condition Property**](erroritem-condition.md)
-   [**External.appColorLight Property**](external-appcolorlight.md)
-   [**External.OnColorChange Event**](external-oncolorchange-event.md)
-   [**External.version Property**](external-version.md)
-   [**IWMPEvents::PlayerDockedStateChange Event**](/windows/win32/wmp/nf-wmp-iwmpevents-playerdockedstatechange?branch=master)
-   [**IWMPEvents::PlayerReconnect Event**](/windows/win32/wmp/nf-wmp-iwmpevents-playerreconnect?branch=master)
-   [**IWMPEvents::SwitchedToControl Event**](/windows/win32/wmp/nf-wmp-iwmpevents-switchedtocontrol?branch=master)
-   [**IWMPEvents::SwitchedToPlayerApplication Event**](/windows/win32/wmp/nf-wmp-iwmpevents-switchedtoplayerapplication?branch=master)
-   [**IWMPPlayerServices Interface**](/windows/win32/wmp/nn-wmp-iwmpplayerservices?branch=master)
-   [**IWMPRemoteMediaServices Interface**](/windows/win32/wmp/nn-wmp-iwmpremotemediaservices?branch=master)
-   [**IWMPSkinManager Interface**](/windows/win32/wmp/nn-wmp-iwmpskinmanager?branch=master)
-   [**Media.getAttributeCountByType Method**](media-getattributecountbytype.md)
-   [**Media.getItemInfoByType Method**](media-getiteminfobytype.md)
-   [**MetadataPicture Object**](metadatapicture-object.md)
-   [**MetadataText Object**](metadatatext-object.md)
-   [**Player.AudioLanguageChange Event**](player-player-audiolanguagechange.md)
-   [**Player.isRemote Property**](player-isremote.md)
-   [**Player.MediaCollectionAttributeStringChanged Event**](player-player-mediacollectionattributestringchanged.md)
-   [**Player.newMedia Method**](player-newmedia.md)
-   [**Player.newPlaylist Method**](player-newplaylist.md)
-   [**Player.openPlayer Method**](player-openplayer.md)
-   [**Player.playerApplication Property**](player-playerapplication.md)
-   [**Player.StatusChange Event**](player-player-statuschange.md)
-   [**PlayerApplication Object**](playerapplication-object.md)
-   [**Settings.defaultAudioLanguage Property**](settings-defaultaudiolanguage.md)
-   [**Settings.mediaAccessRights Property**](settings-mediaaccessrights.md)
-   [**Settings.requestMediaAccessRights Method**](settings-requestmediaaccessrights.md)

## Added for Windows Media Player 10

-   [**IWMPGraphCreation Interface**](/windows/win32/wmpservices/nn-wmpservices-iwmpgraphcreation?branch=master)
-   [**IWMPPlayerServices2 Interface**](/windows/win32/wmp/nn-wmp-iwmpplayerservices2?branch=master)
-   [**IWMPSyncDevice Interface**](/windows/win32/wmp/nn-wmp-iwmpsyncdevice?branch=master)
-   [**IWMPSyncServices Interface**](/windows/win32/wmp/nn-wmp-iwmpsyncservices?branch=master)
-   [**WMPDeviceStatus Enumeration**](/windows/win32/wmp/ne-wmp-wmpdevicestatus?branch=master)
-   [**WMPSyncState Enumeration**](/windows/win32/wmp/ne-wmp-wmpsyncstate?branch=master)

## Added for Windows Media Player 11

-   [**IWMPCdromBurn Interface**](/windows/win32/wmp/nn-wmp-iwmpcdromburn?branch=master)
-   [**IWMPCdromBurn Interface (VB and C#)**](iwmpcdromburn--vb-and-c.md)
-   [**IWMPCdromRip Interface**](/windows/win32/wmp/nn-wmp-iwmpcdromrip?branch=master)
-   [**IWMPCdromRip Interface (VB and C#)**](iwmpcdromrip--vb-and-c.md)
-   [**IWMPEvents3 Interface**](/windows/win32/wmp/nn-wmp-iwmpevents3?branch=master)
-   [**IWMPFolderMonitorServices Interface**](/windows/win32/wmp/nn-wmp-iwmpfoldermonitorservices?branch=master)
-   [**IWMPLibrary Interface**](/windows/win32/wmp/nn-wmp-iwmplibrary?branch=master)
-   [**IWMPLibrary Interface (VB and C#)**](iwmplibrary--vb-and-c.md)
-   [**IWMPLibraryServices Interface**](/windows/win32/wmp/nn-wmp-iwmplibraryservices?branch=master)
-   [**IWMPLibraryServices Interface (VB and C#)**](iwmplibraryservices--vb-and-c.md)
-   [**IWMPLibrarySharingServices Interface**](/windows/win32/wmp/nn-wmp-iwmplibrarysharingservices?branch=master)
-   [**IWMPMediaCollection2 Interface**](/windows/win32/wmp/nn-wmp-iwmpmediacollection2?branch=master)
-   [**IWMPMediaCollection2 Interface (VB and C#)**](iwmpmediacollection2--vb-and-c.md)
-   [**IWMPQuery Interface**](/windows/win32/wmp/nn-wmp-iwmpquery?branch=master)
-   [**IWMPQuery Interface (VB and C#)**](iwmpquery--vb-and-c.md)
-   [**IWMPRenderConfig Interface**](/windows/win32/wmprealestate/nn-wmprealestate-iwmprenderconfig?branch=master)
-   [**IWMPStringCollection2 Interface**](/windows/win32/wmp/nn-wmp-iwmpstringcollection2?branch=master)
-   [**IWMPStringCollection2 Interface (VB and C#)**](iwmpstringcollection2--vb-and-c.md)
-   [**IWMPSyncDevice2 Interface**](/windows/win32/wmp/nn-wmp-iwmpsyncdevice2?branch=master)
-   [**IWMPVideoRenderConfig Interface**](/windows/win32/wmprealestate/nn-wmprealestate-iwmpvideorenderconfig?branch=master)
-   [**Query Object**](query-object.md)
-   [**WMPBurnFormat Enumeration**](/windows/win32/wmp/ne-wmp-wmpburnformat?branch=master)
-   [**WMPBurnState Enumeration**](/windows/win32/wmp/ne-wmp-wmpburnstate?branch=master)
-   [**WMPLibraryType Enumeration**](/windows/win32/wmp/ne-wmp-wmplibrarytype?branch=master)
-   [**WMPRipState Enumeration**](/windows/win32/wmp/ne-wmp-wmpripstate?branch=master)

## Added for Windows Media Player 12

-   [**IWMPAudioRenderConfig Interface**](/windows/win32/wmprealestate/nn-wmprealestate-iwmpaudiorenderconfig?branch=master)
-   [**IWMPEvents4 Interface**](/windows/win32/wmp/nn-wmp-iwmpevents4?branch=master)
-   [**IWMPLibrary2 Interface**](/windows/win32/wmp/nn-wmp-iwmplibrary2?branch=master)
-   [**IWMPSyncDevice3 Interface**](/windows/win32/wmp/nn-wmp-iwmpsyncdevice3?branch=master)

## Related topics

<dl> <dt>

[**About the Player Object Model**](about-the-player-object-model.md)
</dt> <dt>

[**Object Model Reference for Scripting**](object-model-reference-for-scripting.md)
</dt> </dl>

 

 




