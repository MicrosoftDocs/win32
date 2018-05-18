---
Description: 'Gets a FolderItem object that represents the item that has the input focus.'
ms.assetid: 'ca88801d-c8fa-4c1c-9294-f52eada40ff6'
title: 'ShellFolderView.FocusedItem property'
---

# ShellFolderView.FocusedItem property

Gets a [**FolderItem**](folderitem.md) object that represents the item that has the input focus.

This property is read-only.

## Syntax


```JScript
objFocusedItem = ShellFolderView.FocusedItem
```



## Property value

A variable of type [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) that receives the focused item object.

## Remarks

**FocusedItem** can only be called on the local system. It will not work when run on a webpage over HTTP or UNC.

## Examples

The following example shows the proper use of this method in JScript embedded in HTML.


```JScript
<html>
<head>
<title></title>

<script language="JavaScript">
    function fnShellFolderViewFocusedItemJ()
    {
        var objFolderItem;
        
        objFolderItem = WebOC.Document.FocusedItem;
        if (objFolderItem != null)
        {
            alert("Got FolderItem object.");
        }
    }
    
    function fnLoad()
    {
        var webOC;
        
        webOC = document.all("WebOC");
        webOC.Navigate("C:\\");
    }
</script>

</head>
<body onload="fnLoad()">
<object id="WebOC"
        classid="clsid:8856F961-340A-11D0-A96B-00C04FD705A2"
        width=400
        height=400>
</object>
<br><br>
<INPUT id=FocusedItem 
       type=button 
       value=FocusedItem 
       name=FocusedItem 
       onclick="fnShellFolderViewFocusedItemJ()">
</body>
</html>
```



## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                           |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 4.71 or later)</dt> </dl> |



 

 




