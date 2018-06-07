---
title: IWMPDVD back method
description: The back method changes the display from a submenu to its parent menu.
ms.assetid: 81d033d4-f570-44a5-898a-e419101c04fa
keywords:
- back method Windows Media Player
- back method Windows Media Player , IWMPDVD interface
- IWMPDVD interface Windows Media Player , back method
topic_type:
- apiref
api_name:
- IWMPDVD.back
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IWMPDVD::back method

The **back** method changes the display from a submenu to its parent menu.

## Syntax


```CSharp
public void back();
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
<td><pre><code>Public Sub back()
Implements IWMPDVD.back</code></pre></td>
</tr>
</tbody>
</table>



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

Every DVD is authored differently. Some DVDs are authored so that the `back` method is available from the root menu, but when invoked, it will do nothing.

## Requirements



|                      |                                                                                                                        |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                      |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPDVD Interface (VB and C#)**](iwmpdvd--vb-and-c.md)
</dt> </dl>

 

 





