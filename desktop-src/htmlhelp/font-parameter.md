---
title: Font Parameter
description: Use the Font parameter to specify font attributes for the Text or Button parameter.
ms.assetid: FB5ECFF5-FE8E-40e1-A1A0-8B8F0A3D6E39
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Font Parameter

Use the **Font** parameter to specify font attributes for the [Text](text-parameter.md) or [Button](button-parameter.md) parameter.

## Applies to

-   [ALink](alink.md)
-   [Close](close.md)
-   [HH Version](hh-version.md)
-   [KLink](klink.md)
-   [Related Topics](related-topics.md)
-   [Shortcut](shortcut.md)
-   [TCard](tcard.md)
-   [WinHelp](winhelp.md)

## Valid Values



| Syntax                                                                                                                | Description                                                                                                 | Notes                                                                                                                                                                                                                                                                                        |
|-----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| &lt;PARAM name="Font" value="*Facename\[, point size\[, charset\[, color\[, PLAIN BOLD ITALIC UNDERLINE\]\]\]\]*"&gt; | Specifies the following font attributes: font family, point size, character set, color, and format options. | The **Font** parameter is optional. The default font settings are: "Helvetica,12,,,PLAIN"<br/> For best results, specify only standard system fonts.<br/> The **Font** parameter may be ignored if the character set conflicts with the language ID of the help file.<br/> |



 

## Related topics

<dl> <dt>

[About Parameters](parameters.md)
</dt> </dl>

 

 





