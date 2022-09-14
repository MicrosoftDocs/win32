---
title: WebViewFolderContents.FocusedItem property (Shldisp.h)
description: WebViewFolderContents.FocusedItem property - Gets a FolderItem object that represents the item that has the input focus.
ms.assetid: 84cf92ac-dadb-4741-8383-a8ae1d35d4e0
keywords:
- FocusedItem property Legacy Windows Environment Features
- FocusedItem property Legacy Windows Environment Features , WebViewFolderContents object
- WebViewFolderContents object Legacy Windows Environment Features , FocusedItem property
topic_type:
- apiref
api_name:
- WebViewFolderContents.FocusedItem
api_location:
- Shell32.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# WebViewFolderContents.FocusedItem property

Gets a [**FolderItem**](../shell/folderitem.md) object that represents the item that has the input focus.

This property is read-only.

## Syntax


```JScript
objFocusedItem = WebViewFolderContents.FocusedItem
```



## Property value

A variable of type [IDispatch](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-idispatch) that receives the focused item object.

## Examples

The following example shows the proper usage of this property in JScript embedded in HTML.


```HTML
<html>
<head>

...

<script language="JavaScript">
    function fnWebViewFolderContentsFocusedItemJ()
    {
        var objFolderItem;

        objFolderItem = FileList.FocusedItem;
        if (objFolderItem != null)
        {
            alert(objFolderItem.Name);
        }
    }
</script>

</head>
<body>

...

<object id=FileList classid="clsid:1820FED0-473E-11D0-A96C-00C04FD705A2" tabIndex=1>
</body>
</html>
```



## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                           |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 4.71 or later)</dt> </dl> |



 

