---
title: IWMPErrorItem2 condition property
description: The condition property gets a value indicating the condition for the error.
ms.assetid: 68800d75-8341-40d1-b699-ffe27bb1f38a
keywords:
- condition property Windows Media Player
- condition property Windows Media Player , IWMPErrorItem2 interface
- IWMPErrorItem2 interface Windows Media Player , condition property
topic_type:
- apiref
api_name:
- IWMPErrorItem2.condition
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

# IWMPErrorItem2::condition property

The **condition** property gets a value indicating the condition for the error.

## Syntax


```CSharp
public System.Int32 condition {get; set;}
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
<td><pre><code>Public ReadOnly Property condition As System.Int32</code></pre></td>
</tr>
</tbody>
</table>



## Property value

A **System.Int32** that is the condition code.

## Remarks

The condition code is a value that is used by Microsoft to provide additional information for technical support personnel.

## Requirements



|                      |                                                                                                                        |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                      |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPErrorItem2 Interface (VB and C#)**](iwmperroritem2--vb-and-c.md)
</dt> </dl>

 

 





