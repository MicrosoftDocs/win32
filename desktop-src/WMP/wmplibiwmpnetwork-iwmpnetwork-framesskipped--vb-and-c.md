---
title: IWMPNetwork framesSkipped property
description: The framesSkipped property gets the total number of frames skipped during playback.
ms.assetid: eedecfa9-0c82-4800-979e-ca85fb78c480
keywords:
- framesSkipped property Windows Media Player
- framesSkipped property Windows Media Player , IWMPNetwork interface
- IWMPNetwork interface Windows Media Player , framesSkipped property
topic_type:
- apiref
api_name:
- IWMPNetwork.framesSkipped
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IWMPNetwork::framesSkipped property

The **framesSkipped** property gets the total number of frames skipped during playback.

## Syntax


```CSharp
public System.Int32 framesSkipped {get; set;}
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
<td><pre><code>Public ReadOnly Property framesSkipped As System.Int32</code></pre></td>
</tr>
</tbody>
</table>



## Property value

A **System.Int32** that is the number of frames skipped.

## Examples

The following code example uses **framesSkipped** to display the total number of frames skipped during playback. The information is displayed in a label when the user clicks a button. The **AxWMPLib.AxWindowsMediaPlayer** object is represented by the variable named player.


```CSharp
private void showFramesSkipped_Click(object sender, System.EventArgs e)
{
    framesSkippedLabel.Text = ("Frames skipped: " + player.network.framesSkipped.ToString());
}
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
<td><pre><code>Public Sub showFramesSkipped_Click(ByVal sender As Object, ByVal e As System.EventArgs) Handles showFramesSkipped.Click

    framesSkippedLabel.Text = (&quot;Frames skipped: &quot; + player.network.framesSkipped.ToString())

End Sub</code></pre></td>
</tr>
</tbody>
</table>



## Requirements



|                      |                                                                                                                        |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                      |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPNetwork Interface (VB and C#)**](iwmpnetwork--vb-and-c.md)
</dt> </dl>

 

 





