---
title: AxWindowsMediaPlayer.openState property
description: The openState property gets an enumeration value indicating the state of the content source.
ms.assetid: '7a76814a-649f-4516-a92a-5f536fb1b147'
keywords: ["openState property Windows Media Player", "openState property Windows Media Player , AxWindowsMediaPlayer class", "AxWindowsMediaPlayer class Windows Media Player , openState property"]
topic_type:
- apiref
api_name:
- AxWindowsMediaPlayer.openState
api_location:
- AxInterop.WMPLib.dll
api_type:
- COM
---

# AxWindowsMediaPlayer.openState property

The openState property gets an enumeration value indicating the state of the content source.

This property is read-only.

## Syntax


```CSharp
public WMPOpenState openState {get;}
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
<td><pre><code>Public ReadOnly Property openState As WMPOpenState</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The WMPLib.WMPOpenState enumeration value.

## Remarks

Windows Media Player states are not guaranteed to occur in any particular order. Furthermore, not every state necessarily occurs during a sequence of events. You should not write code that relies upon state order.

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

[**AxWindowsMediaPlayer.OpenStateChange Event**](axwmplib-axwindowsmediaplayer-openstatechange.md)
</dt> <dt>

[**WMPLib.WMPOpenState**](wmpopenstate.md)
</dt> </dl>

 

 





