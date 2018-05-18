---
title: Security Descriptors on Files and Registry Keys
description: Active Directory Service Interfaces (ADSI) can be used to manage and secure file systems within an organization, including the ability to set or modify ACLs on files or file shares created by users.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '7233a82f-fc38-4718-b674-4e6a00666184'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
keywords: ["Security Descriptors on Files and Registry Keys ADSI"]
---

# Security Descriptors on Files and Registry Keys

Active Directory Service Interfaces (ADSI) can be used to manage and secure file systems within an organization, including the ability to set or modify ACLs on files or file shares created by users. Security interfaces, such as [**IADsSecurityDescriptor**](iadssecuritydescriptor.md), [**IADsAccessControlList**](iadsaccesscontrollist.md), and [**IADsAccessControlEntry**](iadsaccesscontrolentry.md) set ACLs on Active Directory, Exchange, file, file share, or registry key objects. Before using these interfaces, the security descriptor may need to be modified if it uses a different format from the interface, or if you do not have access rights to the SACL of the security descriptor because you are not a member of the security administrator group.

To get, set, or modify the security descriptor, use the [**IADsSecurityUtility**](iadssecurityutility.md) interface. This interface enables you to retrieve a security descriptor from various resources in its original format, such as the ADSI format [**IADsSecurityDescriptor**](iadssecuritydescriptor.md), a raw security descriptor, or as a hexadecimal string as used in Exchange 5.5. When retrieved, you can convert it to another format, for example, from a raw security descriptor to **IADsSecurityDescriptor**. You can then write the new format back to the resource.

Some of the [**IADsAccessControlEntry**](iadsaccesscontrolentry.md) property values, such as [**AccessMask**](iadsaccesscontrolentry-property-methods.md) and **AceFlags**, will be different for different object types. For example, an Active Directory object will use the **ADS\_RIGHT\_GENERIC\_READ** member of the [**ADS\_RIGHTS\_ENUM**](ads-rights-enum.md) enumeration for the **IADsAccessControlEntry.AccessMask** property, but the equivalent access right for a file object is **FILE\_GENERIC\_READ**. It is not safe to assume that all property values will be the same for Active Directory objects and non-Active Directory objects. The following list shows the **IADsAccessControlEntry** properties that differ for non-Active Directory objects and where the proper values can be obtained.

<dl> <dt>

<span id="AccessMask"></span><span id="accessmask"></span><span id="ACCESSMASK"></span>[**AccessMask**](iadsaccesscontrolentry-property-methods.md)
</dt> <dd>

