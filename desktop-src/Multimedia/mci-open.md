---
title: MCI_OPEN command (Mmsystem.h)
description: The MCI\_OPEN command initializes a device or file. All devices recognize this command.
ms.assetid: e2ee92b5-b10b-4408-950e-3002fe775b25
keywords:
- MCI_OPEN command Windows Multimedia
topic_type:
- apiref
api_name:
- MCI_OPEN
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCI\_OPEN command

The MCI\_OPEN command initializes a device or file. All devices recognize this command.

To send this command, call the [**mciSendCommand**](/previous-versions//dd757160(v=vs.85)) function with the following parameters.


```C++
MCIERROR mciSendCommand(
  MCIDEVICEID wDeviceID, 
  MCI_OPEN, 
  DWORD dwFlags, 
  (DWORD) (LPMCI_OPEN_PARMS) lpOpen
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

MCI\_NOTIFY or MCI\_WAIT. For information about these flags, see [The Wait, Notify, and Test Flags](the-wait-notify-and-test-flags.md).

</dd> <dt>

<span id="lpOpen"></span><span id="lpopen"></span><span id="LPOPEN"></span>*lpOpen*
</dt> <dd>

Pointer to an [**MCI\_OPEN\_PARMS**](mci-open-parms.md) structure. (Devices with extended command sets might replace this structure with a device-specific structure.)

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Remarks

The MCI\_OPEN\_TYPE flag must be used whenever a device is specified in the [**mciSendCommand**](/previous-versions//dd757160(v=vs.85)) function. If you open a device by specifying a device-type constant, you must specify the MCI\_OPEN\_TYPE\_ID flag in addition to MCI\_OPEN\_TYPE. For a list of device-type constants, see [MCI Device Types](mci-device-types.md).

If the MCI\_OPEN\_SHAREABLE flag is not specified when a device or file is initially opened, all subsequent MCI\_OPEN commands to the device or file will fail. If the device or file is already open and this flag is not specified, the call will fail even if the first open command specified MCI\_OPEN\_SHAREABLE. Files opened for the MCISEQ.DRV and MCIWAVE.DRV devices are nonsharable.

Case is ignored in the device name, but there cannot be leading or trailing blanks.

To use automatic type selection (via the entries in the registry), assign the filename and file extension to the **lpstrElementName** member of the structure identified by *lpOpen*, set the **lpstrDeviceType** member to **NULL**, and set the MCI\_OPEN\_ELEMENT flag.

The following additional flags apply to all devices supporting MCI\_OPEN:

<dl> <dt>

<span id="MCI_OPEN_ALIAS"></span><span id="mci_open_alias"></span>MCI\_OPEN\_ALIAS
</dt> <dd>

An alias is included in the **lpstrAlias** member of the structure identified by *lpOpen*.

</dd> <dt>

<span id="MCI_OPEN_SHAREABLE"></span><span id="mci_open_shareable"></span>MCI\_OPEN\_SHAREABLE
</dt> <dd>

The device or file should be opened as sharable.

</dd> <dt>

<span id="MCI_OPEN_TYPE"></span><span id="mci_open_type"></span>MCI\_OPEN\_TYPE
</dt> <dd>

A device type name or constant is included in the **lpstrDeviceType** member of the structure identified by *lpOpen*.

</dd> <dt>

<span id="MCI_OPEN_TYPE_ID"></span><span id="mci_open_type_id"></span>MCI\_OPEN\_TYPE\_ID
</dt> <dd>

The low-order word of the **lpstrDeviceType** member of the structure identified by *lpOpen* contains a standard MCI device type identifier and the high-order word optionally contains the ordinal index for the device. Use this flag with the MCI\_OPEN\_TYPE flag.

</dd> </dl>

The following additional flags apply to compound devices:

<dl> <dt>

<span id="MCI_OPEN_ELEMENT"></span><span id="mci_open_element"></span>MCI\_OPEN\_ELEMENT
</dt> <dd>

A filename is included in the **lpstrElementName** member of the structure identified by *lpOpen*.

</dd> <dt>

<span id="MCI_OPEN_ELEMENT_ID"></span><span id="mci_open_element_id"></span>MCI\_OPEN\_ELEMENT\_ID
</dt> <dd>

The **lpstrElementName** member of the structure identified by *lpOpen* is interpreted as a **DWORD** value and has meaning internal to the device. Use this flag with the MCI\_OPEN\_ELEMENT flag.

</dd> </dl>

The following additional flags are used with the **digitalvideo** device type:

<dl> <dt>

<span id="MCI_DGV_OPEN_NOSTATIC"></span><span id="mci_dgv_open_nostatic"></span>MCI\_DGV\_OPEN\_NOSTATIC
</dt> <dd>

The device should reduce the number of static (system) colors in the palette. This increases the number of colors available for rendering the video stream. This flag applies only to devices that share a palette with Windows.

</dd> <dt>

<span id="MCI_DGV_OPEN_PARENT"></span><span id="mci_dgv_open_parent"></span>MCI\_DGV\_OPEN\_PARENT
</dt> <dd>

The parent window handle is specified in the **hWndParent** member of the structure identified by *lpOpen*.

</dd> <dt>

<span id="MCI_DGV_OPEN_WS"></span><span id="mci_dgv_open_ws"></span>MCI\_DGV\_OPEN\_WS
</dt> <dd>

A window style is specified in the **dwStyle** member of the structure identified by *lpOpen*.

</dd> <dt>

<span id="MCI_DGV_OPEN_16BIT"></span><span id="mci_dgv_open_16bit"></span>MCI\_DGV\_OPEN\_16BIT
</dt> <dd>

Indicates a preference for 16-bit MCI device support.

</dd> <dt>

<span id="MCI_DGV_OPEN_32BIT"></span><span id="mci_dgv_open_32bit"></span>MCI\_DGV\_OPEN\_32BIT
</dt> <dd>

Indicates a preference for 32-bit MCI device support.

</dd> </dl>

For digital-video devices, the *lpOpen* parameter points to an [**MCI\_DGV\_OPEN\_PARMS**](/windows/desktop/api/Digitalv/ns-digitalv-mci_dgv_open_parmsa) structure.

The following additional flags are used with the **overlay** device type:

<dl> <dt>

<span id="MCI_OVLY_OPEN_PARENT"></span><span id="mci_ovly_open_parent"></span>MCI\_OVLY\_OPEN\_PARENT
</dt> <dd>

The parent window handle is specified in the **hWndParent** member of the structure identified by *lpOpen*.

</dd> <dt>

<span id="MCI_OVLY_OPEN_WS"></span><span id="mci_ovly_open_ws"></span>MCI\_OVLY\_OPEN\_WS
</dt> <dd>

A window style is specified in the **dwStyle** member of the structure identified by *lpOpen*. The **dwStyle** value specifies the style of the window that the driver will create and display if the application does not provide one. The style parameter takes an integer that defines the window style. These constants are the same as the standard window styles (such as WS\_CHILD, WS\_OVERLAPPEDWINDOW, or WS\_POPUP).

</dd> </dl>

For video-overlay devices, the *lpOpen* parameter points to an [**MCI\_OVLY\_OPEN\_PARMS**](mci-ovly-open-parms.md) structure.

The following additional flag is used with the **waveaudio** device type:

<dl> <dt>

<span id="MCI_WAVE_OPEN_BUFFER"></span><span id="mci_wave_open_buffer"></span>MCI\_WAVE\_OPEN\_BUFFER
</dt> <dd>

A buffer length is specified in the **dwBufferSeconds** member of the structure identified by *lpOpen*.

</dd> </dl>

For waveform-audio devices, the *lpOpen* parameter points to an [**MCI\_WAVE\_OPEN\_PARMS**](mci-wave-open-parms.md) structure. The MCIWAVE driver requires an asynchronous waveform-audio device.

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

 

