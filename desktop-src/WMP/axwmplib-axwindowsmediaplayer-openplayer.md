---
title: AxWindowsMediaPlayer.openPlayer method
description: The openPlayer method opens Windows Media Player using the specified URL. | AxWindowsMediaPlayer.openPlayer method
ms.assetid: 9a9d8200-f427-42ff-b49f-d973cf86014f
keywords:
- openPlayer method Windows Media Player
- openPlayer method Windows Media Player , AxWindowsMediaPlayer class
- AxWindowsMediaPlayer class Windows Media Player , openPlayer method
topic_type:
- apiref
api_name:
- AxWindowsMediaPlayer.openPlayer
api_location:
- AxInterop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# AxWindowsMediaPlayer.openPlayer method

The **openPlayer** method opens Windows Media Player using the specified URL.

## Syntax


```CSharp
public void openPlayer(
  System.String bstrURL
);
```


```VB

Public Sub openPlayer( _
  ByVal bstrURL As System.String _
)
```





## Parameters

<dl> <dt>

*bstrURL* 
</dt> <dd>

The **System.String** that is the URL of the media item to play.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

This method launches Windows Media Player with the specified URL set as the current media item. If the Player was previously closed in skin mode it will open using the skin last chosen by the user. Otherwise, the Player opens in full mode.

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

 

 





