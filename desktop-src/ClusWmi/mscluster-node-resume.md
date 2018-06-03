---
title: Resume method of the MSCluster\_Node class
description: Resumes the cluster activity on a node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4ee63461-8a7a-4f49-983c-70dc1ac767a6
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Resume method
- Resume method, MSCluster_Node class
- MSCluster_Node class, Resume method
topic_type:
- apiref
api_name:
- MSCluster_Node.Resume
api_location:
- ClusWMI.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Resume method of the MSCluster\_Node class

Resumes the cluster activity on a node.

## Syntax


```mof
void Resume(
  [in] uint32 FailbackType
);
```



## Parameters

<dl> <dt>

*FailbackType* \[in\]
</dt> <dd>

The type of failback which to perform.

<dt>

<span id="Do_Not_Failback_Groups"></span><span id="do_not_failback_groups"></span><span id="DO_NOT_FAILBACK_GROUPS"></span>

**Do Not Failback Groups** (0)


</dt> <dd></dd> <dt>

<span id="Failback_Groups_Immediately"></span><span id="failback_groups_immediately"></span><span id="FAILBACK_GROUPS_IMMEDIATELY"></span>

**Failback Groups Immediately** (1)


</dt> <dd></dd> <dt>

<span id="Failback_Groups_Per_Policy"></span><span id="failback_groups_per_policy"></span><span id="FAILBACK_GROUPS_PER_POLICY"></span>

**Failback Groups Per Policy** (2)


</dt> <dd></dd> <dt>

<span id="Resume_Failback_Type_Count"></span><span id="resume_failback_type_count"></span><span id="RESUME_FAILBACK_TYPE_COUNT"></span>

**Resume Failback Type Count** (3)


</dt> <dd></dd> </dl> </dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSCluster\_Node**](mscluster-node.md)
</dt> <dt>

[**Resume**](mscluster-node-resume.md)
</dt> </dl>

 

 





