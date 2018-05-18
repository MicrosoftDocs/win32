---
title: StorPortGetVirtualAddress routine
description: The StorPortGetVirtualAddress routine obtains a virtual address that maps to the indicated physical address.
ms.assetid: 'b7091dea-8a29-4ad3-a478-29bc28fd57ef'
keywords: ["StorPortGetVirtualAddress routine Storage Devices"]
topic_type:
- apiref
api_name:
- StorPortGetVirtualAddress
api_location:
- Storport.lib
- Storport.dll
api_type:
- LibDef
---

# StorPortGetVirtualAddress routine

The **StorPortGetVirtualAddress** routine obtains a virtual address that maps to the indicated physical address.

## Syntax


```C++
STORPORT_API PVOID StorPortGetVirtualAddress(
  _In_ PVOID                 HwDeviceExtension,
  _In_ STOR_PHYSICAL_ADDRESS PhysicalAddress
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

A pointer to the hardware device extension. This is a per HBA storage area that the port driver allocates and initializes on behalf of the miniport driver. Miniport drivers usually store HBA-specific information in this extension, such as the state of the HBA and the mapped access ranges for the HBA. This area is available to the miniport driver immediately after the miniport driver calls [**StorPortInitialize**](storportinitialize.md). The port driver frees this memory when it removes the device.

</dd> <dt>

*PhysicalAddress* \[in\]
</dt> <dd>

Specifies the physical address to be mapped. This value must have been returned by [**StorPortGetPhysicalAddress**](storportgetphysicaladdress.md) and must be from an uncached device extension or SRB extension.

</dd> </dl>

## Return value

**StorPortGetVirtualAddress** returns a virtual address associated with the physical address indicated in the *PhysicalAddress* parameter. Typically, this physical address was obtained by a call to [**StorPortGetPhysicalAddress**](storportgetphysicaladdress.md).

## Remarks

The physical address must be an address that is obtained through a call to [**StorPortGetPhysicalAddress**](storportgetphysicaladdress.md).

**StorPortGetVirtualAddress** uses **STOR\_PHYSICAL\_ADDRESS** to represent physical addresses.


```C++
typedef PHYSICAL_ADDRESS STOR_PHYSICAL_ADDRESS, *PSTOR_PHYSICAL_ADDRESS;
```



The **STOR\_PHYSICAL\_ADDRESS** type is an operating system-independent data type that Storport miniport drivers use to represent either a physical addresses or a bus-relative address.

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| Library<br/>         | <dl> <dt>Storport.lib</dt> </dl>                                                 |



## See also

<dl> <dt>

[**ScsiPortGetVirtualAddress**](scsiportgetvirtualaddress.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortGetVirtualAddress%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






