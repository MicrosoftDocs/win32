---
title: To insert the JavaScript code
description: To insert the JavaScript code
ms.assetid: 4DB35E67-3FA1-4c84-A193-6B0840EB7679
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# To insert the JavaScript code

Insert the following JavaScript functions between the &lt;HEAD&gt; start and end tags of the page:


```
<SCRIPT LANGUAGE="JavaScript">
<!--
function <i>function1Name</i>(<i>idVariable</i>){
//display the section if it's not displayed; hide it if it is displayed
if (<i>idVariable</i>.style.display=="none"){<i>idVariable</i>.style.display=""}
else{<i>idVariable</i>.style.display="none"}
}
function <i>function2Name</i>(<i>idVariable</i>){
//remove the section when user clicks in the opened DIV
if (<i>idVariable</i>.style.display==""){<i>idVariable</i>.style.display="none"}
}
--> 
```



Where *function1Name* and *function2Name* are the names of each function, and *idVariable* is the variable for the unique ID that is passed to the script each time a user clicks the link.

## Example

The following is the actual JavaScript code used in the HTML Help documentation:


```
function doSection (secNum){
//display the section if it's not displayed; hide it if it is displayed
if (secNum.style.display=="none"){secNum.style.display=""}
else{secNum.style.display="none"}
}

function noSection (secNum){
//remove the section when user clicks in the opened DIV
if (secNum.style.display==""){secNum.style.display="none"}
}
```



## Notes

You can use a [global script file](example--create-a-global-script-file.md) to store all of your scripts in one location. This can make it much easier to maintain scripts that are used on multiple topics in a help system.

## Related topics

<dl> <dt>

[Step 3: Update Your Style Sheet](to-update-your-style-sheet.md)
</dt> </dl>

 

 




