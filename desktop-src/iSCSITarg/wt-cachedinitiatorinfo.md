---
title: WT\_CachedInitiatorInfo class
description: Contains the iSCSI Qualified Name (IQN) of a cached initiator.The target caches initiators that have logged into the target, are manually typed in by the user, or are queried from an iSNS server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 289eb8f8-73e9-4572-afef-2058fd3670b2
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- WT_CachedInitiatorInfo class iSCSI Software Target API
- WT_CachedInitiatorInfo class iSCSI Software Target API , described
topic_type:
- apiref
api_name:
- WT_CachedInitiatorInfo
- WT_CachedInitiatorInfo.Name
api_location:
- WtWmiProv.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WT\_CachedInitiatorInfo class

Contains the iSCSI Qualified Name (IQN) of a cached initiator.

The target caches initiators that have logged into the target, are manually typed in by the user, or are queried from an iSNS server. Initiators that have not logged into the target for seven days are removed from the cache unless that initiator exists in an iSNS server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class WT_CachedInitiatorInfo
{
  string Name;
};
```

## Members

The **WT\_CachedInitiatorInfo** class has these types of members:

-   [Properties](#properties)

### Properties

The **WT\_CachedInitiatorInfo** class has these properties.

<dl> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

The initiator IQN.

</dd> </dl>

## Remarks

Microsoft iSCSI Target Server caches the IQNs of all initiators that connect to the service, all IQNs that were input manually by the user, and all IQNs discovered from ISNS servers. If the initiator does not connect within seven days, the IQN is purged from the list.

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\Wmi<br/>                                                                         |
| MOF<br/>                      | <dl> <dt>WmiWtProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WtWmiProv.dll</dt> </dl>     |



 

 





