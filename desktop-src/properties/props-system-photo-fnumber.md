---
Description: The FNumber value when the photo was taken, as read from the Exchangeable Image File (EXIF) information.
ms.assetid: 914dc34d-34e9-4283-be26-203da945d3e9
title: System.Photo.FNumber
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# System.Photo.FNumber

The FNumber value when the photo was taken, as read from the Exchangeable Image File (EXIF) information.This property is calculated from [System.Photo.FNumberNumerator](https://msdn.microsoft.com/library/Bb760461(v=VS.85).aspx) and [System.Photo.FNumberDenominator](https://msdn.microsoft.com/library/Bb760460(v=VS.85).aspx).

The following are possible values as taken from the EXIF 2.2 specification.

-   1
-   1.4
-   2
-   2.8
-   4
-   5.6
-   8
-   11
-   16
-   22
-   32

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7

```
propertyDescription
   name = System.Photo.FNumber
   shellPKey = PKEY_Photo_FNumber
   formatID = 14B81DA1-0135-4D31-96D9-6CBFC9671A99
   propID = 33437
   SearchInfo
      InInvertedIndex = false
      IsColumn = true
   typeInfo
      type = Double
      IsInnate = true
```

## Windows Vista

```
propertyDescription
   name = System.Photo.FNumber
   shellPKey = PKEY_Photo_FNumber
   formatID = 14B81DA1-0135-4D31-96D9-6CBFC9671A99
   propID = 33437
   SearchInfo
      IsColumn = true
   typeInfo
      type = Double
      IsInnate = true
```

## Remarks

PKEY values are defined in Propkey.h.

## Related topics

<dl> <dt>

[Exchangeable Image File Format for Digital Still Cameras: Exif Version 2.2](http://www.exif.org/Exif2-2.PDF)
</dt> <dt>

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

 

 



