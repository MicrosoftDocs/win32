---
title: MCIWNDM_PLAYTO message (Vfw.h)
description: The MCIWNDM\_PLAYTO message plays the content of an MCI device from the current position to the specified ending location or until another command stops playback.
ms.assetid: ed940ee7-7b96-47da-99d3-6697f8a2e3d5
keywords:
- MCIWNDM_PLAYTO message Windows Multimedia
topic_type:
- apiref
api_name:
- MCIWNDM_PLAYTO
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCIWNDM\_PLAYTO message

The **MCIWNDM\_PLAYTO** message plays the content of an MCI device from the current position to the specified ending location or until another command stops playback. If the specified ending location is beyond the end of the content, playback stops at the end of the content. You can send this message explicitly or by using the [**MCIWndPlayTo**](/windows/desktop/api/Vfw/nf-vfw-mciwndplayto) macro.


```C++
MCIWNDM_PLAYTO 
wParam = 0; 
lParam = (LPARAM) (LONG) lEnd; 
```



## Parameters

<dl> <dt>

<span id="lEnd"></span><span id="lend"></span><span id="LEND"></span>*lEnd*
</dt> <dd>

Ending location. The units for the ending location depend on the current time format.

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Remarks

This macro is defined using the [**MCIWndSeek**](/windows/desktop/api/Vfw/nf-vfw-mciwndseek) and [**MCIWndPlayTo**](/windows/desktop/api/Vfw/nf-vfw-mciwndplayto) macros, which in turn use the [MCI\_SEEK](mci-seek.md) command and the **MCIWNDM\_PLAYTO** message.

You can also specify both a starting and ending location for playback by using the [**MCIWndPlayFromTo**](/windows/desktop/api/Vfw/nf-vfw-mciwndplayfromto) macro.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



## See also

<dl> <dt>

[MCI\_SEEK](mci-seek.md)
</dt> <dt>

[**MCIWndPlayFromTo**](/windows/desktop/api/Vfw/nf-vfw-mciwndplayfromto)
</dt> <dt>

[**MCIWndPlayTo**](/windows/desktop/api/Vfw/nf-vfw-mciwndplayto)
</dt> <dt>

[**MCIWndSeek**](/windows/desktop/api/Vfw/nf-vfw-mciwndseek)
</dt> </dl>

 

 





