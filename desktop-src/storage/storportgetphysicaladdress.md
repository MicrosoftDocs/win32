---
title: StorPortGetPhysicalAddress routine
description: The StorPortGetPhysicalAddress routine converts a given virtual address range to a physical address range for a DMA operation.
ms.assetid: 2b39a6e4-2e11-4b4e-9218-92336629ae80
keywords:
- StorPortGetPhysicalAddress routine Storage Devices
topic_type:
- apiref
api_name:
- StorPortGetPhysicalAddress
api_location:
- Storport.lib
- Storport.dll
api_type:
- LibDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# StorPortGetPhysicalAddress routine

The **StorPortGetPhysicalAddress** routine converts a given virtual address range to a physical address range for a DMA operation.

## Syntax


```C++
STORPORT_API STOR_PHYSICAL_ADDRESS StorPortGetPhysicalAddress(
  _In_     PVOID               HwDeviceExtension,
  _In_opt_ PSCSI_REQUEST_BLOCK Srb,
  _In_     PVOID               VirtualAddress,
  _Out_    ULONG               *Length
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

A pointer to the hardware device extension. This is a per HBA storage area that the port driver allocates and initializes on behalf of the miniport driver. Miniport drivers usually store HBA-specific information in this extension, such as the state of the HBA and the mapped access ranges for the HBA. This area is available to the miniport driver in the **DeviceExtension-&gt;HwDeviceExtension** member of the device object for the HBA immediately after the miniport driver calls [**StorPortInitialize**](storportinitialize.md). The port driver frees this memory when it removes the device.

</dd> <dt>

*Srb* \[in, optional\]
</dt> <dd>

Pointer to the SCSI request block if the virtual address to be converted comes from that SRB's **DataBuffer** member or **SenseInfoBuffer** member. Otherwise, this parameter must be **NULL**.

</dd> <dt>

*VirtualAddress* \[in\]
</dt> <dd>

Pointer to the base virtual address to be converted. If this virtual address falls within the range for an SRB-supplied **DataBuffer**, the caller also must provide the *Srb* pointer.

</dd> <dt>

*Length* \[out\]
</dt> <dd>

Pointer to a value indicating the number of bytes mapped, starting at the returned physical address.

</dd> </dl>

## Return value

**StorPortGetPhysicalAddress** returns the corresponding physical address for a given virtual address. If the given address cannot be converted, the function returns **NULL**.

## Remarks

If the virtual address passed to **StorPortGetPhysicalAddress** is obtained from [**StorPortAllocateContiguousMemorySpecifyCacheNode**](storportallocatecontiguousmemoryspecifycachenode.md), the value returned for *Length* should be ignored.

Starting in Windows 8, the *Srb* parameter may point to either [**SCSI\_REQUEST\_BLOCK**](scsi-request-block.md) or [**STORAGE\_REQUEST\_BLOCK**](storage-request-block.md). If the function identifier in the **Function** field of *Srb* is **SRB\_FUNCTION\_STORAGE\_REQUEST\_BLOCK**, the SRB is a **STORAGE\_REQUEST\_BLOCK** request structure.

**StorPortGetPhysicalAddress** uses **STOR\_PHYSICAL\_ADDRESS** to represent physical addresses.


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

[**SCSI\_REQUEST\_BLOCK**](scsi-request-block.md)
</dt> <dt>

[**ScsiPortGetPhysicalAddress**](scsiportgetphysicaladdress.md)
</dt> <dt>

[**STORAGE\_REQUEST\_BLOCK**](storage-request-block.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortGetPhysicalAddress%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






