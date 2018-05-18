---
title: PS\_RemoteAccessInboxAccountingLocal class
description: Represents the various types of accounting supported for Remote Access.
audience: developer
ms.assetid: '6d576e5a-5463-40f7-abff-f2af82e9b369'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["PS_RemoteAccessInboxAccountingLocal class", "PS_RemoteAccessInboxAccountingLocal class, described"]
topic_type:
- apiref
api_name:
- PS_RemoteAccessInboxAccountingLocal
api_location:
- RAServerPSProvider.dll
api_type:
- DllExport
---

# PS\_RemoteAccessInboxAccountingLocal class

Represents the various types of accounting supported for Remote Access.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAServerPSProvider"), AMENDMENT]
class PS_RemoteAccessInboxAccountingLocal
{
};
```

## Members

The **PS\_RemoteAccessInboxAccountingLocal** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_RemoteAccessInboxAccountingLocal** class has these methods.



| Method                                                                                             | Description                                          |
|:---------------------------------------------------------------------------------------------------|:-----------------------------------------------------|
| [**CleanInboxAccountingStore**](cleaninboxaccountingstore-ps-remoteaccessinboxaccountinglocal.md) | Get the status for Inbox accounting store<br/> |
| [**Get**](get-ps-remoteaccessinboxaccountinglocal.md)                                             | Get the status for Inbox accounting<br/>       |
| [**Set**](set-ps-remoteaccessinboxaccountinglocal.md)                                             | Set the status for Inbox accounting<br/>       |



 

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                    |
| Namespace<br/>                | Root\\microsoft\\windows\\remoteaccess\\server<br/>                                         |
| MOF<br/>                      | <dl> <dt>RAServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAServerPSProvider.dll</dt> </dl> |



 

 





