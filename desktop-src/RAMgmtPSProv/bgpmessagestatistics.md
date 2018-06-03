---
title: BgpMessageStatistics class
description: Retrieves the statistics of a Border Gateway Protocol (BGP) message.
audience: developer
ms.assetid: 82cc7a38-e70b-459a-8423-fa63ebc129b9
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- BgpMessageStatistics class
- BgpMessageStatistics class, described
topic_type:
- apiref
api_name:
- BgpMessageStatistics
- BgpMessageStatistics.LastSent
- BgpMessageStatistics.LastReceived
- BgpMessageStatistics.SentCount
- BgpMessageStatistics.ReceivedCount
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# BgpMessageStatistics class

Retrieves the statistics of a Border Gateway Protocol (BGP) message.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class BgpMessageStatistics
{
  datetime LastSent;
  datetime LastReceived;
  uint64   SentCount;
  uint64   ReceivedCount;
};
```

## Members

The **BgpMessageStatistics** class has these types of members:

-   [Properties](#properties)

### Properties

The **BgpMessageStatistics** class has these properties.

<dl> <dt>

**LastReceived**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The timestamp of the last BGP message received from the peer.

</dd> <dt>

**LastSent**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The timestamp of the last BGP message that was sent to the peer.

</dd> <dt>

**ReceivedCount**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total number of BGP messages received from the peer.

</dd> <dt>

**SentCount**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total number of the BGP messages that were sent to the peer.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[RAMgmtPSProvider Provider Classes](remote-access-management.md)
</dt> </dl>

 

 





