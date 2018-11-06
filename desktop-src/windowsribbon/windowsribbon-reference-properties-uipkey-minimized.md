---
title: UI_PKEY_Minimized
description: Identifies the UI\_PKEY\_Minimized property.
ms.assetid: 52f3558b-f8a0-45d7-9eb4-b63993ae8cac
ms.topic: article
ms.date: 05/31/2018
---

# UI\_PKEY\_Minimized

Identifies the UI\_PKEY\_Minimized property.

```
propertyDescription
   name = UI_PKEY_Minimized
   shellPKey = UI_PKEY_Minimized
   formatID = 00001001-7363-696e-8441798acf5aebb7
   propID = 1001
   typeInfo
      type = VT_BOOL
   booleanFormat
      formatAs = VARIANT_TRUE=-1, VARIANT_FALSE=0
```

## Remarks

UI\_PKEY\_Minimized is used by an application to query the collapsed or expanded state of the ribbon UI.



| Display State | Property Key Value |
|---------------|--------------------|
| Expanded      | **false**          |
| Collapsed     | **true**           |



 

When the ribbon UI is in a minimized state, the ribbon Tab row remains visible and fully functional.

The following screen shot shows the ribbon in minimized state.

![screen shot showing the ribbon ui minimized.](images/overviews/ribbon-minimized.png)

## Related topics

<dl> <dt>

[Ribbon Properties](windowsribbon-reference-properties-ribbon.md)
</dt> <dt>

[Displaying the Ribbon](ribbon-visibility.md)
</dt> </dl>

 

 




