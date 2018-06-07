---
Description: Represents the association between two metric definitions or two metric values.
ms.assetid: 78fb926d-8981-443a-a82d-ebac34d38e13
title: Msvm\_MetricCollectionDependency class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Msvm\_MetricCollectionDependency class

Represents the association between two metric definitions or two metric values.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_MetricCollectionDependency : CIM_Dependency
{
  CIM_ManagedElement REF Antecedent;
  CIM_ManagedElement REF Dependent;
};
```

## Members

The **Msvm\_MetricCollectionDependency** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_MetricCollectionDependency** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_ManagedElement**](https://msdn.microsoft.com/library/mt432218)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A reference to an instance of the [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/mt432218) class that represents the independent metric definition or metric value. This property is inherited from [**CIM\_Dependency**](https://msdn.microsoft.com/library/aa387238).

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_ManagedElement**](https://msdn.microsoft.com/library/mt432218)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A reference to an instance of the [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/mt432218) class that represents the metric definition or metric value that is dependent on the **Antecedent**. This property is inherited from [**CIM\_Dependency**](https://msdn.microsoft.com/library/aa387238).

</dd> </dl>

## Requirements



|                                     |                                                                                                         |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



 

 




