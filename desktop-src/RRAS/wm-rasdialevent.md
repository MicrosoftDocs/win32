---
title: WM_RASDIALEVENT message (Ras.h)
description: The operating system sends a WM\_RASDIALEVENT message to a window procedure when a change of state event occurs during a RAS connection process.
ms.assetid: 4526da20-04e7-47b2-b576-8dc36c08b053
keywords:
- WM_RASDIALEVENT message RAS
topic_type:
- apiref
api_name:
- WM_RASDIALEVENT
api_location:
- Ras.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_RASDIALEVENT message

The operating system sends a **WM\_RASDIALEVENT** message to a window procedure when a change of state event occurs during a RAS connection process. This happens when a window has been specified to handle notifications of such events by using the *notifier* parameter of [**RasDial**](/windows/desktop/api/Ras/nf-ras-rasdiala).

The two message parameters are equivalent to the parameters of the same names that are used with [**RasDialFunc**](/windows/desktop/api/Ras/nc-ras-rasdialfunc) and [**RasDialFunc1**](/windows/desktop/api/Ras/nc-ras-rasdialfunc1) callback functions.


```C++
WM_RASDIALEVENT 
rasconnstate = (RASCONNSTATE) wParam; 
dwError = (DWORD) lParam;
            
```



## Parameters

<dl> <dt>

*rasconnstate* 
</dt> <dd>

Value of *wParam*. Equivalent to the *rasconnstate* parameter of the [**RasDialFunc**](/windows/desktop/api/Ras/nc-ras-rasdialfunc) and [**RasDialFunc1**](/windows/desktop/api/Ras/nc-ras-rasdialfunc1) callback functions. Specifies a [**RASCONNSTATE**](/previous-versions/windows/desktop/legacy/aa376727(v=vs.85)) enumerator value that indicates the state the RasDial remote access connection process is about to enter.

</dd> <dt>

*dwError* 
</dt> <dd>

Value of *lParam*. Equivalent to the *dwError* parameter of the [**RasDialFunc**](/windows/desktop/api/Ras/nc-ras-rasdialfunc) and [**RasDialFunc1**](/windows/desktop/api/Ras/nc-ras-rasdialfunc1) callback functions. A nonzero value indicates the error that has occurred, or zero if no error has occurred.

[**RasDial**](/windows/desktop/api/Ras/nf-ras-rasdiala) sends this message with *dwError* set to zero upon entry to each connection state. If an error occurs within a state, the message is sent again for the state, this time with a nonzero *dwError* value.

</dd> </dl>

## Return value

If an application processes this message, it should return **TRUE**.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Ras.h</dt> </dl> |



## See also

<dl> <dt>

[Remote Access Service (RAS) Overview](about-remote-access-service.md)
</dt> <dt>

[Remote Access Service Messages](remote-access-service-messages.md)
</dt> <dt>

[**RasDial**](/windows/desktop/api/Ras/nf-ras-rasdiala)
</dt> <dt>

[**RasDialFunc**](/windows/desktop/api/Ras/nc-ras-rasdialfunc)
</dt> <dt>

[**RasDialFunc1**](/windows/desktop/api/Ras/nc-ras-rasdialfunc1)
</dt> <dt>

[**RASCONNSTATE**](/previous-versions/windows/desktop/legacy/aa376727(v=vs.85))
</dt> </dl>

 

