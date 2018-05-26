---
title: StorPortStateChangeDetected routine
description: Notifies the Storport port driver of a state change for a logical unit number (LUN), host bus adapter (HBA) port, or target device.
ms.assetid: 3E5E9C4E-5B82-4656-BDF2-23A9A8D40ADF
keywords:
- StorPortStateChangeDetected routine Storage Devices
topic_type:
- apiref
api_name:
- StorPortStateChangeDetected
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

# StorPortStateChangeDetected routine

Notifies the Storport port driver of a state change for a logical unit number (LUN), host bus adapter (HBA) port, or target device.

## Syntax


```C++
ULONG StorPortStateChangeDetected(
  _In_     PVOID            HwDeviceExtension,
  _In_     ULONG            ChangedEntity,
  _In_     PSTOR_ADDRESS    Address,
  _In_     ULONG            Attributes,
  _In_opt_ PHW_STATE_CHANGE HwStateChange,
  _In_opt_ ULONG            HwStateChangeContext
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

A pointer to the hardware device extension. This is a per-HBA storage area that the port driver allocates and initializes on behalf of the miniport driver. Miniport drivers usually store HBA-specific information in this extension, such as the state of the HBA and the mapped access ranges for the HBA. This area is available to the miniport driver immediately after the miniport driver calls [**StorPortInitialize**](storportinitialize.md). The port driver frees this memory when it removes the device.

</dd> <dt>

*ChangedEntity* \[in\]
</dt> <dd>

Flags indicating the entities whose state has changed. This is a bitwise **OR** combination of these values:



| Value                                                                                                                                                                                                                                         | Meaning                                   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| <span id="STATE_CHANGE_LUN"></span><span id="state_change_lun"></span><dl> <dt>**STATE\_CHANGE\_LUN**</dt> <dt>1 (0x1)</dt> </dl>          | LUN state has changed.<br/>         |
| <span id="STATE_CHANGE_TARGET"></span><span id="state_change_target"></span><dl> <dt>**STATE\_CHANGE\_TARGET**</dt> <dt>2 (0x2)</dt> </dl> | Target state has changed.<br/>      |
| <span id="STATE_CHANGE_BUS"></span><span id="state_change_bus"></span><dl> <dt>**STATE\_CHANGE\_BUS**</dt> <dt>4 (0x4)</dt> </dl>          | Bus or port state has changed.<br/> |



 

</dd> <dt>

*Address* \[in\]
</dt> <dd>

The address of the entity with the state change. *Address* value cannot change until the callback at *HwStateChange* is invoked. If *Address* is allocated in memory, the memory should be freed by the callback routine.

</dd> <dt>

*Attributes* \[in\]
</dt> <dd>

Attributes associated with the entity. These are a bitwise **OR** combination of the following:



| Value                                                                                                                                                                                                        | Meaning                                               |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| <span id="ATTRIBUTE_VM_PASSTHROUGH_LUN"></span><span id="attribute_vm_passthrough_lun"></span><dl> <dt>**ATTRIBUTE\_VM\_PASSTHROUGH\_LUN**</dt> </dl> | LUNs are reserved for virtual machine use.<br/> |



 

</dd> <dt>

*HwStateChange* \[in, optional\]
</dt> <dd>

A pointer to a callback routine supplied by the miniport. If present, the Storport driver will call this routine when the driver is finished processing this state change notification.

</dd> <dt>

*HwStateChangeContext* \[in, optional\]
</dt> <dd>

A miniport-supplied context value that is included when the routine set in *HwStateChange* is called.

</dd> </dl>

## Return value

A status value indicating the result of the notification. This can be one of these values:



| Return code                                                                                                     | Description                                                                     |
|-----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| <dl> <dt>**STOR\_STATUS\_SUCCESS**</dt> </dl>            | The state change notification is scheduled for processing.<br/>           |
| <dl> <dt>**STOR\_STATUS\_INVALID\_PARAMETER**</dt> </dl> | The address type or the entity type is invalid.<br/>                      |
| <dl> <dt>**STOR\_STATUS\_UNSUCCESSFUL**</dt> </dl>       | A prior notification is in process and this one cannot be scheduled.<br/> |



 

## Remarks

A successful call to **StorPortStateChangeDetected** results in re-enumeration of the changed entity.

Only one state change request can be active at any time. If a miniport needs to make another **StorPortStateChangeDetected** call, it should provide a *HwStateChange* callback and make another call to **StorPortStateChangeDetected** after the callback to *HwStateChange* occurs. If a miniport wants to indicate multiple state changes at the same time, the miniport can call **StorPortStateChangeDetected** once, with changed entities set in *ChangedEntity* that includes all of the current state changes.

If multiple flags are specified in *ChangedEntity*, the flag with greater value will have precedence over lesser ones.

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Version<br/>         | Available in Windows 8 and later versions of Windows.<br/>                                                                        |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| IRQL<br/>            | Any<br/>                                                                                                                          |



## See also

<dl> <dt>

[**HwStorStateChange**](hwstorstatechange.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortStateChangeDetected%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






