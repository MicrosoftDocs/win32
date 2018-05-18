---
title: MSFT\_CAUReportHelper class
description: A dynamic WMI class that represents operations to retrieve and save an updating run report.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '85f4eb19-ca10-4e50-8154-22af148a30bf'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-aware-patching'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_CAUReportHelper class", "MSFT_CAUReportHelper class, described"]
topic_type:
- apiref
api_name:
- MSFT_CAUReportHelper
- MSFT_CAUReportHelper.OrchestratorGuid
api_location:
- CauWmiV2.dll
api_type:
- DllExport
---

# MSFT\_CAUReportHelper class

A dynamic [*WMI class*](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents operations to retrieve and save an updating run report.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("CAUWMIV2"), AMENDMENT]
class MSFT_CAUReportHelper
{
  String OrchestratorGuid;
};
```

## Members

The **MSFT\_CAUReportHelper** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_CAUReportHelper** class has these methods.



| Method                                           | Description                                                                               |
|:-------------------------------------------------|:------------------------------------------------------------------------------------------|
| [**GetReport**](getreport-msft-caurun.md)       | Gets the contents of an updating run report.<br/>                                   |
| [**GetReportIDs**](getreportids-msft-caurun.md) | Gets identifiers for updating run reports that are stored on the current node.<br/> |
| [**PutReport**](putreport-msft-caurun.md)       | Saves a chunk of an updating run report on the current node.<br/>                   |



 

### Properties

The **MSFT\_CAUReportHelper** class has these properties.

<dl> <dt>

**OrchestratorGuid**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The identifier for the Update Coordinator that drives Cluster-Aware Updating (CAU) operations. Each Update Coordinator has a unique **OrchestratorGuid** value.

</dd> </dl>

## Remarks

An updating run report can be split into multiple chunks, as represented by the [**MSFT\_CAURun\_Report\_Chunk**](msft-caurun-report-chunk.md) class. Each chunk has a sequence number (starting at 0 for the first chunk) and a byte array containing the chunk data. To fetch a report, the requestor specifies the desired report's ID (which can be found using the [**GetReportIDs**](getreportids-msft-caurun.md) method) and chunk size in the [**GetReport**](getreport-msft-caurun.md) method, and the WMI provider responds by streaming a sequence of chunks in the requested report. To save a report, the caller splits a single report into multiple chunks and calls the [**PutReport**](putreport-msft-caurun.md) method once for each chunk until all chunks have been saved.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\Microsoft\\Windows\\ClusterUpdate<br/>                                      |
| MOF<br/>                      | <dl> <dt>CAUWMIv2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CauWmiV2.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_CAURun**](msft-caurun.md)
</dt> </dl>

 

 





