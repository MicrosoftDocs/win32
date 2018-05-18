---
title: CIM\_AuthorizedPrivilege class
description: The base class for all types of activities which are granted or denied to a Role or an Identity.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'e8832353-ef50-4dba-ba48-a66402047b99'
ms.prod: 'windows-server-dev'
ms.technology:
- 'intelligent-platform-management-interface'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CIM_AuthorizedPrivilege class", "CIM_AuthorizedPrivilege class, described"]
topic_type:
- apiref
api_name:
- CIM_AuthorizedPrivilege
- CIM_AuthorizedPrivilege.Caption
- CIM_AuthorizedPrivilege.Description
- CIM_AuthorizedPrivilege.ElementName
- CIM_AuthorizedPrivilege.InstanceID
- CIM_AuthorizedPrivilege.PrivilegeGranted
- CIM_AuthorizedPrivilege.Activities
- CIM_AuthorizedPrivilege.ActivityQualifiers
- CIM_AuthorizedPrivilege.QualifierFormats
api_location:
- IpmiPrv.dll
api_type:
- DllExport
---

# CIM\_AuthorizedPrivilege class

The base class for all types of activities which are granted or denied to a Role or an Identity. Any privileges not specifically granted are assumed to be denied. An explicit denial takes precedence over any granted privileges.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract, Version("2.8.0"), AMENDMENT]
class CIM_AuthorizedPrivilege : CIM_Privilege
{
  string  Caption;
  string  Description;
  string  ElementName;
  string  InstanceID;
  boolean PrivilegeGranted = TRUE;
  uint16  Activities[];
  string  ActivityQualifiers[];
  uint16  QualifierFormats[];
};
```

## Members

The **CIM\_AuthorizedPrivilege** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_AuthorizedPrivilege** class has these properties.

<dl> <dt>

**Activities**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_Privilege.ActivityQualifiers")
</dt> </dl>

An enumeration indicating the activities that are granted or denied. These activities apply to all entities specified in the **ActivityQualifiers** array.

**Detect** (4) indicates that the existence or presence of an entity may be determined, but not necessarily specific data, which requires the **Read** privilege.

<dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Create"></span><span id="create"></span><span id="CREATE"></span>

**Create** (2)


</dt> <dd></dd> <dt>

<span id="Delete"></span><span id="delete"></span><span id="DELETE"></span>

**Delete** (3)


</dt> <dd></dd> <dt>

<span id="Detect"></span><span id="detect"></span><span id="DETECT"></span>

**Detect** (4)


</dt> <dd></dd> <dt>

<span id="Read"></span><span id="read"></span><span id="READ"></span>

**Read** (5)


</dt> <dd></dd> <dt>

<span id="Write"></span><span id="write"></span><span id="WRITE"></span>

**Write** (6)


</dt> <dd></dd> <dt>

<span id="Execute"></span><span id="execute"></span><span id="EXECUTE"></span>

**Execute** (7)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>8–15999</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>16000–65535</dd> </dl>

This property is inherited from [**CIM\_Privilege**](cim-privilege.md).

</dd> <dt>

**ActivityQualifiers**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_Privilege.Activities", "CIM\_Privilege.QualifierFormats")
</dt> </dl>

An array of values used to further qualify and specify the privileges granted or denied. For example, it is used to specify a set of files for which Read or Write access is permitted or denied. The semantics of the individual entries in **ActivityQualifiers** are provided in corresponding entries in the **QualifierFormats** array.

This property is inherited from [**CIM\_Privilege**](cim-privilege.md).

</dd> <dt>

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

This property is inherited from [**CIM\_Privilege**](cim-privilege.md).

</dd> <dt>

**PrivilegeGranted**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether the privilege is granted. The default is to grant permission.

This property is inherited from [**CIM\_Privilege**](cim-privilege.md).

</dd> <dt>

**QualifierFormats**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_Privilege.ActivityQualifiers")
</dt> </dl>

Defines the semantics of corresponding entries in the **ActivityQualifiers** array.

The possible values, with examples, are.

<dt>

<span id="Class_Name"></span><span id="class_name"></span><span id="CLASS_NAME"></span>

<span id="Class_Name"></span><span id="class_name"></span><span id="CLASS_NAME"></span>**Class Name** (2)


</dt> <dd>

If the authorization target is a CIM Service or a Namespace, the **ActivityQualifiers** entries can define a list of classes that the authorized subject is able to create or delete.

</dd> <dt>

<span id="_Class._Property"></span><span id="_class._property"></span><span id="_CLASS._PROPERTY"></span>

<span id="_class._property"></span><span id="_CLASS._PROPERTY"></span>**&lt;Class.&gt;Property** (3)


</dt> <dd>

If the authorization target is a CIM Service, Namespace or Collection of instances, the **ActivityQualifiers** entries can define the class properties that can or cannot be accessed. Since these targets can manage multiple classes, the class names are included to avoid ambiguity.

If the authorization target is an individual instance, there is no possible ambiguity and the class name may be omitted.

Use the "\*" wildcard character to specify all properties.

</dd> <dt>

<span id="_Class._Method"></span><span id="_class._method"></span><span id="_CLASS._METHOD"></span>

<span id="_class._method"></span><span id="_CLASS._METHOD"></span>**&lt;Class.&gt;Method** (4)


</dt> <dd>

Usage is similar to **&lt;Class.&gt;Property** (3).

Use the "\*" wildcard character to specify all properties.

</dd> <dt>

<span id="Object_Reference"></span><span id="object_reference"></span><span id="OBJECT_REFERENCE"></span>

<span id="Object_Reference"></span><span id="object_reference"></span><span id="OBJECT_REFERENCE"></span>**Object Reference** (5)


</dt> <dd>

If the authorization target is a CIM Service or Namespace, the **ActivityQualifiers** entries can define a list of object references that the authorized subject can access.

</dd> <dt>

<span id="Namespace"></span><span id="namespace"></span><span id="NAMESPACE"></span>

<span id="Namespace"></span><span id="namespace"></span><span id="NAMESPACE"></span>**Namespace** (6)


</dt> <dd>

If the authorization target is a CIM Service, then the **ActivityQualifiers** entries can define a list of Namespaces that the authorized subject can access.

</dd> <dt>

<span id="URL"></span><span id="url"></span>

<span id="URL"></span><span id="url"></span>**URL** (7)


</dt> <dd>

An authorization target may not be defined, but a Privilege could be used to deny access to specific URLs.

</dd> <dt>

<span id="Directory_File_Name"></span><span id="directory_file_name"></span><span id="DIRECTORY_FILE_NAME"></span>

<span id="Directory_File_Name"></span><span id="directory_file_name"></span><span id="DIRECTORY_FILE_NAME"></span>**Directory/File Name** (8)


</dt> <dd>

If the authorization target is a file system, then the **ActivityQualifiers** entries can define a list of directories and files whose access is protected.

</dd> <dt>

<span id="Command_Line_Instruction"></span><span id="command_line_instruction"></span><span id="COMMAND_LINE_INSTRUCTION"></span>

<span id="Command_Line_Instruction"></span><span id="command_line_instruction"></span><span id="COMMAND_LINE_INSTRUCTION"></span>**Command Line Instruction** (9)


</dt> <dd>

If the authorization target is a compute system or service, then the **ActivityQualifiers** entries can define a list of command line instructions that can or cannot be run by the authorized subjects.

</dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved**


</dt> <dd></dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>**Vendor Reserved**


</dt> <dd></dd> </dl>

This property is inherited from [**CIM\_Privilege**](cim-privilege.md).

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

[**CIM\_Privilege**](cim-privilege.md)
</dt> </dl>

 

 





