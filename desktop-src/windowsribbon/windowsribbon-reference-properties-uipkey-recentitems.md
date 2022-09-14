---
title: UI_PKEY_RecentItems
description: Identifies the UI\_PKEY\_RecentItems property.
ms.assetid: 54e7ad1f-86b3-45e0-a0f4-5ee0d08e9d4b
ms.topic: article
ms.date: 05/31/2018
---

# UI\_PKEY\_RecentItems

Identifies the UI\_PKEY\_RecentItems property.

```
propertyDescription
   name = UI_PKEY_RecentItems
   shellPKey = UI_PKEY_RecentItems
   formatID = 00000350-7363-696e-8441798acf5aebb7
   propID = 350
   typeInfo
      type = VT_ARRAY | VT_UNKNOWN
```

## Remarks

[UI\_PKEY\_Pinned](windowsribbon-reference-properties-uipkey-pinned.md) is used by an application to query the array of items in the most recently used (MRU) items collection of the [Application Menu](windowsribbon-controls-applicationmenu.md). The information for each MRU item is encapsulated in an [**IUISimplePropertySet**](/windows/desktop/api/uiribbon/nn-uiribbon-iuisimplepropertyset) object and includes the following three property keys:

-   [UI\_PKEY\_Label](windowsribbon-reference-properties-uipkey-label.md)
-   [UI\_PKEY\_LabelDescription](windowsribbon-reference-properties-uipkey-labeldescription.md)
-   [UI\_PKEY\_Pinned](windowsribbon-reference-properties-uipkey-pinned.md)

The list of MRU items is passed to the Ribbon host application as a **SAFEARRAY** of [**IUISimplePropertySet**](/windows/desktop/api/uiribbon/nn-uiribbon-iuisimplepropertyset) pointers to respective implementations in the host application.

## Related topics

<dl> <dt>

[State Properties](windowsribbon-reference-properties-state.md)
</dt> </dl>

 

 