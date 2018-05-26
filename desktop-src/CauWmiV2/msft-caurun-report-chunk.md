---
title: MSFT\_CAURun\_Report\_Chunk class
description: A dynamic WMI class that represents a chunk of input or output to be processed by the helper class of an updating run report.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6586fc0c-c5fc-452f-9d8d-4d3cbf3bdd66
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-aware-patching
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_CAURun_Report_Chunk class
- MSFT_CAURun_Report_Chunk class, described
topic_type:
- apiref
api_name:
- MSFT_CAURun_Report_Chunk
- MSFT_CAURun_Report_Chunk.Data
- MSFT_CAURun_Report_Chunk.SequenceNumber
- MSFT_CAURun_Report_Chunk.Timestamp
api_location:
- CauWmiV2.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_CAURun\_Report\_Chunk class

A dynamic [*WMI class*](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents a chunk of input or output to be processed by the helper class of an updating run report.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("CAUWMIV2"), AMENDMENT]
class MSFT_CAURun_Report_Chunk : MSFT_CAURun_Report_ID
{
  String   Data;
  Uint32   SequenceNumber;
  datetime Timestamp;
};
```

## Members

The **MSFT\_CAURun\_Report\_Chunk** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_CAURun\_Report\_Chunk** class has these properties.

<dl> <dt>

**Data**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The base64-encoded data for a chunk of the CAU updating run report.

</dd> <dt>

**SequenceNumber**
</dt> <dd> <dl> <dt>

Data type: **Uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The sequence number for a chunk within the CAU updating run report. Note that the sequence number for the first chunk is 0.

</dd> <dt>

**Timestamp**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A UTC timestamp that identifies when the CAU report was generated.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\Microsoft\\Windows\\ClusterUpdate<br/>                                      |
| MOF<br/>                      | <dl> <dt>CAUWMIv2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CauWmiV2.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_CAURun\_Report\_ID**](msft-caurun-report-id.md)
</dt> <dt>

[**GetReport**](getreport-msft-caurun.md)
</dt> <dt>

[**PutReport**](putreport-msft-caurun.md)
</dt> </dl>

 

 





