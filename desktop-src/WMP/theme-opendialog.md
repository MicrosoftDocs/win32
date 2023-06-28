---
title: THEME.openDialog
description: The openDialog method opens a file dialog box.
ms.assetid: d7f4549c-a5c3-4902-b13b-51f3d4444ea9
keywords:
- THEME.openDialog Windows Media Player
topic_type:
- apiref
api_name:
- THEME.openDialog
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# THEME.openDialog

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **openDialog** method opens a file dialog box.

``` syntax
        theme.openDialog(dialogType, parameters)
```

## Parameters

<dl> <dt>

<span id="dialogType"></span><span id="dialogtype"></span><span id="DIALOGTYPE"></span>*dialogType*
</dt> <dd>

A **String** that specifies the type of dialog box. Must be set to "FILE\_OPEN".

</dd> <dt>

<span id="parameters"></span><span id="PARAMETERS"></span>*parameters*
</dt> <dd>

A **String** that can be used for additional information. Must be set to "FILES\_ALLMEDIA".

</dd> </dl>

## Return Value

This method returns a **String** containing the URL of the selected file or "" (empty string) if the user clicks cancel.

## Remarks

This method can be used for files on the local hard drives or on network drives.

## Examples


```JScript
<THEME>
  <VIEW id="View1" 
    backgroundImage="greenstone.bmp" 
    width=500 height=300 author="Microsoft Corp.">
    <BUTTON 
      id="Open" 
      image="Open.png" 
      onclick="jscript:
        player.URL = theme.openDialog('FILE_OPEN','FILES_ALLMEDIA')">
    </BUTTON>
  </VIEW>
</THEME>
```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**THEME Element**](theme-element.md)
</dt> </dl>

 

 





