---
title: UI_PKEY_TooltipDescription
description: Identifies the UI\_PKEY\_TooltipDescription property.
ms.assetid: 658e798a-f41e-4538-94ac-38a9cb20dd74
ms.topic: article
ms.date: 05/31/2018
---

# UI\_PKEY\_TooltipDescription

Identifies the UI\_PKEY\_TooltipDescription property.

```
propertyDescription
   name = UI_PKEY_TooltipDescription
   shellPKey = UI_PKEY_TooltipDescription
   formatID = 00000005-7363-696e-8441798acf5aebb7
   propID = 5
   typeInfo
      type = VT_LPWSTR
```

## Remarks

UI\_PKEY\_TooltipDescription is used by an application to query the description associated with a [UI\_PKEY\_TooltipTitle](windowsribbon-reference-properties-uipkey-tooltiptitle.md).

The property value is a string constrained to any sequence of characters, including white space and line-break characters.

> [!Note]  
> Use the Universal Character Set (UCS) XML character reference `&#xA;` to specify a line break.

 

The maximum length of UI\_PKEY\_TooltipDescription is unbounded.

Right alignment is not supported.

## Related topics

<dl> <dt>

[Resource Properties](windowsribbon-reference-properties-resource.md)
</dt> <dt>

[**Command.TooltipDescription**](windowsribbon-element-command-tooltipdescription.md)
</dt> <dt>

[UI\_PKEY\_TooltipTitle](windowsribbon-reference-properties-uipkey-tooltiptitle.md)
</dt> </dl>

 

 




