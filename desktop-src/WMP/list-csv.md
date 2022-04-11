---
title: list.csv
description: list.csv
ms.assetid: 020b213c-826c-430c-8ce7-92b819581de8
keywords:
- Windows Media Player online stores,list.csv
- online stores,list.csv
- type 1 online stores,list.csv
- list.csv
ms.topic: article
ms.date: 05/31/2018
---

# list.csv

This file contains an entry for each of the lists the catalog contains. Lists can be lists of tracks, albums, artists, genres, subgenres, or radio feeds; or they can be lists of other lists. Each list entry is a row composed of the tab-delimited fields described in the table below. Fields must appear in the order listed.

The Format column in the table below describes the way each Unicode text field is formatted. It does not refer to the data type of the contents. For example, if Integer is indicated in the Format column, it means that the field contains a Unicode string representing an integral value, rather than an actual integer.




| Field | Required | Format | Description | 
|-------|----------|--------|-------------|
| ListID | Yes | Non-negative integer. | List identifier, unique within list.csv. Must be non-negative and less than 2^32.<strong>Displaying a list node in tree view control:</strong> If the ListID is 0, 1, 2, 3, 4, 5, 6, or 7, the list will appear as a custom node under your online store's top-level node in the Player's tree view control. Custom nodes appear before the standard nodes under the online store's top-level node, and they are positioned in ascending order by ListID. For example, if there are three custom nodes, with ListIDs of 1, 3, and 5, they will be displayed first, second, and third under the online store's top level node.<br /> | 
| ListTitle | No | Unicode string.Example: Top Ten Hits<br /> | List title. | 
| ListSubtitle | No | Unicode string | List alternate title, displayed in the second line of the Tile view. | 
| ListDescription | Yes | Unicode string | List friendly display text (displayed in property pages). | 
| Linked_ItemType | Yes | Unicode string.Format: [T\|P\|A\|L\|G\|S\|R]<br /> Example: T<br /> | Indicates the type of the linked items.<ul><li>T= Track</li><li>P = Performer</li><li>A = Album</li><li>L = List</li><li>G = Genre</li><li>S = Subgenre</li><li>R = Radio</li></ul> | 
| ListPrice | Yes | Unicode string.Example: $9.99<br /> | Price of the list. The currency symbol should be included.A zero means the list is free. No value means the price is unknown. A hyphen means the list cannot be purchased.<br /> | 
| Popularity | Yes | Integer or decimal value.Example: 1259.3<br /> | Indicates the popularity ranking when this list appears in other lists. Can be zero if not applicable.. | 
| IsRecentlyAdded | Yes | Boolean.Format: [0\|1]<br /> Example: 0<br /> | Indicates whether the list was recently added. | 
| IsFeatured | Yes | Boolean.Format: [0\|1]<br /> Example: 0<br /> | Indicates whether the list is featured. Can be used in determining sort order. | 
| EditorialGlyph | Yes | Non-negative integer. Should be 0. | Not used in this release. Should be 0. | 
| ViewType | Yes | Unicode string. Format: [I\|T\|R\|L\|O]Example: T<br /> | Indicates the view type to use for the list.<ul><li>I = Icon</li><li>T = Tile</li><li>R = Report</li><li>L = List</li><li>O = Ordered List</li></ul> | 
| ViewImageSize | Yes | Non-negative integer.Example: 180<br /> | The size at which the list image is displayed. If 0, size is determined automatically. | 
| GroupBy | Yes | Unicode string.Format: [-\|P\|A\|C\|R\|D]<br /> Example: P<br /> | Indicates what field is used to group the items in the list.<ul><li>- = Automatic</li><li>P = Performer</li><li>A = Album</li><li>C = Composer</li><li>R = Rating</li><li>D = Date</li></ul> | 
| ListItemsAreDynamic | Yes | Boolean. Can be 0 or 1. | Indicates whether the list is generated dynamically. Dynamic lists do not have items in listitem.csv. If a list is marked as dynamic, its items are provided by <a href="/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartner-getlistcontents">IWMPContentPartner::GetListContents</a> | 




 

 

 





