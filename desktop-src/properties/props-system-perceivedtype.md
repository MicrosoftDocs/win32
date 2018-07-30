---
Description: The perceived file type based on its canonical type.
ms.assetid: dc5122a1-43b3-4c91-a44f-315fec5b4862
title: System.PerceivedType
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# System.PerceivedType

The perceived file type based on its canonical type.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7

```
propertyDescription
   name = System.PerceivedType
   shellPKey = PKEY_PerceivedType
   formatID = 28636AA6-953D-11D2-B5D6-00C04FD918D0
   propID = 9
   SearchInfo
      InInvertedIndex = false
      IsColumn = false
   typeInfo
      type = Int32
      IsInnate = true
      EnumeratedList
         UseValueForDefault = True
         enum
            name = Custom
            value = -3
            text = Custom
         enum
            name = Unspecified
            value = -2
            text = Unspecified
         enum
            name = Folder
            value = -1
            text = Folder
            mnemonics = folders
         enum
            name = Unknown
            value = 0
            text = Unknown
         enum
            name = Text
            value = 1
            text = Text
         enum
            name = Image
            value = 2
            text = Image
            mnemonics = images|picture|pictures|pic|pics
         enum
            name = Audio
            value = 3
            text = Audio
         enum
            name = Video
            value = 4
            text = Video
            mnemonics = videos
         enum
            name = Compressed
            value = 5
            text = Compressed
         enum
            name = Document
            value = 6
            text = Document
            mnemonics = documents|doc|docs
         enum
            name = System
            value = 7
            text = System
         enum
            name = Application
            value = 8
            text = Application
         enum
            name = GameMedia
            value = 9
            text = Game Media
         enum
            name = Contacts
            value = 10
            text = Contacts
```

## Windows Vista

```
propertyDescription
   name = System.PerceivedType
   shellPKey = PKEY_PerceivedType
   formatID = 28636AA6-953D-11D2-B5D6-00C04FD918D0
   propID = 9
   SearchInfo
      InInvertedIndex = false
      IsColumn = false
   typeInfo
      type = Int32
      IsInnate = true
      EnumeratedList
         UseValueForDefault = True
         enum
            value = -3
            text = Custom
         enum
            value = -2
            text = Unspecified
         enum
            value = -1
            text = Folder
            mnemonics = folders
         enum
            value = 0
            text = Unknown
         enum
            value = 1
            text = Text
         enum
            value = 2
            text = Image
            mnemonics = images|picture|pictures|pic|pics
         enum
            value = 3
            text = Audio
         enum
            value = 4
            text = Video
            mnemonics = videos
         enum
            value = 5
            text = Compressed
         enum
            value = 6
            text = Document
            mnemonics = documents|doc|docs
         enum
            value = 7
            text = System
         enum
            value = 8
            text = Application
         enum
            value = 9
            text = Game Media
         enum
            value = 10
            text = Contacts
```

## Remarks

PKEY values are defined in Propkey.h. This value is automatically assigned by the Shell.

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

 

 



