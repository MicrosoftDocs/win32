---
title: MSiSCSI\_EventLog structure
description: This MSiSCSI\_EventLog method is used to log any messages to the event log.
ms.assetid: 'a31a8688-6002-4ad7-b135-0a8111e2c849'
keywords: ["MSiSCSI_EventLog structure Storage Devices", "PMSiSCSI_EventLog structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- MSiSCSI_EventLog
api_location:
- Iscsimgt.h
api_type:
- HeaderDef
---

# MSiSCSI\_EventLog structure

This MSiSCSI\_EventLog method is used to log any messages to the event log.

## Syntax


```C++
typedef struct _MSiSCSI_EventLog {
  ULONG Type;
  ULONG LogToEventLog;
  ULONG Size;
  UCHAR AdditionalData[1];
} MSiSCSI_EventLog, *PMSiSCSI_EventLog;
```



## Members

<dl> <dt>

**Type**
</dt> <dd>

This specifies the EVENTLOG\_MESSAGE\_QUALIFIERS type of event log message.

</dd> <dt>

**LogToEventLog**
</dt> <dd>

If this value it set to 1, the message will be logged to the system event log.

</dd> <dt>

**Size**
</dt> <dd>

This specifies the size of the Additional Data field.

</dd> <dt>

**AdditionalData\[1\]**
</dt> <dd>

This provides additional information associated with this event.

</dd> </dl>

## Remarks

We recommend that you implement this class.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsimgt.h (include Iscsimgt.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MSiSCSI_EventLog%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





