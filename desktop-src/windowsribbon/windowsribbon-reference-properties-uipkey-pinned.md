---
title: UI_PKEY_Pinned
description: Identifies the UI\_PKEY\_Pinned property.
ms.assetid: 906b2ab9-1ed7-46a6-88bc-e8f9160ab60c
ms.topic: article
ms.date: 05/31/2018
---

# UI\_PKEY\_Pinned

Identifies the UI\_PKEY\_Pinned property.

```
propertyDescription
   name = UI_PKEY_Pinned
   shellPKey = UI_PKEY_Pinned
   formatID = 00000351-7363-696e-8441798acf5aebb7
   propID = 351
   typeInfo
      type = VT_BOOL
   booleanFormat
      formatAs = VARIANT_TRUE=-1, VARIANT_FALSE=0
```

## Remarks

UI\_PKEY\_Pinned is used by an application to query whether an item in the [Application Menu](windowsribbon-controls-applicationmenu.md) is "pinned", or persistent, across application instances. For example, an item in the most recently used (MRU) items list is accessible and does not drop off the MRU items list until it is "unpinned".

## Related topics

<dl> <dt>

[State Properties](windowsribbon-reference-properties-state.md)
</dt> <dt>

[UI\_PKEY\_RecentItems](windowsribbon-reference-properties-uipkey-recentitems.md)
</dt> <dt>

[Recent Items](windowsribbon-controls-recentitems.md)
</dt> </dl>

 

 




