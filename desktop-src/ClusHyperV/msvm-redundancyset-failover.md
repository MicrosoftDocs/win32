---
title: Failover method of the Msvm\_RedundancySet class
description: Forces a failover from one managed element to another.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: aae6eba3-7ce4-47bc-a5b7-9921eab99b41
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Failover method
- Failover method, Msvm_RedundancySet class
- Msvm_RedundancySet class, Failover method
topic_type:
- apiref
api_name:
- Msvm_RedundancySet.Failover
api_location:
- VMMS.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Failover method of the Msvm\_RedundancySet class

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


</dt> <dd>

0

Completed with No Error

</dd> <dt>


</dt> <dd>

1

Not Supported

</dd> <dt>


</dt> <dd>

2

Unknown/Unspecified Error

</dd> <dt>


</dt> <dd>

3

Busy/In Use

</dd> <dt>


</dt> <dd>

4

Parameter Error

</dd> <dt>


</dt> <dd>

5 32767

DMTF Reserved

</dd> <dt>


</dt> <dd>

32768 65535

Vendor Reserved

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

[**Msvm\_RedundancySet**](msvm-redundancyset.md)
</dt> </dl>

 

 





