---
title: StorPortGetSystemPortNumber routine
description: The StorPortGetSystemPortNumber routine retrieves the system assigned port number for a storage adapter.
ms.assetid: D1205C85-6F23-4D08-A146-2FA8C00FD6E9
keywords:
- StorPortGetSystemPortNumber routine Storage Devices
topic_type:
- apiref
api_name:
- StorPortGetSystemPortNumber
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

# StorPortGetSystemPortNumber routine

The **StorPortGetSystemPortNumber** routine retrieves the system assigned port number for a storage adapter.

## Syntax


```C++
ULONG StorPortGetSystemPortNumber(
  _In_    PVOID         HwDeviceExtension,
  _Inout_ PSTOR_ADDRESS Address
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

A pointer to the hardware device extension for the host bus adapter (HBA).

</dd> <dt>

*Address* \[in, out\]
</dt> <dd>

A pointer to a storage address structure formatted as [**STOR\_ADDR\_BTL8**](stor-addr-btl8.md). On return, the **Port** member of this structure will contain the port value assigned to the adapter.

</dd> </dl>

## Return value

**StorPortGetSystemPortNumber** returns one of the following status codes:



| Return code                                                                                                         | Description                                                                                                                                        |
|---------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**STOR\_STATUS\_INVALID\_DEVICE\_STATE**</dt> </dl> | A port number value is not yet assigned to the storage adapter.<br/>                                                                         |
| <dl> <dt>**STOR\_STATUS\_SUCCESS**</dt> </dl>                | Indicates that port number of the storage adapter was returned successfully.<br/>                                                            |
| <dl> <dt>**STOR\_STATUS\_INVALID\_PARAMETER**</dt> </dl>     | The *HwDeviceExtension* was **NULL**.<br/> -or-<br/> The **Type** member of *Address* is not **STOR\_ADDRESS\_TYPE\_BTL8**.<br/> |



 

## Remarks

The address structure pointed to by *Address* is allocated and formatted as [**STOR\_ADDR\_BTL8**](stor-addr-btl8.md). The **Type** member of *Address* must be set to **STOR\_ADDRESS\_TYPE\_BTL8** and the **Length** member *Address* must be greater than or equal to **STOR\_ADDR\_BTL8\_ADDRESS\_LENGTH**.

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Version<br/>         | Available in starting with Windows 8.<br/>                                                                                        |
| Header<br/>          | <dl> <dt>Storport.h</dt> </dl>                                                   |



## See also

<dl> <dt>

[**STOR\_ADDR\_BTL8**](stor-addr-btl8.md)
</dt> <dt>

[**STOR\_ADDRESS**](stor-address.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortGetSystemPortNumber%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






