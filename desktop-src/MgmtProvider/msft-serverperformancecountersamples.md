---
title: MSFT\_ServerPerformanceCounterSamples class
description: Represents the list of performance counter samples collected from the managed node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'e9471956-11c2-4858-87de-2255461fbd1f'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_ServerPerformanceCounterSamples class", "MSFT_ServerPerformanceCounterSamples class, described"]
topic_type:
- apiref
api_name:
- MSFT_ServerPerformanceCounterSamples
- MSFT_ServerPerformanceCounterSamples.CounterPaths
- MSFT_ServerPerformanceCounterSamples.Timestamps
- MSFT_ServerPerformanceCounterSamples.Values
api_location:
- MgmtProvider.dll
api_type:
- DllExport
---

# MSFT\_ServerPerformanceCounterSamples class

Represents the list of performance counter samples collected from the managed node.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("mgmtprovider"), AMENDMENT]
class MSFT_ServerPerformanceCounterSamples
{
  string   CounterPaths[];
  datetime Timestamps[];
  string   Values[];
};
```

## Members

The **MSFT\_ServerPerformanceCounterSamples** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_ServerPerformanceCounterSamples** class has these properties.

<dl> <dt>

**CounterPaths**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The list of performance counters path that are in the sample.

</dd> <dt>

**Timestamps**
</dt> <dd> <dl> <dt>

Data type: **datetime** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time stamps of the samples.

</dd> <dt>

**Values**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The sample values of the counter paths.

</dd> </dl>

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                              |
| Namespace<br/>                | Root\\Windows\\ServerManager<br/>                                                     |
| MOF<br/>                      | <dl> <dt>MgmtProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MgmtProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**GetCounterSamplesAtTime method of MSFT\_ServerManagerTasks**](getcountersamplesattime-msft-servermanagertasks.md)
</dt> <dt>

[**GetCounterSamplesInTimeRange method of MSFT\_ServerManagerTasks**](getcountersamplesintimerange-msft-servermanagertasks.md)
</dt> </dl>

 

 





