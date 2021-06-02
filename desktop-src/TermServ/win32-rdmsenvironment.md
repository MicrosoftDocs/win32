---
title: Win32_RDMSEnvironment class
description: Manages a Remote Desktop Management Services (RDMS) environment.
ms.assetid: 8a3b10c1-d01d-4e52-8915-29159cc406cc
ms.tgt_platform: multiple
keywords:
- Win32_RDMSEnvironment class Remote Desktop Services
- Win32_RDMSEnvironment class Remote Desktop Services , described
topic_type:
- apiref
api_name:
- Win32_RDMSEnvironment
api_location:
- RDMS.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Win32\_RDMSEnvironment class

Manages a Remote Desktop Management Services (RDMS) environment.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("Win32_RDManagement_Prov"), AMENDMENT]
class Win32_RDMSEnvironment
{
};
```

## Members

The **Win32\_RDMSEnvironment** class has these types of members:

-   [Methods](#methods)

### Methods

The **Win32\_RDMSEnvironment** class has these methods.



| Method                                                                   | Description                                                                                          |
|:-------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------|
| [**GetActiveServer**](getactiveserver-win32-rdmsenvironment.md)         | Retrieves the fully qualified domain name (FQDN) of the RDMS environment.<br/>                 |
| [**GetClientAccessName**](getclientaccessname-win32-rdmsenvironment.md) | Retrieves the Domain Name System (DNS) resource record (RR) name of the RDMS environment.<br/> |
| [**SetActiveServer**](setactiveserver-win32-rdmsenvironment.md)         | Sets the FQDN of the RDMS environment to the current node.<br/>                                |
| [**SetClientAccessName**](setclientaccessname-win32-rdmsenvironment.md) | Updates the DNS RR name of the RDMS environment.<br/>                                          |



 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                              |
| Namespace<br/>                | Root\\cimv2\\rdms<br/>                                                                |
| MOF<br/>                      | <dl> <dt>RDManagement.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RDMS.dll</dt> </dl>         |



## See also

<dl> <dt>

[Remote Desktop Management Services Provider](rdms-api-reference.md)
</dt> </dl>

 

 





