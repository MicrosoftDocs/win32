---
title: MCI_SYSINFO_PARMS structure (Mciapi.h)
description: The MCI\_SYSINFO\_PARMS structure contains information for the MCI\_SYSINFO command.
ms.assetid: 433649ed-7c00-440d-84f3-164949e01cc4
keywords:
- MCI_SYSINFO_PARMS structure Windows Multimedia
topic_type:
- apiref
api_name:
- MCI_SYSINFO_PARMS
api_location:
- mciapi.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCI\_SYSINFO\_PARMS structure

The **MCI\_SYSINFO\_PARMS** structure contains information for the [**MCI\_SYSINFO**](mci-sysinfo.md) command.

## Syntax


```C++
typedef struct {
  DWORD_PTR dwCallback;
  LPTSTR    lpstrReturn;
  DWORD     dwRetSize;
  DWORD     dwNumber;
  UINT      wDeviceType;
} MCI_SYSINFO_PARMS;
```



## Members

<dl> <dt>

**dwCallback**
</dt> <dd>

The low-order word specifies a window handle used for the MCI\_NOTIFY flag.

</dd> <dt>

**lpstrReturn**
</dt> <dd>

Pointer to a user-supplied buffer for the return string. It is also used to return a **DWORD** value when the MCI\_SYSINFO\_QUANTITY flag is used.

</dd> <dt>

**dwRetSize**
</dt> <dd>

Size, in bytes, of return buffer.

</dd> <dt>

**dwNumber**
</dt> <dd>

Number indicating the device position in the MCI device table or in the list of open devices if the MCI\_SYSINFO\_OPEN flag is set.

</dd> <dt>

**wDeviceType**
</dt> <dd>

Type of device. This member can be one of the values listed in [MCI Device Types](mci-device-types.md).

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

[**MCI\_SYSINFO**](mci-sysinfo.md)
</dt> <dt>

[**mciSendCommand**](/previous-versions//dd757160(v=vs.85))
</dt> </dl>

 

