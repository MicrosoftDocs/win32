---
title: System.Gadget.name property
description: Gets the gadget name as specified in the gadget manifest file.
ms.assetid: 33932c9e-2806-4e65-8a68-27d058da10ef
keywords:
- name property Windows Sidebar
- name property Windows Sidebar , System.Gadget object
- System.Gadget object Windows Sidebar , name property
topic_type:
- apiref
api_name:
- System.Gadget.name
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

# System.Gadget.name property

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets the gadget name as specified in the gadget manifest file.

This property is read-only.

## Syntax


```JScript
strname = System.Gadget.name
```



## Property value

A **String** that receives the name of the gadget.

## Remarks

A gadget must have a name specified in the gadget manifest file in order to be displayed in the Gadget Picker.

## Examples

The following example demonstrates how to get the name of a gadget from the gadget manifest.


```JScript
// The gadget manifest.
<gadget>
  <name>SDK Docked</name>
  ...
</gadget>

// The gadget HTML file with inline script.
<html>
<head>
  <script>
    var mytext = "Gadget Name: " + System.Gadget.name;

    function setContentText()
    {
      gadgetContent.innerText = mytext;
    }
  </script>
</head>
<body onload="setContentText()">
  <span id="gadgetContent" style="font-family: Verdana; font-size: 20px;">name</span>
</body>
</html>
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



## See also

<dl> <dt>

[**System.Gadget**](system-gadget.md)
</dt> </dl>

 

 





