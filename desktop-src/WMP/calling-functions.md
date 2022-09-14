---
title: Calling Functions
description: Calling Functions
ms.assetid: c5a675f2-86fc-4f53-8d09-604ab4752d7b
keywords:
- Windows Media Player skins,calling functions in JScript
- skins,calling functions in JScript
- calling functions in JScript
- JScript files for skins,calling functions
- Windows Media Player skins,scriptFile attribute in JScript
- skins,scriptFile attribute in JScript
- attributes,scriptFile in JScript
- scriptFile attribute in JScript
- JScript files for skins,scriptFile attribute
ms.topic: article
ms.date: 05/31/2018
---

# Calling Functions

If you need to call more than a few lines of code, you can load a script file using the **scriptFile** attribute of the **VIEW** element, and call the functions in the script. You can load more than one file per view:


```C++
scriptFile = "myfile1.js;myfile2.js;myfile3.js"

```



After the script files are loaded, you can call functions in them from inside your View section. For example, to call a function called *myfunction* when something is clicked, type the following:


```C++
onclick = "JScript: myfunction()"

```



> [!Note]  
> If you have more than one view, only the functions in files loaded into the current view are available to the XML and JScript code running with the current view. Files loaded in other views are not in scope with the current view.

 

## Related topics

<dl> <dt>

[**Using JScript**](using-jscript.md)
</dt> </dl>

 

 




