---
title: RemoteAccessAccounting class
description: Remote Access Accounting Configuration.
audience: developer
ms.assetid: 382be70a-6b1c-4f94-8d52-7441cbe1525f
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemoteAccessAccounting class
- RemoteAccessAccounting class, described
topic_type:
- apiref
api_name:
- RemoteAccessAccounting
- RemoteAccessAccounting.InboxAccounting
- RemoteAccessAccounting.RadiusAccounting
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RemoteAccessAccounting class

Remote Access Accounting Configuration

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class RemoteAccessAccounting
{
  RemoteAccessInboxAccounting  InboxAccounting;
  RemoteAccessRadiusAccounting RadiusAccounting;
};
```

## Members

The **RemoteAccessAccounting** class has these types of members:

-   [Properties](#properties)

### Properties

The **RemoteAccessAccounting** class has these properties.

<dl> <dt>

**InboxAccounting**
</dt> <dd> <dl> <dt>

Data type: **RemoteAccessInboxAccounting**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**RemoteAccessInboxAccounting**](remoteaccessinboxaccounting.md)")
</dt> </dl>

[**RemoteAccessInboxAccounting**](remoteaccessinboxaccounting.md) embedded instance

</dd> <dt>

**RadiusAccounting**
</dt> <dd> <dl> <dt>

Data type: **RemoteAccessRadiusAccounting**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**RemoteAccessRadiusAccounting**](remoteaccessradiusaccounting.md)")
</dt> </dl>

[**RemoteAccessRadiusAccounting**](remoteaccessradiusaccounting.md) embedded instance

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





