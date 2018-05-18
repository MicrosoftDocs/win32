---
Description: 'Sets the size and screen position of an appbar.'
ms.assetid: 'b3c56278-b9a2-4e08-bf98-7b3e4c8bd082'
title: 'ABM\_SETPOS message'
---

# ABM\_SETPOS message

Sets the size and screen position of an appbar. The message specifies a screen edge and the bounding rectangle for the appbar. The system may adjust the bounding rectangle so that the appbar does not interfere with the Windows taskbar or any other appbars.


```C++
SHAppBarMessage(ABM_SETPOS, pabd); 
```



## Parameters

<dl> <dt>

*pabd* 
</dt> <dd>

A pointer to an [**APPBARDATA**](appbardata.md) structure. The **uEdge** member specifies a screen edge, and the **rc** member contains the bounding rectangle. When the [**SHAppBarMessage**](shappbarmessage.md) function returns, **rc** contains the approved bounding rectangle. You must specify the **cbSize**, **hWnd**, **uEdge**, and **rc** members when sending this message; all other members are ignored.

</dd> </dl>

## Return value

Always returns **TRUE**.

## Remarks

This message causes the system to send the [**ABN\_POSCHANGED**](abn-poschanged.md) notification message to all appbars.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Shellapi.h</dt> </dl> |



 

 




