---
Description: Indicates the direction of saturation processing applied by the camera when the photo was taken.
ms.assetid: 209edf55-fd6c-416b-b175-346f5158fc2a
title: System.Photo.Saturation
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# System.Photo.Saturation

Indicates the direction of saturation processing applied by the camera when the photo was taken.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7

```
propertyDescription
   name = System.Photo.Saturation
   shellPKey = PKEY_Photo_Saturation
   formatID = 49237325-A95A-4F67-B211-816B2D45D2E0
   propID = 100
   SearchInfo
      InInvertedIndex = false
      IsColumn = false
   typeInfo
      type = UInt32
      EnumeratedList
         UseValueForDefault = True
         enum
            name = Normal
            value = 0
            text = Normal
            defineToken = PHOTO_SATURATION_NORMAL
         enum
            name = Low
            value = 1
            text = Low saturation
            defineToken = PHOTO_SATURATION_LOW
         enum
            name = High
            value = 2
            text = High saturation
            defineToken = PHOTO_SATURATION_HIGH
```

## Windows Vista

```
propertyDescription
   name = System.Photo.Saturation
   shellPKey = PKEY_Photo_Saturation
   formatID = 49237325-A95A-4F67-B211-816B2D45D2E0
   propID = 100
   SearchInfo
      InInvertedIndex = false
      IsColumn = false
   typeInfo
      type = UInt32
      EnumeratedList
         UseValueForDefault = True
         enum
            value = 0
            text = Normal
            defineName = PHOTO_SATURATION_NORMAL
         enum
            value = 1
            text = Low saturation
            defineName = PHOTO_SATURATION_LOW
         enum
            value = 2
            text = High saturation
            defineName = PHOTO_SATURATION_HIGH
```

## Remarks

PKEY values are defined in Propkey.h.

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

 

 



