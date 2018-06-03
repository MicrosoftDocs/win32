---
title: Custom Injection of System Information
description: Kernel Trace Control allows custom injection of System Information when multiple trace files are merged into a single output trace file.
ms.assetid: 1f618d2a-2d8c-4074-b661-b058b052fb93
keywords:
- Custom Injection of System Information Windows Performance Analyzer
topic_type:
- apiref
api_name:
- Custom Injection of System Information
api_location:
- KernelTraceControl.dll
- KernelTraceControl.dll.dll
api_type:
- LibDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Custom Injection of System Information

Kernel Trace Control allows custom injection of System Information when multiple trace files are merged into a single output trace file. To include system information, a single flag or combination of flags is set in the [**CreateMergedTraceFile**](createmergedtracefile.md) function. The following flags define the system information to be added to the merged trace file:

<dl> <dt>

<span id="_define_EVENT_TRACE_MERGE_EXTENDED_DATA_NONE________________0x00000000"></span><span id="_define_event_trace_merge_extended_data_none________________0x00000000"></span><span id="_DEFINE_EVENT_TRACE_MERGE_EXTENDED_DATA_NONE________________0X00000000"></span>`#define EVENT_TRACE_MERGE_EXTENDED_DATA_NONE                0x00000000`
</dt> <dd>

No system information should be added to the merged trace file.

</dd> <dt>

<span id="_define_EVENT_TRACE_MERGE_EXTENDED_DATA_IMAGEID_____________0x00000001"></span><span id="_define_event_trace_merge_extended_data_imageid_____________0x00000001"></span><span id="_DEFINE_EVENT_TRACE_MERGE_EXTENDED_DATA_IMAGEID_____________0X00000001"></span>`#define EVENT_TRACE_MERGE_EXTENDED_DATA_IMAGEID             0x00000001`
</dt> <dd>

Inject image information such as checksum and timestamp used during symbol lookup.

</dd> <dt>

<span id="_define_EVENT_TRACE_MERGE_EXTENDED_DATA_BUILDINFO___________0x00000002"></span><span id="_define_event_trace_merge_extended_data_buildinfo___________0x00000002"></span><span id="_DEFINE_EVENT_TRACE_MERGE_EXTENDED_DATA_BUILDINFO___________0X00000002"></span>`#define EVENT_TRACE_MERGE_EXTENDED_DATA_BUILDINFO           0x00000002`
</dt> <dd>

Inject OS build information such as Product name and Build lab.

</dd> <dt>

<span id="_define_EVENT_TRACE_MERGE_EXTENDED_DATA_VOLUME_MAPPING______0x00000004"></span><span id="_define_event_trace_merge_extended_data_volume_mapping______0x00000004"></span><span id="_DEFINE_EVENT_TRACE_MERGE_EXTENDED_DATA_VOLUME_MAPPING______0X00000004"></span>`#define EVENT_TRACE_MERGE_EXTENDED_DATA_VOLUME_MAPPING      0x00000004`
</dt> <dd>

Inject volume mapping between DOS and NT paths. The payload of the event contains two **NULL** terminated Unicode strings. The first string contains the NT Path and the second string contains the DOS Path. The length of the payload is the size in bytes of the two strings including the **NULL** characters.

For example, an NT Path `"\Device\HarddiskVolume1\"` would be translated to the DOS Path `"C:\"`.

</dd> <dt>

<span id="_define_EVENT_TRACE_MERGE_EXTENDED_DATA_WINSAT__0x00000008"></span><span id="_define_event_trace_merge_extended_data_winsat__0x00000008"></span><span id="_DEFINE_EVENT_TRACE_MERGE_EXTENDED_DATA_WINSAT__0X00000008"></span>`#define EVENT_TRACE_MERGE_EXTENDED_DATA_WINSAT  0x00000008`
</dt> <dd>

Inject WinSat information.

</dd> <dt>

<span id="_define_EVENT_TRACE_MERGE_EXTENDED_DATA_EVENT_METADATA_0x00000010"></span><span id="_define_event_trace_merge_extended_data_event_metadata_0x00000010"></span><span id="_DEFINE_EVENT_TRACE_MERGE_EXTENDED_DATA_EVENT_METADATA_0X00000010"></span>`#define EVENT_TRACE_MERGE_EXTENDED_DATA_EVENT_METADATA 0x00000010`
</dt> <dd>

