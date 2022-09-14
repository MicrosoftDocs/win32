---
title: MCI_WINDOW command (Mmsystem.h)
description: The MCI\_WINDOW command specifies the window and the window characteristics for graphic devices. Digital-video, and video-overlay devices recognize this command.
ms.assetid: 8b6c4d9a-ee72-4c64-aebe-6c8153167496
keywords:
- MCI_WINDOW command Windows Multimedia
topic_type:
- apiref
api_name:
- MCI_WINDOW
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCI\_WINDOW command

The MCI\_WINDOW command specifies the window and the window characteristics for graphic devices. Digital-video, and video-overlay devices recognize this command.

To send this command, call the [**mciSendCommand**](/previous-versions//dd757160(v=vs.85)) function with the following parameters.


```C++
MCIERROR mciSendCommand(
  MCIDEVICEID wDeviceID, 
  MCI_WINDOW, 
  DWORD dwFlags, 
  (DWORD) (LPMCI_GENERIC_PARMS) lpWindow
);
```



## Parameters

<dl> <dt>

<span id="wDeviceID"></span><span id="wdeviceid"></span><span id="WDEVICEID"></span>*wDeviceID*
</dt> <dd>

Device identifier of the MCI device that is to receive the command message.

</dd> <dt>

<span id="dwFlags"></span><span id="dwflags"></span><span id="DWFLAGS"></span>*dwFlags*
</dt> <dd>

MCI\_NOTIFY, MCI\_WAIT, or, for digital-video devices, MCI\_TEST. For information about these flags, see [The Wait, Notify, and Test Flags](the-wait-notify-and-test-flags.md).

</dd> <dt>

<span id="lpWindow"></span><span id="lpwindow"></span><span id="LPWINDOW"></span>*lpWindow*
</dt> <dd>

Pointer to an [**MCI\_GENERIC\_PARMS**](mci-generic-parms.md) structure. (Devices with extended command sets might replace this structure with a device-specific structure.)

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Remarks

Graphic devices should create a default window when a device is opened but should not display it until they receive the [MCI\_PLAY](mci-play.md) command. The MCI\_WINDOW command is used to supply an application-created window to the device and to change the display characteristics of an application-defined or default display window. If the application supplies the display window, it should be prepared to update an invalid rectangle on the window.

The following additional flags are used with the **digitalvideo** device type:

<dl> <dt>

<span id="MCI_DGV_WINDOW_HWND"></span><span id="mci_dgv_window_hwnd"></span>MCI\_DGV\_WINDOW\_HWND
</dt> <dd>

The handle of the window needed for use as the destination is included in the **hWnd** member of the structure identified by *lpWindow*.

</dd> <dt>

<span id="MCI_DGV_WINDOW_STATE"></span><span id="mci_dgv_window_state"></span>MCI\_DGV\_WINDOW\_STATE
</dt> <dd>

The **nCmdShow** member of the structure identified by *lpWindow* contains parameters for setting the window state.

</dd> <dt>

<span id="MCI_DGV_WINDOW_TEXT"></span><span id="mci_dgv_window_text"></span>MCI\_DGV\_WINDOW\_TEXT
</dt> <dd>

The **lpstrText** member of the structure identified by *lpWindow* contains an address of a buffer containing the caption used in the window title bar.

</dd> </dl>

For digital-video devices, the *lpWindow* parameter points to an [**MCI\_DGV\_WINDOW\_PARMS**](/windows/desktop/api/Digitalv/ns-digitalv-mci_dgv_window_parmsa) structure.

The following additional flags are used with the **overlay** device type:

<dl> <dt>

<span id="MCI_OVLY_WINDOW_DISABLE_STRETCH"></span><span id="mci_ovly_window_disable_stretch"></span>MCI\_OVLY\_WINDOW\_DISABLE\_STRETCH
</dt> <dd>

Disables stretching of the image.

</dd> <dt>

<span id="MCI_OVLY_WINDOW_ENABLE_STRETCH"></span><span id="mci_ovly_window_enable_stretch"></span>MCI\_OVLY\_WINDOW\_ENABLE\_STRETCH
</dt> <dd>

Enables stretching of the image.

</dd> <dt>

<span id="MCI_OVLY_WINDOW_HWND"></span><span id="mci_ovly_window_hwnd"></span>MCI\_OVLY\_WINDOW\_HWND
</dt> <dd>

The handle of the window used for the destination is included in the **hWnd** member of the structure identified by *lpWindow*. Set this flag to MCI\_OVLY\_WINDOW\_DEFAULT to return to the default window.

</dd> <dt>

<span id="MCI_OVLY_WINDOW_STATE"></span><span id="mci_ovly_window_state"></span>MCI\_OVLY\_WINDOW\_STATE
</dt> <dd>

The **nCmdShow** member of the *lpWindow* structure contains parameters for setting the window state. This flag is equivalent to calling [ShowWindow](/windows/win32/api/winuser/nf-winuser-showwindow) with the *state* parameter. The constants are the same as those defined in WINDOWS.H (such as SW\_HIDE, SW\_MINIMIZE, or SW\_SHOWNORMAL).

</dd> <dt>

<span id="MCI_OVLY_WINDOW_TEXT"></span><span id="mci_ovly_window_text"></span>MCI\_OVLY\_WINDOW\_TEXT
</dt> <dd>

The **lpstrText** member of the structure identified by *lpWindow* contains an address of a buffer containing the caption used for the window.

</dd> </dl>

For video-overlay devices, the *lpWindow* parameter points to an [**MCI\_OVLY\_WINDOW\_PARMS**](mci-ovly-window-parms.md) structure.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Mmsystem.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[MCI](mci.md)
</dt> <dt>

[MCI Commands](mci-commands.md)
</dt> </dl>

 

