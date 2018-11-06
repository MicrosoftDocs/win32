---
title: radio.csv
description: radio.csv
ms.assetid: 8b0a1852-b6c9-4598-b1ab-c679362794b3
keywords:
- Windows Media Player online stores,radio.csv
- online stores,radio.csv
- type 1 online stores,radio.csv
- radio.csv
ms.topic: article
ms.date: 05/31/2018
---

# radio.csv

This file contains entries for each radio feed included in the catalog. Each entry is a row composed of the tab-delimited fields described in the table below. Fields must appear in the order listed.

The Format column in the table below describes the way each Unicode text field is formatted. It does not refer to the data type of the contents. For example, if Integer is indicated in the Format column, it means that the field contains a Unicode string representing an integral value, rather than an actual integer.



| Field              | Required | Format                                                                                                               | Description                                                                                                                        |
|--------------------|----------|----------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| RadioID            | Yes      | Non-negative integer.                                                                                                | ID for the radio feed that is unique within radio.csv.                                                                             |
| RadioTitle         | Yes      | Unicode string.Example: Essential Hits<br/>                                                                    | Radio feed title.                                                                                                                  |
| RadioSubtitle      | No       | Unicode string. Example: Top 40.                                                                                     | Radio feed subtitle. Often a genre or subgenre name.                                                                               |
| Programmer         | Yes      | Unicode string. Example: Terri Lee Duffy                                                                             | Name of the radio feed programmer. It is recommended that this field not exceed 32 characters.                                     |
| PrimaryGenre       | Yes      | Non-negative integer.                                                                                                | The ID of the primary genre. Only one value is allowed.                                                                            |
| Mood               | Yes      | Unicode string.Example: Fun; amiable; energetic; stylish; exuberant<br/>                                       | A series of adjectives that describe the music. No trailing semicolon after the last adjective.                                    |
| Category           | Yes      | Unicode string                                                                                                       | Not used in this release. Should be empty.                                                                                         |
| Description        | No       | Unicode string.Example: Upbeat party-friendly music from the tried-and-true artists who won't disappoint.<br/> | Friendly description for display in property pages. It is recommended that this field not exceed 256 characters.                   |
| Popularity         | Yes      | Non-negative integer or decimal value.Example: 31<br/>                                                         | Popularity ranking among radio feeds. Can be 0.                                                                                    |
| StarRating         | No       | Float.Example: 3.21<br/>                                                                                       | Optional. The value, typically between 0 and 5, is rounded to the nearest 1/4 for display in the user interface.                   |
| IsSubscriptionOnly | Yes      | Boolean. Can be 0 or 1.                                                                                              | Indicates whether the feed is available by subscription only.                                                                      |
| IsRecentlyAdded    | Yes      | Boolean. Can be 0 or 1.                                                                                              | Indicates whether this feed was recently added.                                                                                    |
| IsFeatured         | Yes      | Boolean. Can be 0 or 1.                                                                                              | Indicates whether the feed is featured.                                                                                            |
| EditorialGlyph     | Yes      | Non-negative integer. Should be 0.                                                                                   | Not used in this release. Should be 0.                                                                                             |
| SortOrderRank      | Yes      | Non-negative integer.                                                                                                | Can be used to the determine sort order when all stations are listed in the user interface. Should be 0 if this field is not used. |



 

 

 





