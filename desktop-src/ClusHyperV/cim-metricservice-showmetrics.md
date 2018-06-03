---
title: ShowMetrics method of the CIM\_MetricService class
description: Indicates whether metric collection is enabled for the specified managed elements, and indicates the metrics that are available for collection for each managed element.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 54fa254f-237b-4f89-a385-8ddcead4074b
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ShowMetrics method
- ShowMetrics method, CIM_MetricService class
- CIM_MetricService class, ShowMetrics method
topic_type:
- apiref
api_name:
- CIM_MetricService.ShowMetrics
api_location:
- VMMS.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ShowMetrics method of the CIM\_MetricService class

Indicates whether metric collection is enabled for the specified managed elements, and indicates the metrics that are available for collection for each managed element.

## Syntax


```mof
uint32 ShowMetrics(
  [in]  CIM_ManagedElement       REF Subject,
  [in]  CIM_BaseMetricDefinition REF Definition,
  [out] CIM_ManagedElement       REF ManagedElements[],
  [out] CIM_BaseMetricDefinition REF DefinitionList[],
  [out] string                       MetricNames[],
  [out] uint16                       MetricCollectionEnabled[]
);
```



## Parameters

<dl> <dt>

*Subject* \[in\]
</dt> <dd>

A reference to the managed element for which metrics are being collected.

</dd> <dt>

*Definition* \[in\]
</dt> <dd>

A reference to the metric definition that defines the metrics used to filter the results that are returned in the *ManagedElements* array. The *ManagedElements*array will return the managed elements for which the metrics indicated in the *Definition* property are available for collection.

</dd> <dt>

*ManagedElements* \[out\]
</dt> <dd>

If this method returns successfully, this parameter contains an array of references to the managed elements for which metric collection is available for the metric defined in the *Definition* parameter.

</dd> <dt>

*DefinitionList* \[out\]
</dt> <dd>

If this method returns successfully, this parameter contains an array of references to the metric definitions for the metrics that are available for collection for the managed element specified by the *Subject* parameter.

</dd> <dt>

*MetricNames* \[out\]
</dt> <dd>

If this method returns successfully, this parameter contains an array that contains the metric names for each metric definition in the *DefinitionList* array.

</dd> <dt>

*MetricCollectionEnabled* \[out\]
</dt> <dd>

If this method returns successfully, this parameter contains an array that indicates whether metric collection is enabled for each managed element in the *ManagedElements* array.

<dt>

<span id="Enable"></span><span id="enable"></span><span id="ENABLE"></span>

**Enable** (2)


</dt> <dd></dd> <dt>

<span id="Disable"></span><span id="disable"></span><span id="DISABLE"></span>

**Disable** (3)


</dt> <dd></dd> <dt>

<span id="Reserved"></span><span id="reserved"></span><span id="RESERVED"></span>

**Reserved** (4)


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

 

 





