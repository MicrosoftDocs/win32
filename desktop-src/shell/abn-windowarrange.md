---
description: Notifies an appbar that the user has selected the Cascade, Tile Horizontally, or Tile Vertically command from the taskbar's shortcut menu.
title: ABN_WINDOWARRANGE message (Shellapi.h)
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: 32eb7298-75ca-4ff8-86cf-7c9ca9d71868
api_name: 
 - ABN_WINDOWARRANGE
api_type: 
 - HeaderDef
api_location: 
 - Shellapi.h
topic_type: 
 - APIRef
 - kbSyntax

---

# ABN\_WINDOWARRANGE message

Notifies an appbar that the user has selected the Cascade, Tile Horizontally, or Tile Vertically command from the taskbar's shortcut menu.


```C++
ABN_WINDOWARRANGE 



    fBeginning = (BOOL) lParam; 
```



## Parameters

<dl> <dt>

*fBeginning* 
</dt> <dd>

A flag specifying whether the cascade or tile operation is beginning. This parameter is **TRUE** if the operation is beginning and the windows have not yet been moved. It is **FALSE** if the operation has completed.

</dd> </dl>

## Return value

No return value.

## Remarks

The system sends this notification message twice first with *lParam* set to **TRUE** and then with *lParam* set to **FALSE**. The first notification is sent before the windows are cascaded or tiled, and the second is sent after the cascade or tile operation has occurred.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Shellapi.h</dt> </dl> |



 

 




