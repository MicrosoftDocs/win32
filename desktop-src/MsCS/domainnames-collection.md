---
title: DomainNames collection
description: Provides access to the names of the domains on a network.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e7f806a7-02e7-41be-b8b9-60351180e748
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- DomainNames collection Failover Cluster
- DomainNames collection Failover Cluster , described
topic_type:
- apiref
api_name:
- DomainNames
- ISDomainNames
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# DomainNames collection

\[The **DomainNames** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Provides access to the names of the domains on a [network](networks.md).

## Members

The **DomainNames** collection has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **DomainNames** collection has these methods.



| Method                                 | Description                                      |
|:---------------------------------------|:-------------------------------------------------|
| [**Refresh**](domainnames-refresh.md) | Refreshes the data in the collection.<br/> |



 

### Properties

The **DomainNames** collection has these properties.



| Property                                      | Description                                                 |
|:----------------------------------------------|:------------------------------------------------------------|
| [**Count**](domainnames-count.md)<br/> | Returns the number of objects in the collection.<br/> |
| [**Item**](domainnames-item.md)<br/>   | Returns a name of a domain from the collection.<br/>  |



 

## Remarks

A **DomainNames** collection:

-   Contains domain names.
-   Is obtained from [**ClusApplication.DomainNames**](clusapplication-domainnames.md).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISDomainNames is defined as F2E606E2-2631-11D1-89F1-00A0C90D061E<br/>      |



## See also

<dl> <dt>

[Application Management Objects](application-management-objects.md)
</dt> </dl>

 

 





