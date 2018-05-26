---
title: BgpRouteCounter class
description: Retrieves counters for Border Gateway Protocol (BGP) routes.
audience: developer
ms.assetid: 058046bc-204d-4185-9371-c3534ee98b84
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- BgpRouteCounter class
- BgpRouteCounter class, described
topic_type:
- apiref
api_name:
- BgpRouteCounter
- BgpRouteCounter.UpdateSentCount
- BgpRouteCounter.UpdateReceivedCount
- BgpRouteCounter.WithdrawlSentCount
- BgpRouteCounter.WithdrawlReceivedCount
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# BgpRouteCounter class

Retrieves counters for Border Gateway Protocol (BGP) routes.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class BgpRouteCounter
{
  uint64 UpdateSentCount;
  uint64 UpdateReceivedCount;
  uint64 WithdrawlSentCount;
  uint64 WithdrawlReceivedCount;
};
```

## Members

The **BgpRouteCounter** class has these types of members:

-   [Properties](#properties)

### Properties

The **BgpRouteCounter** class has these properties.

<dl> <dt>

**UpdateReceivedCount**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of BGP route updates received from the peer.

</dd> <dt>

**UpdateSentCount**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of BGP route updates sent to the peer.

</dd> <dt>

**WithdrawlReceivedCount**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of BGP route withdrawals received from the peer.

</dd> <dt>

**WithdrawlSentCount**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of BGP route withdrawals sent to the peer.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                               |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[RAMgmtPSProvider Provider Classes](remote-access-management.md)
</dt> </dl>

 

 





