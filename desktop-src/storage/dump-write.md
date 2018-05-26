---
title: Dump\_Write routine
description: The Dump\_Write callback routine is called before the write to the dump port driver. The filter driver can access the dump data at this time.
ms.assetid: c7eda6a7-a1ce-43a3-b0e4-41f5afc61be6
keywords:
- Dump_Write routine Storage Devices
- PDUMP_WRITE
topic_type:
- apiref
api_name:
- Dump_Write
api_location:
- ntdddump.h
api_type:
- UserDefined
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Dump\_Write routine

The *Dump\_Write* callback routine is called before the write to the dump port driver. The filter driver can access the dump data at this time.

## Syntax


```C++
PDUMP_WRITE Dump_Write;

NTSTATUS Dump_Write(
  _In_    PFILTER_EXTENSION FilterExtension,
  _Inout_ PLARGE_INTEGER    DiskByteOffset,
  _Inout_ PMDL              Mdl
)
{ ... }
```



## Parameters

<dl> <dt>

*FilterExtension* \[in\]
</dt> <dd>

A pointer to a [**FILTER\_EXTENSION**](filter-extension.md) structure.

</dd> <dt>

*DiskByteOffset* \[in, out\]
</dt> <dd>

The value, in bytes, relative to the destination partition for the crash dump or hibernation. Filter drivers should not modify this field.

</dd> <dt>

*Mdl* \[in, out\]
</dt> <dd>

A pointer to an [**MDL**](https://msdn.microsoft.com/library/windows/hardware/ff554414) structure that describes the data buffer. If the **MDL** is modified, the size of the write operation cannot change.

</dd> </dl>

## Return value

If the routine succeeds, it must return STATUS\_SUCCESS. Otherwise, it must return one of the error status values defined in *Ntstatus.h*.

## Remarks

Filter drivers can read the data that needs to be written. However, filter drivers cannot write to the buffer, as this could change the contents of the code or data that is being used by the crash dump process. Also, filter drivers are not allowed to change the size of the data.

To safely modify the data for the dump write, a filter driver should allocate a secondary buffer. The buffer's size will be the value of the **MaxPagesPerWrite** member of [**FILTER\_INITIALIZATION\_DATA**](filter-initialization-data.md) multiplied by **PAGE\_SIZE**. The data for the current buffer described by *Mdl* is copied into the secondary buffer and processed. After the filter is finished handling the dump data in the secondary buffer, the [**MDL**](https://msdn.microsoft.com/library/windows/hardware/ff554414) pointed to by *Mdl* is updated with the address of the secondary buffer. The starting address of the secondary buffer set in the **MDL** must be page aligned.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Version<br/>         | Available starting with Windows Vista and Windows Server 2008.<br/>                                  |
| Header<br/>          | <dl> <dt>Ntdddump.h (include Ntdddump.h)</dt> </dl> |



## See also

<dl> <dt>

[*Dump\_Read*](dump-read.md)
</dt> <dt>

[**FILTER\_EXTENSION**](filter-extension.md)
</dt> <dt>

[**FILTER\_INITIALIZATION\_DATA**](filter-initialization-data.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20Dump_Write%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






