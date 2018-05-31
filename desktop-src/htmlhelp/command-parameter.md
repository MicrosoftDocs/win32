---
title: Command Parameter
description: Use the Command parameter to specify an HTML Help command.
ms.assetid: A9FEE37B-BEAF-46e0-9D96-B16ACACB3C4D
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Command Parameter

Use the **Command** parameter to specify an HTML Help [command](about-commands.md).

## Applies to

-   [ALink](alink.md)
-   [Close](close.md)
-   [Contents](contents.md)
-   [HH Version](hh-version.md)
-   [Index](index.md)
-   [KLink](klink.md)
-   [Related Topics](related-topics.md)
-   [Shortcut](shortcut.md)
-   [Splash](splash.md)
-   [TCard](tcard.md)
-   [WinHelp](winhelp.md)

## Valid Values



| Syntax                                                                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| &lt;PARAM name="Command" value="*command name* \[,menu\|,dialog \[,popup\]\]"&gt; | Specifies the command to invoke. The [ALink](alink.md), [KLink](klink.md), and [Related Topics](related-topics.md) commands include a setting (\[,menu\|,dialog\]) that specifies whether to display target topics [on a pop-up menu or in a dialog box](window-types.md). <br/> The [WinHelp](winhelp.md) command includes a setting (\[,popup\]) that specifies the [window type](winhelp-window-types.md) in which to display the specified WinHelp topic.<br/> Multiple **Command** parameter values are delimited by a comma.<br/> |



 

## Related topics

<dl> <dt>

[About Parameters](parameters.md)
</dt> </dl>

 

 





