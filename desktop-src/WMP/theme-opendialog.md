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
ms.date: 05/31/2018
api_location: 
---

# THEME.openDialog

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

 

 





