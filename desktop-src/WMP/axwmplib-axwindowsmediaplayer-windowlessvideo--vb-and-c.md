---
title: AxWindowsMediaPlayer.windowlessVideo property
description: The windowlessVideo property gets or sets a value indicating whether the Windows Media Player control renders video in windowless mode.
ms.assetid: '70386aae-cd30-405d-90dd-9b3fa63dad17'
keywords: ["windowlessVideo property Windows Media Player", "windowlessVideo property Windows Media Player , AxWindowsMediaPlayer class", "AxWindowsMediaPlayer class Windows Media Player , windowlessVideo property"]
topic_type:
- apiref
api_name:
- AxWindowsMediaPlayer.windowlessVideo
api_location:
- AxInterop.WMPLib.dll
api_type:
- COM
---

# AxWindowsMediaPlayer.windowlessVideo property

The windowlessVideo property gets or sets a value indicating whether the Windows Media Player control renders video in windowless mode.

## Syntax


```CSharp
public System.Boolean windowlessVideo {get; set;}
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
<td><pre><code>Public Property windowlessVideo As System.Boolean</code></pre></td>
</tr>
</tbody>
</table>



## Property value

A System.Boolean value indicating whether the Windows Media Player control renders video in windowless mode. The default value is false.

## Remarks

By default, an embedded Windows Media Player control renders video in its own window within the client area. When **windowlessVideo** is set to true, the Windows Media Player object renders video directly in the client area, so you can apply special effects or layer the video with text.

In Windows Vista, rendering video in windowless mode can degrade performance.

Getting a value for this property is not supported for Netscape Navigator. Setting a value for this property in Netscape Navigator may yield unexpected results.

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

 

 





