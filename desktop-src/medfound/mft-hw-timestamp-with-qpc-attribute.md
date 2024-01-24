---
description: Specifies whether a hardware device source uses the system time for time stamps.
ms.assetid: 54cdfa13-955a-4e92-b337-f645d526a1b8
title: MFT_HW_TIMESTAMP_WITH_QPC_Attribute attribute (Mftransform.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFT\_HW\_TIMESTAMP\_WITH\_QPC\_Attribute attribute

Specifies whether a hardware device source uses the system time for time stamps.

## Data type

**UINT32**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32).

To set this attribute, call [**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32).

## Remarks

If this attribute is **TRUE**, the device source uses the system time, as returned by the **QueryPerformanceCounter**, for time stamps. Otherwise, the device source uses the device's clock. The default value is **FALSE**.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps \| UWP apps\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps \| UWP apps\]<br/>                           |
| Header<br/>                   | <dl> <dt>Mftransform.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Capture Device Attributes](capture-device-attributes.md)
</dt> </dl>

 

 




