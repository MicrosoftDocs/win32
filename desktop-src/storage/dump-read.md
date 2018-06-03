---
title: Dump\_Read routine
description: The Dump\_Read callback routine is called after the read from the dump port driver. The filter driver can access the dump data during the call to this routine.
ms.assetid: 5F95D38C-8E11-49D4-82C4-718BD846A834
keywords:
- Dump_Read routine Storage Devices
- PDUMP_READ
topic_type:
- apiref
api_name:
- Dump_Read
api_location:
- ntdddump.h
api_type:
- UserDefined
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Dump\_Read routine

The *Dump\_Read* callback routine is called after the read from the dump port driver. The filter driver can access the dump data during the call to this routine.

## Syntax


```C++
PDUMP_READ Dump_Read;

NTSTATUS Dump_Read(
  _In_ PFILTER_EXTENSION FilterExtension,
  _In_ PLARGE_INTEGER    DiskByteOffset,
  _In_ PMDL              Mdl
)
{ ... }
```



## Parameters

<dl> <dt>

*FilterExtension* \[in\]
</dt> <dd>

A pointer to a [**FILTER\_EXTENSION**](filter-extension.md) structure.

</dd> <dt>

*DiskByteOffset* \[in\]
</dt> <dd>

The value, in bytes, relative to the source partition for the crash dump or hibernation. Filter drivers should not modify this field.

</dd> <dt>

*Mdl* \[in\]
</dt> <dd>

A pointer to an [**MDL**](https://msdn.microsoft.com/library/windows/hardware/ff554414) structure that describes the data buffer containing the dump data. Filter drivers should not modify this field.

</dd> </dl>

## Return value

If the routine succeeds, it must return STATUS\_SUCCESS. Otherwise, it must return one of the error status values defined in *Ntstatus.h*.

## Remarks

Filter drivers can read the data that was read by the crashdump process.

Filter drivers can modify the contents of the data buffer contained in **Mdl** to revert any changes made to the data when it was written to disk.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Version<br/>         | Available starting with Windows 8<br/>                                                               |
| Header<br/>          | <dl> <dt>Ntdddump.h (include Ntdddump.h)</dt> </dl> |



## See also

<dl> <dt>

[*Dump\_Write*](dump-write.md)
</dt> <dt>

[**FILTER\_EXTENSION**](filter-extension.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20Dump_Read%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






