---
title: WebViewFolderContents.PopupItemMenu method
description: Creates a shortcut menu for the specified item and returns the selected command string.
ms.assetid: 3c07500c-2fe9-4976-a1a8-b128e75f9325
keywords:
- PopupItemMenu method Legacy Windows Environment Features
- PopupItemMenu method Legacy Windows Environment Features , WebViewFolderContents object
- WebViewFolderContents object Legacy Windows Environment Features , PopupItemMenu method
topic_type:
- apiref
api_name:
- WebViewFolderContents.PopupItemMenu
api_location:
- Shell32.dll
api_type:
- COM
ms.topic: article
ms.date: 05/31/2018
---

# WebViewFolderContents.PopupItemMenu method

Creates a shortcut menu for the specified item and returns the selected command string.

## Syntax


```JScript
retVal = WebViewFolderContents.PopupItemMenu(
  vItem,
  [ vx ],
  [ vy ]
)
```



## Parameters

<dl> <dt>

*vItem* \[in\]
</dt> <dd>

Type: **Variant**

The [**FolderItem**](https://msdn.microsoft.com/library/windows/desktop/bb787810) object for which the shortcut menu will be created.

</dd> <dt>

*vx* \[in, optional\]
</dt> <dd>

Type: **Variant**

The horizontal position of the menu, in screen coordinates.

</dd> <dt>

*vy* \[in, optional\]
</dt> <dd>

Type: **Variant**

The vertical position of the menu, in screen coordinates.

</dd> </dl>

## Return value

Type: **[BSTR](https://msdn.microsoft.com/en-US/library/ms221069.aspx)\***

When this method returns, contains the command string.

## Examples

The following example shows the proper use of **PopupItemMenu** for JScript embedded in HTML.


```HTML
<html>
<head>

...

<script language="JavaScript">
    function fnWebViewFolderContentsPopupItemMenuJ()
    {
        var objFolderItem;

        objFolderItem = FileList.FocusedItem;
        if (objFolderItem != null)
        {
            var szCommand;

            szCommand = FileList.PopupItemMenu(objFolderItem);
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



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                           |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 4.71 or later)</dt> </dl> |



 

 





