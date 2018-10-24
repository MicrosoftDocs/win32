---
title: track.csv
description: track.csv
ms.assetid: 5ce782b7-5fb8-4e6e-80cb-fa1dd7c47716
keywords:
- Windows Media Player online stores,track.csv
- online stores,track.csv
- type 1 online stores,track.csv
- track.csv
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# track.csv

This file contains an entry for each track in the catalog. Each entry is a row composed of the tab-delimited fields described in the table below. Fields must appear in the order listed.

The Format column in the table below describes the way each Unicode text field is formatted. It does not refer to the data type of the contents. For example, if Integer is indicated in the Format column, it means that the field contains a Unicode string representing an integral value, rather than an actual integer.



<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>Field</th>
<th>Required</th>
<th>Format</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>TrackID</td>
<td>Yes</td>
<td>Non-negative integer.Example: 32789<br/></td>
<td>Unique identifier provided by the content provider. Must be less than 2^32.Performance tip: If the IDs assigned to tracks from the same album are numbered consecutively, catalog compression will be more efficient. However, consecutive numbering of album tracks is not required.<br/></td>
</tr>
<tr class="even">
<td>TrackTitle</td>
<td>Yes</td>
<td>Unicode string. Example: Raygun Robbers' Blues</td>
<td>Name of the track.</td>
</tr>
<tr class="odd">
<td>Duration</td>
<td>Yes</td>
<td>Non-negative integer.Example: 543<br/></td>
<td>Duration of the track in seconds.</td>
</tr>
<tr class="even">
<td>TrackNumber</td>
<td>Yes</td>
<td>Non-negative integer.Example: 7<br/></td>
<td>Track number on the track's album. Track numbers begin at 1 and increase across disc sets. The track number must be less than 256. A track number greater than or equal to 256 will cause unexpected behavior in Windows Media Player.</td>
</tr>
<tr class="odd">
<td>TrackPrice</td>
<td>Yes</td>
<td>Unicode string. Example: $0.99.</td>
<td>Track price. The currency symbol should be included. The empty string, 0, and - have special meaning. An empty string indicates that the price is unknown. A zero in this field means the track is free, and a hyphen (-) indicates that the track cannot be bought.</td>
</tr>
<tr class="even">
<td>CanStream</td>
<td>Yes</td>
<td>Boolean. Can be 0 or 1.Example: 0<br/></td>
<td>Indicates whether the track can be streamed.</td>
</tr>
<tr class="odd">
<td>CanDownload</td>
<td>Yes</td>
<td>Boolean. Can be 0 or 1.Example: 0<br/></td>
<td>Indicates whether the track can be downloaded.</td>
</tr>
<tr class="even">
<td>HasPreviewClip</td>
<td>Yes</td>
<td>Boolean. Can be 0 or 1.Example: 0<br/></td>
<td>Indicates whether the track has a preview clip.</td>
</tr>
<tr class="odd">
<td>HasVideoClip</td>
<td>Yes</td>
<td>Boolean. Can be 0 or 1.Example: 0<br/></td>
<td>Indicates whether the track has a video clip.</td>
</tr>
<tr class="even">
<td>ParentalRating</td>
<td>Yes</td>
<td>Enumeration. Can be N, E, or C.Example: N<br/></td>
<td>Indicates the Parental Advisory Rating. The values N, E, and C stand for Normal, Explicit, and Clean.</td>
</tr>
<tr class="odd">
<td>LinkedAlbumID</td>
<td>Yes</td>
<td>Non-negative integer. Must be the ID of an Album. Example: 32423</td>
<td>The ID of the album that contains this track.
<blockquote>
[!Note]<br />
Every track must belong to an album. That is, for each track, the LinkedAlbumID field must be equal to one of the album IDs in the album.csv file.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>LinkedTrackArtist_ArtistIDs</td>
<td>Yes</td>
<td>List of integers. The list contains artist IDs, separated by semicolons. Example: 41322;12321; 82123;</td>
<td>A list of IDs corresponding to the contributing artists.</td>
</tr>
<tr class="odd">
<td>Composer</td>
<td>No</td>
<td>Unicode string. Example: Beethoven</td>
<td>The composer of the track. If the track's genre does not have the HasComposer field set, the value of the Composer field will be ignored. Typically used only for jazz or classical tracks.</td>
</tr>
<tr class="even">
<td>Popularity</td>
<td>Yes</td>
<td>Non-negative integer or Float.Example: 1252.6<br/></td>
<td>Determines the position of the track in the list when sorted by popularity. A lower number indicates higher popularity.</td>
</tr>
<tr class="odd">
<td>StarRating</td>
<td>No</td>
<td>Float.Example: 4.21<br/></td>
<td>The star rating will be rounded to the nearest 1/4 star by Windows Media Player before being displayed in the Windows Media Player user interface.</td>
</tr>
</tbody>
</table>



 

 

 





