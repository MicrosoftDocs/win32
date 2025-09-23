---
description: A generic association used to establish dependency relationships between managed elements.
ms.assetid: dce968b1-9ec3-4f59-8267-78dd0002a780
title: CIM\_Dependency class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_Dependency
- CIM_Dependency.Antecedent
- CIM_Dependency.Dependent
api_type: 
- DllExport
api_location: 
- netTCPIP.dll
ROBOTS: INDEX,FOLLOW
---

# CIM\_Dependency class

A generic association used to establish dependency relationships between managed elements.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Abstract, UMLPackagePath("CIM::Core::CoreElements"), Version("2.10.0"), AMENDMENT]
class CIM_Dependency
{
  CIM_ManagedElement REF Antecedent;
  CIM_ManagedElement REF Dependent;
};
```

## Members

The **CIM\_Dependency** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_Dependency** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/win32/wmisdk/key-qualifier)
</dt> </dl>

A [**CIM\_ManagedElement**](cim-managedelement.md) that contains the independent object in this association.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/win32/wmisdk/key-qualifier)
</dt> </dl>

A [**CIM\_ManagedElement**](cim-managedelement.md) that represents the object that is dependent on the **Antecedent**.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\standardcimv2<br/>                                                          |
| MOF<br/>                      | <dl> <dt>NetTCPIP.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetTCPIP.dll</dt> </dl> |



 

