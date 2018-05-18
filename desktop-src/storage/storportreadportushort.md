---
title: StorPortReadPortUshort routine
description: The StorPortReadPortUshort routine reads a value from a specified port address.
ms.assetid: 'e5c9e91a-96b7-4774-8bb4-7519968ce072'
keywords: ["StorPortReadPortUshort routine Storage Devices"]
topic_type:
- apiref
api_name:
- StorPortReadPortUshort
api_location:
- Storport.lib
- Storport.dll
api_type:
- LibDef
---

# StorPortReadPortUshort routine

The **StorPortReadPortUshort** routine reads a value from a specified port address.

## Syntax


```C++
STORPORT_API USHORT StorPortReadPortUshort(
  _In_ PVOID   HwDeviceExtension,
  _In_ PUSHORT Port
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

Pointer to the hardware device extension.

</dd> <dt>

*Port* \[in\]
</dt> <dd>

Pointer to the address from which to read.

</dd> </dl>

## Return value

**StorPortReadPortUshort** returns a data item of length **sizeof**(USHORT).

## Remarks

For more information, see [**ScsiPortReadPortBufferUshort**](scsiportreadportbufferushort.md). For a buffered version of this routine, see [**StorPortReadPortBufferUshort**](storportreadportbufferushort.md).

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| Library<br/>         | <dl> <dt>Storport.lib</dt> </dl>                                                 |



## See also

<dl> <dt>

[**ScsiPortReadPortBufferUshort**](scsiportreadportbufferushort.md)
</dt> <dt>

[**StorPortReadPortBufferUshort**](storportreadportbufferushort.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortReadPortUshort%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






