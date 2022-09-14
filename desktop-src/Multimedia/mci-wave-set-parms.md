---
title: MCI_WAVE_SET_PARMS structure (Mciapi.h)
description: The MCI\_WAVE\_SET\_PARMS structure contains information for the MCI\_SET command for waveform-audio devices.
ms.assetid: 24c26124-274f-457e-ab87-887f3bcffce3
keywords:
- MCI_WAVE_SET_PARMS structure Windows Multimedia
topic_type:
- apiref
api_name:
- MCI_WAVE_SET_PARMS
api_location:
- mciapi.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCI\_WAVE\_SET\_PARMS structure

The **MCI\_WAVE\_SET\_PARMS** structure contains information for the [**MCI\_SET**](mci-set.md) command for waveform-audio devices.

## Syntax


```C++
typedef struct {
  DWORD_PTR dwCallback;
  DWORD     dwTimeFormat;
  DWORD     dwAudio;
  UINT      wInput;
  UINT      wOutput;
  WORD      wFormatTag;
  WORD      wReserved2;
  WORD      nChannels;
  WORD      wReserved3;
  DWORD     nSamplesPerSec;
  DWORD     nAvgBytesPerSec;
  WORD      nBlockAlign;
  WORD      wReserved4;
  WORD      wBitsPerSample;
  WORD      wReserved5;
} MCI_WAVE_SET_PARMS;
```



## Members

<dl> <dt>

**dwCallback**
</dt> <dd>

The low-order word specifies a window handle used for the MCI\_NOTIFY flag.

</dd> <dt>

**dwTimeFormat**
</dt> <dd>

Device's time format.

</dd> <dt>

**dwAudio**
</dt> <dd>

Channel number for audio output. Typically used when turning a channel on or off.

</dd> <dt>

**wInput**
</dt> <dd>

Audio input channel.

</dd> <dt>

**wOutput**
</dt> <dd>

Output device to use. For example, this value could be 2 if a system had two installed sound cards.

</dd> <dt>

**wFormatTag**
</dt> <dd>

Format of the waveform-audio data, such as WAVE\_FORMAT\_PCM. Possible values are defined in Mmreg.h.

</dd> <dt>

**wReserved2**
</dt> <dd>

Reserved.

</dd> <dt>

**nChannels**
</dt> <dd>

Mono (1) or stereo (2).

</dd> <dt>

**wReserved3**
</dt> <dd>

Reserved.

</dd> <dt>

**nSamplesPerSec**
</dt> <dd>

Samples per second.

</dd> <dt>

**nAvgBytesPerSec**
</dt> <dd>

Sample rate in bytes per second.

</dd> <dt>

**nBlockAlign**
</dt> <dd>

Block alignment of the data.

</dd> <dt>

**wReserved4**
</dt> <dd>

Reserved.

</dd> <dt>

**wBitsPerSample**
</dt> <dd>

Bits per sample.

</dd> <dt>

**wReserved5**
</dt> <dd>

Reserved.

</dd> </dl>

## Remarks

When assigning data to the members of this structure, set the corresponding flags in the *fdwCommand* parameter of the [**mciSendCommand**](/previous-versions//dd757160(v=vs.85)) function to validate the members.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Mciapi.h</dt> </dl> |



## See also

<dl> <dt>

[**MCI**](mci.md)
</dt> <dt>

[**MCI Structures**](mci-structures.md)
</dt> <dt>

[**MCI\_SET**](mci-set.md)
</dt> <dt>

[**mciSendCommand**](/previous-versions//dd757160(v=vs.85))
</dt> </dl>

 

