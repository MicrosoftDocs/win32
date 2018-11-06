---
title: UI_PKEY_Viewable
description: Identifies the UI\_PKEY\_Viewable property.
ms.assetid: d52a6d95-a4b6-4efd-8e08-5fed50151455
ms.topic: article
ms.date: 05/31/2018
---

# UI\_PKEY\_Viewable

Identifies the UI\_PKEY\_Viewable property.

```
propertyDescription
   name = UI_PKEY_Viewable
   shellPKey = UI_PKEY_Viewable
   formatID = 00001000-7363-696e-8441798acf5aebb7
   propID = 1000
   typeInfo
      type = VT_BOOL
   booleanFormat
      formatAs = VARIANT_TRUE=-1, VARIANT_FALSE=0
```

## Remarks

UI\_PKEY\_Viewable is used by an application to query the visible or hidden state of the ribbon UI.



| Display State | Property Key Value |
|---------------|--------------------|
| Visible       | **false**          |
| Hidden        | **true**           |



 

The following screen shot shows the ribbon in hidden state.

![screen shot showing the ribbon ui hidden.](images/overviews/ribbon-viewable.png)

## Related topics

<dl> <dt>

[Ribbon Properties](windowsribbon-reference-properties-ribbon.md)
</dt> <dt>

[Displaying the Ribbon](ribbon-visibility.md)
</dt> </dl>

 

 




