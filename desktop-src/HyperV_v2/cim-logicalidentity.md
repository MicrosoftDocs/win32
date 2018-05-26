---
Description: Represents a generic association between two managed elements that represent different aspects of the same underlying entity.
ms.assetid: 28d153de-ce9c-4cd3-8995-0d959846be4d
title: CIM\_LogicalIdentity class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CIM\_LogicalIdentity class

Represents a generic association between two managed elements that represent different aspects of the same underlying entity.

## Syntax

``` syntax
[Association, Abstract, Version("2.10.0"), UMLPackagePath("CIM::Core::CoreElements"), AMENDMENT]
class CIM_LogicalIdentity
{
  CIM_ManagedElement REF SystemElement;
  CIM_ManagedElement REF SameElement;
};
```

## Members

The **CIM\_LogicalIdentity** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_LogicalIdentity** class has these properties.

<dl> <dt>

**SameElement**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The second aspect in the association.

</dd> <dt>

**SystemElement**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The first aspect in the association. The use of System in the property name does not limit the scope of the association.

</dd> </dl>

## Requirements



|                                     |                                                                                                         |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                                  |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                       |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



 

 




