---
title: STOR\_LOG\_EVENT\_DETAILS structure
description: The STOR\_LOG\_EVENT\_DETAILS structure provides details pertaining to Storport-specific error log events and system log events.
ms.assetid: '2370e730-6c35-45e6-a370-62adc10df53b'
keywords: ["STOR_LOG_EVENT_DETAILS structure Storage Devices", "PSTOR_LOG_EVENT_DETAILS structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- STOR_LOG_EVENT_DETAILS
api_location:
- storport.h
api_type:
- HeaderDef
---

# STOR\_LOG\_EVENT\_DETAILS structure

The **STOR\_LOG\_EVENT\_DETAILS** structure provides details pertaining to Storport-specific error log events and system log events.

## Syntax


```C++
typedef struct _STOR_LOG_EVENT_DETAILS {
  ULONG                       InterfaceRevision;
  ULONG                       Size;
  ULONG                       Flags;
  STOR_EVENT_ASSOCIATION_ENUM EventAssociation;
  ULONG                       PathId;
  ULONG                       TargetId;
  ULONG                       LunId;
  BOOLEAN                     StorportSpecificErrorCode;
  ULONG                       ErrorCode;
  ULONG                       UniqueId;
  ULONG                       DumpDataSize;
  PVOID                       DumpData;
  ULONG                       StringCount;
  PWSTR                       *StringList;
} STOR_LOG_EVENT_DETAILS, *PSTOR_LOG_EVENT_DETAILS;
```



## Members

<dl> <dt>

**InterfaceRevision**
</dt> <dd>

The revision number of this interface. Set to STOR\_CURRENT\_LOG\_INTERFACE\_REVISION to use the version of the interface that matches this structure. Both the constant and the data structure are defined in the same header file. This member is set to 0x00000100 for the first revision.

</dd> <dt>

**Size**
</dt> <dd>

The size of this structure. Set before calling [**StorPortLogSystemEvent**](storportlogsystemevent.md).

</dd> <dt>

**Flags**
</dt> <dd>

Not currently used. Must be zero.

</dd> <dt>

**EventAssociation**
</dt> <dd>

Specifies whether the event should be associated with the adapter, the target, or the LUN. For adapter- and target-associated events, the event is logged against the adapter's device object. For LUN-associated events, the event is logged against the LUN's device object if it exists; otherwise, it is logged against the adapter's device object.

</dd> <dt>

**PathId**
</dt> <dd>

The SCSI path/bus corresponding to this event.

</dd> <dt>

**TargetId**
</dt> <dd>

The SCSI target controller or device on the bus corresponding to this event.

</dd> <dt>

**LunId**
</dt> <dd>

The SCSI logical unit number of the target device corresponding to this event.

</dd> <dt>

**StorportSpecificErrorCode**
</dt> <dd>

If the **ErrorCode** value is specific to Storport and should be translated for use with IOLOGMSG.DLL, this value is set to **TRUE**. If the **ErrorCode** value is not specific to Storport and should be passed directly to the system event logging facility, this value is set to **FALSE**.

</dd> <dt>

**ErrorCode**
</dt> <dd>

The event error code to log.

</dd> <dt>

**UniqueId**
</dt> <dd>

Specifies a unique identifier associated with the ErrorCode. Often this is used as a location code, referencing the location in the miniport that triggered the event. This value is passed directly to the event logging facility.

</dd> <dt>

**DumpDataSize**
</dt> <dd>

The size of the miniport-specific data block that is to be appended to the log entry. If no data block is to be written, this should be set to 0.

</dd> <dt>

**DumpData**
</dt> <dd>

Pointer to the miniport-specific data block that is to be appended to the log entry. If no data block is to be written, DumpDataSize should be set to 0, and this field is ignored.

</dd> <dt>

**StringCount**
</dt> <dd>

The count of null-terminated Unicode strings contained in the StringList member. If no strings are to be written, this should be set to 0.

</dd> <dt>

**StringList**
</dt> <dd>

The list of null-terminated Unicode strings to be appended to the log entry for use in string substitution. These strings are substituted for the place holders "%2" through "%n" in the log message text when the log entry is being displayed. This list consists of an array of pointers to the null-terminated Unicode strings. StringCount contains the count of string pointers in this array, so no list termination entry is needed. If no strings are to be written, StringCount should be set to 0, and this field is ignored.

</dd> </dl>

## Remarks

Although [**StorPortLogError**](storportlogerror.md) uses **PathId**, **TargetId**, and **LunId** values that are 8bits wide, for [**StorPortLogSystemEvent**](storportlogsystemevent.md) they are 32bits wide. The combined size of the miniport driver's dump data and string areas cannot exceed 150 bytes. This restriction is due to the &lt; 255 byte limit that the kernel enforces on the event log entries.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Storport.h (include Storport.h)</dt> </dl> |



## See also

<dl> <dt>

[**STOR\_EVENT\_ASSOCIATION\_ENUM**](stor-event-association-enum.md)
</dt> <dt>

[**StorPortLogSystemEvent**](storportlogsystemevent.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STOR_LOG_EVENT_DETAILS%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






