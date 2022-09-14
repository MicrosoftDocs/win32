---
title: WebViewFolderContents.SelectedItems method (Shldisp.h)
description: WebViewFolderContents.SelectedItems method - Gets a FolderItems object that represents all of the selected items in the view.
ms.assetid: 683acac4-f157-4a75-a3f8-c693887c1ea5
keywords:
- SelectedItems method Legacy Windows Environment Features
- SelectedItems method Legacy Windows Environment Features , WebViewFolderContents object
- WebViewFolderContents object Legacy Windows Environment Features , SelectedItems method
topic_type:
- apiref
api_name:
- WebViewFolderContents.SelectedItems
api_location:
- Shell32.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# WebViewFolderContents.SelectedItems method

Gets a [**FolderItems**](../shell/folderitems.md) object that represents all of the selected items in the view.

## Syntax


```JScript
retVal = WebViewFolderContents.SelectedItems()
```



## Parameters

This method has no parameters.

## Return value

Type: **[**FolderItems**](../shell/folderitems.md)\*\***

An object reference to the [**FolderItems**](../shell/folderitems.md) object.

## Examples

The following example shows the proper usage of this method for JScript embedded in HTML.


```HTML
<html>
<head>

...

<script language="JavaScript">
    function fnWebViewFolderContentsSelectedItemsJ()
    {
        var objFolderItems;

        objFolderItems = FileList.SelectedItems();
        if (objFolderItems != null)
        {
            alert(objFolderItems.Count);
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



 

