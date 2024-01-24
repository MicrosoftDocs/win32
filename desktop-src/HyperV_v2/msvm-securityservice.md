---
description: Represents the security service. It is used for configuring virtual system security settings.
ms.assetid: 00097d81-9fea-4b84-b5dd-e45af46d6e0a
title: Msvm_SecurityService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_SecurityService
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_SecurityService class

Represents the security service. It is used for configuring virtual system security settings.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_SecurityService : CIM_Service
{
};
```

## Members

The **Msvm\_SecurityService** class has these types of members:

-   [Methods](#methods)

### Methods

The **Msvm\_SecurityService** class has these methods.



| Method                                                                                            | Description                                                             |
|:--------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------|
| [**GetKeyProtector**](msvm-securityservice-getkeyprotector.md)                                   | Method to retrieve the key protector for a virtual system.<br/>   |
| [**ModifySecuritySettings**](msvm-securityservice-modifysecuritysettings.md)                     | Modifies the current security settings of a virtual machine.<br/> |
| [**RestoreLastKnownGoodKeyProtector**](msvm-securityservice-restorelastknowngoodkeyprotector.md) | Method to restore back to the last known good key protector.<br/> |
| [**SetKeyProtector**](msvm-securityservice-setkeyprotector.md)                                   | Method to set the key protector for a virtual system.<br/>        |
| [**SetSecurityPolicy**](msvm-securityservice-setsecuritypolicy.md)                               | Method to set the key protector for a virtual system.<br/>        |
| [**StartService**](msvm-securityservice-startservice.md)                                         | Starts the service.<br/>                                          |
| [**StopService**](msvm-securityservice-stopservice.md)                                           | Stops the service.<br/>                                           |



 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1703 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                          |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_Service**](cim-service.md)
</dt> </dl>

 

 




