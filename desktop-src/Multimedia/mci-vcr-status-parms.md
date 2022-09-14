---
title: MCI_VCR_STATUS_PARMS structure (Vcr.h)
description: The MCI\_VCR\_STATUS\_PARMS structure contains parameters for the MCI\_STATUS command for video-cassette recorders.
ms.assetid: 5d7cbb64-a81d-4bdd-8f07-8c20dd7b9ef5
keywords:
- MCI_VCR_STATUS_PARMS structure Windows Multimedia
topic_type:
- apiref
api_name:
- MCI_VCR_STATUS_PARMS
api_location:
- Vcr.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCI\_VCR\_STATUS\_PARMS structure

The **MCI\_VCR\_STATUS\_PARMS** structure contains parameters for the [**MCI\_STATUS**](mci-status.md) command for video-cassette recorders.

## Syntax


```C++
typedef struct tagMCI_VCR_STATUS_PARMS {
  DWORD_PTR dwCallback;
  DWORD     dwReturn;
  DWORD     dwItem;
  DWORD     dwTrack;
  DWORD     dwNumber;
} MCI_VCR_STATUS_PARMS;
```



## Members

<dl> <dt>

**dwCallback**
</dt> <dd>

The low-order word specifies a window handle used for the MCI\_NOTIFY flag.

</dd> <dt>

**dwReturn**
</dt> <dd>

Value returned by the [**MCI\_STATUS**](mci-status.md) command. The return value varies according to the inquiry of the command. For more information, see the description of the [**MCI\_STATUS**](mci-status-parms.md) command.

</dd> <dt>

**dwItem**
</dt> <dd>

Type of information requested.

</dd> <dt>

**dwTrack**
</dt> <dd>

Audio or video track that will store information during the next recording. This member is used to return information when the [**MCI\_STATUS**](mci-status-parms.md) command inquires about the video or audio recording status.

</dd> <dt>

**dwNumber**
</dt> <dd>

Logical tuner that the current channel is associated with. This member is used to return information when the [**MCI\_STATUS**](mci-status.md) command inquires about the current channel number.

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

[**MCI\_STATUS**](mci-status.md)
</dt> <dt>

[**mciSendCommand**](/previous-versions//dd757160(v=vs.85))
</dt> </dl>

 

