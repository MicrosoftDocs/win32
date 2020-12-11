---
title: MCI_BREAK command (Mmsystem.h)
description: The MCI\_BREAK command sets a break key for an MCI device. MCI supports this command directly rather than passing it to the device. Any MCI application can use this command.
ms.assetid: 127b5179-2838-4bde-8d0c-37a4cc87fa4d
keywords:
- MCI_BREAK command Windows Multimedia
topic_type:
- apiref
api_name:
- MCI_BREAK
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCI\_BREAK command

The MCI\_BREAK command sets a break key for an MCI device. MCI supports this command directly rather than passing it to the device. Any MCI application can use this command.

To send this command, call the [**mciSendCommand**](/previous-versions//dd757160(v=vs.85)) function with the following parameters.


```C++
MCIERROR mciSendCommand(
  MCIDEVICEID wDeviceID, 
  MCI_BREAK, 
  DWORD dwFlags, 
  (DWORD) (LPMCI_BREAK_PARMS) lpBreak
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

MCI\_NOTIFY, MCI\_WAIT, or, for digital-video and video-cassette recorder (VCR) devices, MCI\_TEST. For information about these flags, see [The Wait, Notify, and Test Flags](the-wait-notify-and-test-flags.md).

</dd> <dt>

<span id="lpBreak"></span><span id="lpbreak"></span><span id="LPBREAK"></span>*lpBreak*
</dt> <dd>

Pointer to an [**MCI\_ BREAK\_PARMS**](mci-break-parms.md) structure.

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Remarks

You might have to press the break key multiple times to interrupt a wait operation. Pressing the break key after a device wait is canceled can send the break to an application. If an application has an action defined for the virtual-key code, then it can inadvertently respond to the break. For example, an application using VK\_CANCEL for an accelerator key can respond to the default CTRL+BREAK key if it is pressed after a wait is canceled.

The following additional flags apply to all devices:

<dl> <dt>

<span id="MCI_BREAK_HWND"></span><span id="mci_break_hwnd"></span>MCI\_BREAK\_HWND
</dt> <dd>

The **hwndBreak** member of the structure identified by *lpBreak* contains a window handle that must be the current window in order to enable break detection for that MCI device. This is usually the application's main window. If omitted, MCI does not check the window handle of the current window.

</dd> <dt>

<span id="MCI_BREAK_KEY"></span><span id="mci_break_key"></span>MCI\_BREAK\_KEY
</dt> <dd>

The **nVirtKey** member of the structure identified by *lpBreak* specifies the virtual-key code used for the break key. By default, MCI assigns CTRL+BREAK as the break key. This flag is required if MCI\_BREAK\_OFF is not specified.

</dd> <dt>

<span id="MCI_BREAK_OFF"></span><span id="mci_break_off"></span>MCI\_BREAK\_OFF
</dt> <dd>

Disables any existing break key for the indicated device.

</dd> </dl>

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

 

