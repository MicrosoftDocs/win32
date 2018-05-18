---
title: IWMPLibraryServices getCountByType method
description: The getCountByType method returns the count of available libraries of a specified type.
ms.assetid: '75f22e21-fbaf-45dc-b64f-1f687a3cf241'
keywords: ["getCountByType method Windows Media Player", "getCountByType method Windows Media Player , IWMPLibraryServices interface", "IWMPLibraryServices interface Windows Media Player , getCountByType method"]
topic_type:
- apiref
api_name:
- IWMPLibraryServices.getCountByType
api_location:
- Interop.WMPLib.dll
api_type:
- COM
---

# IWMPLibraryServices::getCountByType method

The **getCountByType** method returns the count of available libraries of a specified type.

## Syntax


```CSharp
public System.Int32 getCountByType(
  WMPLibraryType wmplt
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
<td><pre><code>Public Function getCountByType( _
  ByVal wmplt As WMPLibraryType _
) As System.Int32
Implements IWMPLibraryServices.getCountByType</code></pre></td>
</tr>
</tbody>
</table>



## Parameters

<dl> <dt>

*wmplt* \[in\]
</dt> <dd>

A value from the **WMPLib.WMPLibraryType** enumeration that specifies the type of library to count.

</dd> </dl>

## Return value

A **System.Int32** that is the library count.

## Requirements



|                      |                                                                                                                        |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 11.<br/>                                                                                    |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPLibraryServices Interface (VB and C#)**](iwmplibraryservices--vb-and-c.md)
</dt> <dt>

[**WMPLibraryType**](wmplibrarytype.md)
</dt> </dl>

 

 





