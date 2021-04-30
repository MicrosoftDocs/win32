---
title: MCI_BREAK_PARMS structure (Mciapi.h)
description: The MCI\_BREAK\_PARMS structure contains virtual-key code and window information for the MCI\_BREAK command.
ms.assetid: c8df8c55-cc6b-4dd7-b275-784d3eb9dce1
keywords:
- MCI_BREAK_PARMS structure Windows Multimedia
topic_type:
- apiref
api_name:
- MCI_BREAK_PARMS
api_location:
- mciapi.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCI\_BREAK\_PARMS structure

The **MCI\_BREAK\_PARMS** structure contains virtual-key code and window information for the [**MCI\_BREAK**](mci-break.md) command.

## Syntax


```C++
typedef struct {
  DWORD_PTR dwCallback;
  int       nVirtKey;
  HWND      hwndBreak;
} MCI_BREAK_PARMS;
```



## Members

<dl> <dt>

**dwCallback**
</dt> <dd>

The low-order word specifies a window handle used for the MCI\_NOTIFY flag.

</dd> <dt>

**nVirtKey**
</dt> <dd>

Virtual-key code for break key.

</dd> <dt>

**hwndBreak**
</dt> <dd>

Handle to the window that must be the current window for break detection.

</dd> </dl>

## Remarks

When assigning data to the members of this structure, set the corresponding flags in the *fdwCommand* parameter of the [**mciSendCommand**](/previous-versions//dd757160(v=vs.85)) function to validate the members. The following flags are defined:

MCI\_BREAK\_HWND

Validates the **hwndBreak** member specifying the window that must have focus to enable break detection.

MCI\_BREAK\_KEY

Validates the **nVirtKey** member specifying the virtual-key code to be used for the break key.

MCI\_BREAK\_OFF

Disables any existing break key.

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

[**MCI\_BREAK**](mci-break.md)
</dt> <dt>

[**mciSendCommand**](/previous-versions//dd757160(v=vs.85))
</dt> </dl>

 

