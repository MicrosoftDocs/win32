---
Description: The amount of free space in a volume, in bytes.
ms.assetid: 84c85468-d3c2-49bf-b52b-bbd3d9ecb914
title: System.FreeSpace
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# System.FreeSpace

The amount of free space in a volume, in bytes.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7

```
propertyDescription
   name = System.FreeSpace
   shellPKey = PKEY_FreeSpace
   formatID = 9B174B35-40FF-11D2-A27E-00C04FC30871
   propID = 2
   SearchInfo
      InInvertedIndex = false
      IsColumn = false
   typeInfo
      type = UInt64
      IsInnate = true
      EnumeratedList
         UseValueForDefault = True
         enumRange
            name = Full
            minValue = 0
            setValue = 0
            text = Full
            defineToken = FREESPACE_FULL
            mnemonics = full
         enumRange
            name = Tiny
            minValue = 1
            setValue = 1
            text = Tiny (0 - 2 GB)
            defineToken = FREESPACE_TINY
            mnemonics = tiny
         enumRange
            name = Small
            minValue = 2147483649
            setValue = 2147483649
            text = Small (2 - 10 GB)
            defineToken = FREESPACE_SMALL
            mnemonics = small
         enumRange
            name = Medium
            minValue = 10737418241
            setValue = 10737418241
            text = Medium (10 - 40 GB)
            defineToken = FREESPACE_MEDIUM
            mnemonics = medium
         enumRange
            name = Large
            minValue = 42949672961
            setValue = 42949672961
            text = Large (40 - 80 GB)
            defineToken = FREESPACE_LARGE
            mnemonics = large
         enumRange
            name = Huge
            minValue = 85899345921
            setValue = 85899345921
            text = Huge (80 - 120 GB)
            defineToken = FREESPACE_HUGE
            mnemonics = huge
         enumRange
            name = Gigantic
            minValue = 137438953473
            setValue = 137438953473
            text = Gigantic (over 120 GB)
            defineToken = FREESPACE_GIGANTIC
            mnemonics = gigantic
```

## Windows Vista

```
propertyDescription
   name = System.FreeSpace
   shellPKey = PKEY_FreeSpace
   formatID = 9B174B35-40FF-11D2-A27E-00C04FC30871
   propID = 2
   SearchInfo
      InInvertedIndex = false
      IsColumn = false
   typeInfo
      type = UInt64
      IsInnate = true
      EnumeratedList
         UseValueForDefault = True
         enumRange
            minValue = 0
            setValue = 0
            text = Zero
            mnemonics = empty
         enumRange
            minValue = 1
            setValue = 1
            text = Tiny (0 - 2 GB)
            mnemonics = tiny
         enumRange
            minValue = 2147483649
            setValue = 2147483649
            text = Small (2 - 10 GB)
            mnemonics = small
         enumRange
            minValue = 10737418241
            setValue = 10737418241
            text = Medium (10 - 40 GB)
            mnemonics = medium
         enumRange
            minValue = 42949672961
            setValue = 42949672961
            text = Large (40 - 80 GB)
            mnemonics = large
         enumRange
            minValue = 85899345921
            setValue = 85899345921
            text = Huge (80 - 120 GB)
            mnemonics = huge
         enumRange
            minValue = 137438953473
            setValue = 137438953473
            text = Gigantic (over 120 GB)
            mnemonics = gigantic
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

 

 



