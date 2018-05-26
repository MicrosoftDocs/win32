---
title: MSFT\_CAURun\_Report\_ID class
description: A dynamic WMI class that identifies an updating run report.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d9413988-b7c4-4cc3-901c-2a911e7dc842
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-aware-patching
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_CAURun_Report_ID class
- MSFT_CAURun_Report_ID class, described
topic_type:
- apiref
api_name:
- MSFT_CAURun_Report_ID
- MSFT_CAURun_Report_ID.Timestamp
api_location:
- CauWmiV2.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_CAURun\_Report\_ID class

A dynamic [*WMI class*](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that identifies an updating run report.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("CAUWMIV2"), AMENDMENT]
class MSFT_CAURun_Report_ID
{
  datetime Timestamp;
};
```

## Members

The **MSFT\_CAURun\_Report\_ID** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_CAURun\_Report\_ID** class has these properties.

<dl> <dt>

**Timestamp**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A UTC timestamp that identifies when the updating run report was generated.

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

[**GetReport**](getreport-msft-caurun.md)
</dt> <dt>

[**GetReportIDs**](getreportids-msft-caurun.md)
</dt> </dl>

 

 





