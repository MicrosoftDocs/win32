---
title: StorPortLogTelemetry routine
description: The StorPortLogTelemetry routine logs a miniport telemetry event to help diagnose or collect any useful information.
ms.assetid: 3B32F31C-3850-43D4-9C6E-40D35B8AF4D4
keywords:
- StorPortLogTelemetry routine Storage Devices
topic_type:
- apiref
api_name:
- StorPortLogTelemetry
api_location:
- storport.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# StorPortLogTelemetry routine

The **StorPortLogTelemetry** routine logs a miniport telemetry event to help diagnose or collect any useful information. The miniport can log eight general purpose name-value pairs and a buffer that has maximum length of 4KB, as well as several event related fields that are defined in structure [**STORPORT\_TELEMETRY\_EVENT**](storport-telemetry-event.md).

## Syntax


```C++
ULONG StorPortLogTelemetry(
  _In_     PVOID                     HwDeviceExtension ,
  _In_opt_ PSTOR_ADDRESS             StorAddress,
  _In_     PSTORPORT_TELEMETRY_EVENT Event
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

A pointer to the hardware device extension for the host bus adapter (HBA).

</dd> <dt>

*StorAddress* \[in, optional\]
</dt> <dd>

The storage unit device address. This parameter is NULL for adapter devices.

</dd> <dt>

*Event* \[in\]
</dt> <dd>

Pointer to the [**STORPORT\_TELEMETRY\_EVENT**](storport-telemetry-event.md) structure that contains the telemetry data payload.

</dd> </dl>

## Return value

**StorPortLogTelemetry** returns one of the following status codes:



| Return code                                                                                                        | Description                                                                                                                 |
|--------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**STOR\_STATUS\_INVALID\_BUFFER\_SIZE**</dt> </dl> | **EventBufferLength** is larger than **EVENT\_BUFFER\_MAX\_LENGTH**.<br/>                                             |
| <dl> <dt>**STOR\_STATUS\_INVALID\_PARAMETER**</dt> </dl>    | A pointer to one of the parameters is NULL or the EventBufferLength/EventBuffer in Event structure not matching.<br/> |
| <dl> <dt>**STOR\_STATUS\_NOT\_IMPLEMENTED**</dt> </dl>      | This function is not implemented on the active operating system.<br/>                                                 |
| <dl> <dt>**STATUS\_SUCCESS**</dt> </dl>                     | The telemetry event data have been successfully logged.<br/>                                                          |



 

## Remarks

If any parameter in Event structure is not named, Event-&gt;ParameterNameX == NULL, the routine will set the corresponding parameter value to 0.

If miniport has no payload to fill in Event-&gt;EventBuffer, it should set Event-&gt;EventBufferLength = 0, as well as Event-&gt;EventBuffer = NULL.

## Requirements



|                                     |                                                                                                            |
|-------------------------------------|------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1703<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                             |
| Header<br/>                   | <dl> <dt>Storport.h (include Storport.h)</dt> </dl> |
| IRQL<br/>                     | Any<br/>                                                                                             |



## See also

<dl> <dt>

[**STORPORT\_TELEMETRY\_EVENT**](storport-telemetry-event.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortLogTelemetry%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






