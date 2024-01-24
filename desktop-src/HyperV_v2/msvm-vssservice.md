---
description: Represents the guest VSS service. It is used for querying guest cluster information from the Hyper-V host.
ms.assetid: 82321456-a24e-4f67-9346-f0844e2913dc
title: Msvm_VssService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_VssService
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_VssService class

Represents the guest VSS service. It is used for querying guest cluster information from the Hyper-V host.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_VssService : Msvm_GuestService
{
};
```

## Members

The **Msvm\_VssService** class has these types of members:

-   [Methods](#methods)

### Methods

The **Msvm\_VssService** class has these methods.



| Method                                                                               | Description                                                                 |
|:-------------------------------------------------------------------------------------|:----------------------------------------------------------------------------|
| [**QueryGuestClusterInformation**](msvm-vssservice-queryguestclusterinformation.md) | Querying cluster information from the Hyper-V host to the guest.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                          |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**Msvm\_GuestService**](msvm-guestservice.md)
</dt> </dl>

 

 




