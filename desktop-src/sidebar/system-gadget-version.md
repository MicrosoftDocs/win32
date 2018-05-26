---
title: System.Gadget.version property
description: Gets the gadget version as specified in the gadget manifest file.
ms.assetid: fdf946b7-ae88-4093-9a71-620c95812cf1
keywords:
- version property Windows Sidebar
- version property Windows Sidebar , System.Gadget object
- System.Gadget object Windows Sidebar , version property
topic_type:
- apiref
api_name:
- System.Gadget.version
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

# System.Gadget.version property

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets the gadget version as specified in the gadget manifest file.

This property is read-only.

## Syntax


```JScript
strversion = System.Gadget.version
```



## Property value

A **String** that receives the version of the gadget.

## Remarks

A gadget must have a version specified in the gadget manifest file in order to be displayed in the Gadget Picker.

Possible uses include checking if a newer version of a gadget is available or displaying warnings of possible conflicts with other versions of the same gadget.

## Examples

The following example demonstrates how to get the version of a gadget from the gadget manifest.


```JScript
// The gadget manifest.
<gadget>
  <name>SDK Docked</name>
  <version>1.0.0.0</version>
  ...
</gadget>

// The gadget HTML file with inline script.
<html>
<head>
  <script>
    var mytext = "Gadget Version: " + System.Gadget.version;

    function setContentText()
    {
      gadgetContent.innerText = mytext;
    }
  </script>
</head>
<body onload="setContentText()">
  <span id="gadgetContent" style="font-family: Verdana; font-size: 20px;"/>
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

 

 





