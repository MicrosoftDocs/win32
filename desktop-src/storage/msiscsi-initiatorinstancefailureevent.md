---
title: MSiSCSI\_InitiatorInstanceFailureEvent structure
description: The MSiSCSI\_InitiatorInstanceFailureEvent structure is used to report an event when an initiator instance failure occurs.
ms.assetid: f0213dc9-7299-4cf7-b2c9-27e5d1caea00
keywords:
- MSiSCSI_InitiatorInstanceFailureEvent structure Storage Devices
- PMSiSCSI_InitiatorInstanceFailureEvent structure pointer Storage Devices
topic_type:
- apiref
api_name:
- MSiSCSI_InitiatorInstanceFailureEvent
api_location:
- iscsimgt.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MSiSCSI\_InitiatorInstanceFailureEvent structure

The MSiSCSI\_InitiatorInstanceFailureEvent structure is used to report an event when an initiator instance failure occurs.

## Syntax


```C++
typedef struct _MSiSCSI_InitiatorInstanceFailureEvent {
  UCHAR FailureType;
  WCHAR RemoteNodeName[223 + 1];
} MSiSCSI_InitiatorInstanceFailureEvent, *PMSiSCSI_InitiatorInstanceFailureEvent;
```



## Members

<dl> <dt>

**FailureType**
</dt> <dd>

A [ISCSI\_INITIATOR\_FAILURE\_TYPE\_QUALIFIERS](https://msdn.microsoft.com/library/windows/hardware/ff561533) value that indicates why the initiator instance failed.

</dd> <dt>

**RemoteNodeName**
</dt> <dd>

The name of the target that is associated with the initiator instance that is reporting a failure.

</dd> </dl>

## Remarks

We recommend that you implement this class.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsimgt.h (include Iscsimgt.h)</dt> </dl> |



## See also

<dl> <dt>

[ISCSI\_INITIATOR\_FAILURE\_TYPE\_QUALIFIERS](https://msdn.microsoft.com/library/windows/hardware/ff561533)
</dt> <dt>

[MSiSCSI\_InitiatorInstanceFailureEvent WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff563032)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MSiSCSI_InitiatorInstanceFailureEvent%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






