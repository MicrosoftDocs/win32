---
title: StorPortReadRegisterBufferUshort routine
description: The StorPortReadRegisterBufferUshort routine reads a value from a specified register address.
ms.assetid: 169f1089-ac17-4d4c-b989-018ff087aa39
keywords:
- StorPortReadRegisterBufferUshort routine Storage Devices
topic_type:
- apiref
api_name:
- StorPortReadRegisterBufferUshort
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

# StorPortReadRegisterBufferUshort routine

The **StorPortReadRegisterBufferUshort** routine reads a value from a specified register address.

## Syntax


```C++
STORPORT_API VOID StorPortReadRegisterBufferUshort(
  _In_ PVOID   HwDeviceExtension,
  _In_ PUSHORT Register,
  _In_ PUSHORT Buffer,
  _In_ ULONG   Count
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

Pointer to the hardware device extension.

</dd> <dt>

*Register* \[in\]
</dt> <dd>

Pointer to the register where the data is to be read.

</dd> <dt>

*Buffer* \[in\]
</dt> <dd>

Pointer to the buffer that receives the data that is read.

</dd> <dt>

*Count* \[in\]
</dt> <dd>

Number of data items to be read. Each data item has a size of **sizeof**(USHORT).

</dd> </dl>

## Return value

None

## Remarks

For more information, see [**ScsiPortReadRegisterBufferUshort**](scsiportreadregisterbufferushort.md). For a nonbuffered version of this routine, see [**StorPortReadRegisterUshort**](storportreadregisterushort.md).

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| Library<br/>         | <dl> <dt>Storport.lib</dt> </dl>                                                 |



## See also

<dl> <dt>

[**ScsiPortReadRegisterBufferUshort**](scsiportreadregisterbufferushort.md)
</dt> <dt>

[**StorPortReadRegisterUshort**](storportreadregisterushort.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortReadRegisterBufferUshort%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






