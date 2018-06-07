---
Description: The prefix of an item, used for e-mail messages where the subject begins with the prefix &\#0034;Re:&\#0034;.
ms.assetid: 3c257edc-b7f7-498d-8347-0be4fca41023
title: System.ItemNamePrefix
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# System.ItemNamePrefix

The prefix of an item, used for e-mail messages where the subject begins with the prefix "Re:".

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7, Windows Vista

```
propertyDescription
   name = System.ItemNamePrefix
   shellPKey = PKEY_ItemNamePrefix
   formatID = D7313FF1-A77A-401C-8C99-3DBDD68ADD36
   propID = 100
   SearchInfo
      InInvertedIndex = false
      IsColumn = true
   typeInfo
      type = String
      IsInnate = true
```

## Remarks

PKEY values are defined in Propkey.h.

If the item is a file, then the value of this property is VT\_EMPTY. If the item is a message, then the value of this property is the forwarding or reply prefixes (including the delimiting colon, but no whitespace), or VT\_EMPTY if there is no prefix.

Example values:



| System.ItemNamePrefix | System.ItemName  | System.ItemNameDisplay |
|-----------------------|------------------|------------------------|
| VT\_EMPTY             | "Great day"      | "Great day"            |
| "Re:"                 | "Great day"      | "Re: Great day"        |
| "Fwd: "               | "Monthly budget" | "Fwd: Monthly budget"  |
| VT\_EMPTY             | accounts.xls     | accounts.xls           |



 

## Related topics

<dl> <dt>

[propertyDescription](https://www.bing.com/search?q=propertyDescription)
</dt> <dt>

[searchInfo](https://www.bing.com/search?q=searchInfo)
</dt> <dt>

[labelInfo](https://www.bing.com/search?q=labelInfo)
</dt> <dt>

[typeInfo](https://www.bing.com/search?q=typeInfo)
</dt> <dt>

[displayInfo](https://www.bing.com/search?q=displayInfo)
</dt> <dt>

[stringFormat](https://www.bing.com/search?q=stringFormat)
</dt> <dt>

[booleanFormat](https://www.bing.com/search?q=booleanFormat)
</dt> <dt>

[numberFormat](https://www.bing.com/search?q=numberFormat)
</dt> <dt>

[dateTimeFormat](https://www.bing.com/search?q=dateTimeFormat)
</dt> <dt>

[enumeratedList](https://www.bing.com/search?q=enumeratedList)
</dt> <dt>

[drawControl](https://www.bing.com/search?q=drawControl)
</dt> <dt>

[editControl](https://www.bing.com/search?q=editControl)
</dt> <dt>

[filterControl](https://www.bing.com/search?q=filterControl)
</dt> <dt>

[queryControl](https://www.bing.com/search?q=queryControl)
</dt> </dl>

 

 



