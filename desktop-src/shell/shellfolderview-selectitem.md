---
description: ShellFolderView.SelectItem method - Sets the selection state of an item in the view.
title: ShellFolderView.SelectItem method (Shldisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ShellFolderView.SelectItem
api_type: 
- COM
api_location: 
- Shell32.dll
ms.assetid: 91c39d4c-56c3-4c2b-93e8-9f782ca0aa93

---

# ShellFolderView.SelectItem method

Sets the selection state of an item in the view.

## Syntax


```JScript
ShellFolderView.SelectItem(
  vItem,
  dwFlags
)
```



## Parameters

<dl> <dt>

*vItem* \[in\]
</dt> <dd>

Type: **Variant\***

The [**FolderItem**](folderitem.md) object for which the selection state will be set.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **Integer**

A set of flags that indicate the new selection state. This can be one or more of the following values.

<dt>



 (0)


</dt> <dd>

Deselect the item.

</dd> <dt>



 (1)


</dt> <dd>

Select the item.

</dd> <dt>



 (3)


</dt> <dd>

Put the item in edit mode.

</dd> <dt>



 (4)


</dt> <dd>

Deselect all but the specified item.

</dd> <dt>



 (8)


</dt> <dd>

Ensure the item is displayed in the view.

</dd> <dt>



 (16)


</dt> <dd>

Give the item the focus.

</dd> </dl> </dd> </dl>

## Return value

This method does not return a value.

## Remarks

[**FocusedItem**](shellfolderview-focuseditem.md) can only be called on the local system. It will not work when run on a webpage over HTTP or UNC.

## Examples

The following example shows the proper use of this method in JScript embedded in HTML.


```JScript
<html>
<head>
<title></title>

<script language="JavaScript">
    function fnShellFolderViewSelectItemJ()
    {
        var objFolder;
        
        objFolder = WebOC.Document.Folder;
        if (objFolder != null)
        {
            var objFolderItem;
            
            objFolderItem = objFolder.Self;
            if (objFolderItem != null)
            {
                WebOC.Document.SelectItem(objFolderItem, 16);
                alert("item selected");
            }
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
<INPUT id=SelectItem 
       type=button 
       value=SelectItem 
       name=SelectItem 
       onclick="fnShellFolderViewSelectItemJ()">
</body>
</html>
```



## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                           |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 4.71 or later)</dt> </dl> |



 

 




