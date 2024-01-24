---
description: The ORDER IN GROUP clause is used in conjunction with the GROUP ON statement, which returns result sets in groups.
ms.assetid: edfa2037-3360-411d-8a12-cdb9680222f2
title: ORDER IN GROUP Clause
ms.topic: article
ms.date: 05/31/2018
---

# ORDER IN GROUP Clause

The ORDER IN GROUP clause is used in conjunction with the [GROUP ON](-search-sql-group-on-over.md) statement, which returns result sets in groups. The ORDER IN GROUP clause enables you to sort each returned group in a different way. If you group on System.Kind, for example, you can then sort all documents by System.Document.LastAuthor, all music files by System.Music.AlbumArtist, and all emails by System.Message.FromName.

## Syntax

The following is the syntax of the ORDER IN GROUP clause:


```
GROUP ON <group column and optional ranges>
OVER (SELECT ... FROM SystemIndex
    ORDER 
        IN GROUP '<group name>' BY <column> [<direction>] [,<column> [<direction>]]
        [IN GROUP '<group name>' BY <column> [<direction>] [,<column> [<direction>]] ]
        [BY <column> [<direction>] [,<column> [<direction>]] ])
```



The group name specifier is a range or known value from the group column, as specified in the GROUP ON statement. For example, known values for System.Photo.ISOSpeed would include 'ISO-100', 'ISO-200', and so on. A range for System.Photo.DateTaken would include '2006-1-1' and '2007-1-1' for a statement like GROUP ON System.ItemDate \['2006-1-1', '2007-1-1'\].

The column specifier must be a valid column specified in either the GROUP ON or the SELECT statement. You can include more than one column, separated by commas. For example, if you group on System.Photo.ISOSpeed, you can sort all ISO-100 photos, first by System.Photo.ShutterSpeed, and then by System.Photo.Aperture.

The optional direction specifier can be either ASC for ascending (low to high) or DESC for descending (high to low). If you do not provide a direction specifier, the default, ascending, is used. If you specify more than one column, but do not specify all directions, the direction you specify last is applied to each successive column until you explicitly change the direction.

Ranges or values that are not explicitly specified in an ORDER GROUP IN clause are sorted in ascending order by the values in the GROUP ON column.

## Examples

The following example groups results by the System.Kind property. The query would order the 'program' group by the application name and the 'music' group by album title and track number. The **NULL** group would be ordered by the item name. All other groups would by ordered by the item date.


```
GROUP ON System.Kind 
OVER (SELECT System.ItemUrl, System.Music.AlbumTitle, System.Music.TrackNumber, System.ItemName, System.ItemDate, System.Kind FROM SystemIndex
    ORDER 
        IN GROUP 'program' BY System.ApplicationName ASC
        IN GROUP 'music' BY System.Music.AlbumTitle ASC, System.Music.TrackNumber ASC
        IN GROUP NULL BY System.ItemName
        BY System.ItemDate DESC)
```



The following example groups results by the System.ItemDate property, and then sorts each group by item URL, kind, or name.


```
GROUP ON System.ItemDate ['2006-1-1', '2007-1-1', '2008-1-1'] 
OVER (SELECT System.ItemUrl, System.ItemName, System.ItemDate System.Kind FROM SystemIndex
    ORDER 
        IN GROUP MINVALUE BY System.ItemUrl ASC
        IN GROUP '2007-1-1' BY System.Kind
        IN GROUP NULL BY System.ItemName)
```



The results of the preceding query would be returned in five groups and sorted as described in the following table.



| Group    | Description                                               | Sorted by                                    |
|----------|-----------------------------------------------------------|----------------------------------------------|
| MINVALUE | Items with dates before 2006-1-1                          | Sorted by the item's URL, in ascending order |
| 2006-1-1 | Items with dates on or after 2006-1-1 but before 2007-1-1 | Sorted by item date, in ascending order      |
| 2007-1-1 | Items with dates on or after 2007-1-1 but before 2008-1-1 | Sorted by kind value, in ascending order     |
| 2008-1-1 | Items with dates on or after 2008-1-1                     | Sorted by item date, in ascending order      |
| **NULL** | Items with no value in the System.ItemDate column         | Sorted by item name, in ascending order      |



 

## Related topics

<dl> <dt>

**Reference**
</dt> <dt>

[GROUP ON ... OVER... Statement](-search-sql-group-on-over.md)
</dt> <dt>

[ORDER BY Clause](-search-sql-orderby.md)
</dt> </dl>

 

 



