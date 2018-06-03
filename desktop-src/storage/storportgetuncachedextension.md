---
title: StorPortGetUncachedExtension routine
description: The StorPortGetUncachedExtension routine allocates an uncached common buffer to be shared by the CPU and the device.
ms.assetid: d5fa83d6-d733-4fff-89a9-f519ed608e57
keywords:
- StorPortGetUncachedExtension routine Storage Devices
topic_type:
- apiref
api_name:
- StorPortGetUncachedExtension
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

# StorPortGetUncachedExtension routine

The **StorPortGetUncachedExtension** routine allocates an uncached common buffer to be shared by the CPU and the device.

## Syntax


```C++
PVOID StorPortGetUncachedExtension(
   IN PVOID                           HwDeviceExtension,
   IN PPORT_CONFIGURATION_INFORMATION ConfigInfo,
   ULONG                              NumberOfBytes
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* 
</dt> <dd>

A pointer to the hardware device extension. This is a per HBA storage area that the port driver allocates and initializes on behalf of the miniport driver. Miniport drivers usually store HBA-specific information in this extension, such as the state of the HBA and the mapped access ranges for the HBA. This area is available to the miniport driver immediately after the miniport driver calls [**StorPortInitialize**](storportinitialize.md). The port driver frees this memory when it removes the device.

</dd> <dt>

*ConfigInfo* 
</dt> <dd>

Specifies information about the HBA's DMA capabilities. The following members must be filled in: **DmaChannel** or **DmaPort**, **DmaWidth**, **DmaSpeed**, **MaximumTransferLength**, **ScatterGather**, **Master** set to **TRUE**, **NumberOfPhysicalBreaks**, **AdapterInterfaceType**, **Dma32BitAddresses**, **Dma64BitAddresses**, **SystemIoBusNumber**, **AutoRequestSense**, and **SrbExtensionSize**.

Members that are not pertinent to the HBA, such as **DmaChannel** for an EISA bus-master adapter, must be left as is.

</dd> <dt>

*NumberOfBytes* 
</dt> <dd>

The size required, in bytes, of the uncached extension to allocate.

</dd> </dl>

## Return value

**StorPortGetUncachedExtension** returns a virtual address pointer to the uncached extension. If it cannot allocate the requested memory, it returns **NULL**. If the memory was previously allocated, the virtual address pointer to the current uncached extension is returned.

## Remarks

Bus-master devices use common buffer space for DMA transfers.

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| Library<br/>         | <dl> <dt>Storport.lib</dt> </dl>                                                 |



## See also

<dl> <dt>

[**ScsiPortGetUncachedExtension**](scsiportgetuncachedextension.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortGetUncachedExtension%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






