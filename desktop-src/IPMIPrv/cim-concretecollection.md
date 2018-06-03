---
title: CIM\_ConcreteCollection class
description: Represents a generic and instantiable collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b0092a5e-e755-4249-9c71-892d6c9759a6
ms.prod: windows-server-dev
ms.technology:
- intelligent-platform-management-interface
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_ConcreteCollection class
- CIM_ConcreteCollection class, described
topic_type:
- apiref
api_name:
- CIM_ConcreteCollection
- CIM_ConcreteCollection.Caption
- CIM_ConcreteCollection.Description
- CIM_ConcreteCollection.ElementName
- CIM_ConcreteCollection.InstanceID
api_location:
- IpmiPrv.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CIM\_ConcreteCollection class

Represents a generic and instantiable collection. It is a general purpose subclass of the abstract [**CIM\_Collection**](cim-collection.md) class used to represent a general collection or bag.

Collections with specific semantics should be defined as subclasses of [**CIM\_Collection**](cim-collection.md), not **CIM\_ConcreteCollection**.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract, Version("2.8.0"), AMENDMENT]
class CIM_ConcreteCollection : CIM_Collection
{
  string Caption;
  string Description;
  string ElementName;
  string InstanceID;
};
```

## Members

The **CIM\_ConcreteCollection** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_ConcreteCollection** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

A short textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties/identity data, and description information.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Opaquely and uniquely identifies an instance of this class within the scope of the instantiating Namespace. To ensure uniqueness within the NameSpace, the value of **InstanceID** should be constructed using the following format:

&lt;*OrgID*&gt;:&lt;*LocalID*&gt;

&lt;*OrgID*&gt; must include a copyrighted, trademarked or otherwise unique name that is owned by the business entity creating the **InstanceID**, or is a registered ID that is assigned to the business entity by a recognized global authority. &lt;OrgID&gt; must not contain a colon (":"). The first colon to appear in **InstanceID** must be between &lt;*OrgID*&gt; and &lt;*LocalID*&gt;.

&lt;*LocalID*&gt; is chosen by the business entity and should not be re-used to identify different underlying elements.

If the above format is not used, the defining entity must assure that the resultant **InstanceID** is not re-used by this or other providers for this instance's NameSpace.

For DMTF defined instances, the format must have &lt;*OrgID*&gt; set to "CIM".

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\Hardware<br/>                                                              |
| MOF<br/>                      | <dl> <dt>IpmiPrv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IpmiPrv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Collection**](cim-collection.md)
</dt> </dl>

 

 





