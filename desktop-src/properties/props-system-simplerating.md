---
Description: A rating system that uses a range of integer values between 0 and 5.
ms.assetid: 50353ba9-86dd-4172-91b4-1898c8fc5522
title: System.SimpleRating
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# System.SimpleRating

A rating system that uses a range of integer values between 0 and 5.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7, Windows Vista

```
propertyDescription
   name = System.SimpleRating
   shellPKey = PKEY_SimpleRating
   formatID = A09F084E-AD41-489F-8076-AA5BE3082BCA
   propID = 100
   SearchInfo
      InInvertedIndex = false
      IsColumn = false
   typeInfo
      type = UInt32
      IsInnate = true
```

## Remarks

PKEY values are defined in Propkey.h.

For compatibility with the Windows Vista Shell rating system, your property handler should also populate the [System.Rating](https://msdn.microsoft.com/library/Bb787554(v=VS.85).aspx) property with the mapping as described for that property.

Use the following table to convert from [System.Rating](https://msdn.microsoft.com/library/Bb787554(v=VS.85).aspx) to [System.SimpleRating](https://msdn.microsoft.com/library/Bb787564(v=VS.85).aspx).



| System.Rating | System.SimpleRating |
|---------------|---------------------|
| 0             | 0                   |
| 1-12          | 1                   |
| 13-37         | 2                   |
| 38-62         | 3                   |
| 63-87         | 4                   |
| 88-99         | 5                   |



 

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

 

 



