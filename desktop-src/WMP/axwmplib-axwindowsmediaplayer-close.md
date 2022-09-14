---
title: AxWindowsMediaPlayer.close method
description: The close method closes the current digital media file, stops playback in Windows Media Player and releases Windows Media Player resources.
ms.assetid: 3e555086-c31c-42d7-b671-0fd824f66641
keywords:
- close method Windows Media Player
- close method Windows Media Player , AxWindowsMediaPlayer class
- AxWindowsMediaPlayer class Windows Media Player , close method
topic_type:
- apiref
api_name:
- AxWindowsMediaPlayer.close
api_location:
- AxInterop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# AxWindowsMediaPlayer.close method

The close method closes the current digital media file, stops playback in Windows Media Player and releases Windows Media Player resources.

## Syntax


```CSharp
public void close();
```


```VB

Public Sub close()
```





## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

This method closes the current digital media file, not Windows Media Player itself.

## Examples

The following example creates a button that, when clicked, stops playback in Windows Media Player and releases the resources in use. The AxWMPLib.AxWindowsMediaPlayer object is represented by the variable named player.


```CSharp
private void closeIt_Click(object sender, System.EventArgs e)
{
    // Close the Player. 
    player.close();
}
```


```VB

Public Sub closeIt_Click(ByVal sender As Object, ByVal e As System.EventArgs) Handles closeIt.Click

    &#39; Close the Player. 
    player.close()

End Sub
```





## Requirements



| Requirement | Value |
|----------------------|----------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                          |
| Namespace<br/> | **AxWMPLib**<br/>                                                                                                    |
| Assembly<br/>  | <dl> <dt>AxInterop.WMPLib.dll (AxInterop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**AxWindowsMediaPlayer Object (VB and C#)**](axwindowsmediaplayer-object--vb-and-c.md)
</dt> </dl>

 

 





