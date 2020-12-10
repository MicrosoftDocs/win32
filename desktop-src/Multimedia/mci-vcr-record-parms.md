---
title: MCI_VCR_RECORD_PARMS structure (Vcr.h)
description: The MCI\_VCR\_RECORD\_PARMS structure contains parameters for the MCI\_RECORD command for video-cassette recorders.
ms.assetid: a95a6dab-9854-4c44-989a-032dff680106
keywords:
- MCI_VCR_RECORD_PARMS structure Windows Multimedia
topic_type:
- apiref
api_name:
- MCI_VCR_RECORD_PARMS
api_location:
- Vcr.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCI\_VCR\_RECORD\_PARMS structure

The **MCI\_VCR\_RECORD\_PARMS** structure contains parameters for the [**MCI\_RECORD**](mci-record.md) command for video-cassette recorders.

## Syntax


```C++
typedef struct tagMCI_VCR_RECORD_PARMS {
  DWORD_PTR dwCallback;
  DWORD     dwFrom;
  DWORD     dwTo;
  DWORD     dwAt;
} MCI_VCR_RECORD_PARMS;
```



## Members

<dl> <dt>

**dwCallback**
</dt> <dd>

The low-order word specifies a window handle used for the MCI\_NOTIFY flag.

</dd> <dt>

**dwFrom**
</dt> <dd>

Position to play from.

</dd> <dt>

**dwTo**
</dt> <dd>

Position to play to.

</dd> <dt>

**dwAt**
</dt> <dd>

Time value that affects the [**MCI\_RECORD**](mci-record.md) or [**MCI\_CUE**](mci-cue.md) command. For **MCI\_RECORD**, this is the time when recording begins. For **MCI\_CUE**, this is the time when the cued device reaches the position given in **dwFrom**.

</dd> </dl>

## Remarks

Positions are specified in the current time format.

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

[**MCI\_CUE**](mci-cue.md)
</dt> <dt>

[**MCI\_RECORD**](mci-record.md)
</dt> <dt>

[**mciSendCommand**](/previous-versions//dd757160(v=vs.85))
</dt> </dl>

 

