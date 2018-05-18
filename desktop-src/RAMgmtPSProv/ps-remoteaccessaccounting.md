---
title: PS\_RemoteAccessAccounting class
description: Represents the various types of accounting supported for Remote Access.
audience: developer
ms.assetid: '382be70a-6b1c-4f94-8d52-7441cbe1525f'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["PS_RemoteAccessAccounting class", "PS_RemoteAccessAccounting class, described"]
topic_type:
- apiref
api_name:
- PS_RemoteAccessAccounting
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
---

# PS\_RemoteAccessAccounting class

Represents the various types of accounting supported for Remote Access.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class PS_RemoteAccessAccounting
{
};
```

## Members

The **PS\_RemoteAccessAccounting** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_RemoteAccessAccounting** class has these methods.



| Method                                                                             | Description                                                                                                                                                                                        |
|:-----------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Get**](get-ps-remoteaccessaccounting.md)                                       | This cmdlet displays the accounting configuration for Remote Access, viz. the different types of accounting that are enabled and their respective configuration<br/>                         |
| [**SetByDisableAccounting**](setbydisableaccounting-ps-remoteaccessaccounting.md) | This cmdlet does the following1. Enables inbox and RADIUS accounting (both external RADIUS and Windows accounting) and configures their settings2. Disables inbox and RADIUS accounting<br/> |
| [**SetByEnableAccounting**](setbyenableaccounting-ps-remoteaccessaccounting.md)   | This cmdlet does the following1. Enables inbox and Radius accounting (both external Radius and Windows accounting) and configures their settings2. Disables inbox and Radius accounting<br/> |



 

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





