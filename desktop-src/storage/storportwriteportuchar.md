---
title: StorPortWritePortUchar routine
description: The StorPortWritePortUchar routine writes a value to a specified register address.
ms.assetid: '421bd075-e919-4389-af38-e0dd686f7c05'
keywords: ["StorPortWritePortUchar routine Storage Devices"]
topic_type:
- apiref
api_name:
- StorPortWritePortUchar
api_location:
- Storport.lib
- Storport.dll
api_type:
- LibDef
---

# StorPortWritePortUchar routine

The **StorPortWritePortUchar** routine writes a value to a specified register address.

## Syntax


```C++
STORPORT_API VOID StorPortWritePortUchar(
  _In_ PVOID  HwDeviceExtension,
  _In_ PUCHAR Port,
  _In_ UCHAR  Value
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

Contains the address of the port to be written to.

</dd> <dt>

*Value* \[in\]
</dt> <dd>

Contains the value to be written.

</dd> </dl>

## Return value

None

## Remarks

For more information, see [**ScsiPortWritePortUchar**](scsiportwriteportuchar.md). For a buffered equivalent of this routine, see [**StorPortWritePortBufferUchar**](storportwriteportbufferuchar.md).

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| Library<br/>         | <dl> <dt>Storport.lib</dt> </dl>                                                 |



## See also

<dl> <dt>

[**ScsiPortWritePortUchar**](scsiportwriteportuchar.md)
</dt> <dt>

[**StorPortWritePortBufferUchar**](storportwriteportbufferuchar.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortWritePortUchar%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






