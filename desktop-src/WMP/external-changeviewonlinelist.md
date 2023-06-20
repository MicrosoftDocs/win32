---
title: External.changeViewOnlineList method
description: Note This topic describes functionality designed for use by online stores. | External.changeViewOnlineList method
ms.assetid: d7a45ced-431f-4d35-8c9c-c6eeba6fcbf3
keywords:
- changeViewOnlineList method Windows Media Player
- changeViewOnlineList method Windows Media Player , External class
- External class Windows Media Player , changeViewOnlineList method
topic_type:
- apiref
api_name:
- External.changeViewOnlineList
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# External.changeViewOnlineList method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This topic describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **changeViewOnlineList** method changes the view in Windows Media Player to display a list generated dynamically by the online store.

## Syntax


```JScript
External.changeViewOnlineList(
  LibraryLocationType,
  LibraryLocationID,
  Params,
  FriendlyName,
  ListType,
  ViewMode
)
```



## Parameters

<dl> <dt>

*LibraryLocationType* \[in\]
</dt> <dd>

A [library location constant](library-location-constants.md) that specifies the type of the new view. For example, the constant CPGenreID specifies that the new view will show a particular genre.

</dd> <dt>

*LibraryLocationID* \[in\]
</dt> <dd>

**String** containing the ID of the specific item to show in the new view. For example, if *LibraryLocationType* is CPGenreID, then this parameter specifies the ID of the genre to show in the new view. This string can be empty.

</dd> <dt>

*Params* \[in\]
</dt> <dd>

**String** containing parameters that Windows Media Player passes along to the online store's plug-in by calling [IWMPContentPartner::GetTemplate](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartner-gettemplate). These parameters are not interpreted by Windows Media Player. They are created by the online store and have meaning only to the online store. This string can be empty

</dd> <dt>

*FriendlyName* \[in\]
</dt> <dd>

**String** containing a friendly name, to be displayed by Windows Media Player, for the dynamic list.

</dd> <dt>

*ListType* \[in\]
</dt> <dd>

A library location constant that specifies the type of the items in the dynamically generated list. For example, if the value of this parameter is CPTrackID, then the dynamic list will contain tracks.

</dd> <dt>

*ViewMode* \[in\]
</dt> <dd>

**String** that specifies the mode that Windows Media Player will use to display the dynamic list. The caller must set this parameter to one of the following values, which are defined in contentpartner.h:

ViewModeReport

ViewModeDetails

ViewModeIcon

ViewModeTile

ViewModeOrderedList

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

When script on a discovery page calls **changeViewOnlineList**, Windows Media Player passes some of the parameters along to the [IWMPContentPartner::GetListContents](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartner-getlistcontents) and [IWMPContentPartner::GetTemplate](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartner-gettemplate) methods, which are implemented by the online store's plug-in. The following table shows the correspondence between the parameters of the three methods.



| changeViewOnlineList parameter | GetListContents parameter | GetTemplate parameter |
|--------------------------------|---------------------------|-----------------------|
| *LocationType*                 | *location*                | *location*            |
| *LocationID*                   | *pContext*                | *pContext*            |
| *Params*                       | *bstrParams*              | *bstrViewParams*      |
| *ListType*                     | *bstrListType*            | not applicable        |



 

Because all three of the methods shown in the preceding table are implemented by the online store, you have some flexibility in how you use the parameters. The idea is that you provide enough information for **GetListContents** to determine which list it should retrieve and for **GetTemplate** to determine which discovery page should be displayed next. The following examples illustrate two possibilities.

**Example 1: A dynamic list that is in the online store's catalog**

Suppose you want the plug-in to get the contents of the dynamic list that has an ID of 6 in the online store's catalog. Assume that list 6 is a list of tracks. You could provide the plug-in with enough information by making the following call.


```C++
external.changeViewOnlineList(
   "CPListID", 6, "", 
   "Songs for Today", "CPTrackID", "ViewModeDetails");
```



Note that the *Params* parameter is empty; the plug-in has enough information in the other parameters.

**Example 2: A dynamic list that is not in the online store's catalog**

Suppose that you want the plug-in to get the contents of a dynamic list that is not in the online store's catalog. Perhaps you have decided to have a dynamic list that includes songs picked by a particular artist. Assume the artist has an ID of 2 in the online store's catalog. You could make the following call.


```C++
external.changeViewOnlineList(
   "CPArtistID", 2, "songs picked by Sally", 
   "Sally Picks", "CPTrackID", "ViewModeDetails");
```



Note that the *LocationType* and *LocationID* parameters do not specify the list. Instead, the *Params* parameter specifies the list. The *LocationType* and *LocationID* parameters are passed to **IWMPContentPartner::GetListContents**, but in this case, **GetListContents** can ignore them. The *LocationType* and *LocationID* parameters are also passed to **IWMPContentPartner::GetTemplate**, which can use them to determine which discovery page should be displayed with the dynamic list.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 11<br/>                                                 |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**External Object for Type 1 Online Stores**](external-object-for-type-1-online-stores.md)
</dt> <dt>

[**IWMPContentPartner::GetListContents**](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartner-getlistcontents)
</dt> <dt>

[**IWMPContentPartnerCallback::AddListContents**](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartnercallback-addlistcontents)
</dt> <dt>

[**IWMPContentPartner::GetTemplate**](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartner-gettemplate)
</dt> <dt>

[**Location and Selected Item**](location-and-selected-item.md)
</dt> </dl>

 

 





