---
title: genre.csv
description: genre.csv
ms.assetid: e05517f4-a69b-4db7-943d-3490253b92f3
keywords:
- Windows Media Player online stores,genre.csv
- online stores,genre.csv
- type 1 online stores,genre.csv
- genre.csv
ms.topic: article
ms.date: 05/31/2018
---

# genre.csv

This file contains an entry for each genre represented in the catalog. Each entry is a row composed of the tab-delimited fields described in the table below. Fields must appear in the order listed.

All fields in genre.csv are required.

The Format column in the table below describes the way each Unicode text field is formatted. It does not refer to the data type of the contents. For example, if Integer is indicated in the Format column, it means that the field contains a Unicode string representing an integral value, rather than an actual integer.



| Field             | Format                                                    | Description                                                                                                                                        |
|-------------------|-----------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Genre\_ID         | Non-negative integer.Example: 22<br/>               | Genre identifier, unique within genre.csv. Must be less than 2^32. A maximum of 64 genres is possible.                                             |
| GenreTitle        | Unicode string.Example: Rock<br/>                   | Genre display name.                                                                                                                                |
| FeedsAreAvailable | Boolean.Format: \[0\|1\]<br/> Example: 0<br/> | Indicates whether "radio play" behavior is possible by jumping to a feed.                                                                          |
| HasComposer       | Boolean.Format: \[0\|1\]<br/> Example: 1<br/> | True if this genre should save composer information in the catalog. If not set, composer information is ignored and not compiled into the catalog. |



 

 

 





