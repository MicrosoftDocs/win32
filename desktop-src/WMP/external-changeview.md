---
title: External.changeView method
description: Note This topic describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported. The changeView method changes the view in Windows Media Player.
ms.assetid: bd9d7d4b-ee4c-4d7c-92ef-dd0b8ab46d9d
keywords:
- changeView method Windows Media Player
- changeView method Windows Media Player , External class
- External class Windows Media Player , changeView method
topic_type:
- apiref
api_name:
- External.changeView
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# External.changeView method

> [!Note]  
> This topic describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **changeView** method changes the view in Windows Media Player.

## Syntax


```JScript
External.changeView(
  LibraryLocationType,
  LibraryLocationID,
  Filter,
  ViewParams
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

**String** containing the ID of the specific item to show in the new view. For example, if *LibraryLocationType* is CPGenreID, then this parameter specifies the ID of the genre to show in the new view. This string can be empty. See Remarks.

</dd> <dt>

*Filter* \[in\]
</dt> <dd>

**String** containing the filter for the new view. The view will be filtered as if the user had entered this text in the Player's word wheel control. This string can be empty.

</dd> <dt>

*ViewParams* \[in\]
</dt> <dd>

**String** containing parameters that Windows Media Player makes available to the new discovery page that is displayed with the new view. These parameters are not interpreted by Windows Media Player. They are created by the online store and have meaning only to the online store.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

In some cases, it makes sense to set the *LibraryLocationID* parameter to the empty string. For example, if you set the *LibraryLocationType* parameter to AllCPAlbumIDs, the new view will represent all albums. No individual album will be the focus of the new view, so there is no need to supply an album ID in the *LibraryLocationID* parameter.

The *ViewParams* parameter provides a way for a discovery page to communicate with another discovery page. When script on a discovery page calls **changeView**, Windows Media Player adjusts its user interface. That adjustment causes the Player to call the plug-in's [IWMPContentPartner::GetTemplate](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartner-gettemplate) method to get the URL of a new discovery page. The string that the original discovery page passes in the *ViewParams* parameter does not get passed to **GetTemplate**. However, the new discovery page can retrieve the *ViewParams* string by calling [External.viewParameters](external-viewparameters.md).

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 11.<br/>                                                |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**External Object for Type 1 Online Stores**](external-object-for-type-1-online-stores.md)
</dt> <dt>

[**External.changeViewOnlineList**](external-changeviewonlinelist.md)
</dt> <dt>

[**External.libraryLocationID**](external-librarylocationid.md)
</dt> <dt>

[**External.libraryLocationType**](external-librarylocationtype.md)
</dt> <dt>

[**External.viewParameters**](external-viewparameters.md)
</dt> </dl>

 

 





