---
description: Issuing Raw AV/C Commands
ms.assetid: 18081652-962f-4605-84b7-1fa60f61ad05
title: Issuing Raw AV/C Commands
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Issuing Raw AV/C Commands

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The [**IAMExtDevice**](/windows/desktop/api/Strmif/nn-strmif-iamextdevice), [**IAMExtTransport**](/windows/desktop/api/Strmif/nn-strmif-iamexttransport), and [**IAMTimecodeReader**](/windows/desktop/api/Strmif/nn-strmif-iamtimecodereader) interfaces work by translating the method calls into commands for the driver, then interpreting the driver's response and returning it through an **HRESULT** or an output parameter. However, some device functions may not be accessible through these methods. Therefore, MSDV supports sending raw AV/C commands to the device.

You should keep the following points in mind when using this feature:

-   The command is passed directly to the device, with no error checking or parameter validation. For this reason, you should issue raw AV/C commands only when the DirectShow interfaces do not implement the functionality you need.
-   All raw AV/C commands are synchronous. The thread issuing the command blocks until the command returns.
-   Only one command can be given at a time. While the command is being processed, the device will reject any additional commands.
-   The UVC driver does not support raw AV/C commands.

To send an AV/C command, format the command as an array of bytes. Then call [**IAMExtTransport::GetTransportBasicParameters**](/windows/desktop/api/Strmif/nf-strmif-iamexttransport-gettransportbasicparameters). Pass in the ED\_RAW\_EXT\_DEV\_CMD flag, the array size, and the array. You must cast the array address to an **LPOLESTR\*** type, because the original purpose of this parameter was to return a string value.


```C++
BYTE AvcCmd[] = { ... }; // Contains the AV/C command (not shown)
long cbCmd = sizeof(AvcCmd);
hr = pTransport->GetTransportBasicParameters(
    ED_RAW_EXT_DEV_CMD, 
    &cbCmd,
    (LPOLESTR*) AvcCmd);
```



The contents of the array are passed directly to the device, so you must be careful to format it correctly. A command can target the unit (camcorder) or a subunit (tape or camera). The relevant standards are available from the [1394 Trade Association Web site](https://1394ta.org).

-   AV/C Digital Interface Command Set General Specification
-   AV/C Tape Recorder/Player Subunit Specification

The former describes how to format AV/C commands and lists the unit commands. The latter specification lists the subunit commands.

The **GetTransportBasicParameters** method may return one of the following error codes:



| Error Code              | Description                                                                      |
|-------------------------|----------------------------------------------------------------------------------|
| ERROR\_TIMEOUT          | The command timed out.                                                           |
| ERROR\_REQ\_NOT\_ACCEP  | The device did not accept the command.                                           |
| ERROR\_NOT\_SUPPORTED   | The device does not support the command.                                         |
| ERROR\_REQUEST\_ABORTED | The command was aborted. Possbly the device was removed or a bus reset occurred. |



 

> [!Note]  
> These errors are returned as Win32 error codes, not HRESULTs, so you should test for these values directly, rather than using the **SUCCEEDED** and **FAILED** macros.

 

If the method returns S\_OK, the response from the device is copied into the array. The response payload might be larger than the command, so you must allocate a buffer large enough to hold it. The maximum payload size is 512 bytes. Note that a return value of S\_OK does not always mean the device successfully carried out the command. The application must examine the response payload to determine the status.

The following example shows the command to search for an absolute track number search:


```C++
// Set up the ATN search command.
BYTE AvcCmd[] = 
{ 
    0x00,   // ctype = "control"
    0x20,   // subunit_type, subunit_id
    0x52,   // opcode (ATN)
    0x20,   // operand 0 = "search"
    0x00,   // operand 1 = ATN
    0x00,   // operand 2 = ATN
    0x00,   // operand 3 = ATN
    0xFF   //  operand 4 = D-VCR medium type.
};
// Specify a track number.
ULONG ulTrackNumber = track_number; // Specify the track number here.
// Shift over by 1 (LSB of operand 1 is a 1-bit blank flag)
ulTrackNumber = ulTrackNumber << 1; 
// Plug this number into operands 1 - 3.
AvcCmd[4] = (BYTE) (ulTrackNumber & 0x000000FF);
AvcCmd[5] = (BYTE)((ulTrackNumber & 0x0000FF00) >> 8);
AvcCmd[6] = (BYTE)((ulTrackNumber & 0x00FF0000) >> 16);
```



## Related topics

<dl> <dt>

[Controlling a DV Camcorder](controlling-a-dv-camcorder.md)
</dt> </dl>

 

 



