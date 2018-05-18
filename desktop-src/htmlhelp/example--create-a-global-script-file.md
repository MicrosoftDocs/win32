---
title: Example Create a Global Script File
description: Example Create a Global Script File
ms.assetid: '96BB8F7A-A85D-4568-83AA-2B7BEF4CCF03'
---

# Example: Create a Global Script File

You can consolidate scripts in a global file that can be referenced from pages in both compiled and uncompiled help systems. This makes it easier to maintain scripts that are used by many different pages, such as those used for image-swapping. This example shows a global file using JavaScript, but it will work with other Web scripting languages, such as Microsoft Visual Basic Scripting Edition.

There are three steps to implementing a global script file:

Create the script file using Notepad (or another text editor). This is the file that contains all of the script code. Save this file with a .js extension.

Add a **&lt;SCRIPT&gt;** tag to the **&lt;HEAD&gt;** tag of each HTML file. This links the code in your global file to the page. The tag should look like this:


```
<script language="JavaScript" src="master.js"></script>
```



Where JavaScript is the name of the scripting language you are using and master.js is the name of the global script file.

If you are creating a compiled help (.chm) file, add the file name of your master script file to the \[FILES\] section of your project (.hhp) file.

You can call scripts that are stored in a global file the same way you would call script code that is actually on the page. For example, if you created a global file with function Func(), you could reference it like this: &lt;a onclick="Func()"&gt;.

## Notes

-   You can create more than one global script file.
-   This procedure can be used with any scripting language.

## Related topics

<dl> <dt>

[About the Script and DHTML Examples](script-and-dhtml-examples.md)
</dt> </dl>

 

 




