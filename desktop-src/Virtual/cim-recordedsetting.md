---
title: CIM\_RecordedSetting class
description: TBD
ms.assetid: 798f17c6-0926-4979-8bf5-85dd01684d09
keywords:
- CIM_RecordedSetting class Hyper-V
- CIM_RecordedSetting class Hyper-V , described
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CIM\_RecordedSetting class

TBD

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Abstract, Experimental, Association, Version("2.13.0")]
class CIM_RecordedSetting : CIM_Dependency
{
  CIM_ManagedElement                REF Antecedent;
  CIM_ManagedElement                REF Dependent;
  CIM_ResourceAllocationSettingData REF CurrentSetting;
  CIM_ResourceAllocationSettingData REF RecordedSetting;
};
```

## Members

The **CIM\_RecordedSetting** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_RecordedSetting** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_ManagedElement**](cim-managedelement.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The independent object in this association.

This property is inherited from [**CIM\_Dependency**](cim-dependency.md).

</dd> <dt>

**CurrentSetting**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ResourceAllocationSettingData**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The current setting.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_ManagedElement**](cim-managedelement.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The dependent object in the association.

This property is inherited from [**CIM\_Dependency**](cim-dependency.md).

</dd> <dt>

**RecordedSetting**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ResourceAllocationSettingData**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

TBD

</dd> </dl>

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012 R2<br/>                                                                    |
| Namespace<br/>                | Root\\virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Dependency**](cim-dependency.md)
</dt> </dl>

 

 