For more information and a list of possible values for file or file share objects, see [File Security and Access Rights](https://msdn.microsoft.com/library/windows/desktop/aa364399).

For more information and a list of possible values for registry objects, see [Registry Key Security and Access Rights](https://msdn.microsoft.com/library/windows/desktop/ms724878).

</dd> <dt>

<span id="AceType"></span><span id="acetype"></span><span id="ACETYPE"></span>[**AceType**](iadsaccesscontrolentry-property-methods.md)
</dt> <dd>

For more information, see the **AceType** member of the [**ACE\_HEADER**](https://msdn.microsoft.com/library/windows/desktop/aa374919) structure.

</dd> <dt>

<span id="AceFlags"></span><span id="aceflags"></span><span id="ACEFLAGS"></span>[**AceFlags**](iadsaccesscontrolentry-property-methods.md)
</dt> <dd>

For more information, see the **AceFlags** member of the [**ACE\_HEADER**](https://msdn.microsoft.com/library/windows/desktop/aa374919) structure.

</dd> <dt>

<span id="Flags"></span><span id="flags"></span><span id="FLAGS"></span>[**Flags**](iadsaccesscontrolentry-property-methods.md)
</dt> <dd>

Contains zero or a combination of one or more of the following values from WinNT.h.

<dl> <dt>

<span id="ACE_OBJECT_TYPE_PRESENT__1_"></span><span id="ace_object_type_present__1_"></span>**ACE\_OBJECT\_TYPE\_PRESENT** (1)
</dt> <dd>

[**ObjectType**](iadsaccesscontrolentry-property-methods.md) contains a valid value.

</dd> <dt>

<span id="ACE_INHERITED_OBJECT_TYPE_PRESENT__2_"></span><span id="ace_inherited_object_type_present__2_"></span>**ACE\_INHERITED\_OBJECT\_TYPE\_PRESENT** (2)
</dt> <dd>

[**InheritedObjectType**](iadsaccesscontrolentry-property-methods.md) contains a valid value.

</dd> </dl> </dd> <dt>

<span id="ObjectType"></span><span id="objecttype"></span><span id="OBJECTTYPE"></span>[**ObjectType**](iadsaccesscontrolentry-property-methods.md)
</dt> <dd>

For more information, see the **ObjectType** member of the [**ACCESS\_DENIED\_OBJECT\_ACE**](https://msdn.microsoft.com/library/windows/desktop/aa374887), [**ACCESS\_ALLOWED\_OBJECT\_ACE**](https://msdn.microsoft.com/library/windows/desktop/aa374857), and similar structures. This property should not be set or modified for non-Active Directory objects.

</dd> <dt>

<span id="InheritedObjectType"></span><span id="inheritedobjecttype"></span><span id="INHERITEDOBJECTTYPE"></span>[**InheritedObjectType**](iadsaccesscontrolentry-property-methods.md)
</dt> <dd>

For more information, see the **InheritedObjectType** member of the [**ACCESS\_DENIED\_OBJECT\_ACE**](https://msdn.microsoft.com/library/windows/desktop/aa374887), [**ACCESS\_ALLOWED\_OBJECT\_ACE**](https://msdn.microsoft.com/library/windows/desktop/aa374857), and similar structures. This property should not be set or modified for non-Active Directory objects.

</dd> </dl>

Normally, [**IADsSecurityUtility.GetSecurityDescriptor**](iadssecurityutility-getsecuritydescriptor.md) will retrieve all parts of the security descriptor, such as owner, group, SACL, or DACL. Similarly, [**IADsSecurityUtility.SetSecurityDescriptor**](iadssecurityutility-setsecuritydescriptor.md) will overwrite all parts of the security descriptor by default. You can use the [**IADsSecurityUtility.SecurityMask**](iadssecurityutility-securitymask.md) property to specify individual parts of the security descriptor to retrieve or set. For example, you can set **SecurityMask** to [**ADS\_SECURITY\_INFO\_DACL**](ads-security-info-enum.md) before calling **GetSecurityDescriptor** to only retrieve the DACL without retrieving the other parts of the security descriptor.

For more information and a code example that uses the [**IADsSecurityUtility**](iadssecurityutility.md) interface to add an ACE to a file, see [Example Code for Adding an ACE to a File](example-code-for-adding-an-ace-to-a-file.md).

The following example code provides the constant identifiers for file, file share and registry objects for the [**AccessMask**](iadsaccesscontrolentry-property-methods.md), **AceType**, **AceFlags**, and **Flags** properties for use with Visual Basic and Microsoft Visual Basic Scripting Edition.


```VB
' Identifiers for the IADsAccessControlEntry.AccessMask property for file,
' file share, and registry objects.
Const DELETE = &amp;H10000
Const READ_CONTROL = &amp;H20000
Const WRITE_DAC = &amp;H40000
Const WRITE_OWNER = &amp;H80000
Const SYNCHRONIZE = &amp;H100000

Const STANDARD_RIGHTS_REQUIRED = &amp;HF0000

Const STANDARD_RIGHTS_READ = &amp;H20000
Const STANDARD_RIGHTS_WRITE = &amp;H20000
Const STANDARD_RIGHTS_EXECUTE = &amp;H20000

Const STANDARD_RIGHTS_ALL = &amp;H1F0000

Const SPECIFIC_RIGHTS_ALL = &amp;HFFFF

' Identifiers for the IADsAccessControlEntry.AccessMask property for file and
' file share objects.
Const FILE_READ_DATA = &amp;H1                  '  file & pipe
Const FILE_LIST_DIRECTORY = &amp;H1             '  directory

Const FILE_WRITE_DATA = &amp;H2                 '  file & pipe
Const FILE_ADD_FILE = &amp;H2                   '  directory

Const FILE_APPEND_DATA = &amp;H4                '  file
Const FILE_ADD_SUBDIRECTORY = &amp;H4           '  directory
Const FILE_CREATE_PIPE_INSTANCE = &amp;H4       '  named pipe

Const FILE_READ_EA = &amp;H8                    '  file & directory

Const FILE_WRITE_EA = &amp;H10                  '  file & directory

Const FILE_EXECUTE = &amp;H20                   '  file
Const FILE_TRAVERSE = &amp;H20                  '  directory

Const FILE_DELETE_CHILD = &amp;H40              '  directory

Const FILE_READ_ATTRIBUTES = &amp;H80           '  all

Const FILE_WRITE_ATTRIBUTES = &amp;H100         '  all

Const FILE_ALL_ACCESS = STANDARD_RIGHTS_REQUIRED Or SYNCHRONIZE Or &amp;H1FF

Const FILE_GENERIC_READ = STANDARD_RIGHTS_READ Or FILE_READ_DATA Or FILE_READ_ATTRIBUTES Or _
                          FILE_READ_EA Or SYNCHRONIZE

Const FILE_GENERIC_WRITE = STANDARD_RIGHTS_WRITE Or FILE_WRITE_DATA Or FILE_WRITE_ATTRIBUTES Or _
                           FILE_WRITE_EA Or FILE_APPEND_DATA Or SYNCHRONIZE

Const FILE_GENERIC_EXECUTE = STANDARD_RIGHTS_EXECUTE Or FILE_READ_ATTRIBUTES Or FILE_EXECUTE Or SYNCHRONIZE


' Identifiers for the IADsAccessControlEntry.AccessMask property for registry
' objects.
Const KEY_QUERY_VALUE = &amp;H1
Const KEY_SET_VALUE = &amp;H2
Const KEY_CREATE_SUB_KEY = &amp;H4
Const KEY_ENUMERATE_SUB_KEYS = &amp;H8
Const KEY_NOTIFY = &amp;H10
Const KEY_CREATE_LINK = &amp;H20
Const KEY_WOW64_32KEY = &amp;H200
Const KEY_WOW64_64KEY = &amp;H100
Const KEY_WOW64_RES = &amp;H300

Const KEY_READ = ((STANDARD_RIGHTS_READ Or KEY_QUERY_VALUE Or KEY_ENUMERATE_SUB_KEYS Or KEY_NOTIFY) And _
                  (Not SYNCHRONIZE))

Const KEY_WRITE = ((STANDARD_RIGHTS_WRITE Or KEY_SET_VALUE Or KEY_CREATE_SUB_KEY) And (Not SYNCHRONIZE))

Const KEY_EXECUTE = ((KEY_READ) And (Not SYNCHRONIZE))

Const KEY_ALL_ACCESS = ((STANDARD_RIGHTS_ALL Or KEY_QUERY_VALUE Or KEY_SET_VALUE Or KEY_CREATE_SUB_KEY Or _
                         KEY_ENUMERATE_SUB_KEYS Or KEY_NOTIFY Or KEY_CREATE_LINK) And (Not SYNCHRONIZE))
    

' Identifiers for the IADsAccessControlEntry.AceFlags property for file and
' file share objects.
Const OBJECT_INHERIT_ACE = &amp;H1
Const CONTAINER_INHERIT_ACE = &amp;H2
Const NO_PROPAGATE_INHERIT_ACE = &amp;H4
Const INHERIT_ONLY_ACE = &amp;H8
Const INHERITED_ACE = &amp;H10
    

' Identifiers for the IADsAccessControlEntry.Flags property.
Const ACE_OBJECT_TYPE_PRESENT = 1
Const ACE_INHERITED_OBJECT_TYPE_PRESENT = 2
```



 

 




