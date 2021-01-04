---
title: MCI_OVLY_OPEN_PARMS structure (Mmsystem.h)
description: The MCI\_OVLY\_OPEN\_PARMS structure contains information for the MCI\_OPEN command for video-overlay devices.
ms.assetid: 1559ae40-4aa5-4dfc-b337-7b056c706b67
keywords:
- MCI_OVLY_OPEN_PARMS structure Windows Multimedia
topic_type:
- apiref
api_name:
- MCI_OVLY_OPEN_PARMS
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCI\_OVLY\_OPEN\_PARMS structure

The **MCI\_OVLY\_OPEN\_PARMS** structure contains information for the [**MCI\_OPEN**](mci-open.md) command for video-overlay devices.

## Syntax


```C++
typedef struct {
  DWORD_PTR   dwCallback;
  MCIDEVICEID wDeviceID;
  LPCTSTR     lpstrDeviceType;
  LPCTSTR     lpstrElementName;
  LPCTSTR     lpstrAlias;
  DWORD       dwStyle;
  DWORD       hWndParent;
} MCI_OVLY_OPEN_PARMS;
```



## Members

<dl> <dt>

**dwCallback**
</dt> <dd>

The low-order word specifies a window handle used for the MCI\_NOTIFY flag.

</dd> <dt>

**wDeviceID**
</dt> <dd>

Identifier returned to application.

</dd> <dt>

**lpstrDeviceType**
</dt> <dd>

Name or constant identifier of the device type. (The name of the device is typically obtained from the registry or SYSTEM.INI file.) If this member is a constant, it can be one of the values listed in [MCI Device Types](mci-device-types.md).

</dd> <dt>

**lpstrElementName**
</dt> <dd>

Device element name (usually a path).

</dd> <dt>

**lpstrAlias**
</dt> <dd>

Optional device alias.

</dd> <dt>

**dwStyle**
</dt> <dd>

Window style.

</dd> <dt>

**hWndParent**
</dt> <dd>

Handle to parent window.

</dd> </dl>

## Remarks

When assigning data to the members of this structure, set the corresponding flags in the *fdwCommand* parameter of the [**mciSendCommand**](/previous-versions//dd757160(v=vs.85)) function to validate the members.

You can use the [**MCI\_OPEN\_PARMS**](mci-open-parms.md) structure in place of **MCI\_OVLY\_OPEN\_PARMS** if you are not using the extended data members.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Mmsystem.h</dt> </dl> |



## See also

<dl> <dt>

[**MCI**](mci.md)
</dt> <dt>

[**MCI Structures**](mci-structures.md)
</dt> <dt>

[**MCI\_OPEN**](mci-open.md)
</dt> <dt>

[**MCI\_OPEN\_PARMS**](mci-open-parms.md)
</dt> <dt>

[**mciSendCommand**](/previous-versions//dd757160(v=vs.85))
</dt> </dl>

 

