---
title: ControlMetricsByClass method of the CIM\_MetricService class
description: Enables and disables the collection of metrics for the specified class.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ddbdfedf-47e8-4922-bcc7-e8383ff63e57
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ControlMetricsByClass method
- ControlMetricsByClass method, CIM_MetricService class
- CIM_MetricService class, ControlMetricsByClass method
topic_type:
- apiref
api_name:
- CIM_MetricService.ControlMetricsByClass
api_location:
- VMMS.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ControlMetricsByClass method of the CIM\_MetricService class

Enables and disables the collection of metrics for the specified class. This method controls the collection of each type of metric for all instances of a class, or the collection of a specific metric for all instances of a class.

## Syntax


```mof
uint32 ControlMetricsByClass(
  [in] CIM_ManagedElement       REF Subject,
  [in] CIM_BaseMetricDefinition REF Definition,
  [in] uint16                       MetricCollectionEnabled
);
```



## Parameters

<dl> <dt>

*Subject* \[in\]
</dt> <dd>

The class for which to modify metric collection.

</dd> <dt>

*Definition* \[in\]
</dt> <dd>

The definition of the metrics for which to modify metric collection.

</dd> <dt>

*MetricCollectionEnabled* \[in\]
</dt> <dd>

Indicates whether metric collection is enabled for the class.

The possible values are:

<dt>

<span id="Enable"></span><span id="enable"></span><span id="ENABLE"></span>

**Enable** (2)


</dt> <dd></dd> <dt>

<span id="Disable"></span><span id="disable"></span><span id="DISABLE"></span>

**Disable** (3)


</dt> <dd></dd> <dt>

<span id="Reset"></span><span id="reset"></span><span id="RESET"></span>

**Reset** (4)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>5 32767</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>32768 65535</dd> </dl> </dd> </dl>

## Return value

The possible return values are:

<dl> <dt>

**Success** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Failed** (2)
</dt> <dt>

**Method Reserved** (3 32767)
</dt> <dt>

**Vendor Specific** (32768 65535)
</dt> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**CIM\_MetricService**](cim-metricservice.md)
</dt> </dl>

 

 





