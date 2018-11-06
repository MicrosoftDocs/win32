---
title: IWMPPlaylist name property
description: The name property gets or sets the name of the playlist.
ms.assetid: abf25a49-5e07-43e6-ab45-6bc09c952c45
keywords:
- name property Windows Media Player
- name property Windows Media Player , IWMPPlaylist interface
- IWMPPlaylist interface Windows Media Player , name property
topic_type:
- apiref
api_name:
- IWMPPlaylist.name
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: article
ms.date: 05/31/2018
---

# IWMPPlaylist::name property

The **name** property gets or sets the name of the playlist.

## Syntax


```CSharp
public System.String name {get; set;}
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
<td><pre><code>Public Property name As System.String</code></pre></td>
</tr>
</tbody>
</table>



## Property value

A **System.String** that is the name of the playlist.

## Remarks

Before using this property, you must have read access to the library. For more information, see [Library Access](library-access.md).

## Requirements



|                      |                                                                                                                        |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                      |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPPlaylist Interface (VB and C#)**](iwmpplaylist--vb-and-c.md)
</dt> <dt>

[**IWMPSettings2.mediaAccessRights (VB and C#)**](wmplibiwmpsettings2-iwmpsettings2-mediaaccessrights--vb-and-c.md)
</dt> <dt>

[**IWMPSettings2.requestMediaAccessRights (VB and C#)**](wmplibiwmpsettings2-iwmpsettings2-requestmediaaccessrights--vb-and-c.md)
</dt> </dl>

 

 





