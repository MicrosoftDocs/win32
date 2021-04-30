---
description: Adds an item to the Microsoft Active Desktop.
title: ShellUIHelper.AddDesktopComponent method (Exdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ShellUIHelper.AddDesktopComponent
api_type: 
- COM
api_location: 
- Shell32.dll
ms.assetid: 41634a89-15b9-41c8-ba3f-4bf19b786f6f
api_name: 
 - ShellUIHelper.AddDesktopComponent
api_type: 
 - COM
api_location: 
 - Shell32.dll
topic_type: 
 - APIRef
 - kbSyntax

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

Type: **[**BSTR**](/previous-versions/windows/desktop/automat/bstr)**

A **String** value that specifies the URL of the new favorite item.

</dd> <dt>

*sType* \[in\]
</dt> <dd>

Type: **[**BSTR**](/previous-versions/windows/desktop/automat/bstr)**

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
        ShellUIHelper.AddDesktopComponent("https://www.microsoft.com/", "website");
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
        objShellUIHelper.AddDesktopComponent "https://www.microsoft.com/", "website"
    Set objShellUIHelper = Nothing
End Sub
```



## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                           |
| Header<br/>                   | <dl> <dt>Exdisp.h</dt> </dl>                            |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 4.71 or later)</dt> </dl> |



 

 
