---
title: UI_PKEY_LabelDescription
description: Identifies the UI\_PKEY\_LabelDescription property.
ms.assetid: e7dfbe7e-c9c9-44fe-9e2d-39e20f5f7062
ms.topic: article
ms.date: 05/31/2018
---

# UI\_PKEY\_LabelDescription

Identifies the UI\_PKEY\_LabelDescription property.

```
propertyDescription
   name = UI_PKEY_LabelDescription
   shellPKey = UI_PKEY_LabelDescription
   formatID = 00000002-7363-696e-8441798acf5aebb7
   propID = 2
   typeInfo
      type = VT_LPWSTR
```

## Remarks

UI\_PKEY\_LabelDescription is used by an application to query the description associated with a [UI\_PKEY\_Label](windowsribbon-reference-properties-uipkey-label.md).

The property value is a string constrained to any sequence of characters, including white space and line-break characters.

> [!Note]  
> Use the Universal Character Set (UCS) XML character reference `&#xA;` to specify a line break.

 

The maximum length is unbounded.

Right alignment is not supported.

The following screen shot illustrates the use of a label and an associated label description in an Application Menu.

![screen shot showing a label and an associated label description in an application menu.](images/properties/ui-pkey-labeldescription.png)

## Related topics

<dl> <dt>

[Resource Properties](windowsribbon-reference-properties-resource.md)
</dt> <dt>

[**Command.LabelDescription**](windowsribbon-element-command-labeldescription.md)
</dt> <dt>

[UI\_PKEY\_Label](windowsribbon-reference-properties-uipkey-label.md)
</dt> </dl>

 

 




