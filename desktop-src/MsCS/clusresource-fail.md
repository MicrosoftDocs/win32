---
title: ClusResource.Fail method
description: Initiates failure of the resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c184a7f3-b09a-4349-a940-20d622f729a6
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Fail method Failover Cluster
- Fail method Failover Cluster , ClusResource class
- ClusResource class Failover Cluster , Fail method
topic_type:
- apiref
api_name:
- ClusResource.Fail
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusResource.Fail method

\[The **Fail** method is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Initiates [failure](resource-failure.md) of the [resource](resources.md).

## Syntax


```VB
ClusResource.Fail()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

The **Fail** method causes the [*cluster*](https://www.bing.com/search?q=*cluster*) to initiate the same procedures that would result if the resource had actually failed. Use the **Fail** method to test [failover](failover.md) policies for resources and [groups](groups.md). For more information about resource failure policies, see [Resource Failure](resource-failure.md).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusResource is defined as F2E6070A-2631-11D1-89F1-00A0C90D061E<br/>     |



## See also

<dl> <dt>

[**ClusResource**](clusresource-object.md)
</dt> </dl>

 

 





