---
title: About the Object Model Versions
description: About the Object Model Versions
ms.assetid: '20bb1681-9079-4f8c-bb5e-5c98e3bdc76a'
keywords: ["Windows Media Player,versions", "Windows Media Player object model,versions", "object model,versions", "Windows Media Player ActiveX control,versions for object model", "ActiveX control,versions for object model", "Windows Media Player Mobile ActiveX control,versions for object model", "Windows Media Player Mobile,versions for object model", "versions of Windows Media Player,object model"]
---

# About the Object Model Versions

Windows Media Player 7.0 introduced a new object model. This object model has been extended with Windows Media Player 7.1, Windows Media Player for Windows XP, Windows Media Player 9 Series, Windows Media Player 10, Windows Media Player 11, and Windows Media Player 12. Each topic in the Object Model Reference includes a Requirements section that details the minimum requirement for the individual property, method, or event. The following lists detail the new objects, methods, properties, and events that have been added for each version since version 7.0. These lists also include new C++ interfaces, methods, and events.

Where a new or updated interface is also exposed as an object, only the object is listed. To locate the interface, refer to the [Object Model Reference for C++](object-model-reference-for-c.md). Usually, you will simply need to add the IWMP prefix to the object name. If a new interface extends an existing one, you may need to look for the latest version number. For example, Windows Media Player 9 Series introduced new properties and methods available from the [**Settings**](settings-object.md) object. In C++, these are available through the [**IWMPSettings2**](iwmpsettings2.md) interface, which extends [**IWMPSettings**](iwmpsettings.md).

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
-   [**IWMPEvents::PlayerDockedStateChange Event**](iwmpevents-iwmpevents--playerdockedstatechange.md)
-   [**IWMPEvents::PlayerReconnect Event**](iwmpevents-iwmpevents--playerreconnect.md)
-   [**IWMPEvents::SwitchedToControl Event**](iwmpevents-iwmpevents--switchedtocontrol.md)
-   [**IWMPEvents::SwitchedToPlayerApplication Event**](iwmpevents-iwmpevents--switchedtoplayerapplication.md)
-   [**IWMPPlayerServices Interface**](iwmpplayerservices.md)
-   [**IWMPRemoteMediaServices Interface**](iwmpremotemediaservices.md)
-   [**IWMPSkinManager Interface**](iwmpskinmanager.md)
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

-   [**IWMPGraphCreation Interface**](iwmpgraphcreation.md)
-   [**IWMPPlayerServices2 Interface**](iwmpplayerservices2.md)
-   [**IWMPSyncDevice Interface**](iwmpsyncdevice.md)
-   [**IWMPSyncServices Interface**](iwmpsyncservices.md)
-   [**WMPDeviceStatus Enumeration**](wmpdevicestatus.md)
-   [**WMPSyncState Enumeration**](wmpsyncstate.md)

## Added for Windows Media Player 11

-   [**IWMPCdromBurn Interface**](iwmpcdromburn.md)
-   [**IWMPCdromBurn Interface (VB and C#)**](iwmpcdromburn--vb-and-c.md)
-   [**IWMPCdromRip Interface**](iwmpcdromrip.md)
-   [**IWMPCdromRip Interface (VB and C#)**](iwmpcdromrip--vb-and-c.md)
-   [**IWMPEvents3 Interface**](iwmpevents3.md)
-   [**IWMPFolderMonitorServices Interface**](iwmpfoldermonitorservices.md)
-   [**IWMPLibrary Interface**](iwmplibrary.md)
-   [**IWMPLibrary Interface (VB and C#)**](iwmplibrary--vb-and-c.md)
-   [**IWMPLibraryServices Interface**](iwmplibraryservices.md)
-   [**IWMPLibraryServices Interface (VB and C#)**](iwmplibraryservices--vb-and-c.md)
-   [**IWMPLibrarySharingServices Interface**](iwmplibrarysharingservices.md)
-   [**IWMPMediaCollection2 Interface**](iwmpmediacollection2.md)
-   [**IWMPMediaCollection2 Interface (VB and C#)**](iwmpmediacollection2--vb-and-c.md)
-   [**IWMPQuery Interface**](iwmpquery.md)
-   [**IWMPQuery Interface (VB and C#)**](iwmpquery--vb-and-c.md)
-   [**IWMPRenderConfig Interface**](iwmprenderconfig.md)
-   [**IWMPStringCollection2 Interface**](iwmpstringcollection2.md)
-   [**IWMPStringCollection2 Interface (VB and C#)**](iwmpstringcollection2--vb-and-c.md)
-   [**IWMPSyncDevice2 Interface**](iwmpsyncdevice2.md)
-   [**IWMPVideoRenderConfig Interface**](iwmpvideorenderconfig.md)
-   [**Query Object**](query-object.md)
-   [**WMPBurnFormat Enumeration**](wmpburnformat.md)
-   [**WMPBurnState Enumeration**](wmpburnstate.md)
-   [**WMPLibraryType Enumeration**](wmplibrarytype.md)
-   [**WMPRipState Enumeration**](wmpripstate.md)

## Added for Windows Media Player 12

-   [**IWMPAudioRenderConfig Interface**](iwmpaudiorenderconfig.md)
-   [**IWMPEvents4 Interface**](iwmpevents4.md)
-   [**IWMPLibrary2 Interface**](iwmplibrary2.md)
-   [**IWMPSyncDevice3 Interface**](iwmpsyncdevice3.md)

## Related topics

<dl> <dt>

[**About the Player Object Model**](about-the-player-object-model.md)
</dt> <dt>

[**Object Model Reference for Scripting**](object-model-reference-for-scripting.md)
</dt> </dl>

 

 




