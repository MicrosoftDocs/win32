---
title: System.Gadget.document property
description: Gets an object that represents the Document Object Model (DOM) of the gadget HTML file.
ms.assetid: c0197f6e-279c-45fb-a74d-4e7838d88228
keywords:
- document property Windows Sidebar
- document property Windows Sidebar , System.Gadget object
- System.Gadget object Windows Sidebar , document property
topic_type:
- apiref
api_name:
- System.Gadget.document
api_location:
- Sidebar.Exe
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# System.Gadget.document property

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets an object that represents the Document Object Model (DOM) of the gadget HTML file.

This property is read-only.

## Syntax


```JScript
objdocument = System.Gadget.document
```



## Property value

An **Object** that receives the gadget DOM.

## Remarks

Equivalent to the JavaScript object.

Facilitates interaction between the main gadget window and a gadget **Flyout** by providing the ability to modify the other window's DOM and trigger events.

## Examples

The following example demonstrates how to use the **document** object to update the gadget DOM from a gadget Flyout.

The gadget HTML file.


```JScript
<body onload="Init();">
<g:background id="imgBackground" src="url(images/background.png)" />
<div id="gadgetContent">
<a id="aFlyout" href="javascript:void(0);" onclick="showFlyout();">Show Flyout</a><br />
<span id="sFlyoutFeedback"></span>
</div>
</body>
```



The gadget Flyout HTML file.


```JScript
<body>
<g:background id="imgBackground" src="url(images/background.png)" />
<div id="flyoutContent">
<a href="javascript:void(0);" onclick="hideFlyout();">Hide Flyout</a><br />
<input type="text" id="txtFeedback" onkeyup="showInGadget(this);" />
</div>
</body>
```



The gadget Flyout script file.


```JScript
var oGadgetDocument = System.Gadget.document;

// --------------------------------------------------------------------
// Hide the flyout.
// --------------------------------------------------------------------
function hideFlyout()
{
    System.Gadget.Flyout.show = false;
}

// --------------------------------------------------------------------
// Display the Flyout user input in the gadget.
// --------------------------------------------------------------------
function showInGadget(userInput)
{
    oGadgetDocument.getElementById("sFlyoutFeedback").innerText = userInput.value;
}
```



## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



 

 





