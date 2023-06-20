---
title: External Object for Type 1 Online Stores
description: External Object for Type 1 Online Stores
ms.assetid: 5c42e1a9-c5c6-4725-8528-de2839d84e77
keywords:
- Windows Media Player online stores,external objects
- online stores,external objects
- type 1 online stores,external objects
- external objects
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# External Object for Type 1 Online Stores

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This section describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **External** object provides functionality to webpages, provided by an online store, hosted in Windows Media Player.

The **External** object exposes the following properties for type 1 online stores.



| Property                                                                                  | Description                                                                                                                              |
|-------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| [accountType](external-accounttype.md)                                                   | Retrieves the account type of the current user.                                                                                          |
| [appColorButtonHighlight](external-appcolorbuttonhighlight.md)                           | Retrieves the current button highlight color for the Windows Media Player user interface.                                                |
| [appColorButtonHoverFace](external-appcolorbuttonhoverface.md)                           | Retrieves the current button hover color for the Windows Media Player user interface.                                                    |
| [appColorButtonShadow](external-appcolorbuttonshadow.md)                                 | Retrieves the current button shadow color for the Windows Media Player user interface.                                                   |
| [appColorDark](external-appcolordark.md)                                                 | Retrieves the current dark shaded color of the Windows Media Player user interface.                                                      |
| [appColorLight](external-appcolorlight.md)                                               | Retrieves the current light shaded color of the Windows Media Player user interface.                                                     |
| [appColorMedium](external-appcolormedium.md)                                             | Retrieves the current medium shaded color of the Windows Media Player user interface.                                                    |
| [basketTitle](external-baskettitle.md)                                                   | Retrieves the title of the button in the list pane (also called the basket) in Windows Media Player.                                     |
| [filter](external-filter.md)                                                             | Retrieves the search filter currently in use by Windows Media Player.                                                                    |
| [ignoreIEHistory](external-ignoreiehistory.md)                                           | Specifies whether Windows Media Player should ignore Internet Explorer history.                                                          |
| [libraryLocationID](external-librarylocationid.md)                                       | Retrieves the identifier of a specific media item that is currently displayed in the Player's view.                                      |
| [libraryLocationType](external-librarylocationtype.md)                                   | Retrieves a [library location constant](library-location-constants.md) that indicates type of the current view in Windows Media Player. |
| [pluginRunning](external-pluginrunning.md)                                               | Retrieves a value that indicates whether the online store's plug-in is running.                                                          |
| [selectedItemID](external-selecteditemid.md)                                             | Retrieves the identifier of the media item that is currently selected in Windows Media Player.                                           |
| [selectedItemType](external-selecteditemtype.md)                                         | Retrieves the type of the media item that is currently selected in Windows Media Player.                                                 |
| [task](external-task.md)                                                                 | Retrieves the name of the current task pane.                                                                                             |
| [templateBeingDisplayedInLocalLibrary](external-templatebeingdisplayedinlocallibrary.md) | Indicates whether the feed represented by the current discovery page is being displayed in the local library tree-view control.          |
| [userLoggedIn](external-userloggedin.md)                                                 | Retrieves a value indicating whether the user is logged in to the online store.                                                          |
| [version](external-version.md)                                                           | Retrieves the current version of Windows Media Player.                                                                                   |
| [viewParameters](external-viewparameters.md)                                             | Retrieves parameters associated with the current view in Windows Media Player.                                                           |



 

The **External** object exposes the following methods for type 1 online stores.



| Method                                                            | Description                                                                                                                  |
|-------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| [addToBasket](external-addtobasket.md)                           | Adds media items to the list pane (also called the basket) in Windows Media Player.                                          |
| [attemptLogin](external-attemptlogin.md)                         | Displays a dialog box so the user can attempt to log in to the online store.                                                 |
| [authenticate](external-authenticate.md)                         | Initiates an attempt to authenticate the user.                                                                               |
| [buy](external-buy.md)                                           | Initiates the purchase of a set of media items.                                                                              |
| [cancelNavigate](external-cancelnavigate.md)                     | Informs Windows Media Player that it should not display a new discovery page even though the view has changed in the Player. |
| [changeView](external-changeview.md)                             | Changes the view in Windows Media Player.                                                                                    |
| [changeViewOnlineList](external-changeviewonlinelist.md)         | Changes the view in Windows Media Player to display a list generated dynamically by the online store.                        |
| [download](external-download.md)                                 | Initiates the download of a set of media items.                                                                              |
| [play](external-play.md)                                         | Instructs Windows Media Player to play a set of media items.                                                                 |
| [saveCurrentViewToLibrary](external-savecurrentviewtolibrary.md) | Creates a playlist from the media items in the current view and saves the playlist to the local library.                     |
| [sendMessage](external-sendmessage.md)                           | Sends a message to the online store's plug-in.                                                                               |
| [showPopup](external-showpopup.md)                               | Instructs Windows Media Player to display a pop-up webpage; that is, a webpage that appears in a separate window.            |



 

The **External** object exposes the following events for type 1 online stores.



| Event                                                                         | Description                                                                             |
|-------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| [OnChangeViewError](external-onchangeviewerror-event.md)                     | Occurs when a call to the **External.ChangeView** method results in an error.           |
| [OnChangeViewOnlineListError](external-onchangeviewonlinelisterror-event.md) | Occurs when a call to the **External.ChangeViewOnlineList** method results in an error. |
| [OnColorChange](external-oncolorchange-event.md)                             | Occurs when the color of the Windows Media Player user interface changes.               |
| [OnLoginChange](external-onloginchange-event.md)                             | Occurs when the user's log-in status changes or when an attempt to log in fails.        |
| [OnSendMessageComplete](external-onsendmessagecomplete-event.md)             | Occurs when the online store has finished processing a message.                         |
| [OnViewChange](external-onviewchange-event.md)                               | Occurs when the view changes in Windows Media Player.                                   |



 

## Related topics

<dl> <dt>

[**Reference for Type 1 Online Stores**](reference-for-type-1-online-stores.md)
</dt> <dt>

[**Remoting the Windows Media Player Control**](remoting-the-windows-media-player-control.md)
</dt> </dl>

 

 




