---
Description: 'Sent to all windows after the user has logged on or off. When the user logs on or off, the system updates the user-specific settings. The system sends this message immediately after updating the settings.'
title: 'WM\_USERCHANGED message'
---

# WM\_USERCHANGED message

Sent to all windows after the user has logged on or off. When the user logs on or off, the system updates the user-specific settings. The system sends this message immediately after updating the settings.

A window receives this message through its [**WindowProc**](windowproc.md) function.

> [!Note]  
> This message is not supported as of Windows Vista.

 


```C++
#define WM_USERCHANGED                  0x0054
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

Type: **LRESULT**

An application should return zero if it processes this message.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | None supported<br/>                                                                                |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[Windows Overview](windows.md)
</dt> </dl>

 

 




