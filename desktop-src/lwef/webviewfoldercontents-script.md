---
title: WebViewFolderContents.Script property (Shldisp.h)
description: Gets the scripting object for the view.
ms.assetid: f65246c5-3cd6-43bd-b267-ad27bdd0b41e
keywords:
- Script property Legacy Windows Environment Features
- Script property Legacy Windows Environment Features , WebViewFolderContents object
- WebViewFolderContents object Legacy Windows Environment Features , Script property
topic_type:
- apiref
api_name:
- WebViewFolderContents.Script
api_location:
- Shell32.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# WebViewFolderContents.Script property

Gets the scripting object for the view.

This property is read-only.

## Syntax


```JScript
objScript = WebViewFolderContents.Script
```



## Property value

A variable of type [IDispatch](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-idispatch) that receives the scripting object.

## Examples

The following example shows the proper usage of this property in JScript embedded in HTML.


```HTML
<html>
<head>

...

<script language="JavaScript">
    function fnWebViewFolderContentsScriptJ()
    {
        var objScript;

        objScript = FileList.Script;
        if (objScript != null)
        {
            alert(objScript.Name);
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



 

