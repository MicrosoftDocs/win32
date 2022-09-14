---
title: WebViewFolderContents.ViewOptions property (Shldisp.h)
description: Gets a set of ShellFolderViewOptions flags that indicate the current options of the view.
ms.assetid: 96edb144-e532-4ab5-99ae-d945e211d744
keywords:
- ViewOptions property Legacy Windows Environment Features
- ViewOptions property Legacy Windows Environment Features , WebViewFolderContents object
- WebViewFolderContents object Legacy Windows Environment Features , ViewOptions property
topic_type:
- apiref
api_name:
- WebViewFolderContents.ViewOptions
api_location:
- Shell32.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# WebViewFolderContents.ViewOptions property

Gets a set of [**ShellFolderViewOptions**](/windows/desktop/api/shldisp/ne-shldisp-shellfolderviewoptions) flags that indicate the current options of the view.

This property is read-only.

## Syntax


```JScript
objViewOptions = WebViewFolderContents.ViewOptions
```



## Property value

A variable of type [IDispatch](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-idispatch) that receives the view options object.

## Examples

The following example shows the proper usage of this property in JScript embedded in HTML.


```HTML
<html>
<head>

...

<script language="JavaScript">
    function fnWebViewFolderContentsViewOptionsJ()
    {
        var nViewOptions;

        nViewOptions = FileList.ViewOptions;
        if (nViewOptions != "")
        {
            alert(nViewOptions);
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



 

