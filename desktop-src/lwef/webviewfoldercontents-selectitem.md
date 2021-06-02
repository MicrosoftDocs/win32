---
title: WebViewFolderContents.SelectItem method (Shldisp.h)
description: WebViewFolderContents.SelectItem method - Sets the selection state of an item in the view.
ms.assetid: c0e163ee-1951-476c-807a-781e26766d99
keywords:
- SelectItem method Legacy Windows Environment Features
- SelectItem method Legacy Windows Environment Features , WebViewFolderContents object
- WebViewFolderContents object Legacy Windows Environment Features , SelectItem method
topic_type:
- apiref
api_name:
- WebViewFolderContents.SelectItem
api_location:
- Shell32.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# WebViewFolderContents.SelectItem method

Sets the selection state of an item in the view.

## Syntax


```JScript
WebViewFolderContents.SelectItem(
  vItem,
  dwFlags
)
```



## Parameters

<dl> <dt>

*vItem* \[in\]
</dt> <dd>

Type: **Variant\***

The [**FolderItem**](../shell/folderitem.md) object for which the selection state will be set.

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

## Examples

The following example shows the proper usage of this method for JScript embedded in HTML.


```HTML
<html>
<head>

...

<script language="JavaScript">
    function fnWebViewFolderContentsSelectItemJ()
    {
        var objFolderItem;

        objFolderItem = FileList.FocusedItem;
        if (objFolderItem != null)
        {
            FileList.SelectItem(objFolderItem, 1);
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



 

