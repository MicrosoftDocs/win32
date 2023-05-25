---
title: MCIWnd Reference
description: MCIWnd Reference
ms.assetid: 11fba6bb-17f1-4fbe-b148-4755a3c6216a
keywords:
- MCI (Media Control Interface),MCIWnd reference
- MCIWnd window class,reference
- MCIWnd window,reference
- MCIWnd reference,about
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# MCIWnd Reference

\[The feature associated with this page, [MCIWnd Window Class](/windows/win32/multimedia/mciwnd-window-class), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **MCIWnd Window Class**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This section describes the functions, messages, and macros associated with the MCIWnd window class. These elements are grouped as follows.

## Window Management

-   [**MCIWndChangeStyles**](/windows/desktop/api/Vfw/nf-vfw-mciwndchangestyles)
-   [**MCIWndCreate**](/windows/desktop/api/Vfw/nf-vfw-mciwndcreatea)
-   [**MCIWndGetStyles**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetstyles)
-   [**MCIWndRegisterClass**](/windows/desktop/api/Vfw/nf-vfw-mciwndregisterclass)

## File and Device Management

-   [**MCIWndClose**](/windows/desktop/api/Vfw/nf-vfw-mciwndclose)
-   [**MCIWndDestroy**](/windows/desktop/api/Vfw/nf-vfw-mciwnddestroy)
-   [**MCIWndEject**](/windows/desktop/api/Vfw/nf-vfw-mciwndeject)
-   [**MCIWndNew**](/windows/desktop/api/Vfw/nf-vfw-mciwndnew)
-   [**MCIWndOpen**](/windows/desktop/api/Vfw/nf-vfw-mciwndopen)
-   [**MCIWndOpenDialog**](/windows/desktop/api/Vfw/nf-vfw-mciwndopendialog)
-   [**MCIWndSave**](/windows/desktop/api/Vfw/nf-vfw-mciwndsave)
-   [**MCIWndSaveDialog**](/windows/desktop/api/Vfw/nf-vfw-mciwndsavedialog)

## Playback Options

-   [**MCIWndGetRepeat**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetrepeat)
-   [**MCIWndPlay**](/windows/desktop/api/Vfw/nf-vfw-mciwndplay)
-   [**MCIWndPlayFrom**](/windows/desktop/api/Vfw/nf-vfw-mciwndplayfrom)
-   [**MCIWndPlayFromTo**](/windows/desktop/api/Vfw/nf-vfw-mciwndplayfromto)
-   [**MCIWndPlayReverse**](/windows/desktop/api/Vfw/nf-vfw-mciwndplayreverse)
-   [**MCIWndPlayTo**](/windows/desktop/api/Vfw/nf-vfw-mciwndplayto)
-   [**MCIWndSetRepeat**](/windows/desktop/api/Vfw/nf-vfw-mciwndsetrepeat)

## Recording

-   [**MCIWndRecord**](/windows/desktop/api/Vfw/nf-vfw-mciwndrecord)

## Positioning

-   [**MCIWndEnd**](/windows/desktop/api/Vfw/nf-vfw-mciwndend)
-   [**MCIWndGetEnd**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetend)
-   [**MCIWndGetLength**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetlength)
-   [**MCIWndGetPosition**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetposition)
-   [**MCIWndGetPositionString**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetpositionstring)
-   [**MCIWndGetStart**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetstart)
-   [**MCIWndHome**](/windows/desktop/api/Vfw/nf-vfw-mciwndhome)
-   [**MCIWndSeek**](/windows/desktop/api/Vfw/nf-vfw-mciwndseek)
-   [**MCIWndStep**](/windows/desktop/api/Vfw/nf-vfw-mciwndstep)

## Pause and Resume Playback

-   [**MCIWndGetRepeat**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetrepeat)
-   [**MCIWndPlay**](/windows/desktop/api/Vfw/nf-vfw-mciwndplay)
-   [**MCIWndPlayFrom**](/windows/desktop/api/Vfw/nf-vfw-mciwndplayfrom)
-   [**MCIWndPlayFromTo**](/windows/desktop/api/Vfw/nf-vfw-mciwndplayfromto)
-   [**MCIWndPlayReverse**](/windows/desktop/api/Vfw/nf-vfw-mciwndplayreverse)
-   [**MCIWndPlayTo**](/windows/desktop/api/Vfw/nf-vfw-mciwndplayto)
-   [**MCIWndSetRepeat**](/windows/desktop/api/Vfw/nf-vfw-mciwndsetrepeat)

## Performance Tuning

-   [**MCIWndGetSpeed**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetspeed)
-   [**MCIWndGetVolume**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetvolume)
-   [**MCIWndGetZoom**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetzoom)
-   [**MCIWndSetSpeed**](/windows/desktop/api/Vfw/nf-vfw-mciwndsetspeed)
-   [**MCIWndSetVolume**](/windows/desktop/api/Vfw/nf-vfw-mciwndsetvolume)
-   [**MCIWndSetZoom**](/windows/desktop/api/Vfw/nf-vfw-mciwndsetzoom)

## Image and Palette Adjustments

-   [**MCIWndGetDest**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetdest)
-   [**MCIWndGetPalette**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetpalette)
-   [**MCIWndGetSource**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetsource)
-   [**MCIWndPutDest**](/windows/desktop/api/Vfw/nf-vfw-mciwndputdest)
-   [**MCIWndPutSource**](/windows/desktop/api/Vfw/nf-vfw-mciwndputsource)
-   [**MCIWndRealize**](/windows/desktop/api/Vfw/nf-vfw-mciwndrealize)
-   [**MCIWndSetPalette**](/windows/desktop/api/Vfw/nf-vfw-mciwndsetpalette)

## Event and Error Notification

-   [**MCIWndGetError**](/windows/desktop/api/Vfw/nf-vfw-mciwndgeterror)
-   [**MCIWNDM\_NOTIFYERROR**](mciwndm-notifyerror.md)
-   [**MCIWNDM\_NOTIFYMEDIA**](mciwndm-notifymedia.md)
-   [**MCIWNDM\_NOTIFYMODE**](mciwndm-notifymode.md)
-   [**MCIWNDM\_NOTIFYPOS**](mciwndm-notifypos.md)
-   [**MCIWNDM\_NOTIFYSIZE**](mciwndm-notifysize.md)

## Time Formats

-   [**MCIWndGetTimeFormat**](/windows/desktop/api/Vfw/nf-vfw-mciwndgettimeformat)
-   [**MCIWndSetTimeFormat**](/windows/desktop/api/Vfw/nf-vfw-mciwndsettimeformat)
-   [**MCIWndUseFrames**](/windows/desktop/api/Vfw/nf-vfw-mciwnduseframes)
-   [**MCIWndUseTime**](/windows/desktop/api/Vfw/nf-vfw-mciwndusetime)
-   [**MCIWndValidateMedia**](/windows/desktop/api/Vfw/nf-vfw-mciwndvalidatemedia)

## Status Updates

-   [**MCIWndGetActiveTimer**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetactivetimer)
-   [**MCIWndGetInactiveTimer**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetinactivetimer)
-   [**MCIWndSetActiveTimer**](/windows/desktop/api/Vfw/nf-vfw-mciwndsetactivetimer)
-   [**MCIWndSetInactiveTimer**](/windows/desktop/api/Vfw/nf-vfw-mciwndsetinactivetimer)
-   [**MCIWndSetTimers**](/windows/desktop/api/Vfw/nf-vfw-mciwndsettimers)

## Device Capabilities

-   [**MCIWndCanConfig**](/windows/desktop/api/Vfw/nf-vfw-mciwndcanconfig)
-   [**MCIWndCanEject**](/windows/desktop/api/Vfw/nf-vfw-mciwndcaneject)
-   [**MCIWndCanPlay**](/windows/desktop/api/Vfw/nf-vfw-mciwndcanplay)
-   [**MCIWndCanRecord**](/windows/desktop/api/Vfw/nf-vfw-mciwndcanrecord)
-   [**MCIWndCanSave**](/windows/desktop/api/Vfw/nf-vfw-mciwndcansave)
-   [**MCIWndCanWindow**](/windows/desktop/api/Vfw/nf-vfw-mciwndcanwindow)

## MCI Device Settings

-   [**MCIWndGetAlias**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetalias)
-   [**MCIWndGetDevice**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetdevice)
-   [**MCIWndGetDeviceID**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetdeviceid)
-   [**MCIWndGetFileName**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetfilename)
-   [**MCIWndGetMode**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetmode)

## MCI Command-String Interface

-   [**MCIWndReturnString**](/windows/desktop/api/Vfw/nf-vfw-mciwndreturnstring)
-   [**MCIWndSendString**](/windows/desktop/api/Vfw/nf-vfw-mciwndsendstring)

## Related topics

<dl> <dt>

[MCIWnd Window Class](mciwnd-window-class.md)
</dt> </dl>

 

 




