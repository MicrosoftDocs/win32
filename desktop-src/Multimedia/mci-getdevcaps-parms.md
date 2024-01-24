---
title: MCI_GETDEVCAPS_PARMS structure (Mciapi.h)
description: The MCI\_GETDEVCAPS\_PARMS structure contains device-capability information for the MCI\_GETDEVCAPS command.
ms.assetid: a7b128c5-2121-49cd-b668-3a8466d49a73
keywords:
- MCI_GETDEVCAPS_PARMS structure Windows Multimedia
topic_type:
- apiref
api_name:
- MCI_GETDEVCAPS_PARMS
api_location:
- mciapi.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCI\_GETDEVCAPS\_PARMS structure

The **MCI\_GETDEVCAPS\_PARMS** structure contains device-capability information for the [**MCI\_GETDEVCAPS**](mci-getdevcaps.md) command.

## Syntax


```C++
typedef struct {
  DWORD_PTR dwCallback;
  DWORD     dwReturn;
  DWORD     dwItem;
} MCI_GETDEVCAPS_PARMS;
```



## Members

<dl> <dt>

**dwCallback**
</dt> <dd>

The low-order word specifies a window handle used for the MCI\_NOTIFY flag.

</dd> <dt>

**dwReturn**
</dt> <dd>

Contains information on exit.

</dd> <dt>

**dwItem**
</dt> <dd>

Capability being queried. This member can be one of the constants listed in the reference material for the [**MCI\_GETDEVCAPS**](mci-getdevcaps.md) command.

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

[**MCI\_GETDEVCAPS**](mci-getdevcaps.md)
</dt> <dt>

[**mciSendCommand**](/previous-versions//dd757160(v=vs.85))
</dt> </dl>

 

