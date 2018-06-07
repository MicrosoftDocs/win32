---
title: AxWindowsMediaPlayer.enableContextMenu property
description: The enableContextMenu property gets or sets a value indicating whether to enable the context menu, which appears when the right mouse button is clicked.
ms.assetid: 6096cab7-c1fa-4b71-804b-e84facab2229
keywords:
- enableContextMenu property Windows Media Player
- enableContextMenu property Windows Media Player , AxWindowsMediaPlayer class
- AxWindowsMediaPlayer class Windows Media Player , enableContextMenu property
topic_type:
- apiref
api_name:
- AxWindowsMediaPlayer.enableContextMenu
api_location:
- AxInterop.WMPLib.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AxWindowsMediaPlayer.enableContextMenu property

The enableContextMenu property gets or sets a value indicating whether to enable the context menu, which appears when the right mouse button is clicked.

## Syntax


```CSharp
public System.Boolean enableContextMenu {get; set;}
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
<td><pre><code>Public Property enableContextMenu As System.Boolean</code></pre></td>
</tr>
</tbody>
</table>



## Property value

A System.Boolean value that indicates whether to enable the context menu. The default value is true.

## Remarks

During full-screen playback, Windows Media Player hides the mouse cursor when **enableContextMenu** equals false and **uiMode** equals "none".

## Requirements



|                      |                                                                                                                            |
|----------------------|----------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                          |
| Namespace<br/> | **AxWMPLib**<br/>                                                                                                    |
| Assembly<br/>  | <dl> <dt>AxInterop.WMPLib.dll (AxInterop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**AxWindowsMediaPlayer Object (VB and C#)**](axwindowsmediaplayer-object--vb-and-c.md)
</dt> </dl>

 

 





