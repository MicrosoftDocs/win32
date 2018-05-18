---
title: StorPortValidateRange routine
description: The StorPortValidateRange routine determines whether a specified range of I/O addresses is in use by another adapter. This routine is obsolete in Windows NT 4.0 and later operating systems.
ms.assetid: '505d6986-c59d-46b3-8437-29fc6a808ccd'
keywords: ["StorPortValidateRange routine Storage Devices"]
topic_type:
- apiref
api_name:
- StorPortValidateRange
api_location:
- Storport.lib
- Storport.dll
api_type:
- LibDef
---

# StorPortValidateRange routine

The **StorPortValidateRange** routine determines whether a specified range of I/O addresses is in use by another adapter. This routine is obsolete in Windows NT 4.0 and later operating systems.

## Syntax


```C++
STORPORT_API BOOLEAN StorPortValidateRange(
  _In_ PVOID                 HwDeviceExtension,
  _In_ INTERFACE_TYPE        BusType,
  _In_ ULONG                 SystemToBusNumber,
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

Contains a value of type [**STORAGE\_BUS\_TYPE**](storage-bus-type.md) that indicates the bus type.

</dd> <dt>

*SystemToBusNumber* \[in\]
</dt> <dd>

Contains an integer identifying a system bus.

</dd> <dt>

*IoAddress* \[in\]
</dt> <dd>

Contains the beginning address of the range of addresses to be validated.

</dd> <dt>

*NumberOfBytes* \[in\]
</dt> <dd>

Contains the length in bytes of the range of addresses to be validated.

</dd> <dt>

*InIoSpace* \[in\]
</dt> <dd>

Indicates, when **TRUE**, that the address range is in I/O space. If **FALSE**, the address is in memory space.

</dd> </dl>

## Return value

**StorPortValidateRange** returns **TRUE** if a specified range of addresses is not claimed by another driver. This routine returns **FALSE** if another driver has claimed the address range.

## Remarks

For compatibility with older versions of Windows, this routine always returns **TRUE**.

Miniport drivers are given valid I/O ranges in the **AccessRanges** member of the [**PORT\_CONFIGURATION\_INFORMATION**](port-configuration-information--storport-.md) structure when the Storport driver calls the miniport's [**HwStorFindAdapter**](hwstorfindadapter.md) callback routine.

**StorPortValidateRange** uses **STOR\_PHYSICAL\_ADDRESS** to represent bus-relative addresses.


```C++
typedef PHYSICAL_ADDRESS STOR_PHYSICAL_ADDRESS, *PSTOR_PHYSICAL_ADDRESS;
```



The **STOR\_PHYSICAL\_ADDRESS** type is an operating system-independent data type that Storport miniport drivers use to represent either a physical addresses or a bus-relative address.

## Requirements



|                                 |                                                                                                                                         |
|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/>      | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>               | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| Library<br/>              | <dl> <dt>Storport.lib</dt> </dl>                                                 |
| DDI compliance rules<br/> | [**StorPortDeprecated**](https://msdn.microsoft.com/library/windows/hardware/hh454263)                                                                           |



## See also

<dl> <dt>

[**ScsiPortValidateRange**](scsiportvalidaterange.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortValidateRange%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






