---
title: MCI_SEQ_SET_PARMS structure (Mciapi.h)
description: The MCI\_SEQ\_SET\_PARMS structure contains information for the MCI\_SET command for MIDI sequencer devices.
ms.assetid: 71638a92-c1d6-474b-bc97-ea63ca586aaa
keywords:
- MCI_SEQ_SET_PARMS structure Windows Multimedia
topic_type:
- apiref
api_name:
- MCI_SEQ_SET_PARMS
api_location:
- mciapi.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCI\_SEQ\_SET\_PARMS structure

The **MCI\_SEQ\_SET\_PARMS** structure contains information for the [**MCI\_SET**](mci-set.md) command for MIDI sequencer devices.

## Syntax


```C++
typedef struct {
  DWORD_PTR dwCallback;
  DWORD     dwTimeFormat;
  DWORD     dwAudio;
  DWORD     dwTempo;
  DWORD     dwPort;
  DWORD     dwSlave;
  DWORD     dwMaster;
  DWORD     dwOffset;
} MCI_SEQ_SET_PARMS;
```



## Members

<dl> <dt>

**dwCallback**
</dt> <dd>

The low-order word specifies a window handle used for the MCI\_NOTIFY flag.

</dd> <dt>

**dwTimeFormat**
</dt> <dd>

Sequencer's time format.

</dd> <dt>

**dwAudio**
</dt> <dd>

Audio output channel.

</dd> <dt>

**dwTempo**
</dt> <dd>

Tempo.

</dd> <dt>

**dwPort**
</dt> <dd>

Port.

</dd> <dt>

**dwSlave**
</dt> <dd>

Type of synchronization used by the sequencer for subordinate operation.

</dd> <dt>

**dwMaster**
</dt> <dd>

Type of synchronization used by the sequencer for master operation.

</dd> <dt>

**dwOffset**
</dt> <dd>

Data offset.

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

 

