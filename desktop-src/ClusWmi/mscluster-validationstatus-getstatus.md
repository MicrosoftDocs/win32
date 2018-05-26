---
title: GetStatus method of the MSCluster\_ValidationStatus class
description: Gets the status of the cluster validation.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: BFA9C882-9409-412B-993E-FCB4B4FA1206
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetStatus method
- GetStatus method, MSCluster_ValidationStatus interface
- MSCluster_ValidationStatus interface, GetStatus method
topic_type:
- apiref
api_name:
- MSCluster_ValidationStatus.GetStatus
api_location:
- ClusWMI.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetStatus method of the MSCluster\_ValidationStatus class

Gets the status of the cluster validation.

## Syntax


```mof
void GetStatus(
  [out] uint32 Status
);
```



## Parameters

<dl> <dt>

*Status* \[out\]
</dt> <dd>

The status of the validation. The possible values are a bit mask combining the following values.

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

<span id="None"></span><span id="none"></span><span id="NONE"></span>**None** (0)


</dt> <dd></dd> <dt>

<span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span>

<span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span>**Completed** (1)


</dt> <dd></dd> <dt>

<span id="Has_Unselected_Tests"></span><span id="has_unselected_tests"></span><span id="HAS_UNSELECTED_TESTS"></span>

<span id="Has_Unselected_Tests"></span><span id="has_unselected_tests"></span><span id="HAS_UNSELECTED_TESTS"></span>**Has Unselected Tests** (2)


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

 

 





