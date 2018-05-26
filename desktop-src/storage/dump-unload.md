---
title: Dump\_Unload routine
description: The Dump\_Unload callback routine is called when the dump stack is unloaded.
ms.assetid: 51a04ca9-4ccd-409e-b47a-1105637e6f6f
keywords:
- Dump_Unload routine Storage Devices
- PDUMP_UNLOAD
topic_type:
- apiref
api_name:
- Dump_Unload
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

# Dump\_Unload routine

The *Dump\_Unload* callback routine is called when the dump stack is unloaded. For the dump stack, this routine is called when the crash dump functionality is disabled. For the hibernation stack, this routine is called after the system resumes from hibernation. This gives the filter driver an opportunity to free any resources that it may have allocated or do any clean-up required by the filter driver.

## Syntax


```C++
PDUMP_UNLOAD Dump_Unload;

NTSTATUS Dump_Unload(
  _In_ PFILTER_EXTENSION FilterExtension
)
{ ... }
```



## Parameters

<dl> <dt>

*FilterExtension* \[in\]
</dt> <dd>

A pointer to a [**FILTER\_EXTENSION**](filter-extension.md) structure.

</dd> </dl>

## Return value

If the routine succeeds, it must return STATUS\_SUCCESS. Otherwise, it must return one of the error status values defined in *Ntstatus.h*.

## Remarks

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Version<br/>         | Available starting with Windows Vista and Windows Server 2008.<br/>                                  |
| Header<br/>          | <dl> <dt>Ntdddump.h (include Ntdddump.h)</dt> </dl> |



## See also

<dl> <dt>

[**FILTER\_EXTENSION**](filter-extension.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20Dump_Unload%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






