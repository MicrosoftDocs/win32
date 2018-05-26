---
Description: Displays the default user interface for creating a favorite item. The user interface is initialized to the specified parameters.
title: ShellUIHelper.AddFavorite method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ShellUIHelper.AddFavorite method

Displays the default user interface for creating a favorite item. The user interface is initialized to the specified parameters.

## Syntax


```JScript
iRetVal = ShellUIHelper.AddFavorite(
  sURL,
  [ vTitle ]
)
```



## Parameters

<dl> <dt>

*sURL* \[in\]
</dt> <dd>

Type: **[**BSTR**](1b2d7d2c-47af-4389-a6b6-b01b7e915228)**

A **String** value that specifies the URL of the item to be added to the **Favorites** folder.

</dd> <dt>

*vTitle* \[in, optional\]
</dt> <dd>

Type: **Variant\***

A **Variant** value that specifies the name of the item.

</dd> </dl>

## Examples

The following example shows the proper usage of this method for JScript embedded in HTML and Visual Basic.

JScript:


```JScript
<html>
<head>
<title></title>

<object id="ShellUIHelper"
        classid="CLSID:64AB4BB7-111E-11d1-8F79-00C04FC2FBE1"
        width=0
        height=0
        VIEWASTEXT>
</object>

<script language="JavaScript">
    function fnShellUIHelperAddFavoriteJ()
    {
        ShellUIHelper.AddFavorite("http://www.msn.com", "MSN Home Page");
    }
</script>

</head>
<body onload=fnShellUIHelperAddFavoriteJ()>
</body>
</html>
```



Visual Basic:


```VB
Private Sub fnShellUIHelperAddFavoriteVB()
    Dim objShellUIHelper As ShellUIHelper
    
    Set objShellUIHelper = New ShellUIHelper
        objShellUIHelper.AddFavorite "http://www.msn.com", "MSN Home Page"
    Set objShellUIHelper = Nothing
End Sub
```



## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                           |
| Header<br/>                   | <dl> <dt>Exdisp.h</dt> </dl>                            |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 4.71 or later)</dt> </dl> |



 

 




