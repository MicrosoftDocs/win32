---
title: PS\_DAEntryPointDC class
description: DAEntryPointDC Object.
audience: developer
ms.assetid: 'e91c5f8d-17ef-4db1-8624-33df87eb4962'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["PS_DAEntryPointDC class", "PS_DAEntryPointDC class, described"]
topic_type:
- apiref
api_name:
- PS_DAEntryPointDC
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
---

# PS\_DAEntryPointDC class

DAEntryPointDC Object.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class PS_DAEntryPointDC
{
};
```

## Members

The **PS\_DAEntryPointDC** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DAEntryPointDC** class has these methods.



| Method                                                       | Description                                                                                   |
|:-------------------------------------------------------------|:----------------------------------------------------------------------------------------------|
| [**Get**](get-ps-daentrypointdc.md)                         | Retrieves the domain controller that is associated with the specified entry point.<br/> |
| [**SetByDCName**](setbydcname-ps-daentrypointdc.md)         | Modifies domain controller settings for the entry point.<br/>                           |
| [**SetByEntryPoint**](setbyentrypoint-ps-daentrypointdc.md) | Modifies domain controller settings for the entry point.<br/>                           |



 

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





