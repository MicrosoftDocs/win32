---
title: PS\_RemoteAccessInboxAccountingStore class
description: Represents the configuration of the store used for inbox accounting.
audience: developer
ms.assetid: 22652f3f-b799-4877-83bc-38884a7c422c
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_RemoteAccessInboxAccountingStore class
- PS_RemoteAccessInboxAccountingStore class, described
topic_type:
- apiref
api_name:
- PS_RemoteAccessInboxAccountingStore
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PS\_RemoteAccessInboxAccountingStore class

Represents the configuration of the store used for inbox accounting.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class PS_RemoteAccessInboxAccountingStore
{
};
```

## Members

The **PS\_RemoteAccessInboxAccountingStore** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_RemoteAccessInboxAccountingStore** class has these methods.



| Method                                                     | Description                                                                            |
|:-----------------------------------------------------------|:---------------------------------------------------------------------------------------|
| [**Clear**](clear-ps-remoteaccessinboxaccountingstore.md) | This cmdlet clears the inbox accounting store for the specified time period<br/> |
| [**Set**](set-ps-remoteaccessinboxaccountingstore.md)     | This cmdlet modifies the size of the inbox accounting store<br/>                 |



 

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





