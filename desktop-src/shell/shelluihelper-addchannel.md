---
Description: Adds a new channel to the list of channels in the Windows Internet Explorer Favorites menu and to the Channel bar on the desktop.
title: ShellUIHelper.AddChannel method
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ShellUIHelper.AddChannel
api_type: 
- COM
api_location: 
- Shell32.dll
---

# ShellUIHelper.AddChannel method

Adds a new channel to the list of channels in the Windows Internet Explorer **Favorites** menu and to the **Channel** bar on the desktop.

> [!Note]  
> This method is no longer supported under Windows Vista. Under that operating system, it returns E\_NOTIMPL.

 

## Syntax


```JScript
iRetVal = ShellUIHelper.AddChannel(
  sURL
)
```



## Parameters

<dl> <dt>

*sURL* \[in\]
</dt> <dd>

Type: **[**BSTR**](https://msdn.microsoft.com/en-us/library/ms221069(v=VS.71).aspx)**

A **String** value that specifies the URL of the CDF file.

> [!Note]  
> The links in the CDF file must use HTTP, HTTPS, or FTP protocols. If the CDF file contains any other protocol, the addition of the channel fails and no dialog box appears.

 

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
    function fnShellUIHelperAddChannelJ()
    {
        ShellUIHelper.AddChannel("http://www.microsoft.com/windows/cdf/g_stock.cdf");
    }
</script>

</head>
<body onload=fnShellUIHelperAddChannelJ()>
</body>
</html>
```



Visual Basic:


```VB
Private Sub fnShellUIHelperAddChannelVB()
    Dim objShellUIHelper As ShellUIHelper
    
    Set objShellUIHelper = New ShellUIHelper
        objShellUIHelper.AddChannel ("http://www.microsoft.com/windows/cdf/g_stock.cdf")
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



 

 




