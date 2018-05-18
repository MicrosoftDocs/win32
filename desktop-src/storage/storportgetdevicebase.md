---
title: StorPortGetDeviceBase routine
description: The StorPortGetDeviceBase routine maps an I/O address to system address space.
ms.assetid: '6d25f2fb-be77-480f-b07c-294ab8a4272e'
keywords: ["StorPortGetDeviceBase routine Storage Devices"]
topic_type:
- apiref
api_name:
- StorPortGetDeviceBase
api_location:
- Storport.lib
- Storport.dll
api_type:
- LibDef
---

# StorPortGetDeviceBase routine

The **StorPortGetDeviceBase** routine maps an I/O address to system address space.

## Syntax


```C++
STORPORT_API PVOID StorPortGetDeviceBase(
  _In_ PVOID                 HwDeviceExtension,
  _In_ INTERFACE_TYPE        BusType,
  _In_ ULONG                 SystemIoBusNumber,
  _In_ STOR_PHYSICAL_ADDRESS IoAddress,
  _In_ ULONG                 NumberOfBytes,
  _In_ BOOLEAN               InIoSpace
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

A pointer to the hardware device extension. This is a per HBA storage area that the port driver allocates and initializes on behalf of the miniport driver. Miniport drivers usually store HBA-specific information in this extension, such as the state of the HBA and the mapped access ranges for the HBA. This area is available to the miniport driver immediately after the miniport driver calls [**StorPortInitialize**](storportinitialize.md). The port driver frees this memory when it removes the device.

</dd> <dt>

*BusType* \[in\]
</dt> <dd>

Specifies the interface type of the I/O bus on which the HBA is connected. The miniport driver's [**HwStorFindAdapter**](hwstorfindadapter.md) routine obtains the value for this parameter from the **AdapterInterfaceType** member of the input [**PORT\_CONFIGURATION\_INFORMATION**](port-configuration-information--storport-.md).

</dd> <dt>

*SystemIoBusNumber* \[in\]
</dt> <dd>

Specifies the system-assigned number of the I/O bus on which the HBA is connected. The [**HwStorFindAdapter**](hwstorfindadapter.md) routine obtains the value for this parameter from the **SystemIoBusNumber** member of the input [**PORT\_CONFIGURATION\_INFORMATION**](port-configuration-information--storport-.md).

</dd> <dt>

*IoAddress* \[in\]
</dt> <dd>

Specifies the bus-relative base address of a range used by the HBA. The [**HwStorFindAdapter**](hwstorfindadapter.md) routine obtains the value for this parameter from one of the **AccessRanges** elements in the [**PORT\_CONFIGURATION\_INFORMATION**](port-configuration-information--storport-.md) if the port driver supplies range-configuration information. Otherwise, this address can be a value returned by [**StorPortGetBusData**](storportgetbusdata.md) or a miniport driver-supplied default value. Avoid using a base address of zero because its successful return status can conflict with the error status (**NULL**).

</dd> <dt>

*NumberOfBytes* \[in\]
</dt> <dd>

Specifies the size in bytes of the range that the mapping should cover. The [**HwStorFindAdapter**](hwstorfindadapter.md) routine obtains the value of this parameter from the same **AccessRanges** element as *IoAddress* if the port driver supplies range configuration information. Otherwise, this value can be returned by [**StorPortGetBusData**](storportgetbusdata.md) or a miniport driver-supplied default. In any case, the driver must not access the hardware outside of the returned, mapped range.

</dd> <dt>

*InIoSpace* \[in\]
</dt> <dd>

TRUE indicates the range to be mapped is in I/O space, and the miniport driver will pass mapped addresses in this range to the Storport *port* read/write routines to communicate with the HBA. The [**HwStorFindAdapter**](hwstorfindadapter.md) routine obtains the value of this parameter from the same **AccessRanges** element as *IoAddress*. Note that a miniport driver *must invert* the value of the **InMemorySpace** member in an ACCESS\_RANGE-type element before it is passed to **StorPortGetDeviceBase** as the *InIoSpace* argument. **FALSE** indicates that the range to be mapped is in memory space.

</dd> </dl>

## Return value

A mapped, logical base address corresponding to the bus-relative address supplied in the *IoAddress* parameter.

## Remarks

Every miniport driver must pass mapped, logical access range addresses to the Storport *port* read/write routines and the Storport *register* read/write routines when communicating with its HBA(s).

This routine supports only those addresses that were assigned to the driver by the system Plug and Play (PnP) manager.

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| Library<br/>         | <dl> <dt>Storport.lib</dt> </dl>                                                 |



## See also

<dl> <dt>

[**StorPortFreeDeviceBase**](storportfreedevicebase.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortGetDeviceBase%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






