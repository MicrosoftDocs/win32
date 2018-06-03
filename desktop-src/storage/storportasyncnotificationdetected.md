---
title: StorPortAsyncNotificationDetected routine
description: A storage miniport driver calls StorPortAsyncNotificationDetected to notify the Storport driver of a storage device status change event.
ms.assetid: 558F652C-6D1A-4BAF-9C2C-3F4FE24651D2
keywords:
- StorPortAsyncNotificationDetected routine Storage Devices
topic_type:
- apiref
api_name:
- StorPortAsyncNotificationDetected
api_location:
- storport.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# StorPortAsyncNotificationDetected routine

A storage miniport driver calls **StorPortAsyncNotificationDetected** to notify the Storport driver of a storage device status change event.

The notification is queued as a work item for deferred processing at DISPATCH\_LEVEL or lower IRQL.

## Syntax


```C++
ULONG StorPortAsyncNotificationDetected(
  _In_ PVOID         HwDeviceExtension,
       PSTOR_ADDRESS Address,
       ULONGLONG     Flags
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

A pointer to the hardware device extension. This is a per-HBA storage area that the port driver allocates and initializes on behalf of the miniport driver. Miniport drivers usually store HBA-specific information in this extension, such as the state of the HBA and the mapped access ranges for the HBA. This area is available to the miniport driver immediately after the miniport driver calls [**StorPortInitialize**](storportinitialize.md). The port driver frees this memory when it removes the device.

</dd> <dt>

*Address* 
</dt> <dd>

The address of the storage device with a status change event.

</dd> <dt>

*Flags* 
</dt> <dd>

The status notifications to indicate to Storport.

The Flags parameter contains a bitwise OR combination of status notifications. All status values can be set with the single **RAID\_ASYNC\_NOTIFY\_SUPPORTED\_FLAGS** value.



| Value                                                                                                                                                                                                                                           | Meaning                                                                                  |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| <span id="RAID_ASYNC_NOTIFY_FLAG_MEDIA_STATUS"></span><span id="raid_async_notify_flag_media_status"></span><dl> <dt>**RAID\_ASYNC\_NOTIFY\_FLAG\_MEDIA\_STATUS**</dt> </dl>             | Notify Storport that a media change occurred.<br/>                                 |
| <span id="RAID_ASYNC_NOTIFY_FLAG_DEVICE_STATUS"></span><span id="raid_async_notify_flag_device_status"></span><dl> <dt>**RAID\_ASYNC\_NOTIFY\_FLAG\_DEVICE\_STATUS**</dt> </dl>          | Notify Storport that the functional status of the storage device has changed.<br/> |
| <span id="RAID_ASYNC_NOTIFY_FLAG_DEVICE_OPERATION"></span><span id="raid_async_notify_flag_device_operation"></span><dl> <dt>**RAID\_ASYNC\_NOTIFY\_FLAG\_DEVICE\_OPERATION**</dt> </dl> | Notify Storport that an operational role of the storage device has changed.<br/>   |



 

</dd> </dl>

## Return value

A status value indicating the result of the notification. This can be one of these values:



| Return code                                                                                                           | Description                                                                                                                                                      |
|-----------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**STOR\_STATUS\_SUCCESS**</dt> </dl>                  | The state change notification is scheduled for processing.<br/>                                                                                            |
| <dl> <dt>**STOR\_STATUS\_INVALID\_PARAMETER**</dt> </dl>       | The address type invalid.<br/> -or-<br/> *HwDeviceExtension* is **NULL**.<br/> -or-<br/> *Flags* contains an undefined value.<br/> |
| <dl> <dt>**STOR\_STATUS\_INVALID\_DEVICE\_REQUEST**</dt> </dl> | The storage device unit cannot be found at *address*.<br/> -or-<br/> The storage device does not support asynchronous notifications.<br/>      |
| <dl> <dt>**STOR\_STATUS\_BUSY**</dt> </dl>                     | A prior notification is in process and this one cannot be scheduled.<br/>                                                                                  |



 

## Remarks

A miniport can detect status events in its [**HwStorInterrupt**](hwstorinterrupt.md) routine and call **StorPortAsyncNotificationDetected** to queue and process the status change notification later at a lower IRQL.

When processed by Storport, the status event notification is forwarded to the storage class driver to initiate any necessary system response actions.

If the *Flags* parameter is 0, Storport will indicate all status values in its notification to the storage class driver.

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Version<br/>         | Available starting with Windows 8.<br/>                                                                                           |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| IRQL<br/>            | Any<br/>                                                                                                                          |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortAsyncNotificationDetected%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





