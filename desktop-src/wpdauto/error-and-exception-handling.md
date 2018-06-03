---
title: Error and Exception Handling
description: All WPD Automation errors are returned as standard JScript exceptions. Script writers are encouraged to wrap script code in try-catch blocks and handle errors appropriately.
ms.assetid: ea17d052-79d6-4e53-87c8-033c0a1c7fe6
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Error and Exception Handling

All WPD Automation errors are returned as standard JScript exceptions. Script writers are encouraged to wrap script code in try-catch blocks and handle errors appropriately.

> [!Note]  
> For Windows 7, the primary scripting language supported by WPD Automation is JScript 5.6. Other scripting languages, such as VBScript or JScript.NET are not supported.

 

The following JScript example demonstrates how to wrap script code in a try-catch block to handle errors.


```JScript
try
{
    // Script code here.

}
catch (e)
{
    // Handle exception here.

    alert("An error has occurred: " + e.description);
}
```



## Related topics

<dl> <dt>

[Best Practices for Writing WPD Automation Scripts](best-practices-for-writing-wpd-automation-scripts.md)
</dt> </dl>

 

 




