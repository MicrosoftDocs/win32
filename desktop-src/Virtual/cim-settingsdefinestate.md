---
title: CIM\_SettingsDefineState class
description: Associates settings data with a managed element.
ms.assetid: '02c613a2-0497-4274-af68-8d629a69d96f'
keywords: ["CIM_SettingsDefineState class Hyper-V", "CIM_SettingsDefineState class Hyper-V , described"]
topic_type:
- apiref
api_name:
- CIM_SettingsDefineState
- CIM_SettingsDefineState.ManagedElement
- CIM_SettingsDefineState.SettingData
api_location:
- Root\virtualization
api_type:
- Schema
---

# CIM\_SettingsDefineState class

Associates settings data with a managed element.

In this association, the setting data provides information about the state of the managed element.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract, Association, Experimental, Version("2.14.0"), AMENDMENT]
class CIM_SettingsDefineState
{
  CIM_ManagedElement REF ManagedElement;
  CIM_SettingData    REF SettingData;
};
```

## Members

The **CIM\_SettingsDefineState** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_SettingsDefineState** class has these properties.

<dl> <dt>

**ManagedElement**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The managed element in the association.

</dd> <dt>

**SettingData**
</dt> <dd> <dl> <dt>

Data type: **CIM\_SettingData**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The settings data in the association.

</dd> </dl>

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012 R2<br/>                                                                    |
| Namespace<br/>                | Root\\virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



 

 





