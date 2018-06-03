---
title: MSISCSITARGET\_AuthorizedPrivilege class
description: Defines static copies of authorization policy rules. It is the base class for all activities which are protected by these rules.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a43e6081-ac3d-4e9b-8e70-e580be425eea
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSISCSITARGET_AuthorizedPrivilege class iSCSI Software Target API
- MSISCSITARGET_AuthorizedPrivilege class iSCSI Software Target API , described
topic_type:
- apiref
api_name:
- MSISCSITARGET_AuthorizedPrivilege
- MSISCSITARGET_AuthorizedPrivilege.Caption
- MSISCSITARGET_AuthorizedPrivilege.Description
- MSISCSITARGET_AuthorizedPrivilege.ElementName
- MSISCSITARGET_AuthorizedPrivilege.InstanceID
- MSISCSITARGET_AuthorizedPrivilege.PrivilegeGranted
- MSISCSITARGET_AuthorizedPrivilege.Activities
- MSISCSITARGET_AuthorizedPrivilege.ActivityQualifiers
- MSISCSITARGET_AuthorizedPrivilege.QualifierFormats
- MSISCSITARGET_AuthorizedPrivilege.RepresentsAuthorizationRights
api_location:
- WTWmiProv.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSISCSITARGET\_AuthorizedPrivilege class

