---
title: System.Gadget.Flyout.document property
description: Gets an object that represents the Document Object Model (DOM) of the gadget Flyout HTML file.
ms.assetid: eeb6e1e6-3c48-4346-999d-14de6c027837
keywords:
- document property Windows Sidebar
- document property Windows Sidebar , System.Gadget.Flyout object
- System.Gadget.Flyout object Windows Sidebar , document property
topic_type:
- apiref
api_name:
- System.Gadget.Flyout.document
api_location:
- Sidebar.Exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# System.Gadget.Flyout.document property

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets an object that represents the Document Object Model (DOM) of the gadget **Flyout** HTML file.

This property is read-only.

## Syntax


```JScript
objdocument = System.Gadget.Flyout.document
```



## Property value

An **Object** that receives the gadget DOM.

## Remarks

Equivalent to the JavaScript object.

Facilitates interaction between the main gadget window and a gadget Flyout by providing the ability to modify the other window's DOM and trigger events.

## Examples

The following example demonstrates how to use the [**document**](system-gadget-document.md) object to update the gadget DOM from a gadget Flyout.

The gadget HTML file.


```JScript
<body onload="Init();">
    <g:background id="imgBackground" src="url(images/background.png)">
    <div id="gadgetContent">
        <span id="strTimeDisplay"></span><br />
        <a href="javascript:void(0);" onclick="showFlyout();">Show Flyout</a><br />
        <span id="sFlyoutFeedback"></span>
    </div>
    </g:background>
</body>
```



The gadget Flyout HTML file.


```JScript
<body>
<g:background id="imgBackground" src="url(images/background.png)">
<div id="flyoutContent">
    <span id="strTimeDisplay"></span><br />
    <a href="javascript:void(0);" onclick="hideFlyout();">Hide Flyout</a><br />
    <input type="text" id="txtFeedback" onkeyup="showInGadget(this);" />
</div>
</g:background>
</body>
```



The gadget script file.


```JScript
// --------------------------------------------------------------------
// Display the flyout associated with the "Flyout" gadget sample.
// --------------------------------------------------------------------
function showFlyout()
{
    System.Gadget.Flyout.show = true;
    oFlyoutDocument = System.Gadget.Flyout.document;
}

// --------------------------------------------------------------------
// Display the system time.
// --------------------------------------------------------------------
function DisplayTime()
{
    // Retrieve the local time.
    var sTimeInfo = System.Time.getLocalTime(System.Time.currentTimeZone);
    var dDateInfo = new Date(Date.parse(sTimeInfo));   
    var tHours = dDateInfo.getHours();
    var tMinutes = dDateInfo.getMinutes();
    tMinutes = ((tMinutes < 10) ? ":0" : ":") + tMinutes
    var tSeconds = dDateInfo.getSeconds();
    tSeconds = ((tSeconds < 10) ? ":0" : ":") + tSeconds;
    strTimeDisplay.innerHTML = tHours + tMinutes + tSeconds;
    if (oFlyoutDocument)
    {
        oFlyoutDocument.getElementById("strTimeDisplay").innerText = strTimeDisplay.innerHTML;
    }
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



 

 





