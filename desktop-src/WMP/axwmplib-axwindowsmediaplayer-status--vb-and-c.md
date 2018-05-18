---
title: AxWindowsMediaPlayer.status property
description: The status property gets a value indicating the status of Windows Media Player.
ms.assetid: 'fefed54d-1fae-4599-8efc-eb2efdbd8ebd'
keywords: ["status property Windows Media Player", "status property Windows Media Player , AxWindowsMediaPlayer class", "AxWindowsMediaPlayer class Windows Media Player , status property"]
topic_type:
- apiref
api_name:
- AxWindowsMediaPlayer.status
api_location:
- AxInterop.WMPLib.dll
api_type:
- COM
---

# AxWindowsMediaPlayer.status property

The status property gets a value indicating the status of Windows Media Player.

This property is read-only.

## Syntax


```CSharp
public System.String status {get;}
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
<td><pre><code>Public ReadOnly Property status As System.String</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The System.String that is the status.

## Remarks

The values contained in this property are subject to change at any time, and should be used for display purposes only.

The AxWindowsMediaPlayer.**StatusChange** event is fired whenever this property changes value.

## Requirements



|                      |                                                                                                                            |
|----------------------|----------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                          |
| Namespace<br/> | **AxWMPLib**<br/>                                                                                                    |
| Assembly<br/>  | <dl> <dt>AxInterop.WMPLib.dll (AxInterop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**AxWindowsMediaPlayer Object (VB and C#)**](axwindowsmediaplayer-object--vb-and-c.md)
</dt> <dt>

[**AxWindowsMediaPlayer.StatusChange Event (VB and C#)**](axwmplib-axwindowsmediaplayer-statuschange.md)
</dt> </dl>

 

 





