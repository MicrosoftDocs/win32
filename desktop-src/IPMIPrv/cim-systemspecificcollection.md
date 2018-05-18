---
title: CIM\_SystemSpecificCollection class
description: A base class for collections that are scoped or contained by a system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '77437951-740d-46c5-b5f4-5cd22d3de390'
ms.prod: 'windows-server-dev'
ms.technology:
- 'intelligent-platform-management-interface'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CIM_SystemSpecificCollection class", "CIM_SystemSpecificCollection class, described"]
topic_type:
- apiref
api_name:
- CIM_SystemSpecificCollection
- CIM_SystemSpecificCollection.Caption
- CIM_SystemSpecificCollection.Description
- CIM_SystemSpecificCollection.ElementName
- CIM_SystemSpecificCollection.InstanceID
api_location:
- IpmiPrv.dll
api_type:
- DllExport
---

# CIM\_SystemSpecificCollection class

A base class for collections that are scoped or contained by a system. Such a collection only has meaning in the context of the containing system.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract, Version("2.7.0"), UUID("{ccbd0dd0-c124-4e03-b4ae-81ba236b629f}"), AMENDMENT]
class CIM_SystemSpecificCollection : CIM_Collection
{
  string Caption;
  string Description;
  string ElementName;
  string InstanceID;
};
```

## Members

The **CIM\_SystemSpecificCollection** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_SystemSpecificCollection** class has these properties.

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
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\Hardware<br/>                                                              |
| MOF<br/>                      | <dl> <dt>IpmiPrv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IpmiPrv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Collection**](cim-collection.md)
</dt> </dl>

 

 





