---
title: IWMPLibrary isIdentical method
description: The isIdentical method returns a value that indicates whether the supplied object is the same as the current one.
ms.assetid: c4eebc46-6a5f-4f9a-8cd4-7421b156670c
keywords:
- isIdentical method Windows Media Player
- isIdentical method Windows Media Player , IWMPLibrary interface
- IWMPLibrary interface Windows Media Player , isIdentical method
topic_type:
- apiref
api_name:
- IWMPLibrary.isIdentical
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IWMPLibrary::isIdentical method

The **isIdentical** method returns a value that indicates whether the supplied object is the same as the current one.

## Syntax


```CSharp
public System.Boolean isIdentical(
  IWMPLibrary pIWMPLibrary
);
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
<td><pre><code>Public Function isIdentical( _
  ByVal pIWMPLibrary As IWMPLibrary _
) As System.Boolean
Implements IWMPLibrary.isIdentical</code></pre></td>
</tr>
</tbody>
</table>



## Parameters

<dl> <dt>

*pIWMPLibrary* \[in\]
</dt> <dd>

A **WMPLib.IWMPLibrary** interface that represents the object to compare with current one.

</dd> </dl>

## Return value

A **System.Boolean** that is the result of the comparison. The value **true** indicates that the objects are the same.

## Requirements



|                      |                                                                                                                        |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 11.<br/>                                                                                    |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPLibrary Interface (VB and C#)**](iwmplibrary--vb-and-c.md)
</dt> </dl>

 

 





