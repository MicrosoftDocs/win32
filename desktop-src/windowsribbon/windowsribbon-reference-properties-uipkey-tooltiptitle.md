---
title: UI_PKEY_TooltipTitle
description: Identifies the UI\_PKEY\_TooltipTitle property.
ms.assetid: ed9f422d-a782-4950-a579-060185550891
ms.topic: article
ms.date: 05/31/2018
---

# UI\_PKEY\_TooltipTitle

Identifies the UI\_PKEY\_TooltipTitle property.

```
propertyDescription
   name = UI_PKEY_TooltipTitle
   shellPKey = UI_PKEY_TooltipTitle
   formatID = 00000006-7363-696e-8441798acf5aebb7
   propID = 6
   typeInfo
      type = VT_LPWSTR
```

## Remarks

UI\_PKEY\_TooltipTitle is used by an application to query the tooltip of tabs, groups, buttons, gallery items, and other Ribbon controls.

The property value is a string constrained to any sequence of characters, including white space and line-break characters.

> [!Note]  
> Use the Universal Character Set (UCS) XML character reference `&#xA;` to specify a line break.

 

Right alignment is not supported.

The maximum length of UI\_PKEY\_TooltipTitle is unbounded.

To display an ampersand in a tooltip, escape the special character designation with a double ampersand (`&&`) as shown in the following example.


```XML
<Command.TooltipTitle>Tooltip title with &amp;&amp; for Save Command</Command.TooltipTitle>
```



## Related topics

<dl> <dt>

[Resource Properties](windowsribbon-reference-properties-resource.md)
</dt> <dt>

[**Command.TooltipTitle**](windowsribbon-element-command-tooltiptitle.md)
</dt> <dt>

[UI\_PKEY\_TooltipDescription](windowsribbon-reference-properties-uipkey-tooltipdescription.md)
</dt> </dl>

 

 




