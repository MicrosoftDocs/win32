---
title: System.Gadget.close method
description: Ends a running instance of a gadget.
ms.assetid: b7f83aed-afc3-4f3e-9cfd-8c2b8b371899
keywords:
- close method Windows Sidebar
- close method Windows Sidebar , System.Gadget object
- System.Gadget object Windows Sidebar , close method
topic_type:
- apiref
api_name:
- System.Gadget.close
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

# System.Gadget.close method

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Ends a running instance of a gadget.

## Syntax


```JScript
System.Gadget.close()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

The **close** method is asynchronous. The gadget script should not attempt to continue execution after the **close** call.

## Examples


```HTML
<html> 
<body onload="loaded()">
<script>
function loaded()
{
  window.setTimeout(close, 0);
}

function close()
{
  System.Gadget.close();
}
</script>
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

 

 





