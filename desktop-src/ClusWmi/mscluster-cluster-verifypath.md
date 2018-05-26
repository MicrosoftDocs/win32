---
title: VerifyPath method of the MSCluster\_Cluster class
description: Verifies if the path is valid cluster storage for the resource group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: AF06CD57-DC94-4EED-88A5-AA2AD4E9D18D
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- VerifyPath method
- VerifyPath method, MSCluster_Cluster class
- MSCluster_Cluster class, VerifyPath method
topic_type:
- apiref
api_name:
- MSCluster_Cluster.VerifyPath
api_location:
- ClusWMI.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# VerifyPath method of the MSCluster\_Cluster class

Verifies if the path is valid cluster storage for the resource group.

## Syntax


```mof
void VerifyPath(
  [in]  string Path,
  [in]  string Group,
  [out] uint32 result
);
```



## Parameters

<dl> <dt>

*Path* \[in\]
</dt> <dd>

The path to verify.

</dd> <dt>

*Group* \[in\]
</dt> <dd>

The group to verify the path for.

</dd> <dt>

*result* \[out\]
</dt> <dd>

The result of the path validation.

<dt>

<span id="Valid"></span><span id="valid"></span><span id="VALID"></span>

**Valid** (0)


</dt> <dd></dd> <dt>

<span id="Available_Storage"></span><span id="available_storage"></span><span id="AVAILABLE_STORAGE"></span>

**Available Storage** (1)


</dt> <dd></dd> <dt>

<span id="Smb"></span><span id="smb"></span><span id="SMB"></span>

**Smb** (2)


</dt> <dd></dd> <dt>

<span id="Non_Cluster"></span><span id="non_cluster"></span><span id="NON_CLUSTER"></span>

**Non Cluster** (3)


</dt> <dd></dd> <dt>

<span id="Not_Valid"></span><span id="not_valid"></span><span id="NOT_VALID"></span>

**Not Valid** (128)


</dt> <dd></dd> <dt>

<span id="Not_In_Group"></span><span id="not_in_group"></span><span id="NOT_IN_GROUP"></span>

**Not In Group** (129)


</dt> <dd></dd> <dt>

<span id="Other_Group"></span><span id="other_group"></span><span id="OTHER_GROUP"></span>

**Other Group** (130)


</dt> <dd></dd> </dl> </dd> </dl>

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

[**MSCluster\_Cluster**](mscluster-cluster.md)
</dt> </dl>

 

 





