---
Description: Represents and association between a view, and an instance that represents the normalized view of a managed resource.
ms.assetid: 9c6eb3d5-7366-4954-9e64-12f889c64114
title: CIM\_ElementView class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CIM\_ElementView class

Represents and association between a view, and an instance that represents the normalized view of a managed resource.

## Syntax

``` syntax
[Abstract, Association, Experimental, Version("2.21.1"), UMLPackagePath("CIM::Core::CoreElements")]
class CIM_ElementView : CIM_Dependency
{
  CIM_ManagedElement REF Antecedent;
  CIM_View           REF Dependent;
};
```

## Members

The **CIM\_ElementView** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_ElementView** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent")
</dt> </dl>

The instance that represents the normalized view of the managed resource.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_View**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

The view that represents a de-normalized or aggregate view of the managed resource.

</dd> </dl>

## Requirements



|                                     |                                                                                                         |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                          |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_Dependency**](cim-dependency.md)
</dt> </dl>

 

 




