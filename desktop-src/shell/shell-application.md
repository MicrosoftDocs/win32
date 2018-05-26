---
Description: Contains the objects Application object.
ms.assetid: 5335f4dd-ca80-49c8-8953-e32a6e6308e0
title: Shell.Application property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Shell.Application property

Contains the object's Application object.

This property is read-only.

## Syntax


```JScript
objApplication = Shell.Application
```

<span codelanguage="VisualBasic"></span>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>VB</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>Property Application As Object</code></pre></td>
</tr>
</tbody>
</table>



## Property value

A variable of type [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) that receives the Application object.

## Remarks

The **Application** property returns the automation object supported by the application that contains the WebBrowser control, if that object is accessible. Otherwise, this property returns the WebBrowser control's automation object.

Use this property with the **Set** and **CreateObject** commands or with the **GetObject** command to create and manipulate an instance of the Windows Internet Explorer application.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                           |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 4.71 or later)</dt> </dl> |



 

 




