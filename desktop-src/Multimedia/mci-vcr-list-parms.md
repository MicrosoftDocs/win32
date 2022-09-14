---
title: MCI_VCR_LIST_PARMS structure (Vcr.h)
description: The MCI\_VCR\_LIST\_PARMS structure contains parameters for the MCI\_LIST command for video-cassette recorders.
ms.assetid: 88725599-8057-4787-96e6-49b4a651c894
keywords:
- MCI_VCR_LIST_PARMS structure Windows Multimedia
topic_type:
- apiref
api_name:
- MCI_VCR_LIST_PARMS
api_location:
- Vcr.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCI\_VCR\_LIST\_PARMS structure

The **MCI\_VCR\_LIST\_PARMS** structure contains parameters for the [**MCI\_LIST**](mci-list.md) command for video-cassette recorders.

## Syntax


```C++
typedef struct tagMCI_VCR_LIST_PARMS {
  DWORD_PTR dwCallback;
  DWORD     dwReturn;
  DWORD     dwNumber;
} MCI_VCR_LIST_PARMS;
```



## Members

<dl> <dt>

**dwCallback**
</dt> <dd>

The low-order word specifies a window handle used for the MCI\_NOTIFY flag.

</dd> <dt>

**dwReturn**
</dt> <dd>

Buffer for returned information.

</dd> <dt>

**dwNumber**
</dt> <dd>

Number of VCR's video or audio inputs.

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

[**MCI\_LIST**](mci-list.md)
</dt> <dt>

[**mciSendCommand**](/previous-versions//dd757160(v=vs.85))
</dt> </dl>

 

