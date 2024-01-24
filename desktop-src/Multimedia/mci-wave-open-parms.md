---
title: MCI_WAVE_OPEN_PARMS structure (Mciapi.h)
description: The MCI\_WAVE\_OPEN\_PARMS structure contains information for MCI\_OPEN command for waveform-audio devices.
ms.assetid: 2fc9383e-4610-4751-acad-b545dc6d8992
keywords:
- MCI_WAVE_OPEN_PARMS structure Windows Multimedia
topic_type:
- apiref
api_name:
- MCI_WAVE_OPEN_PARMS
api_location:
- mciapi.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCI\_WAVE\_OPEN\_PARMS structure

The **MCI\_WAVE\_OPEN\_PARMS** structure contains information for [**MCI\_OPEN**](mci-open.md) command for waveform-audio devices.

## Syntax


```C++
typedef struct {
  DWORD_PTR   dwCallback;
  MCIDEVICEID wDeviceID;
  LPCTSTR     lpstrDeviceType;
  LPCTSTR     lpstrElementName;
  LPCTSTR     lpstrAlias;
  DWORD       dwBufferSeconds;
} MCI_WAVE_OPEN_PARMS;
```



## Members

<dl> <dt>

**dwCallback**
</dt> <dd>

The low-order word specifies a window handle used for the MCI\_NOTIFY flag.

</dd> <dt>

**wDeviceID**
</dt> <dd>

Indentifier returned to application.

</dd> <dt>

**lpstrDeviceType**
</dt> <dd>

Name or constant identifier of the device type. (The name of the device is typically obtained from the registry or SYSTEM.INI file.) This member can be one of the values listed in [MCI Device Types](mci-device-types.md).

</dd> <dt>

**lpstrElementName**
</dt> <dd>

Device element name (usually a path).

</dd> <dt>

**lpstrAlias**
</dt> <dd>

Optional device alias.

</dd> <dt>

**dwBufferSeconds**
</dt> <dd>

Buffer length, in seconds.

</dd> </dl>

## Remarks

When assigning data to the members of this structure, set the corresponding flags in the *fdwCommand* parameter of the [**mciSendCommand**](/previous-versions//dd757160(v=vs.85)) function to validate the members.

You can use the [**MCI\_OPEN\_PARMS**](mci-open-parms.md) structure instead of **MCI\_WAVE\_OPEN\_PARMS** if you are not using the extended data members.

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

[**MCI\_OPEN**](mci-open.md)
</dt> <dt>

[**mciSendCommand**](/previous-versions//dd757160(v=vs.85))
</dt> <dt>

[**MCI\_OPEN\_PARMS**](mci-open-parms.md)
</dt> </dl>

 

