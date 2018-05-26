---
title: StorPortConvertUlongToPhysicalAddress routine
description: The StorPortConvertUlongToPhysicalAddress routine converts an unsigned long address into a physical address.
ms.assetid: 772ca60b-a957-47de-b95d-486497b295ce
keywords:
- StorPortConvertUlongToPhysicalAddress routine Storage Devices
topic_type:
- apiref
api_name:
- StorPortConvertUlongToPhysicalAddress
api_location:
- Storport.lib
- Storport.dll
api_type:
- LibDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# StorPortConvertUlongToPhysicalAddress routine

The **StorPortConvertUlongToPhysicalAddress** routine converts an unsigned long address into a physical address.

## Syntax


```C++
STORPORT_API STOR_PHYSICAL_ADDRESS StorPortConvertUlongToPhysicalAddress(
  _In_ ULONG_PTR UlongAddress
);
```



## Parameters

<dl> <dt>

*UlongAddress* \[in\]
</dt> <dd>

Contains the address to be converted.

</dd> </dl>

## Return value

The **StorPortConvertUlongToPhysicalAddress** routine returns the physical address that corresponds to the unsigned long address that the caller passed in.

## Remarks

**StorPortConvertUlongToPhysicalAddress** uses **STOR\_PHYSICAL\_ADDRESS** to represent physical addresses.


```C++
typedef PHYSICAL_ADDRESS STOR_PHYSICAL_ADDRESS, *PSTOR_PHYSICAL_ADDRESS;
```



The **STOR\_PHYSICAL\_ADDRESS** type is an operating system-independent data type that Storport miniport drivers use to represent either a physical addresses or a bus-relative address.

The StorPortConvertPhysicalAddressToULong64 macro converts a physical address to a ULONG64 value.


```C++
ULONG64 StorPortConvertPhysicalAddressToULong64(
  [in] STOR_PHYSICAL_ADDRESS Address
);
```





| Term                                                                                                                     | Description                                                                                                                                                    |
|--------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Address__in_"></span><span id="address__in_"></span><span id="ADDRESS__IN_"></span>*Address \[in\]*<br/> | **STOR\_PHYSICAL\_ADDRESS**<br/> Specifies an address value of type STOR\_PHYSICAL\_ADDRESS.<br/>                                                  |
| <span id="Return_value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return value<br/>     | **ULONG64**<br/> **StorPortConvertPhysicalAddressToULong64** returns a ULONG64 value derived from the physical address that was passed to it.<br/> |



 

StorPortConvertPhysicalAddressToULong64 uses **STOR\_PHYSICAL\_ADDRESS** to represent physical addresses.

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| Library<br/>         | <dl> <dt>Storport.lib</dt> </dl>                                                 |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortConvertUlongToPhysicalAddress%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





