---
title: DomainNames.Item property
description: Returns a single domain name from a DomainNames collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'b4d57afc-82d1-4cdd-8347-da9053cafdcb'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["Item property Failover Cluster", "Item property Failover Cluster , DomainNames collection", "DomainNames collection Failover Cluster , Item property"]
topic_type:
- apiref
api_name:
- DomainNames.Item
api_location:
- MsClus.dll
api_type:
- COM
---

# DomainNames.Item property

\[The **Item** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns a single domain name from a [**DomainNames**](domainnames-collection.md) collection.

This property is read-only.

## Syntax


```VB
DomainNames.Item( _
  ByVal varIndex _
)
```



## Property value

**String** that receives the name of a domain from the collection.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISDomainNames is defined as F2E606E2-2631-11D1-89F1-00A0C90D061E<br/>      |



## See also

<dl> <dt>

[**DomainNames.Count**](domainnames-count.md)
</dt> <dt>

[**DomainNames**](domainnames-collection.md)
</dt> </dl>

 

 





