---
title: Flags Parameter
description: Use the Flags parameter to specify how topics should be searched for, and how they should appear, for certain commands.
ms.assetid: C07A1314-46F5-46be-A64F-5E194906034A
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Flags Parameter

Use the **Flags** parameter to specify how topics should be searched for, and how they should appear, for certain commands.

## Applies to

-   [ALink](alink.md)
-   [Contents](contents.md)
-   [KLink](klink.md)

## Valid Values



| Syntax                                                                       | Description                                                                                                                                                                                                                  | Notes                                                                                                                                                                                                                                                            |
|------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| &lt;PARAM name="Flags" value="1"&gt;                                         | Used with the [ALink](alink.md) or [KLink](klink.md) commands to specify that when a single target topic is found, the topic should appear in the window type specified in the [Command](command-parameter.md) parameter. | If this parameter is empty (value=" "), clicking the ALink or KLink navigates directly to the target topic when a single topic is found.                                                                                                                         |
| &lt;PARAM name="Flags" value=",,1"&gt;                                       | Used with the [ALink](alink.md) or [KLink](klink.md) commands to specify that when a target topic cannot be found, the ALink or KLink button (or text) should be unavailable.                                              | If this parameter is empty (value=" "), clicking the ALink or KLink opens a **Topic Not Found** dialog box when the topic cannot be located.                                                                                                                     |
| &lt;PARAM name="Flags" value="*numeric value of selected window styles*"&gt; | Used with the [Contents](contents.md) command to store the numeric value of the selected window style attributes.                                                                                                           | The window style hexadecimal numeric values are not currently mapped. We recommend that you use the HTML Help ActiveX Control Wizard to select window styles. The wizard automatically inserts the appropriate parameter values in the format 0x*n*. <br/> |



 

## Related topics

<dl> <dt>

[About Parameters](parameters.md)
</dt> </dl>

 

 





