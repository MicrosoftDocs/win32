---
Description: Adds an item to the Microsoft Active Desktop.
title: ShellUIHelper.AddDesktopComponent method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ShellUIHelper.AddDesktopComponent method

Adds an item to the Microsoft Active Desktop.

## Syntax


```JScript
iRetVal = ShellUIHelper.AddDesktopComponent(
  sURL,
  sType,
  [ Left ],
  [ Top ],
  [ Width ],
  [ Height ]
)
```



## Parameters

<dl> <dt>

*sURL* \[in\]
</dt> <dd>

Type: **[**BSTR**](1b2d7d2c-47af-4389-a6b6-b01b7e915228)**

A **String** value that specifies the URL of the new favorite item.

</dd> <dt>

*sType* \[in\]
</dt> <dd>

Type: **[**BSTR**](1b2d7d2c-47af-4389-a6b6-b01b7e915228)**

A **String** value that specifies the type of item being added. This can be one of the following values.

<dt>



 (image)


</dt> <dd>

The component is an image.

</dd> <dt>



 (website)


</dt> <dd>

The component is a website.

</dd> </dl> </dd> <dt>

*Left* \[in, optional\]
</dt> <dd>

Type: **Variant**

The position of the left edge of the component, in screen coordinates.

</dd> <dt>

*Top* \[in, optional\]
</dt> <dd>

Type: **Variant**

The position of the top edge of the component, in screen coordinates.

</dd> <dt>

*Width* \[in, optional\]
</dt> <dd>

Type: **Variant**

The width of the component, in screen units.

</dd> <dt>

*Height* \[in, optional\]
</dt> <dd>

Type: **Variant**

The height of the component, in screen units.

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
    function fnShellUIHelperAddDesktopComponentJ()
    {
        ShellUIHelper.AddDesktopComponent("http://www.microsoft.com/", "website");
    }
</script>

</head>
<body onload=fnShellUIHelperAddDesktopComponentJ()>
</body>
</html>
```



Visual Basic:


```VB
Private Sub fnShellUIHelperAddDesktopComponentVB()
    Dim objShellUIHelper As ShellUIHelper
    
    Set objShellUIHelper = New ShellUIHelper
        objShellUIHelper.AddDesktopComponent "http://www.microsoft.com/", "website"
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



 

 




