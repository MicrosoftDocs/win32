---
Description: Specifies the start time for presentations that are queued after the first presentation.
ms.assetid: 087f5d61-b3e6-4fdf-98e6-b018de7b237f
title: MF\_TOPOLOGY\_START\_TIME\_ON\_PRESENTATION\_SWITCH attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_TOPOLOGY\_START\_TIME\_ON\_PRESENTATION\_SWITCH attribute

Specifies the start time for presentations that are queued after the first presentation.

## Data type

**INT64** stored as **UINT64**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT64**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getuint64?branch=master).

To set this attribute, call [**IMFAttributes::SetUINT64**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setuint64?branch=master).

## Applies To

[**IMFTopology**](/windows/win32/mfidl/nn-mfidl-imftopology?branch=master)

## Remarks

When the application queues the first presentation on the Media Session, the application specifies the start time in the *pvarStartPosition* parameter of the [**IMFMediaSession::Start**](/windows/win32/mfidl/nf-mfidl-imfmediasession-start?branch=master) method. For any subsequent presentations, however, the start time is given by the MF\_TOPOLOGY\_START\_TIME\_ON\_PRESENTATION\_SWITCH attribute on the topology. The start time is specified in 100-nanosecond units, relative to the beginning of the presentation. For example, if the value is 50000000, playback starts 5 seconds into the presentation. If this attribute is not set, the default start time is zero.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                            |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Topology Attributes](topology-attributes.md)
</dt> </dl>

 

 




