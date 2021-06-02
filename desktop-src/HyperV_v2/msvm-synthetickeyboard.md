---
description: Represents a synthetic keyboard device.
ms.assetid: 8fe9bdd5-59e8-421d-812a-08aa3c54c88f
title: Msvm_SyntheticKeyboard class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_SyntheticKeyboard
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_SyntheticKeyboard class

Represents a synthetic keyboard device.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_SyntheticKeyboard : CIM_UserDevice
{
};
```

## Members

The **Msvm\_SyntheticKeyboard** class has these types of members:

-   [Methods](#methods)

### Methods

The **Msvm\_SyntheticKeyboard** class has these methods.



| Method                                                                  | Description                         |
|:------------------------------------------------------------------------|:------------------------------------|
| [**RequestStateChange**](msvm-synthetickeyboard-requeststatechange.md) | Requests a state change.<br/> |
| [**Reset**](msvm-synthetickeyboard-reset.md)                           | resets the device.<br/>       |



 

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

[**CIM\_UserDevice**](cim-userdevice.md)
</dt> </dl>

 

 




