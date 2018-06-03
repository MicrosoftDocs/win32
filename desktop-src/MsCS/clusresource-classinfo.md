---
title: ClusResource.ClassInfo property
description: Resource class of the resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0af280ef-ea5a-4cca-8065-2ee74d2dafc1
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- ClassInfo property Failover Cluster
- ClassInfo property Failover Cluster , ClusResource class
- ClusResource class Failover Cluster , ClassInfo property
topic_type:
- apiref
api_name:
- ClusResource.ClassInfo
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusResource.ClassInfo property

\[The **ClassInfo** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the resource class of the [resource](resources.md).

This property is read-only.

## Syntax


```VB
ClusResource.ClassInfo
```



## Property value

**Long** that receives the class information. **ClassInfo** returns one of the following values enumerated from the [**CLUSTER\_RESOURCE\_CLASS**](/previous-versions/windows/desktop/api/ClusAPI/ne-clusapi-cluster_resource_class) enumeration.

<dt>

<span id="CLUS_RESCLASS_UNKNOWN"></span><span id="clus_resclass_unknown"></span>

<span id="CLUS_RESCLASS_UNKNOWN"></span><span id="clus_resclass_unknown"></span>****CLUS\_RESCLASS\_UNKNOWN**** (0)


</dt> <dd>

Resource class is unknown.

</dd> <dt>

<span id="CLUS_RESCLASS_STORAGE"></span><span id="clus_resclass_storage"></span>

<span id="CLUS_RESCLASS_STORAGE"></span><span id="clus_resclass_storage"></span>****CLUS\_RESCLASS\_STORAGE**** (1)


</dt> <dd>

Resource is a storage device, such as a [*Physical Disk resource*](https://www.bing.com/search?q=*Physical Disk resource*).

</dd> <dt>

<span id="CLUS_RESCLASS_NETWORK"></span><span id="clus_resclass_network"></span>

<span id="CLUS_RESCLASS_NETWORK"></span><span id="clus_resclass_network"></span>****CLUS\_RESCLASS\_NETWORK**** (2)


</dt> <dd>

Resource is a [*network*](https://www.bing.com/search?q=*network*) device.

</dd> <dt>

<span id="CLUS_RESCLASS_USER"></span><span id="clus_resclass_user"></span>

<span id="CLUS_RESCLASS_USER"></span><span id="clus_resclass_user"></span>****CLUS\_RESCLASS\_USER**** (32768)


</dt> <dd>

Resource classes beginning at this value are user-defined.

</dd> </dl>

## Remarks

A [resource DLL](resource-dlls.md) that defines its own resource class should provide a unique identifier for the class that is set to a value greater than **CLUS\_RESCLASS\_USER** (32768). **CLUS\_RESCLASS\_USER** specifies the beginning for user-defined resource class identifiers.

For information on making constants defined by the Cluster Automation Server type library (MsClus.tlb) available to scripts, see [Creating a Cluster Automation Server Script](creating-a-cluster-automation-server-script.md).

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
</dt> <dt>

[**Cluster**](cluster-object.md)
</dt> <dt>

[**CLUSTER\_RESOURCE\_CLASS**](/previous-versions/windows/desktop/api/ClusAPI/ne-clusapi-cluster_resource_class)
</dt> </dl>

 

 





