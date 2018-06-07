---
title: StorPortWriteRegisterUshort routine
description: The StorPortWriteRegisterUshort routine transfers a ULONG value to the indicated HBA register address.
ms.assetid: f4beff75-6177-40c7-a62c-6e24bc54ea58
keywords:
- StorPortWriteRegisterUshort routine Storage Devices
topic_type:
- apiref
api_name:
- StorPortWriteRegisterUshort
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

# StorPortWriteRegisterUshort routine

The **StorPortWriteRegisterUshort** routine transfers a ULONG value to the indicated HBA register address.

## Syntax


```C++
STORPORT_API VOID StorPortWriteRegisterUshort(
  _In_ PVOID   HwDeviceExtension,
  _In_ PUSHORT Register,
  _In_ USHORT  Value
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

A pointer to the hardware device extension. This is a per HBA storage area that the port driver allocates and initializes on behalf of the miniport driver. Miniport drivers usually store HBA-specific information in this extension, such as the state of the HBA and the mapped access ranges for the HBA. This area is available to the miniport driver immediately after the miniport driver calls [**StorPortInitialize**](storportinitialize.md). The port driver frees this memory when it removes the device.

</dd> <dt>

*Register* \[in\]
</dt> <dd>

Pointer to the register. The given *Register* must be in a mapped memory space range returned by [**StorPortGetDeviceBase**](storportgetdevicebase.md).

</dd> <dt>

*Value* \[in\]
</dt> <dd>

Specifies the USHORT value to be written to the HBA's register.

</dd> </dl>

## Return value

None

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| Library<br/>         | <dl> <dt>Storport.lib</dt> </dl>                                                 |



## See also

<dl> <dt>

[**ScsiPortWriteRegisterUshort**](scsiportwriteregisterushort.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortWriteRegisterUshort%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






