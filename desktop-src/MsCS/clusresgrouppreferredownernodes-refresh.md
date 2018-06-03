---
title: ClusResGroupPreferredOwnerNodes.Refresh method
description: Refreshes the data in the ClusResGroupPreferredOwnerNodes collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 05085f9c-776c-4dc9-8c48-8157eeec6280
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Refresh method Failover Cluster
- Refresh method Failover Cluster , ClusResGroupPreferredOwnerNodes class
- ClusResGroupPreferredOwnerNodes class Failover Cluster , Refresh method
topic_type:
- apiref
api_name:
- ClusResGroupPreferredOwnerNodes.Refresh
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusResGroupPreferredOwnerNodes.Refresh method

\[The **Refresh** method is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Refreshes the data in the [**ClusResGroupPreferredOwnerNodes**](clusresgrouppreferredownernodes-collection.md) collection.

## Syntax


```VB
ClusResGroupPreferredOwnerNodes.Refresh()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

Any unsaved changes to the collection will be lost when the **Refresh** method is called. Use the [**ClusResGroupPreferredOwnerNodes.SaveChanges**](clusresgrouppreferredownernodes-savechanges.md) method to save changes to the collection.

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>                            |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>                  |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl>                |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl>                |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl>                |
| IID<br/>                      | IID\_ISClusResGroupPreferredOwnerNodes is defined as F2E606E8-2631-11D1-89F1-00A0C90D061E<br/> |



## See also

<dl> <dt>

[**ClusResGroupPreferredOwnerNodes**](clusresgrouppreferredownernodes-collection.md)
</dt> </dl>

 

 





