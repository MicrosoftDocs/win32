---
title: MCI_VCR_SET_PARMS structure (Vcr.h)
description: The MCI\_VCR\_SET\_PARMS structure contains parameters for the MCI\_SET command for video-cassette recorders.
ms.assetid: f55515f5-14f6-47e4-8be2-4524975fc950
keywords:
- MCI_VCR_SET_PARMS structure Windows Multimedia
topic_type:
- apiref
api_name:
- MCI_VCR_SET_PARMS
api_location:
- Vcr.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCI\_VCR\_SET\_PARMS structure

The **MCI\_VCR\_SET\_PARMS** structure contains parameters for the [**MCI\_SET**](mci-set.md) command for video-cassette recorders.

## Syntax


```C++
typedef struct tagMCI_VCR_SET_PARMS {
  DWORD_PTR dwCallback;
  DWORD     dwTimeFormat;
  DWORD     dwAudio;
  DWORD     dwTimeMode;
  DWORD     dwRecordFormat;
  DWORD     dwCounterFormat;
  DWORD     dwIndex;
  DWORD     dwTracking;
  DWORD     dwSpeed;
  DWORD     dwLength;
  DWORD     dwCounter;
  DWORD     dwClock;
  DWORD     dwPauseTimeout;
  DWORD     dwPrerollDuration;
  DWORD     dwPostrollDuration;
} MCI_VCR_SET_PARMS;
```



## Members

<dl> <dt>

**dwCallback**
</dt> <dd>

The low-order word specifies a window handle used for the MCI\_NOTIFY flag.

</dd> <dt>

**dwTimeFormat**
</dt> <dd>

Current time format.

</dd> <dt>

**dwAudio**
</dt> <dd>

Not used.

</dd> <dt>

**dwTimeMode**
</dt> <dd>

Constant that specifies the timing source used by the device. The timing source is either a timecode recorded on videotape, or the counters in the device that sense videotape movement.

</dd> <dt>

**dwRecordFormat**
</dt> <dd>

Recording rate.

</dd> <dt>

**dwCounterFormat**
</dt> <dd>

Format of a new counter time value.

</dd> <dt>

**dwIndex**
</dt> <dd>

Contents of on-screen display.

</dd> <dt>

**dwTracking**
</dt> <dd>

Speed adjustment used when tracking the VCR playback rate.

</dd> <dt>

**dwSpeed**
</dt> <dd>

Playback speed used by the device as an integer. Normal playback speed is 1000, double speed is 2000, and half speed is 500.

</dd> <dt>

**dwLength**
</dt> <dd>

Videotape length when the length is undetectable by the device.

</dd> <dt>

**dwCounter**
</dt> <dd>

New counter value.

</dd> <dt>

**dwClock**
</dt> <dd>

New clock time.

</dd> <dt>

**dwPauseTimeout**
</dt> <dd>

New timeout value for pause command.

</dd> <dt>

**dwPrerollDuration**
</dt> <dd>

Videotape length needed to stabilize the VCR output.

</dd> <dt>

**dwPostrollDuration**
</dt> <dd>

Videotape length needed to brake the VCR transport when a [**MCI\_STOP**](mci-stop.md) or [**MCI\_PAUSE**](mci-pause.md) command is issued.

</dd> </dl>

## Remarks

When assigning data to the members of this structure, set the corresponding flags in the *fdwCommand* parameter of the [**mciSendCommand**](/previous-versions//dd757160(v=vs.85)) function to validate the members.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vcr.h</dt> </dl> |



## See also

<dl> <dt>

[**MCI**](mci.md)
</dt> <dt>

[**MCI Structures**](mci-structures.md)
</dt> <dt>

[**MCI\_PAUSE**](mci-pause.md)
</dt> <dt>

[**MCI\_SET**](mci-set.md)
</dt> <dt>

[**MCI\_STOP**](mci-stop.md)
</dt> <dt>

[**mciSendCommand**](/previous-versions//dd757160(v=vs.85))
</dt> </dl>

 

