---
Description: The acquisition date of the file or media.
ms.assetid: 7c673d21-5243-4e41-91df-c5d84aaf620a
title: System.DateAcquired
ms.topic: article
ms.date: 05/31/2018
---

# System.DateAcquired

The acquisition date of the file or media. This property is related to a particular user or group of users. For example, this data is used as the main sorting axis for the virtual folder **New Music**, which enables people to browse the latest additions to their collection.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7

```
propertyDescription
   name = System.DateAcquired
   shellPKey = PKEY_DateAcquired
   formatID = 2CBAA8F5-D81F-47CA-B17A-F8D822300131
   propID = 100
   SearchInfo
      InInvertedIndex = false
      IsColumn = true
   typeInfo
      type = DateTime
```

## Windows Vista

```
propertyDescription
   name = System.DateAcquired
   shellPKey = PKEY_DateAcquired
   formatID = 2CBAA8F5-D81F-47CA-B17A-F8D822300131
   propID = 100
   SearchInfo
      IsColumn = true
   typeInfo
      type = DateTime
```

## Remarks

PKEY values are defined in Propkey.h.

[DateAcquired](https://msdn.microsoft.com/library/Bb760675(v=VS.85).aspx) is stored as a value in the main stream of the file, but it may not always be present. In those instances, the acquisition date can be approximated based on other known dates for the content. The metadata handler should use a set of rules to determine the date to return. The following example demonstrates this for music files.

-   For purchased music, the file's creation time should be used if no acquired date is present. However, the download provider should set the [DateAcquired](https://msdn.microsoft.com/library/Bb760675(v=VS.85).aspx) property in the file.
-   For music files that the user or group "ripped" (copying music or video from a CD or DVD to a hard disk), the acquisition date should be the date that action took place. For instance, the [WM/EncodingTime](https://msdn.microsoft.com/library/Dd564908(v=VS.85).aspx) attribute.
-   For music copied from another location, the file's creation time should be used as the acquisition date.

Examples of [System.DateAcquired](https://msdn.microsoft.com/library/Bb760675(v=VS.85).aspx) are the date and time when pictures are acquired from a camera or when music is purchased online. This is not the same as [System.DateImported](https://msdn.microsoft.com/library/Bb760683(v=VS.85).aspx).

## Related topics

<dl> <dt>

[propertyDescription](https://msdn.microsoft.com/library/Bb773880(v=VS.85).aspx)
</dt> <dt>

[searchInfo](https://msdn.microsoft.com/library/Bb773885(v=VS.85).aspx)
</dt> <dt>

[labelInfo](https://msdn.microsoft.com/library/Bb773876(v=VS.85).aspx)
</dt> <dt>

[typeInfo](https://msdn.microsoft.com/library/Bb773889(v=VS.85).aspx)
</dt> <dt>

[displayInfo](https://msdn.microsoft.com/library/Bb773865(v=VS.85).aspx)
</dt> <dt>

[stringFormat](https://msdn.microsoft.com/library/Bb773886(v=VS.85).aspx)
</dt> <dt>

[booleanFormat](https://msdn.microsoft.com/library/Bb773862(v=VS.85).aspx)
</dt> <dt>

[numberFormat](https://msdn.microsoft.com/library/Bb773877(v=VS.85).aspx)
</dt> <dt>

[dateTimeFormat](https://msdn.microsoft.com/library/Bb773863(v=VS.85).aspx)
</dt> <dt>

[enumeratedList](https://msdn.microsoft.com/library/Bb773871(v=VS.85).aspx)
</dt> <dt>

[drawControl](https://msdn.microsoft.com/library/Bb773866(v=VS.85).aspx)
</dt> <dt>

[editControl](https://msdn.microsoft.com/library/Bb773868(v=VS.85).aspx)
</dt> <dt>

[filterControl](https://msdn.microsoft.com/library/Bb773874(v=VS.85).aspx)
</dt> <dt>

[queryControl](https://msdn.microsoft.com/library/Bb773883(v=VS.85).aspx)
</dt> </dl>

 

 



