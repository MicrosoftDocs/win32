---
title: open command (Corecrt\_io.h)
description: The open command initializes a device. All MCI devices recognize this command.
ms.assetid: '0bb97c8c-8222-4d4e-b20b-94e9f9095afe'
keywords:
- open command Windows Multimedia
topic_type:
- apiref
api_name:
- open
api_location:
- corecrt_io.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# open command

The open command initializes a device. All MCI devices recognize this command.

To send this command, call the [**mciSendString**](/previous-versions//dd757161(v=vs.85)) function with the *lpszCommand* parameter set as follows.

``` syntax
_stprintf_s(
  lpszCommand, 
  TEXT("open %s %s %s"), 
  lpszDevice, 
  lpszOpenFlags, 
  lpszFlags
); 
```

## Parameters

<dl> <dt>

<span id="lpszDevice"></span><span id="lpszdevice"></span><span id="LPSZDEVICE"></span>*lpszDevice*
</dt> <dd>

Identifier of an MCI device or device driver. This can be either a device name (as given in the registry or the SYSTEM.INI file) or the filename of the device driver. If you specify the filename of the device driver, you can optionally include the .DRV extension, but you should not include the path to the file.

</dd> <dt>

<span id="lpszOpenFlags"></span><span id="lpszopenflags"></span><span id="LPSZOPENFLAGS"></span>*lpszOpenFlags*
</dt> <dd>

Flag that identifies what to initialize. The following table lists device types that recognize the **open** command and the flags used by each type.



| Value        | Meaning                                                        | Meaning                                                                         |
|--------------|----------------------------------------------------------------|---------------------------------------------------------------------------------|
| cdaudio      | alias *device\_alias*sharable                                  | type *device\_type*                                                             |
| digitalvideo | alias *device\_aliaselementname*nostatic parent *hwnd*sharable | style child style overlapped style popup style *style\_type*type *device\_type* |
| overlay      | alias *device\_alias*parent *hwnd*sharable style child         | style overlapped style popup style *style\_type*type *device\_type*             |
| sequencer    | alias *device\_alias* sharable                                 | type *device\_type*                                                             |
| vcr          | alias *device\_alias*sharable                                  | type *device\_type*                                                             |
| videodisk    | alias *device\_alias*sharable                                  | type *device\_type*                                                             |
| waveaudio    | alias *device\_alias*buffer *buffer\_size*                     | sharable type *device\_type*                                                    |



 

The following table lists the flags that can be specified in the **lpszOpenFlags** parameter and their meanings.



| Value                 | Meaning                                                                                                                                                                                                                                                                                                                                                              |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| alias *device\_alias* | Specifies an alternate name for the given device. If specified, it must be used as the *device\_id* in subsequent commands.                                                                                                                                                                                                                                          |
| *elementname*         | Specifies the name of the device element (file) loaded when the device opens.                                                                                                                                                                                                                                                                                        |
| buffer *buffer\_size* | Sets the size, in seconds, of the buffer used by the waveform-audio device. The default size of the buffer is set when the waveform-audio device is installed or configured. Typically the buffer size is set to 4 seconds. With the MCIWAVE device, the minimum size is 2 seconds and the maximum size is 9 seconds.                                                |
| parent *hwnd*         | Specifies the window handle of the parent window.                                                                                                                                                                                                                                                                                                                    |
| sharable              | Initializes the device or file as sharable. Subsequent attempts to open the device or file fail unless you specify "sharable" in both the original and subsequent **open** commands. MCI returns an invalid device error if the device is already open and not sharable.<br/> The MCISEQ sequencer and MCIWAVE devices do not support shared files.<br/> |
| style child           | Opens a window with a child window style.                                                                                                                                                                                                                                                                                                                            |
| style overlapped      | Opens a window with an overlapped window style.                                                                                                                                                                                                                                                                                                                      |
| style popup           | Opens a window with a pop-up window style.                                                                                                                                                                                                                                                                                                                           |
| style *style\_type*   | Indicates a window style.                                                                                                                                                                                                                                                                                                                                            |
| type *device\_type*   | Specifies the device type of a file.                                                                                                                                                                                                                                                                                                                                 |



 

</dd> <dt>

<span id="lpszFlags"></span><span id="lpszflags"></span><span id="LPSZFLAGS"></span>*lpszFlags*
</dt> <dd>

Can be "wait", "notify", or both. For more information about these flags, see [The Wait, Notify, and Test Flags](the-wait-notify-and-test-flags.md).

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Remarks

MCI reserves "cdaudio" for the CD audio device type, "videodisc" for the videodisc device type, "sequencer" for the MIDI sequencer device type, "AVIVideo" for the digital-video device type, and "waveaudio" for the waveform-audio device type.

As an alternative to the "type" flag, MCI can select the device based on the extension used by the file, as recorded in the registry or the \[mci extension\] section of the SYSTEM.INI file.

MCI can open AVI files by using a file-interface pointer or a stream-interface pointer. To open a file by using either type of interface pointer, specify an at sign (@) followed by the interface pointer in place of the file or device name for the *lpszDevice* parameter. For more information about the file and stream interfaces, see " [AVIFile Functions and Macros](avifile-functions-and-macros.md)."

The following command opens the "mysound" device.

``` syntax
open new type waveaudio alias mysound buffer 6
```

With device name "new", the waveform driver prepares a new waveform resource. The command assigns the device alias "mysound" and specifies a 6-second buffer.

You can eliminate the "type" flag if you combine the device name with the filename. MCI recognizes this combination when you use the following syntax:

*device\_name* ! *element\_name*

The exclamation point separates the device name from the filename. The exclamation point should not be delimited by white spaces.

The following example opens the RIGHT.WAV file using the "waveaudio" device.

``` syntax
open waveaudio!right.wav
```

The MCIWAVE driver requires an asynchronous waveform-audio device.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>Corecrt\_io.h</dt> </dl> |



## See also

<dl> <dt>

[MCI](mci.md)
</dt> <dt>

[MCI Command Strings](mci-command-strings.md)
</dt> </dl>

 

