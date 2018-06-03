---
Description: The MSFT\_SomFilter class represents a list of rules, expressed as a query, which are evaluated on a target computer.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: da743886-0726-47b9-afc6-dff84b3dde1f
ms.prod: windows-server-dev
ms.technology:
- group-policy
- windows-management-instrumentation
ms.tgt_platform: multiple
title: MSFT\_SomFilter class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_SomFilter class

The **MSFT\_SomFilter** class represents a list of rules, expressed as a query, which are evaluated on a target computer. The **MSFT\_SomFilter** instances are held in the Active Directory and may be written one time and be valid for the entire domain. The **MSFT\_SomFilter** class is compiled in the \\\\root\\policy namespace.

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("PolicSOM"), UUID("{AE7B614F-AFE0-41ea-807E-3BD3F83CAF66}"), AMENDMENT]
class MSFT_SomFilter
{
  string    ID;
  string    Domain;
  string    Name;
  string    Description;
  MSFT_Rule Rules[];
  string    Author;
  string    SourceOrganization;
  datetime  ChangeDate;
  datetime  CreationDate;
};
```

## Members

The **MSFT\_SomFilter** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_SomFilter** class has these methods.



| Method                                                                | Description                                                                                                                 |
|:----------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------|
| [**BatchEvaluate**](batchevaluate-method-in-class-msft-somfilter.md) | Evaluates a list of **MSFT\_SomFilter** objects to determine whether the queries in each apply to this computer.<br/> |
| [**Evaluate**](evaluate-method-in-class-msft-somfilter.md)           | Determines whether the queries expressed in Rules apply to this computer.<br/>                                        |



 

### Properties

The **MSFT\_SomFilter** class has these properties.

<dl> <dt>

**Author**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Originator of the **MSFT\_SomFilter** object.

</dd> <dt>

**ChangeDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Date and time the object was last updated.

</dd> <dt>

**CreationDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Date and time the object was created.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Text that describes the object.

</dd> <dt>

**Domain**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Domain of the object in DNS format. For example, "microsoft.com".

</dd> <dt>

**ID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (38)
</dt> </dl>

Unique identifier for the object instance. The identifier can be any unique name. If the name is missing, the GUID in registry format is used.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**NOT\_NULL**](https://msdn.microsoft.com/library/aa392729)
</dt> </dl>

Friendly name for the object.

</dd> <dt>

**Rules**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_Rule** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**NOT\_NULL**](https://msdn.microsoft.com/library/aa392729)
</dt> </dl>

Array of [**MSFT\_Rule**](msft-rule.md) objects to be evaluated.

</dd> <dt>

**SourceOrganization**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Organization of the author.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\policy<br/>                                                                 |
| MOF<br/>                      | <dl> <dt>PolicMan.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>PolicMan.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_Rule**](msft-rule.md)
</dt> </dl>

 

 




