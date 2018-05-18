---
title: FILTER\_INITIALIZATION\_DATA structure
description: The filter driver fills in a FILTER\_INITIALIZATION\_DATA structure and returns it to the crash dump driver.
ms.assetid: '71f9d0c2-ffc9-4fe1-ae95-f38a1d1e82df'
keywords: ["FILTER_INITIALIZATION_DATA structure Storage Devices", "PFILTER_INITIALIZATION_DATA structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- FILTER_INITIALIZATION_DATA
api_location:
- ntdddump.h
api_type:
- HeaderDef
---

# FILTER\_INITIALIZATION\_DATA structure

The filter driver fills in a **FILTER\_INITIALIZATION\_DATA** structure and returns it to the crash dump driver.

## Syntax


```C++
typedef struct _FILTER_INITIALIZATION_DATA {
  ULONG        MajorVersion;
  ULONG        MinorVersion;
  PDUMP_START  DumpStart;
  PDUMP_WRITE  DumpWrite;
  PDUMP_FINISH DumpFinish;
  PDUMP_UNLOAD DumpUnload;
  PVOID        DumpData;
  ULONG        MaxPagesPerWrite;
  ULONG        Flags;
  PDUMP_READ   DumpRead;
} FILTER_INITIALIZATION_DATA, *PFILTER_INITIALIZATION_DATA;
```



## Members

<dl> <dt>

**MajorVersion**
</dt> <dd>

Set to one of the following major version values:

<dl> <dt>

<span id="DUMP_FILTER_MAJOR_VERSION_1"></span><span id="dump_filter_major_version_1"></span>**DUMP\_FILTER\_MAJOR\_VERSION\_1** (0x1)
</dt> <dt>

<span id="DUMP_FILTER_MAJOR_VERSION"></span><span id="dump_filter_major_version"></span>**DUMP\_FILTER\_MAJOR\_VERSION** (0x2)
</dt> </dl> </dd> <dt>

**MinorVersion**
</dt> <dd>

Set to **DUMP\_FILTER\_MINOR\_VERSION**.

</dd> <dt>

**DumpStart**
</dt> <dd>

A pointer to the dump initialization routine. This routine is called when the crash dump starts.

</dd> <dt>

**DumpWrite**
</dt> <dd>

A pointer to the write routine. This routine is called before every crash dump write request.

</dd> <dt>

**DumpFinish**
</dt> <dd>

A pointer to the dump finish routine. This routine is called when the crash dump is finished.

</dd> <dt>

**DumpUnload**
</dt> <dd>

A pointer to the dump unload routine. This routine is called before the driver is unloaded.

</dd> <dt>

**DumpData**
</dt> <dd>

The filter driver can pass a pointer to internal context data in this member. This pointer is passed back to the filter driver in a [**FILTER\_EXTENSION**](filter-extension.md) structure during each callback.

</dd> <dt>

**MaxPagesPerWrite**
</dt> <dd>

The maximum number of pages for each dump read or write request.

</dd> <dt>

**Flags**
</dt> <dd>

A set of flags for dump filter initialization. This value is set to either 0 or the following:



| Value                                                                                                                                                                                                                                  | Meaning                                                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="DUMP_FILTER_FLAG_SYSTEM_SUPPORT_READ"></span><span id="dump_filter_flag_system_support_read"></span><dl> <dt>**DUMP\_FILTER\_FLAG\_SYSTEM\_SUPPORT\_READ**</dt> </dl> | The dump filter supports filtering reads, and a read callback routine is set for **DumpRead**. This flag is supported starting in Windows 8.<br/>                                  |
| <span id="DUMP_FILTER_CRITICAL"></span><span id="dump_filter_critical"></span><dl> <dt>**DUMP\_FILTER\_CRITICAL**</dt> </dl>                                                    | Fail the filter initialization immediately if the dump filter driver's **DriverEntry** routine does not return STATUS\_SUCCESS. This flag is supported starting in Windows 8.<br/> |



 

</dd> <dt>

**DumpRead**
</dt> <dd>

A pointer to the read routine. This routine is called after every crash dump read request. This member is available starting in Windows 8.

</dd> </dl>

## Remarks

For a dump filter driver to support read filtering, the following settings are required:

-   The **DUMP\_FILTER\_FLAG\_SYSTEM\_SUPPORT\_READ** flag is set in **Flags**.
-   **MajorVersion** is set to **DUMP\_FILTER\_MAJOR\_VERSION** = 2.
-   The **DumpRead** pointer is set to the dump filter driver's read routine.

If any of these members are not set, the dump filter driver will be marked as not supporting dump reads by the crashdump stack.

## Requirements



|                    |                                                                                                            |
|--------------------|------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows Vista and Windows Server 2008.<br/>                                  |
| Header<br/>  | <dl> <dt>Ntdddump.h (include Ntdddump.h)</dt> </dl> |



## See also

<dl> <dt>

[*Dump\_Finish*](dump-finish.md)
</dt> <dt>

[*Dump\_Read*](dump-read.md)
</dt> <dt>

[*Dump\_Start*](dump-start.md)
</dt> <dt>

[*Dump\_Write*](dump-write.md)
</dt> <dt>

[*Dump\_Unload*](dump-unload.md)
</dt> <dt>

[**FILTER\_EXTENSION**](filter-extension.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20FILTER_INITIALIZATION_DATA%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






