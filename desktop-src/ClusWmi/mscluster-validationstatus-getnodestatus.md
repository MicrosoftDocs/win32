---
title: GetNodeStatus method of the MSCluster\_ValidationStatus class
description: Gets the validation status of the node(s) not yet clustered.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 872C40AC-D8A2-4244-8DD5-9D561127D4A5
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetNodeStatus method
- GetNodeStatus method, MSCluster_ValidationStatus interface
- MSCluster_ValidationStatus interface, GetNodeStatus method
topic_type:
- apiref
api_name:
- MSCluster_ValidationStatus.GetNodeStatus
api_location:
- ClusWMI.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetNodeStatus method of the MSCluster\_ValidationStatus class

Gets the validation status of the node(s) not yet clustered.

## Syntax


```mof
void GetNodeStatus(
  [in]  string NodeNames[],
  [out] uint32 Status
);
```



## Parameters

<dl> <dt>

*NodeNames* \[in\]
</dt> <dd>

The nodes names to validate.

</dd> <dt>

*Status* \[out\]
</dt> <dd>

The status of the validation.

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

<span id="None"></span><span id="none"></span><span id="NONE"></span>**None** (0)


</dt> <dd></dd> <dt>

<span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span>

<span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span>**Completed** (1)


</dt> <dd></dd> <dt>

<span id="Has_UnselectedTests"></span><span id="has_unselectedtests"></span><span id="HAS_UNSELECTEDTESTS"></span>

<span id="Has_UnselectedTests"></span><span id="has_unselectedtests"></span><span id="HAS_UNSELECTEDTESTS"></span>**Has UnselectedTests** (2)


</dt> <dd></dd> <dt>

<span id="Has_Failures"></span><span id="has_failures"></span><span id="HAS_FAILURES"></span>

<span id="Has_Failures"></span><span id="has_failures"></span><span id="HAS_FAILURES"></span>**Has Failures** (4)


</dt> <dd></dd> <dt>

<span id="Has_Warnings"></span><span id="has_warnings"></span><span id="HAS_WARNINGS"></span>

<span id="Has_Warnings"></span><span id="has_warnings"></span><span id="HAS_WARNINGS"></span>**Has Warnings** (8)


</dt> <dd></dd> <dt>

<span id="Canceled"></span><span id="canceled"></span><span id="CANCELED"></span>

<span id="Canceled"></span><span id="canceled"></span><span id="CANCELED"></span>**Canceled** (16)


</dt> <dd></dd> <dt>

<span id="Has_Inapplicable_Tests"></span><span id="has_inapplicable_tests"></span><span id="HAS_INAPPLICABLE_TESTS"></span>

<span id="Has_Inapplicable_Tests"></span><span id="has_inapplicable_tests"></span><span id="HAS_INAPPLICABLE_TESTS"></span>**Has Inapplicable Tests** (64)


</dt> <dd>

**Windows Server 2012 R2 and Windows Server 2012:  **

This value is not supported before Windows Server 2016.

</dd> </dl> </dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSCluster\_ValidationStatus**](mscluster-validationstatus.md)
</dt> </dl>

 

 





