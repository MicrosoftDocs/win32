---
title: STORPORT\_TELEMETRY\_EVENT structure
description: The STORPORT\_TELEMETRY\_EVENT structure describes the miniport telemetry data payload.
ms.assetid: 50A3EB6D-C485-4C04-8E88-9BD7D7ED0A62
keywords:
- STORPORT_TELEMETRY_EVENT structure Storage Devices
- PSTORPORT_TELEMETRY_EVENT structure pointer Storage Devices
topic_type:
- apiref
api_name:
- STORPORT_TELEMETRY_EVENT
api_location:
- storport.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# STORPORT\_TELEMETRY\_EVENT structure

The **STORPORT\_TELEMETRY\_EVENT** structure describes the miniport telemetry data payload.

## Syntax


```C++
typedef struct _STORPORT_TELEMETRY_EVENT {
  ULONG                                             DriverVersion;
  ULONG                                             EventId;
  UCHAR                                             EventName[EVENT_NAME_MAX_LENGTH];
  ULONG                                             EventVersion;
  ULONG                                             Flags;
  _Field_range_(0, EVENT_BUFFER_MAX_LENGTH)
  ULONG EventBufferLength;
  _Field_size_bytes_(EventBufferLength)
    PUCHAR  EventBuffer;
  UCHAR                                             ParameterName0[EVENT_MAX_PARAM_NAME_LEN];
  ULONGLONG                                         ParameterValue0;
  UCHAR                                             ParameterName1[EVENT_MAX_PARAM_NAME_LEN];
  ULONGLONG                                         ParameterValue1;
  UCHAR                                             ParameterName2[EVENT_MAX_PARAM_NAME_LEN];
  ULONGLONG                                         ParameterValue2;
  UCHAR                                             ParameterName3[EVENT_MAX_PARAM_NAME_LEN];
  ULONGLONG                                         ParameterValue3;
  UCHAR                                             ParameterName4[EVENT_MAX_PARAM_NAME_LEN];
  ULONGLONG                                         ParameterValue4;
  UCHAR                                             ParameterName5[EVENT_MAX_PARAM_NAME_LEN];
  ULONGLONG                                         ParameterValue5;
  UCHAR                                             ParameterName6[EVENT_MAX_PARAM_NAME_LEN];
  ULONGLONG                                         ParameterValue6;
  UCHAR                                             ParameterName7[EVENT_MAX_PARAM_NAME_LEN];
  ULONGLONG                                         ParameterValue7;
} STORPORT_TELEMETRY_EVENT, *PSTORPORT_TELEMETRY_EVENT;
```



## Members

<dl> <dt>

**DriverVersion**
</dt> <dd>

Miniport driver version.

</dd> <dt>

**EventId**
</dt> <dd>

A miniport defined identifier for the telemetry event.

</dd> <dt>

**EventName**
</dt> <dd>

A miniport defined name for the telemetry event, which has the maximum length of **EVENT\_NAME\_MAX\_LENGTH**.

</dd> <dt>

**EventVersion**
</dt> <dd>

A miniport defined version for the telemetry event.

</dd> <dt>

**Flags**
</dt> <dd>

Reserved.

</dd> <dt>

**EventBufferLength**
</dt> <dd>

The length of **EventBuffer**, which should be not larger than **EVENT\_BUFFER\_MAX\_LENGTH** that is 4KB.

</dd> <dt>

**EventBuffer**
</dt> <dd>

A miniport defined telemetry payload, the length of which is **EventBufferLength**.

</dd> <dt>

**ParameterName0**
</dt> <dd>

A description of the of the meaning of ParameterValue0. This parameter name string must be &lt;= EVENT\_MAX\_PARAM\_NAME\_LEN.

</dd> <dt>

**ParameterValue0**
</dt> <dd>

The value for parameter 0.

</dd> <dt>

**ParameterName1**
</dt> <dd>

A description of the of the meaning of ParameterValue1. This parameter name string must be &lt;= EVENT\_MAX\_PARAM\_NAME\_LEN.

</dd> <dt>

**ParameterValue1**
</dt> <dd>

The value for parameter 1.

</dd> <dt>

**ParameterName2**
</dt> <dd>

A description of the of the meaning of ParameterValue2. This parameter name string must be &lt;= EVENT\_MAX\_PARAM\_NAME\_LEN.

</dd> <dt>

**ParameterValue2**
</dt> <dd>

The value for parameter 2.

</dd> <dt>

**ParameterName3**
</dt> <dd>

A description of the of the meaning of ParameterValue3. This parameter name string must be &lt;= EVENT\_MAX\_PARAM\_NAME\_LEN.

</dd> <dt>

**ParameterValue3**
</dt> <dd>

The value for parameter 3.

</dd> <dt>

**ParameterName4**
</dt> <dd>

A description of the of the meaning of ParameterValue4. This parameter name string must be &lt;= EVENT\_MAX\_PARAM\_NAME\_LEN.

</dd> <dt>

**ParameterValue4**
</dt> <dd>

The value for parameter 4.

</dd> <dt>

**ParameterName5**
</dt> <dd>

A description of the of the meaning of ParameterValue5. This parameter name string must be &lt;= EVENT\_MAX\_PARAM\_NAME\_LEN.

</dd> <dt>

**ParameterValue5**
</dt> <dd>

The value for parameter 5.

</dd> <dt>

**ParameterName6**
</dt> <dd>

A description of the of the meaning of ParameterValue6. This parameter name string must be &lt;= EVENT\_MAX\_PARAM\_NAME\_LEN.

</dd> <dt>

**ParameterValue6**
</dt> <dd>

The value for parameter 6.

</dd> <dt>

**ParameterName7**
</dt> <dd>

A description of the of the meaning of ParameterValue7. This parameter name string must be &lt;= EVENT\_MAX\_PARAM\_NAME\_LEN.

</dd> <dt>

**ParameterValue7**
</dt> <dd>

The value for parameter 7.

</dd> </dl>

## Remarks

A **STORPORT\_TELEMETRY\_EVENT** structure describes the miniport telemetry data payload. The miniport should fill it when calling StorPortLogTelemetry.

## Requirements



|                                     |                                                                                                            |
|-------------------------------------|------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1703<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                             |
| Header<br/>                   | <dl> <dt>Storport.h (include Storport.h)</dt> </dl> |



## See also

<dl> <dt>

[**StorPortLogTelemetry**](storportlogtelemetry.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORPORT_TELEMETRY_EVENT%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






