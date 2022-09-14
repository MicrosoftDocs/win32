---
title: Security Descriptors on Files and Registry Keys
description: Active Directory Service Interfaces (ADSI) can be used to manage and secure file systems within an organization, including the ability to set or modify ACLs on files or file shares created by users.
ms.assetid: 7233a82f-fc38-4718-b674-4e6a00666184
ms.tgt_platform: multiple
keywords:
- Security Descriptors on Files and Registry Keys ADSI
ms.topic: article
ms.date: 05/31/2018
---

# Security Descriptors on Files and Registry Keys

Active Directory Service Interfaces (ADSI) can be used to manage and secure file systems within an organization, including the ability to set or modify ACLs on files or file shares created by users. Security interfaces, such as [**IADsSecurityDescriptor**](/windows/desktop/api/Iads/nn-iads-iadssecuritydescriptor), [**IADsAccessControlList**](/windows/desktop/api/Iads/nn-iads-iadsaccesscontrollist), and [**IADsAccessControlEntry**](/windows/desktop/api/Iads/nn-iads-iadsaccesscontrolentry) set ACLs on Active Directory, Exchange, file, file share, or registry key objects. Before using these interfaces, the security descriptor may need to be modified if it uses a different format from the interface, or if you do not have access rights to the SACL of the security descriptor because you are not a member of the security administrator group.

To get, set, or modify the security descriptor, use the [**IADsSecurityUtility**](/windows/desktop/api/Iads/nn-iads-iadssecurityutility) interface. This interface enables you to retrieve a security descriptor from various resources in its original format, such as the ADSI format [**IADsSecurityDescriptor**](/windows/desktop/api/Iads/nn-iads-iadssecuritydescriptor), a raw security descriptor, or as a hexadecimal string as used in Exchange 5.5. When retrieved, you can convert it to another format, for example, from a raw security descriptor to **IADsSecurityDescriptor**. You can then write the new format back to the resource.

Some of the [**IADsAccessControlEntry**](/windows/desktop/api/Iads/nn-iads-iadsaccesscontrolentry) property values, such as [**AccessMask**](iadsaccesscontrolentry-property-methods.md) and **AceFlags**, will be different for different object types. For example, an Active Directory object will use the **ADS\_RIGHT\_GENERIC\_READ** member of the [**ADS\_RIGHTS\_ENUM**](/windows/win32/api/iads/ne-iads-ads_rights_enum) enumeration for the **IADsAccessControlEntry.AccessMask** property, but the equivalent access right for a file object is **FILE\_GENERIC\_READ**. It is not safe to assume that all property values will be the same for Active Directory objects and non-Active Directory objects. The following list shows the **IADsAccessControlEntry** properties that differ for non-Active Directory objects and where the proper values can be obtained.

<dl> <dt>

<span id="AccessMask"></span><span id="accessmask"></span><span id="ACCESSMASK"></span>[**AccessMask**](iadsaccesscontrolentry-property-methods.md)
</dt> <dd>

For more information and a list of possible values for file or file share objects, see [File Security and Access Rights](/windows/desktop/FileIO/file-security-and-access-rights).

For more information and a list of possible values for registry objects, see [Registry Key Security and Access Rights](/windows/desktop/SysInfo/registry-key-security-and-access-rights).

</dd> <dt>

<span id="AceType"></span><span id="acetype"></span><span id="ACETYPE"></span>[**AceType**](iadsaccesscontrolentry-property-methods.md)
</dt> <dd>

For more information, see the **AceType** member of the [**ACE\_HEADER**](/windows/desktop/api/winnt/ns-winnt-ace_header) structure.

</dd> <dt>

<span id="AceFlags"></span><span id="aceflags"></span><span id="ACEFLAGS"></span>[**AceFlags**](iadsaccesscontrolentry-property-methods.md)
</dt> <dd>

For more information, see the **AceFlags** member of the [**ACE\_HEADER**](/windows/desktop/api/winnt/ns-winnt-ace_header) structure.

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

For more information, see the **ObjectType** member of the [**ACCESS\_DENIED\_OBJECT\_ACE**](/windows/desktop/api/winnt/ns-winnt-access_denied_object_ace), [**ACCESS\_ALLOWED\_OBJECT\_ACE**](/windows/desktop/api/winnt/ns-winnt-access_allowed_object_ace), and similar structures. This property should not be set or modified for non-Active Directory objects.

</dd> <dt>

<span id="InheritedObjectType"></span><span id="inheritedobjecttype"></span><span id="INHERITEDOBJECTTYPE"></span>[**InheritedObjectType**](iadsaccesscontrolentry-property-methods.md)
</dt> <dd>

For more information, see the **InheritedObjectType** member of the [**ACCESS\_DENIED\_OBJECT\_ACE**](/windows/desktop/api/winnt/ns-winnt-access_denied_object_ace), [**ACCESS\_ALLOWED\_OBJECT\_ACE**](/windows/desktop/api/winnt/ns-winnt-access_allowed_object_ace), and similar structures. This property should not be set or modified for non-Active Directory objects.

</dd> </dl>

Normally, [**IADsSecurityUtility.GetSecurityDescriptor**](/windows/desktop/api/Iads/nf-iads-iadssecurityutility-getsecuritydescriptor) will retrieve all parts of the security descriptor, such as owner, group, SACL, or DACL. Similarly, [**IADsSecurityUtility.SetSecurityDescriptor**](/windows/desktop/api/Iads/nf-iads-iadssecurityutility-setsecuritydescriptor) will overwrite all parts of the security descriptor by default. You can use the [**IADsSecurityUtility.SecurityMask**](/windows/desktop/api/Iads/nf-iads-iadssecurityutility-get_securitymask) property to specify individual parts of the security descriptor to retrieve or set. For example, you can set **SecurityMask** to [**ADS\_SECURITY\_INFO\_DACL**](/windows/win32/api/iads/ne-iads-ads_security_info_enum) before calling **GetSecurityDescriptor** to only retrieve the DACL without retrieving the other parts of the security descriptor.

