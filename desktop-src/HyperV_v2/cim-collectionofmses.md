---
description: An abstract class for subclasses that represent a collection of CIM\_ManagedSystemElement objects. These collections allow managed system elements to be grouped for identification purposes and to simplify the association of settings and configurations.
ms.assetid: f47bf1d6-6d89-4d9f-82d1-99a7343481bc
title: CIM_CollectionOfMSEs class (Hyper-V management)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_CollectionOfMSEs
- CIM_CollectionOfMSEs.CollectionID
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# CIM_CollectionOfMSEs class (Hyper-V management)

An abstract class for subclasses that represent a collection of [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md) objects. These collections allow managed system elements to be grouped for identification purposes and to simplify the association of settings and configurations.

## Syntax

``` syntax
[Abstract, Version("2.10.0"), UMLPackagePath("CIM::Core::Collection"), AMENDMENT]
class CIM_CollectionOfMSEs : CIM_Collection
{
  string CollectionID;
};
```

## Members

The **CIM\_CollectionOfMSEs** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_CollectionOfMSEs** class has these properties.

<dl> <dt>

**CollectionID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (256)
</dt> </dl>

The identification of the collection object. When subclassed, the **CollectionID** property can be overridden as a key property.

</dd> </dl>

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

[**CIM\_Collection**](cim-collection.md)
</dt> </dl>

 

