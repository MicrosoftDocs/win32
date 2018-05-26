---
title: StorPortIsDeviceOperationAllowed routine
description: A miniport driver can call the StorPortIsDeviceOperationAllowedminiport routine to determine if operations for a certain device management class are allowed.
ms.assetid: 2FA71DC1-8068-42E3-A5C0-903858E496FA
keywords:
- StorPortIsDeviceOperationAllowed routine Storage Devices
topic_type:
- apiref
api_name:
- StorPortIsDeviceOperationAllowed
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

# StorPortIsDeviceOperationAllowed routine

A miniport driver can call the **StorPortIsDeviceOperationAllowedminiport** routine to determine if operations for a certain device management class are allowed. A status value is set in the return parameter to indicate whether such operations are allowed or not allowed for the device in its current operating environment.

## Syntax


```C++
ULONG StorPortIsDeviceOperationAllowed(
  _In_  PVOID         HwDeviceExtension,
  _In_  PSTOR_ADDRESS Address,
  _In_  LPCGUID       DeviceOperation,
  _Out_ ULONG         *AllowedFlag
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

A pointer to the hardware device extension for the host bus adapter (HBA).

</dd> <dt>

*Address* \[in\]
</dt> <dd>

The address of a storage device unit.

</dd> <dt>

*DeviceOperation* \[in\]
</dt> <dd>

A pointer to a GUID specifying a device management operation class. The following GUID is valid.



| Value                                                                                                                                                                                                                                                                     | Meaning                                                                    |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| <span id="STORPORT_DEVICEOPERATION_SECURE_REPROVISION_GUID"></span><span id="storport_deviceoperation_secure_reprovision_guid"></span><dl> <dt>**STORPORT\_DEVICEOPERATION\_SECURE\_REPROVISION\_GUID**</dt> </dl> | The device is enabled to receive secured provisioning commands.<br/> |



 

</dd> <dt>

*AllowedFlag* \[out\]
</dt> <dd>

TRUE when the operation specified in *DeviceOperation* is allowed. Otherwise, FALSE.

</dd> </dl>

## Return value

The **StorPortIsDeviceOperationAllowed** routine returns one of these status codes:



| Return code                                                                                                     | Description                                                                                                                                                                                                                 |
|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**STOR\_STATUS\_SUCCESS**</dt> </dl>            | A valid value for *AllowedFlag* was returned.<br/>                                                                                                                                                                    |
| <dl> <dt>**STOR\_STATUS\_INVALID\_PARAMETER**</dt> </dl> | *Address* points to an invalid unit address structure.<br/> -or-<br/> The storage device specified by *Address* is not found.<br/> -or-<br/> The pointer value in *AllowedFlag* is NULL.<br/> |
| <dl> <dt>**STOR\_STATUS\_INVALID\_IRQL**</dt> </dl>      | The current IRQL &gt; PASSIVE\_LEVEL.<br/>                                                                                                                                                                            |
| <dl> <dt>**STOR\_STATUS\_NOT\_IMPLEMENTED**</dt> </dl>   | The management class specified in *DeviceOperation* is not available or invalid.<br/>                                                                                                                                 |



 

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Version<br/>         | Available in starting with Windows 8.1.<br/>                                                                                      |
| Header<br/>          | <dl> <dt>Storport.h</dt> </dl>                                                   |
| IRQL<br/>            | IRQL == PASSIVE\_LEVEL<br/>                                                                                                       |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortIsDeviceOperationAllowed%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