For more information and a code example that uses the [**IADsSecurityUtility**](/windows/desktop/api/Iads/nn-iads-iadssecurityutility) interface to add an ACE to a file, see [Example Code for Adding an ACE to a File](example-code-for-adding-an-ace-to-a-file.md).

The following example code provides the constant identifiers for file, file share and registry objects for the [**AccessMask**](iadsaccesscontrolentry-property-methods.md), **AceType**, **AceFlags**, and **Flags** properties for use with Visual Basic and Microsoft Visual Basic Scripting Edition.


```VB
' Identifiers for the IADsAccessControlEntry.AccessMask property for file,
' file share, and registry objects.
Const DELETE = &H10000
Const READ_CONTROL = &H20000
Const WRITE_DAC = &H40000
Const WRITE_OWNER = &H80000
Const SYNCHRONIZE = &H100000

Const STANDARD_RIGHTS_REQUIRED = &HF0000

Const STANDARD_RIGHTS_READ = &H20000
Const STANDARD_RIGHTS_WRITE = &H20000
Const STANDARD_RIGHTS_EXECUTE = &H20000

Const STANDARD_RIGHTS_ALL = &H1F0000

Const SPECIFIC_RIGHTS_ALL = &HFFFF

' Identifiers for the IADsAccessControlEntry.AccessMask property for file and
' file share objects.
Const FILE_READ_DATA = &H1                  '  file & pipe
Const FILE_LIST_DIRECTORY = &H1             '  directory

Const FILE_WRITE_DATA = &H2                 '  file & pipe
Const FILE_ADD_FILE = &H2                   '  directory

Const FILE_APPEND_DATA = &H4                '  file
Const FILE_ADD_SUBDIRECTORY = &H4           '  directory
Const FILE_CREATE_PIPE_INSTANCE = &H4       '  named pipe

Const FILE_READ_EA = &H8                    '  file & directory

Const FILE_WRITE_EA = &H10                  '  file & directory

Const FILE_EXECUTE = &H20                   '  file
Const FILE_TRAVERSE = &H20                  '  directory

Const FILE_DELETE_CHILD = &H40              '  directory

Const FILE_READ_ATTRIBUTES = &H80           '  all

Const FILE_WRITE_ATTRIBUTES = &H100         '  all

Const FILE_ALL_ACCESS = STANDARD_RIGHTS_REQUIRED Or SYNCHRONIZE Or &H1FF

Const FILE_GENERIC_READ = STANDARD_RIGHTS_READ Or FILE_READ_DATA Or FILE_READ_ATTRIBUTES Or _
                          FILE_READ_EA Or SYNCHRONIZE

Const FILE_GENERIC_WRITE = STANDARD_RIGHTS_WRITE Or FILE_WRITE_DATA Or FILE_WRITE_ATTRIBUTES Or _
                           FILE_WRITE_EA Or FILE_APPEND_DATA Or SYNCHRONIZE

Const FILE_GENERIC_EXECUTE = STANDARD_RIGHTS_EXECUTE Or FILE_READ_ATTRIBUTES Or FILE_EXECUTE Or SYNCHRONIZE


' Identifiers for the IADsAccessControlEntry.AccessMask property for registry
' objects.
Const KEY_QUERY_VALUE = &H1
Const KEY_SET_VALUE = &H2
Const KEY_CREATE_SUB_KEY = &H4
Const KEY_ENUMERATE_SUB_KEYS = &H8
Const KEY_NOTIFY = &H10
Const KEY_CREATE_LINK = &H20
Const KEY_WOW64_32KEY = &H200
Const KEY_WOW64_64KEY = &H100
Const KEY_WOW64_RES = &H300

Const KEY_READ = ((STANDARD_RIGHTS_READ Or KEY_QUERY_VALUE Or KEY_ENUMERATE_SUB_KEYS Or KEY_NOTIFY) And _
                  (Not SYNCHRONIZE))

Const KEY_WRITE = ((STANDARD_RIGHTS_WRITE Or KEY_SET_VALUE Or KEY_CREATE_SUB_KEY) And (Not SYNCHRONIZE))

Const KEY_EXECUTE = ((KEY_READ) And (Not SYNCHRONIZE))

Const KEY_ALL_ACCESS = ((STANDARD_RIGHTS_ALL Or KEY_QUERY_VALUE Or KEY_SET_VALUE Or KEY_CREATE_SUB_KEY Or _
                         KEY_ENUMERATE_SUB_KEYS Or KEY_NOTIFY Or KEY_CREATE_LINK) And (Not SYNCHRONIZE))
    

' Identifiers for the IADsAccessControlEntry.AceFlags property for file and
' file share objects.
Const OBJECT_INHERIT_ACE = &H1
Const CONTAINER_INHERIT_ACE = &H2
Const NO_PROPAGATE_INHERIT_ACE = &H4
Const INHERIT_ONLY_ACE = &H8
Const INHERITED_ACE = &H10
    

' Identifiers for the IADsAccessControlEntry.Flags property.
Const ACE_OBJECT_TYPE_PRESENT = 1
Const ACE_INHERITED_OBJECT_TYPE_PRESENT = 2
```



 

 