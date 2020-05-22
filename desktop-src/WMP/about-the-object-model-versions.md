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
ms.topic: article
ms.date: 05/31/2018
---

# About the Object Model Versions

Windows Media Player 7.0 introduced a new object model. This object model has been extended with Windows Media Player 7.1, Windows Media Player for Windows XP, Windows Media Player 9 Series, Windows Media Player 10, Windows Media Player 11, and Windows Media Player 12. Each topic in the Object Model Reference includes a Requirements section that details the minimum requirement for the individual property, method, or event. The following lists detail the new objects, methods, properties, and events that have been added for each version since version 7.0. These lists also include new C++ interfaces, methods, and events.

Where a new or updated interface is also exposed as an object, only the object is listed. To locate the interface, refer to the [Object Model Reference for C++](object-model-reference-for-c.md). Usually, you will simply need to add the IWMP prefix to the object name. If a new interface extends an existing one, you may need to look for the latest version number. For example, Windows Media Player 9 Series introduced new properties and methods available from the [**Settings**](settings-object.md) object. In C++, these are available through the [**IWMPSettings2**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpsettings2) interface, which extends [**IWMPSettings**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpsettings).

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
-   [**IWMPEvents::PlayerDockedStateChange Event**](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpevents-playerdockedstatechange)
-   [**IWMPEvents::PlayerReconnect Event**](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpevents-playerreconnect)
-   [**IWMPEvents::SwitchedToControl Event**](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpevents-switchedtocontrol)
-   [**IWMPEvents::SwitchedToPlayerApplication Event**](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpevents-switchedtoplayerapplication)
-   [**IWMPPlayerServices Interface**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpplayerservices)
-   [**IWMPRemoteMediaServices Interface**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpremotemediaservices)
-   [**IWMPSkinManager Interface**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpskinmanager)
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

-   [**IWMPGraphCreation Interface**](/previous-versions/windows/desktop/api/wmpservices/nn-wmpservices-iwmpgraphcreation)
-   [**IWMPPlayerServices2 Interface**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpplayerservices2)
-   [**IWMPSyncDevice Interface**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpsyncdevice)
-   [**IWMPSyncServices Interface**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpsyncservices)
-   [**WMPDeviceStatus Enumeration**](/previous-versions/windows/desktop/api/wmp/ne-wmp-wmpdevicestatus)
-   [**WMPSyncState Enumeration**](/previous-versions/windows/desktop/api/wmp/ne-wmp-wmpsyncstate)

## Added for Windows Media Player 11

-   [**IWMPCdromBurn Interface**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpcdromburn)
-   [**IWMPCdromBurn Interface (VB and C#)**](iwmpcdromburn--vb-and-c.md)
-   [**IWMPCdromRip Interface**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpcdromrip)
-   [**IWMPCdromRip Interface (VB and C#)**](iwmpcdromrip--vb-and-c.md)
-   [**IWMPEvents3 Interface**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpevents3)
-   [**IWMPFolderMonitorServices Interface**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpfoldermonitorservices)
-   [**IWMPLibrary Interface**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmplibrary)
-   [**IWMPLibrary Interface (VB and C#)**](iwmplibrary--vb-and-c.md)
-   [**IWMPLibraryServices Interface**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmplibraryservices)
-   [**IWMPLibraryServices Interface (VB and C#)**](iwmplibraryservices--vb-and-c.md)
-   [**IWMPLibrarySharingServices Interface**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmplibrarysharingservices)
-   [**IWMPMediaCollection2 Interface**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpmediacollection2)
-   [**IWMPMediaCollection2 Interface (VB and C#)**](iwmpmediacollection2--vb-and-c.md)
-   [**IWMPQuery Interface**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpquery)
-   [**IWMPQuery Interface (VB and C#)**](iwmpquery--vb-and-c.md)
-   [**IWMPRenderConfig Interface**](/previous-versions/windows/desktop/api/wmprealestate/nn-wmprealestate-iwmprenderconfig)
-   [**IWMPStringCollection2 Interface**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpstringcollection2)
-   [**IWMPStringCollection2 Interface (VB and C#)**](iwmpstringcollection2--vb-and-c.md)
-   [**IWMPSyncDevice2 Interface**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpsyncdevice2)
-   [**IWMPVideoRenderConfig Interface**](/previous-versions/windows/desktop/api/wmprealestate/nn-wmprealestate-iwmpvideorenderconfig)
-   [**Query Object**](query-object.md)
-   [**WMPBurnFormat Enumeration**](/previous-versions/windows/desktop/api/wmp/ne-wmp-wmpburnformat)
-   [**WMPBurnState Enumeration**](/previous-versions/windows/desktop/api/wmp/ne-wmp-wmpburnstate)
-   [**WMPLibraryType Enumeration**](/previous-versions/windows/desktop/api/wmp/ne-wmp-wmplibrarytype)
-   [**WMPRipState Enumeration**](/previous-versions/windows/desktop/api/wmp/ne-wmp-wmpripstate)

## Added for Windows Media Player 12

-   [**IWMPAudioRenderConfig Interface**](/previous-versions/windows/desktop/api/wmprealestate/nn-wmprealestate-iwmpaudiorenderconfig)
-   [**IWMPEvents4 Interface**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpevents4)
-   [**IWMPLibrary2 Interface**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmplibrary2)
-   [**IWMPSyncDevice3 Interface**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpsyncdevice3)

## Related topics

<dl> <dt>

[**About the Player Object Model**](about-the-player-object-model.md)
</dt> <dt>

[**Object Model Reference for Scripting**](object-model-reference-for-scripting.md)
</dt> </dl>

 

 




