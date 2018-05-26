---
title: AxWindowsMediaPlayer.stretchToFit property
description: The stretchToFit property gets or sets a value indicating whether video displayed by the Windows Media Player control automatically sizes to fit the video window, when the video window is larger than the dimensions of the video image.
ms.assetid: 02e2bcba-4975-4ddd-996b-9bd40774ebc1
keywords:
- stretchToFit property Windows Media Player
- stretchToFit property Windows Media Player , AxWindowsMediaPlayer class
- AxWindowsMediaPlayer class Windows Media Player , stretchToFit property
topic_type:
- apiref
api_name:
- AxWindowsMediaPlayer.stretchToFit
api_location:
- AxInterop.WMPLib.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# AxWindowsMediaPlayer.stretchToFit property

The stretchToFit property gets or sets a value indicating whether video displayed by the Windows Media Player control automatically sizes to fit the video window, when the video window is larger than the dimensions of the video image.

## Syntax


```CSharp
public System.Boolean stretchToFit {get; set;}
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
<td><pre><code>Public Property stretchToFit As System.Boolean</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The System.Boolean value that indicates whether the video will stretch to fit the window. The default value is false.

## Remarks

When **stretchToFit** is set to true, the Windows Media Player control maintains the original aspect ratio of the video. If the aspect ratio of the video does not match the aspect ratio of the video window, black mask areas may appear on either the top and the bottom, or left and right, of the video image.

This property applies to the Windows Media Player control only when it is embedded in a webpage.

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

 

 