Defines static copies of authorization policy rules. It is the base class for all activities which are protected by these rules. Use the [**MSISCSITARGET\_AuthorizedSubject**](msiscsitarget-authorizedsubject.md) class to associate **MSISCSITARGET\_AuthorizedPrivilege** with roles and identities. Define the entities to be protected by using the [**MSISCSITARGET\_AuthorizedTarget**](msiscsitarget-authorizedtarget.md) association. Note that these classes provide a compact, static mechanism to represent authorization policies.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("MSiSCSITargetProv"), Version("1.0.0")]
class MSISCSITARGET_AuthorizedPrivilege : CIM_AuthorizedPrivilege
{
  string  Caption;
  string  Description;
  string  ElementName;
  string  InstanceID;
  boolean PrivilegeGranted = TRUE;
  uint16  Activities[];
  string  ActivityQualifiers[];
  uint16  QualifierFormats[];
  boolean RepresentsAuthorizationRights = FALSE;
};
```

## Members

The **MSISCSITARGET\_AuthorizedPrivilege** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSISCSITARGET\_AuthorizedPrivilege** class has these properties.

<dl> <dt>

**Activities**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_Privilege.ActivityQualifiers")
</dt> </dl>

An enumeration indicating the activities that are granted or denied. These activities apply to all entities specified in the ActivityQualifiers array. The values in the enumeration are straightforward except for one, 4="Detect". This value indicates that the existence or presence of an entity may be determined, but not necessarily specific data (which requires the Read privilege to be true). This activity is exemplified by 'hidden files'- if you list the contents of a directory, you will not see hidden files. However, if you know a specific file name, or know how to expose hidden files, then they can be 'detected'. Another example is the ability to define search privileges in directory implementations.

This property is inherited from [**CIM\_Privilege**](cim-privilege.md).

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


</dt> <dd>8 15999</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>16000 65535</dd> </dl>

</dd> <dt>

**ActivityQualifiers**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_Privilege.Activities", "CIM\_Privilege.QualifierFormats")
</dt> </dl>

The ActivityQualifiers property is an array of string values used to further qualify and specify the privileges granted or denied. For example, it is used to specify a set of files for which 'Read'/'Write' access is permitted or denied. Or, it defines a class' methods that may be 'Executed'. Details on the semantics of the individual entries in ActivityQualifiers are provided by corresponding entries in the QualifierFormats array.

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

The Caption property is a short textual description (one- line string) of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Contains a textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Contains a user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties, identity data, and description information.

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

Within the scope of the instantiating Namespace, InstanceID opaquely and uniquely identifies an instance of this class. In order to ensure uniqueness within the NameSpace, the value of InstanceID SHOULD be constructed using the following 'preferred' algorithm:

&lt;OrgID&gt;:&lt;LocalID&gt;

Where &lt;OrgID&gt; and &lt;LocalID&gt; are separated by a colon ':', and where &lt;OrgID&gt; MUST include a copyrighted, trademarked or otherwise unique name that is owned by the business entity creating/defining the InstanceID, or is a registered ID that is assigned to the business entity by a recognized global authority. (This is similar to the &lt;Schema Name&gt;\_&lt;Class Name&gt; structure of Schema class names.) In addition, to ensure uniqueness &lt;OrgID&gt; MUST NOT contain a colon (':'). When using this algorithm, the first colon to appear in InstanceID MUST appear between &lt;OrgID&gt; and &lt;LocalID&gt;.

&lt;LocalID&gt; is chosen by the business entity and SHOULD not be re-used to identify different underlying (real-world) elements. If the above 'preferred' algorithm is not used, the defining entity MUST assure that the resultant InstanceID is not re-used across any InstanceIDs produced by this or other providers for this instance's NameSpace. For DMTF defined instances, the 'preferred' algorithm MUST be used with the &lt;OrgID&gt; set to 'CIM'.

This property is inherited from [**CIM\_Privilege**](cim-privilege.md).

</dd> <dt>

**PrivilegeGranted**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Boolean indicating whether the Privilege is granted (TRUE) or denied (FALSE). The default is to grant permission.

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

Defines the semantics of corresponding entries in the ActivityQualifiers array. An example of each of these 'formats' and their use follows:

\- 2=Class Name. Example: If the authorization target is a CIM Service or a Namespace, then the ActivityQualifiers entries can define a list of classes that the authorized subject is able to create or delete.

\- 3=&lt;Class.&gt;Property. Example: If the authorization target is a CIM Service, Namespace or Collection of instances, then the ActivityQualifiers entries can define the class properties that may or may not be accessed. In this case, the class names are specified with the property names to avoid ambiguity - since a CIM Service, Namespace or Collection could manage multiple classes. On the other hand, if the authorization target is an individual instance, then there is no possible ambiguity and the class name may be omitted. To specify ALL properties, the wildcard string "\*" should be used.

\- 4=&lt;Class.&gt;Method. This example is very similar to the Property one, above. And, as above, the string "\*" may be specified to select ALL methods.

\- 5=Object Reference. Example: If the authorization target is a CIM Service or Namespace, then the ActivityQualifiers entries can define a list of object references (as strings) that the authorized subject can access.

\- 6=Namespace. Example: If the authorization target is a CIM Service, then the ActivityQualifiers entries can define a list of Namespaces that the authorized subject is able to access.

\- 7=URL. Example: An authorization target may not be defined, but a Privilege could be used to deny access to specific URLs by individual Identities or for specific Roles, such as the 'under 17' Role.

\- 8=Directory/File Name. Example: If the authorization target is a FileSystem, then the ActivityQualifiers entries can define a list of directories and files whose access is protected.

\- 9=Command Line Instruction. Example: If the authorization target is a ComputerSystem or Service, then the ActivityQualifiers entries can define a list of command line instructions that may or may not be 'Executed' by the authorized subjects.

\- 10=SCSI Command, using a format of 'CDB=xx\[,Page=pp\]'. For example, the ability to select the VPD page of the Inquiry command is encoded as 'CDB=12,Page=83' in the corresponding ActivityQualifiers entry. A '\*' may be used to indicate all CDBs or Page numbers.

\- 11=Packets. Example: The transmission of packets is permitted or denied by the Privilege for the target (a ComputerSystem, ProtocolEndpoint, Pipe, or other ManagedSystemElement).

This property is inherited from [**CIM\_Privilege**](cim-privilege.md).

<dt>

<span id="Class_Name"></span><span id="class_name"></span><span id="CLASS_NAME"></span>

**Class Name** (2)


</dt> <dd></dd> <dt>

<span id="_Class._Property"></span><span id="_class._property"></span><span id="_CLASS._PROPERTY"></span>

**&lt;Class.&gt;Property** (3)


</dt> <dd></dd> <dt>

<span id="_Class._Method"></span><span id="_class._method"></span><span id="_CLASS._METHOD"></span>

**&lt;Class.&gt;Method** (4)


</dt> <dd></dd> <dt>

<span id="Object_Reference"></span><span id="object_reference"></span><span id="OBJECT_REFERENCE"></span>

**Object Reference** (5)


</dt> <dd></dd> <dt>

<span id="Namespace"></span><span id="namespace"></span><span id="NAMESPACE"></span>

**Namespace** (6)


</dt> <dd></dd> <dt>

<span id="URL"></span><span id="url"></span>

**URL** (7)


</dt> <dd></dd> <dt>

<span id="Directory_File_Name"></span><span id="directory_file_name"></span><span id="DIRECTORY_FILE_NAME"></span>

**Directory/File Name** (8)


</dt> <dd></dd> <dt>

<span id="Command_Line_Instruction"></span><span id="command_line_instruction"></span><span id="COMMAND_LINE_INSTRUCTION"></span>

**Command Line Instruction** (9)


</dt> <dd></dd> <dt>

<span id="SCSI_Command"></span><span id="scsi_command"></span><span id="SCSI_COMMAND"></span>

**SCSI Command** (10)


</dt> <dd></dd> <dt>

<span id="Packets"></span><span id="packets"></span><span id="PACKETS"></span>

**Packets** (11)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>12 15999</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>16000 65535</dd> </dl>

</dd> <dt>

**RepresentsAuthorizationRights**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The RepresentsAuthorizationRights flag indicates whether the rights defined by this instance should be interpreted as rights of Subjects to access Targets or as rights of Subjects to change those rights on/for Targets.

This property is inherited from [**CIM\_Privilege**](cim-privilege.md).

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                            |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                 |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WTWmiProv.dll</dt> </dl>     |



## See also

<dl> <dt>

[**CIM\_AuthorizedPrivilege**](cim-authorizedprivilege.md)
</dt> <dt>

[iSCSI Target Server Reference](https://msdn.microsoft.com/library/hh830439)
</dt> <dt>

[**MSISCSITARGET\_AuthorizedSubject**](msiscsitarget-authorizedsubject.md)
</dt> <dt>

[**MSISCSITARGET\_AuthorizedTarget**](msiscsitarget-authorizedtarget.md)
</dt> <dt>

[**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898)
</dt> </dl>

 

 





