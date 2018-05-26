---
title: HBA\_Pty\_EventInfo structure
description: The HBA\_Link\_EventInfo structure contains information about a WMI proprietary event associated with the fibre channel HBA API.
ms.assetid: 4291e6cd-9497-4106-82bf-c054108a0946
keywords:
- HBA_Pty_EventInfo structure Storage Devices
- HBA_PTY_EVENTINFO structure Storage Devices
- PHBA_PTY_EVENTINFO structure pointer Storage Devices
topic_type:
- apiref
api_name:
- HBA_PTY_EVENTINFO
api_location:
- hbaapi.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# HBA\_Pty\_EventInfo structure

The HBA\_Link\_EventInfo structure contains information about a WMI proprietary event associated with the fibre channel HBA API.

## Syntax


```C++
typedef struct HBA_Pty_EventInfo {
  HBA_UINT32 PtyData[4];
} HBA_PTY_EVENTINFO, *PHBA_PTY_EVENTINFO;
```



## Members

<dl> <dt>

**PtyData**
</dt> <dd>

Contains proprietary data defined by the vendor.

</dd> </dl>

## Requirements



|                   |                                                                                                        |
|-------------------|--------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbaapi.h (include Hbaapi.h)</dt> </dl> |



## See also

<dl> <dt>

[**HBA\_EventInfo**](hba-eventinfo.md)
</dt> <dt>

[**HBA\_Link\_EventInfo**](hba-link-eventinfo.md)
</dt> <dt>

[**HBA\_RSCN\_EventInfo**](hba-rscn-eventinfo.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HBA_Pty_EventInfo%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






