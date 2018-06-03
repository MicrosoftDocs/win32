---
title: StorPortMarkDumpMemory routine
description: A miniport should mark memory used for the dump file or the hibernation file.
ms.assetid: DE17FF55-A573-41FE-8979-1DB32AD5B7C0
keywords:
- StorPortMarkDumpMemory routine Storage Devices
topic_type:
- apiref
api_name:
- StorPortMarkDumpMemory
api_location:
- Storport.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# StorPortMarkDumpMemory routine

A miniport should mark memory used for the dump file or the hibernation file. Marked memory is retained and remains valid after a resume from hibernation operation. The memory to mark is specified by an address and range length in a call to **StorPortMarkDumpMemory**.

## Syntax


```C++
ULONG StorPortMarkDumpMemory(
  _In_ PVOID HwDeviceExtension,
  _In_ PVOID Address,
  _In_ PVOID Length,
  _In_ PVOID Flags
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

A pointer to the hardware device extension for the host bus adapter (HBA).

</dd> <dt>

*Address* \[in\]
</dt> <dd>

The starting address of the memory range to mark.

</dd> <dt>

*Length* \[in\]
</dt> <dd>

The length of the marked memory range.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

Dump memory marking flags. The *Flags* parameter must be 0 or contain only the following value.



| Value                                                                                                                                                                                                                                        | Meaning                                                                                              |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| <span id="MARK_DUMP_MEMORY_FLAG_PHYSICAL_ADDRESS"></span><span id="mark_dump_memory_flag_physical_address"></span><dl> <dt>**MARK\_DUMP\_MEMORY\_FLAG\_PHYSICAL\_ADDRESS**</dt> </dl> | The address provided in *Address* is a physical address and not a system virtual address.<br/> |



 

</dd> </dl>

## Return value

**StorPortMarkDumpMemory** returns one of the following status codes:



| Return code                                                                                                     | Description                                                                 |
|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| <dl> <dt>**STOR\_STATUS\_SUCCESS**</dt> </dl>            | Indicates that the routine set the unit attributes successfully.<br/> |
| <dl> <dt>**STOR\_STATUS\_INVALID\_PARAMETER**</dt> </dl> | An invalid flag value was specified in the *Flags* parameter.<br/>    |



 

## Remarks

The **StorPortMarkDumpMemory** routine must only be called by a miniport driver in its [*DriverEntry*](https://msdn.microsoft.com/library/windows/hardware/ff544113) or [**HwStorFindAdapter**](hwstorfindadapter.md) routines.

If *Length* = 0, the entire section containing *Address* is marked.

Miniport drivers should call **StorPortMarkDumpMemory** to ensure that the memory used by the miniport to generate either the dump file or the hibernation file is identified. At a minimum, miniports should call **StorPortMarkDumpMemory** when the **DumpMode** member of [**PORT\_CONFIGURATION\_INFORMATION**](port-configuration-information--storport-.md) is set to either **DUMP\_MODE\_MARK\_MEMORY** or **DUMP\_MODE\_HIBER**.

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Version<br/>         | Available starting with Windows 8.<br/>                                                                                           |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| IRQL<br/>            | Any<br/>                                                                                                                          |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortMarkDumpMemory%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





