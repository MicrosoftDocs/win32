---
Description: 'Contains partition information pulled from an ETW trace.'
ms.assetid: '8D8F8E79-B273-417A-B8C2-6CE4FC454C07'
title: 'ETW\_TRACE\_PARTITION\_INFORMATION structure'
---

# ETW\_TRACE\_PARTITION\_INFORMATION structure

Contains partition information pulled from an ETW trace. Most commonly used as a return structure for [**QueryTraceProcessingHandle**](querytraceprocessinghandle.md).

## Syntax


```C++
typedef struct _ETW_TRACE_PARTITION_INFORMATION {
  GUID    PartitionId;
  GUID    ParentId;
  ULONG64 Reserved;
  ULONG   PartitionType;
} ETW_TRACE_PARTITION_INFORMATION, *PETW_TRACE_PARTITION_INFORMATION;
```



## Members

<dl> <dt>

**PartitionId**
</dt> <dd>

GUID to identify the machine.

</dd> <dt>

**ParentId**
</dt> <dd>

GUID that identifies the partition instance that contains the traced partition. If the traced partition is a host, then **ParentId** will be 0.

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved for future use.

</dd> <dt>

**PartitionType**
</dt> <dd>

Enumeration value of the container type. the value may be one of the following:



| Value                                                                                                                                                                                                                                       | Meaning                                                                                                                                                                                                      |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Process"></span><span id="process"></span><span id="PROCESS"></span><dl> <dt>**Process**</dt> <dt>1</dt> </dl>                 | For events originating from inside a “Windows Server Container”.<br/>                                                                                                                                  |
| <span id="VmHost"></span><span id="vmhost"></span><span id="VMHOST"></span><dl> <dt>**VmHost**</dt> <dt>2</dt> </dl>                     | For events originating from inside a “Hyper-V Container”.<br/>                                                                                                                                         |
| <span id="VmHostedUvm"></span><span id="vmhosteduvm"></span><span id="VMHOSTEDUVM"></span><dl> <dt>**VmHostedUvm**</dt> <dt>3</dt> </dl> | For events originating from a “Hyper-V Container” template virtual machine.<br/>                                                                                                                       |
| <span id="VmDirectUvm"></span><span id="vmdirectuvm"></span><span id="VMDIRECTUVM"></span><dl> <dt>**VmDirectUvm**</dt> <dt>4</dt> </dl> | For events originating from applications running with [Windows Defender Application Guard](https://blogs.windows.com/msedgedev/2016/09/27/application-guard-microsoft-edge/#b7mtxirshs7blio7-97).<br/> |



 

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709 \[desktop apps only\]<br/>                             |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Evntrace.h</dt> </dl> |



 

 




