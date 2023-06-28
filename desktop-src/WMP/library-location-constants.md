---
title: Library Location Constants
description: Library Location Constants
ms.assetid: 88ff9b91-6b21-4f7d-ae13-e8456a3e0f75
keywords:
- Windows Media Player online stores,library location constants
- online stores,library location constants
- type 1 online stores,library location constants
- Windows Media Player online stores,locations
- online stores,locations
- type 1 online stores,locations
- Windows Media Player library,location constants
- library,location constants
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Library Location Constants

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This section describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The library location constants are global string variables defined in contentpartner.h. They are used by certain methods of the [IWMPContentPartner](/previous-versions/windows/desktop/api/contentpartner/nn-contentpartner-iwmpcontentpartner) and [IWMPContentPartnerCallback](/previous-versions/windows/desktop/api/contentpartner/nn-contentpartner-iwmpcontentpartnercallback) interfaces and by certain methods of the [External](external-object-for-type-1-online-stores.md) object. These constants are used to indicate the following types.

-   Library location type: This is the type of library view being displayed by Windows Media Player. For example, the Player might be displaying a view of a particular album (g\_szCPAlbumID) or the view of all genres (g\_szAllCPGenreIDs).
-   Selected item type: This is the type of item selected in the library view. For example, the user might select a particular album (g\_szCPAlbumID) in the view of all albums.
-   List type: This is the type of list being requested from the content partner plug-in. For example, Windows Media Player might ask the plug-in to supply a list of items associated with a particular playlist (g\_szCPListID).
-   List item type: The type of individual list item being requested from the content partner plug-in. For example, Windows Media Player might ask the plug-in to supply the list of tracks (g\_szCPTrackID) in a particular playlist.

The following table gives the name and value of each constant, and a brief description of the library location or type. In C or C++ code that is compiled with the contentpartner.h header file, you can use either the name or the value of a constant. Using the name is preferable because the compiler will detect misspellings. In script (for example, when calling the methods of the [External](external-object-for-type-1-online-stores.md) object), you cannot use the name of a constant; you must use the value.



| Name                              | Value                        | Location or type                                                                                                                                                   |
|-----------------------------------|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| g\_szUnknownLocation              | UnknownLocation              | A set of tracks that is neither an album nor a playlist. Windows Media Player also uses this constant in the rare event that it cannot determine a valid location. |
| g\_szRootLocation                 | RootLocation                 | The top node in the library tree-view control                                                                                                                      |
| g\_szFlyoutMenu                   | FlyoutMenu                   | The current online store's flyout menu                                                                                                                             |
| g\_szOnlineStore                  | OnlineStore                  | All online stores                                                                                                                                                  |
| g\_szCPListID                     | CPListID                     | An individual list                                                                                                                                                 |
| g\_szAllCPListIDs                 | AllCPListIDs                 | All lists                                                                                                                                                          |
| g\_szCPTrackID                    | CPTrackID                    | An individual track                                                                                                                                                |
| g\_szAllCPTrackIDs                | AllCPTrackIDs                | All tracks                                                                                                                                                         |
| g\_szCPArtistID                   | CPArtistID                   | An individual artist                                                                                                                                               |
| g\_szAllCPArtistIDs               | AllCPArtistIDs               | All artists                                                                                                                                                        |
| g\_szCPAlbumID                    | CPAlbumID                    | An individual album                                                                                                                                                |
| g\_szAllCPAlbumIDs                | AllCPAlbumIDs                | All albums                                                                                                                                                         |
| g\_szCPGenreID                    | CPGenreID                    | An individual genre                                                                                                                                                |
| g\_szAllCPGenreIDs                | AllCPGenreIDs                | All genres                                                                                                                                                         |
| g\_szCPAlbumSubGenreID            | CPAlbumSubGenreID            | An individual subgenre                                                                                                                                             |
| g\_szAllCPAlbumSubGenreIDs        | AllCPAlbumSubGenreIDs        | All subgenres                                                                                                                                                      |
| g\_szReleaseDateYear              | ReleaseDateYear              | An individual year that catalog content was released                                                                                                               |
| g\_szAllReleaseDateYears          | AllReleaseDateYears          | All years that catalog content was released                                                                                                                        |
| g\_szCPRadioID                    | CPRadioID                    | An individual radio stream                                                                                                                                         |
| g\_szAllCPRadioIDs                | AllCPRadioIDs                | All radio streams                                                                                                                                                  |
| g\_szAuthor                       | Author                       | An individual author                                                                                                                                               |
| g\_szAllAuthors                   | AllAuthors                   | All authors                                                                                                                                                        |
| g\_szWMParentalRating             | WMParentalRating             | An individual parental rating                                                                                                                                      |
| g\_szAllWMParentalRatings         | AllWMParentalRatings         | All parental ratings                                                                                                                                               |
| g\_szUserEffectiveRatingStars     | UserEffectiveRatingStars     | An individual user rating, measured as a number of stars                                                                                                           |
| g\_szAllUserEffectiveRatingStarss | AllUserEffectiveRatingStarss | All user ratings                                                                                                                                                   |



 

## Related topics

<dl> <dt>

[**External.addToBasket**](external-addtobasket.md)
</dt> <dt>

[**External.buy**](external-buy.md)
</dt> <dt>

[**External.changeView**](external-changeview.md)
</dt> <dt>

[**External.changeViewOnlineList**](external-changeviewonlinelist.md)
</dt> <dt>

[**External.download**](external-download.md)
</dt> <dt>

[**External.libraryLocationType**](external-librarylocationtype.md)
</dt> <dt>

[**External.play**](external-play.md)
</dt> <dt>

[**IWMPContentPartner::GetCommands**](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartner-getcommands)
</dt> <dt>

[**IWMPContentPartner::GetListContents**](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartner-getlistcontents)
</dt> <dt>

[**IWMPContentPartner::GetTemplate**](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartner-gettemplate)
</dt> <dt>

[**IWMPContentPartner::InvokeCommand**](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartner-invokecommand)
</dt> <dt>

[**IWMPContentPartnerCallback::ChangeView**](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartnercallback-changeview)
</dt> </dl>

 

 




