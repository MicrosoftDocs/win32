---
title: StorPortWriteRegisterBufferUlong64 routine
description: This StorPortWriteRegisterBufferUlong64 routine writes a number of ULONG64 values from a the specified 64-bit register address.
ms.assetid: 3C36DB8F-46C2-4E81-B2F3-6DE78D91566E
keywords:
- StorPortWriteRegisterBufferUlong64 routine Storage Devices
topic_type:
- apiref
api_name:
- StorPortWriteRegisterBufferUlong64
api_location:
- storport.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# StorPortWriteRegisterBufferUlong64 routine

This **StorPortWriteRegisterBufferUlong64** routine writes a number of **ULONG64** values from a the specified 64-bit register address.

## Syntax


```C++
 VOID StorPortWriteRegisterBufferUlong64(
  _In_ PULONG64  Register,
  _In_ PULONG64  Buffer,
  _In_ ULONG     Count
);
```



## Parameters

<dl> <dt>

*Register* \[in\]
</dt> <dd>

Pointer to the register where the data is written to. The register must be a mapped range in memory space

</dd> <dt>

*Buffer* \[in\]
</dt> <dd>

Pointer to the buffer to write the **ULONG64** values from.

</dd> <dt>

*Count* \[in\]
</dt> <dd>

Specifies the number of data values to write. Each data item has a size of **sizeof**(ULONG64).

</dd> </dl>

## Return value

This routine does not return a value.

## Remarks

The **StorPortWriteRegisterBufferUlong64** routine is only available on the 64-bit version of Windows.

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Version<br/>         | Available starting with Windows 8.<br/>                                                                                           |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |



## See also

<dl> <dt>

[**StorPortReadRegisterBufferUlong64**](storportreadregisterbufferulong64.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortWriteRegisterBufferUlong64%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






