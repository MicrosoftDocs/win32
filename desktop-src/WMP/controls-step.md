---
title: Controls.step method
description: The step method causes the current video media item to freeze playback on the next frame or the previous frame.
ms.assetid: f717c583-4073-45a9-b05d-7134d02724a4
keywords:
- step method Windows Media Player
- step method Windows Media Player , Controls class
- Controls class Windows Media Player , step method
topic_type:
- apiref
api_name:
- Controls.step
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Controls.step method

The **step** method causes the current video media item to freeze playback on the next frame or the previous frame.

## Syntax


```JScript
Controls.step(
  frameCount
)
```



## Parameters

<dl> <dt>

*frameCount* \[in\]
</dt> <dd>

**Number** (**long**) indicating how many frames to step before freezing. Must currently be set to 1 or -1.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

This method currently only supports the parameters 1 or -1, so you can only step one frame at a time.

**Windows Media Player 10 Mobile:** This method is not supported.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player for Windows XP or later.<br/>                           |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Controls Object**](controls-object.md)
</dt> <dt>

[**DVD Object**](dvd-object.md)
</dt> </dl>

 

 





