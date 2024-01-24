---
description: Unregisters an appbar by removing it from the system's internal list. The system no longer sends notification messages to the appbar or prevents other applications from using the screen area used by the appbar.
title: ABM_REMOVE message (Shellapi.h)
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: 3da73a52-3dbb-4133-a9bd-86540e1c4154
api_name: 
 - ABM_REMOVE
api_type: 
 - HeaderDef
api_location: 
 - Shellapi.h
topic_type: 
 - APIRef
 - kbSyntax

---

# ABM\_REMOVE message

Unregisters an appbar by removing it from the system's internal list. The system no longer sends notification messages to the appbar or prevents other applications from using the screen area used by the appbar.


```C++
                SHAppBarMessage(ABM_REMOVE, pabd); 
            
```



## Parameters

<dl> <dt>

*pabd* 
</dt> <dd>

A pointer to an [**APPBARDATA**](/windows/desktop/api/Shellapi/ns-shellapi-appbardata) structure that contains the handle to the appbar to unregister. You must specify the **cbSize** and **hWnd** members when sending this message; all other members are ignored.

</dd> </dl>

## Return value

Always returns **TRUE**.

## Remarks

This message causes the system to send the [**ABN\_POSCHANGED**](abn-poschanged.md) notification message to all appbars.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Shellapi.h</dt> </dl> |



 

 




