---
title: ShowMetricsByClass method of the CIM\_MetricService class
description: Indicates whether metric collection is enabled for each instance of the specified CIM class, and indicates the metrics that are available for collection for each of those class instances.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 109c0b28-1d04-4f9f-bd7c-620b585348ff
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ShowMetricsByClass method
- ShowMetricsByClass method, CIM_MetricService class
- CIM_MetricService class, ShowMetricsByClass method
topic_type:
- apiref
api_name:
- CIM_MetricService.ShowMetricsByClass
api_location:
- VMMS.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ShowMetricsByClass method of the CIM\_MetricService class

Indicates whether metric collection is enabled for each instance of the specified CIM class, and indicates the metrics that are available for collection for each of those class instances.

## Syntax


```mof
uint32 ShowMetricsByClass(
  [in]  CIM_ManagedElement       REF Subject,
  [in]  CIM_BaseMetricDefinition REF Definition,
  [out] CIM_BaseMetricDefinition REF DefinitionList[],
  [out] string                       MetricNames[],
  [out] uint16                       MetricCollectionEnabled[]
);
```



## Parameters

<dl> <dt>

*Subject* \[in\]
</dt> <dd>

A reference to the managed element that identifies the CIM class for which to retrieve metrics.

</dd> <dt>

*Definition* \[in\]
</dt> <dd>

A reference to the metric definition used to filter the class instances for which metrics are reported by this method.

</dd> <dt>

*DefinitionList* \[out\]
</dt> <dd>

If this method returns successfully, this parameter contains an array of references to the metric definitions of the metrics that are available for collection for each instance of the class indicated in the *Subject* parameter.

</dd> <dt>

*MetricNames* \[out\]
</dt> <dd>

If this method returns successfully, this parameter contains an array that contains the metric names for each metric definition in the *DefinitionList* array.

</dd> <dt>

*MetricCollectionEnabled* \[out\]
</dt> <dd>

If this method returns successfully, this parameter contains an array that indicates whether metric collection is enabled for each instance of the class indicated by the *Subject* parameter.

The possible values are:

<dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>**Enabled** (2)


</dt> <dd>

Enable

</dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>**Disabled** (3)


</dt> <dd>

Disable

</dd> <dt>

<span id="Reserved"></span><span id="reserved"></span><span id="RESERVED"></span>

<span id="Reserved"></span><span id="reserved"></span><span id="RESERVED"></span>**Reserved** (4)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved**


</dt> <dd></dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>**Vendor Reserved**


</dt> <dd></dd> </dl> </dd> </dl>

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

 

 





