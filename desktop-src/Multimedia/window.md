---
title: window command
description: The window command controls the display window.
ms.assetid: '613dfedb-5ca8-45da-a4ba-ce465b933451'
keywords:
- window command Windows Multimedia
topic_type:
- apiref
api_name:
- window
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# window command

The window command controls the display window. You can use this command to change the display characteristics of the window or provide a destination window for the driver to use in place of the default display window. Digital-video, and video-overlay devices recognize this command.

To send this command, call the [**mciSendString**](/previous-versions//dd757161(v=vs.85)) function with the *lpszCommand* parameter set as follows.

``` syntax
_stprintf_s(
  lpszCommand, 
  TEXT("window %s %s %s"), 
  lpszDeviceID, 
  lpszWindowFlags, 
  lpszFlags
); 
```

## Parameters

<dl> <dt>

<span id="lpszDeviceID"></span><span id="lpszdeviceid"></span><span id="LPSZDEVICEID"></span>*lpszDeviceID*
</dt> <dd>

Identifier of an MCI device. This identifier or alias is assigned when the device is opened.

</dd> <dt>

<span id="lpszWindowFlags"></span><span id="lpszwindowflags"></span><span id="LPSZWINDOWFLAGS"></span>*lpszWindowFlags*
</dt> <dd>

Flag for controlling the display window. The following table lists device types that recognize the window command and the flags used by each type.



| Value        | Meaning                                                                                                                                        | Meaning                                                                                                                                   |
|--------------|------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| digitalvideo | handle *hwnd* state hidestate minimizestate restorestate showshow maximized                                                                    | show minimizedshow [**min**](min.md) noactiveshow nashow noactivateshow normaltext *caption*                                             |
| overlay      | fixedhandle defaulthandle *hwnd* state hidestate iconicstate maximizedstate minimizestate minimizedstate no actionstate noactivatestate normal | state restorestate showshow maximizedshow minimizedshow [**min**](min.md) noactiveshow nashow noactivateshow normalstretchtext *caption* |



 

The following table lists the flags that can be specified in the **lpszWindowFlags** parameter and their meanings.



| Value                            | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| fixed                            | Disables stretching of the image.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| handle default                   | Specifies that the device should set the display window back to the default window created during the [open](open.md) operation. For video-overlay devices, specifies that the device should create and manage its own destination window.                                                                                                                                                                                                                                                                                                                                                  |
| handle *hwnd*                    | Specifies the handle of the destination window to use instead of the default window. The *hwnd* parameter contains the ASCII numeric equivalent of the window handle returned by the [CreateWindow](/windows/win32/api/winuser/nf-winuser-createwindowa) function. Two device instances can use the same window handle provided that each instance updates the video and image pixels in the window as if the other instance did not exist. When video output is disabled with [setvideo](setvideo.md) "off", an [update](update.md) command will make the destination rectangle a solid color. |
| show maximized                   | Maximizes the destination window.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| show [**min**](min.md) noactive | Displays the destination window as an icon.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| show minimized                   | Minimizes the destination window.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| show na                          | Displays the destination window in its current state; the window that is currently active remains active.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| show noactivate                  | Displays the destination window in its most recent size and position; the window that is currently active remains active.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| show normal                      | Activates and displays the destination window in its original size and position. (This is the same as the "state restore" flag.)                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| state hide                       | Hides the destination window.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| state iconic                     | Displays the destination window as an icon.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| state maximized                  | Maximizes the destination window.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| state minimize                   | Minimizes the destination window and activates the top-level window in the window-manager's list.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| state minimized                  | Minimizes the destination window.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| state no action                  | Displays the destination window in its current state. The window that is currently active remains active.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| state noactivate                 | Displays the destination window in its most recent size and state. The currently active window remains active.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| state normal                     | Activates and displays the destination window in its original size and position.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| state restore                    | Activates and displays the destination window in its original size and position.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| state show                       | Shows the destination window.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| stretch                          | Enables stretching of the image.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| text *caption*                   | Specifies the caption for the destination window. If this text contains embedded blanks, the entire caption must be enclosed in quotation marks. The default caption for the default window is blank.                                                                                                                                                                                                                                                                                                                                                                                        |



 

</dd> <dt>

<span id="lpszFlags"></span><span id="lpszflags"></span><span id="LPSZFLAGS"></span>*lpszFlags*
</dt> <dd>

Can be "wait", "notify", or both. For digital-video devices, "test" can also be specified. For more information about these flags, see [The Wait, Notify, and Test Flags](the-wait-notify-and-test-flags.md).

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Remarks

Video-overlay devices typically create and display a window when opened. If your application provides a window to the driver, your application is responsible for managing the messages sent to the window.

Because you can use the [status](status.md) command to retrieve the handle to the driver display window, you can also use the standard window manager functions (such as [ShowWindow](/windows/win32/api/winuser/nf-winuser-showwindow)) to manipulate the window.

## Examples

The following command displays and sets the caption for the "movie" playback window.

``` syntax
window movie text "Welcome to the Movies" state show
```

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>       |



## See also

<dl> <dt>

[MCI](mci.md)
</dt> <dt>

[MCI Command Strings](mci-command-strings.md)
</dt> <dt>

[open](open.md)
</dt> <dt>

[play](play.md)
</dt> <dt>

[setvideo](setvideo.md)
</dt> <dt>

[update](update.md)
</dt> </dl>

 

