---
description: Indicates whether a specified URL is subscribed to.
title: ShellUIHelper.IsSubscribed method (Exdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ShellUIHelper.IsSubscribed
api_type: 
- COM
api_location: 
- Shell32.dll
ms.assetid: fcf23352-6603-4b17-9c3b-b353cca1c003
api_name: 
 - ShellUIHelper.IsSubscribed
api_type: 
 - COM
api_location: 
 - Shell32.dll
topic_type: 
 - APIRef
 - kbSyntax

---

# ShellUIHelper.IsSubscribed method

Indicates whether a specified URL is subscribed to.

## Syntax


```JScript
bRetVal = ShellUIHelper.IsSubscribed(
  sURL
)
```



## Parameters

<dl> <dt>

*sURL* \[in\]
</dt> <dd>

Type: **[**BSTR**](/previous-versions/windows/desktop/automat/bstr)**

A **String** value that specifies the URL.

</dd> </dl>

## Return value

Type: **Boolean\***

**true** if the URL is subscribed to; otherwise, **false**.

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
    function fnShellUIHelperIsSubscribedJ()
    {
        var bReturn;
        
        bReturn = ShellUIHelper.IsSubscribed("https://www.microsoft.com/");
        alert(bReturn);
    }
</script>

</head>
<body onload=fnShellUIHelperIsSubscribedJ()>
</body>
</html>
```



Visual Basic:


```VB
Private Sub fnShellUIHelperIsSubscribedVB()
    Dim objShellUIHelper As ShellUIHelper
    Dim bReturn          As Boolean
    
    Set objShellUIHelper = New ShellUIHelper
        bReturn = objShellUIHelper.IsSubscribed("https://www.microsoft.com/")
        Debug.Print bReturn
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



 

 