Inject trace data header (TDH) metadata for events that are captured on machines other than the machine where the events are being analyzed. The payload of the event is formatted as an [**TRACE\_EVENT\_INFO**](https://msdn.microsoft.com/library/windows/desktop/aa964853) structure.

For more information on trace data header information, see [MSDN](http://go.microsoft.com/fwlink/p/?linkid=141498).

</dd> <dt>

<span id="_define_EVENT_METADATA_LOG_TYPE_TRACE_EVENT_INFO____________0x20"></span><span id="_define_event_metadata_log_type_trace_event_info____________0x20"></span><span id="_DEFINE_EVENT_METADATA_LOG_TYPE_TRACE_EVENT_INFO____________0X20"></span>`#define EVENT_METADATA_LOG_TYPE_TRACE_EVENT_INFO            0x20`
</dt> <dd>

Inject trace information that identifies the events logged through EVENT\_TRACE\_MERGE\_EXTENDED\_DATA\_EVENT\_METADATA.

</dd> <dt>

<span id="_define_EVENT_METADATA_LOG_TYPE_EVENT_MAP_INFO__0x21"></span><span id="_define_event_metadata_log_type_event_map_info__0x21"></span><span id="_DEFINE_EVENT_METADATA_LOG_TYPE_EVENT_MAP_INFO__0X21"></span>`#define EVENT_METADATA_LOG_TYPE_EVENT_MAP_INFO  0x21`
</dt> <dd>

Inject information that defines the metadata for the events logged as a result of setting the EVENT\_TRACE\_MERGE\_EXTENDED\_DATA\_EVENT\_METADATA flag. For more information, see the [**EVENT\_MAP\_INFO**](https://msdn.microsoft.com/library/windows/desktop/aa964762) structure.

</dd> <dt>

<span id="_define_EVENT_TRACE_MERGE_EXTENDED_DATA_PERFTRACK_METADATA__0x00000020"></span><span id="_define_event_trace_merge_extended_data_perftrack_metadata__0x00000020"></span><span id="_DEFINE_EVENT_TRACE_MERGE_EXTENDED_DATA_PERFTRACK_METADATA__0X00000020"></span>`#define EVENT_TRACE_MERGE_EXTENDED_DATA_PERFTRACK_METADATA  0x00000020`
</dt> <dd>

Inject PerfTrack events metadata for decoding of PerfTrack events on different machines. These events are injected only on Windows7 and Windows Server 2008.

</dd> <dt>

<span id="_define_EVENT_TRACE_MERGE_EXTENDED_DATA_DEFAULT_____________0x000FFFFF"></span><span id="_define_event_trace_merge_extended_data_default_____________0x000fffff"></span><span id="_DEFINE_EVENT_TRACE_MERGE_EXTENDED_DATA_DEFAULT_____________0X000FFFFF"></span>`#define EVENT_TRACE_MERGE_EXTENDED_DATA_DEFAULT             0x000FFFFF`
</dt> <dd>

Inject the data for Image, Build, Volume mapping, WinSat, Event metadata, and PerfTrack metadata.

</dd> <dt>

<span id="_define_EVENT_TRACE_MERGE_EXTENDED_DATA_ALL_________________0xFFFFFFFF"></span><span id="_define_event_trace_merge_extended_data_all_________________0xffffffff"></span><span id="_DEFINE_EVENT_TRACE_MERGE_EXTENDED_DATA_ALL_________________0XFFFFFFFF"></span>`#define EVENT_TRACE_MERGE_EXTENDED_DATA_ALL                 0xFFFFFFFF`
</dt> <dd>

Inject all the extended data information to the output trace file.

</dd> </dl>

## Requirements



|                    |                                                                                                                                                                 |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available in Windows Vista and later versions of the Windows operating system. This structure is distributed with the Windows Performance Analyzer. <br/> |
| Header<br/>  | <dl> <dt>KernelTraceControl.h (include KernelTraceControl.h)</dt> </dl>                                  |
| Library<br/> | <dl> <dt>KernelTraceControl.dll</dt> </dl>                                                               |



## See also

<dl> <dt>

[**CreateMergedTraceFile**](createmergedtracefile.md)
</dt> </dl>

 

 





