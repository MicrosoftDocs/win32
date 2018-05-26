---
title: MCI\_VCR\_SETAUDIO\_PARMS structure
description: The MCI\_VCR\_SETAUDIO\_PARMS structure contains parameters for the MCI\_SETAUDIO command for video-cassette recorders.
ms.assetid: 328d8e63-7ddd-4c9b-85d6-2e56fd802dbc
keywords:
- MCI_VCR_SETAUDIO_PARMS structure Windows Multimedia
topic_type:
- apiref
api_name:
- MCI_VCR_SETAUDIO_PARMS
api_location:
- Vcr.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MCI\_VCR\_SETAUDIO\_PARMS structure

The **MCI\_VCR\_SETAUDIO\_PARMS** structure contains parameters for the [**MCI\_SETAUDIO**](mci-setaudio.md) command for video-cassette recorders.

## Syntax


```C++
typedef struct tagMCI_VCR_SETAUDIO_PARMS {
  DWORD_PTR dwCallback;
  DWORD     dwTrack;
  DWORD     dwTo;
  DWORD     dwNumber;
} MCI_VCR_SETAUDIO_PARMS;
```



## Members

<dl> <dt>

**dwCallback**
</dt> <dd>

The low-order word specifies a window handle used for the MCI\_NOTIFY flag.

</dd> <dt>

**dwTrack**
</dt> <dd>

Audio track.

</dd> <dt>

**dwTo**
</dt> <dd>

Type of input or monitored input.

</dd> <dt>

**dwNumber**
</dt> <dd>

Audio input (of the type specified in the **dwTo** member) to use.

</dd> </dl>

## Remarks

When assigning data to the members of this structure, set the corresponding flags in the *fdwCommand* parameter of the [**mciSendCommand**](/windows/win32/Mmsystem/?branch=master) function to validate the members.

## Requirements



|                                     |                                                                                  |
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

[**MCI\_SETAUDIO**](mci-setaudio.md)
</dt> <dt>

[**mciSendCommand**](/windows/win32/Mmsystem/?branch=master)
</dt> </dl>

 

 





