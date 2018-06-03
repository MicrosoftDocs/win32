---
title: StorPortSetUnitAttributes routine
description: The StorPortSetUnitAttributes routine registers the power attributes of a storage unit device with the Storport driver.
ms.assetid: 0E05233D-79B0-4FC7-B13C-91B6B1F57E89
keywords:
- StorPortSetUnitAttributes routine Storage Devices
topic_type:
- apiref
api_name:
- StorPortSetUnitAttributes
api_location:
- Storport.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# StorPortSetUnitAttributes routine

The **StorPortSetUnitAttributes** routine registers the power attributes of a storage unit device with the Storport driver.

## Syntax


```C++
ULONG StorPortSetUnitAttributes(
  _In_ PVOID                HwDeviceExtension,
  _In_ PSTOR_ADDRESS        Address,
  _In_ STOR_UNIT_ATTRIBUTES Attributes
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

The storage unit device address. This parameter must not be NULL.

</dd> <dt>

*Attributes* \[in\]
</dt> <dd>

A set of bitfields indicating the attributes supported for the unit device.

</dd> </dl>

## Return value

**StorPortSetUnitAttributes** returns one of the following status codes:



| Return code                                                                                                     | Description                                                                                                                                                                                                                                                                                                        |
|-----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**STOR\_STATUS\_SUCCESS**</dt> </dl>            | Indicates that the routine set the unit attributes successfully.<br/>                                                                                                                                                                                                                                        |
| <dl> <dt>**STOR\_STATUS\_INVALID\_PARAMETER**</dt> </dl> | The *HwDeviceExtension* pointer is **NULL**.<br/> -or-<br/> One or more reserved bits in *Attributes* are set.<br/> -or-<br/> The unit address in *Address* is formatted incorrectly.<br/> -or-<br/> A unit device is not found for the address given in *Address*.<br/> |



 

## Remarks

A miniport driver will call this routine to register the unit attributes with Storport during completion of an SRB containing a SCSIOP\_INQUIRY command request. The bitfields in *attributes* are set based on the data returned from the adapter for the inquiry command. Storport will issue an inquiry for the unit at *Address* during a bus enumeration.

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Version<br/>         | Available starting with Windows 8.<br/>                                                                                           |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| IRQL<br/>            | Any<br/>                                                                                                                          |



## See also

<dl> <dt>

[**STOR\_ADDRESS**](stor-address.md)
</dt> <dt>

[**STOR\_UNIT\_ATTRIBUTES**](stor-unit-attributes.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortSetUnitAttributes%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






