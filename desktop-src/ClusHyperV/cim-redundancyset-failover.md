---
title: Failover method of the CIM\_RedundancySet class
description: Forces a failover from one managed element to another.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4efac7ce-83bf-4975-b9b2-fabc8a59fa5f
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Failover method
- Failover method, CIM_RedundancySet class
- CIM_RedundancySet class, Failover method
topic_type:
- apiref
api_name:
- CIM_RedundancySet.Failover
api_location:
- VMMS.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Failover method of the CIM\_RedundancySet class

Forces a failover from one managed element to another.

## Syntax


```mof
uint32 Failover(
  [in] CIM_ManagedElement REF FailoverFrom,
  [in] CIM_ManagedElement REF FailoverTo
);
```



## Parameters

<dl> <dt>

*FailoverFrom* \[in\]
</dt> <dd>

A reference to the primary managed system element that will become inactive.

</dd> <dt>

*FailoverTo* \[in\]
</dt> <dd>

A reference to the managed system element that will take over from the primary managed system element.

</dd> </dl>

## Return value

The possible return values are.

<dl> <dt>

**Completed with No Error**
</dt> <dd>

0

</dd> <dt>

**Not Supported**
</dt> <dd>

1

</dd> <dt>

**Unknown/Unspecified Error**
</dt> <dd>

2

</dd> <dt>

**Busy/In Use**
</dt> <dd>

3

</dd> <dt>

**Paramter Error**
</dt> <dd>

4

Parameter Error

</dd> <dt>

**DMTF Reserved**
</dt> <dd>

5 32767

</dd> <dt>

**Vendor Reserved**
</dt> <dd>

32768 65535

</dd> </dl>

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

[**CIM\_RedundancySet**](cim-redundancyset.md)
</dt> </dl>

 

 





