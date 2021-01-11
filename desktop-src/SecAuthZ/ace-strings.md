---
description: Explains the strings used in an access control entry.
ms.assetid: 82c99170-784b-4724-a25b-2f2e8a2e0225
title: ACE Strings
ms.topic: article
ms.date: 05/31/2018
---

# ACE Strings

The [security descriptor definition language](security-descriptor-definition-language.md) (SDDL) uses ACE strings in the DACL and SACL components of a [*security descriptor*](/windows/desktop/SecGloss/s-gly) string.

As shown in the [Security Descriptor String Format](security-descriptor-string-format.md) examples, each ACE in a security descriptor string is enclosed in parentheses. The fields of the ACE are in the following order and are separated by semicolons (;).

> [!Note]  
> There is a different format for conditional [*access control entries*](/windows/desktop/SecGloss/a-gly) (ACEs) than other ACE types. For conditional ACEs, see [Security Descriptor Definition Language for Conditional ACEs](security-descriptor-definition-language-for-conditional-aces-.md).

 

``` syntax
ace_type;ace_flags;rights;object_guid;inherit_object_guid;account_sid;(resource_attribute)
```

## Fields

<dl> <dt>

<span id="ace_type"></span><span id="ACE_TYPE"></span>**ace\_type**
</dt> <dd>

A string that indicates the value of the **AceType** member of the [**ACE\_HEADER**](/windows/desktop/api/Winnt/ns-winnt-ace_header) structure. The ACE type string can be one of the following strings defined in Sddl.h.



| ACE type string | Constant in Sddl.h                      | AceType value                                                                                                                                                      |
|-----------------|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| "A"             | SDDL\_ACCESS\_ALLOWED                   | ACCESS\_ALLOWED\_ACE\_TYPE                                                                                                                                         |
| "D"             | SDDL\_ACCESS\_DENIED                    | ACCESS\_DENIED\_ACE\_TYPE                                                                                                                                          |
| "OA"            | SDDL\_OBJECT\_ACCESS\_ALLOWED           | ACCESS\_ALLOWED\_OBJECT\_ACE\_TYPE                                                                                                                                 |
| "OD"            | SDDL\_OBJECT\_ACCESS\_DENIED            | ACCESS\_DENIED\_OBJECT\_ACE\_TYPE                                                                                                                                  |
| "AU"            | SDDL\_AUDIT                             | SYSTEM\_AUDIT\_ACE\_TYPE                                                                                                                                           |
| "AL"            | SDDL\_ALARM                             | SYSTEM\_ALARM\_ACE\_TYPE                                                                                                                                           |
| "OU"            | SDDL\_OBJECT\_AUDIT                     | SYSTEM\_AUDIT\_OBJECT\_ACE\_TYPE                                                                                                                                   |
| "OL"            | SDDL\_OBJECT\_ALARM                     | SYSTEM\_ALARM\_OBJECT\_ACE\_TYPE                                                                                                                                   |
| "ML"            | SDDL\_MANDATORY\_LABEL                  | SYSTEM\_MANDATORY\_LABEL\_ACE\_TYPE                                                                                                                                |
| "XA"            | SDDL\_CALLBACK\_ACCESS\_ALLOWED         | ACCESS\_ALLOWED\_CALLBACK\_ACE\_TYPE**Windows Vista and Windows Server 2003:** Not available.<br/>                                                           |
| "XD"            | SDDL\_CALLBACK\_ACCESS\_DENIED          | ACCESS\_DENIED\_CALLBACK\_ACE\_TYPE**Windows Vista and Windows Server 2003:** Not available.<br/>                                                            |
| "RA"            | SDDL\_RESOURCE\_ATTRIBUTE               | SYSTEM\_RESOURCE\_ATTRIBUTE\_ACE\_TYPE**Windows Server 2008 R2, Windows 7, Windows Server 2008, Windows Vista and Windows Server 2003:** Not available.<br/> |
| "SP"            | SDDL\_SCOPED\_POLICY\_ID                | SYSTEM\_SCOPED\_POLICY\_ID\_ACE\_TYPE**Windows Server 2008 R2, Windows 7, Windows Server 2008, Windows Vista and Windows Server 2003:** Not available.<br/>  |
| "XU"            | SDDL\_CALLBACK\_AUDIT                   | SYSTEM\_AUDIT\_CALLBACK\_ACE\_TYPE**Windows Server 2008 R2, Windows 7, Windows Server 2008, Windows Vista and Windows Server 2003:** Not available.<br/>     |
| "ZA"            | SDDL\_CALLBACK\_OBJECT\_ACCESS\_ALLOWED | ACCESS\_ALLOWED\_CALLBACK\_ACE\_TYPE**Windows Server 2008 R2, Windows 7, Windows Server 2008, Windows Vista and Windows Server 2003:** Not available.<br/>   |



 

> [!Note]  
> If **ace\_type** is ACCESS\_ALLOWED\_OBJECT\_ACE\_TYPE and neither **object\_guid** nor **inherit\_object\_guid** has a [**GUID**](/windows/win32/api/guiddef/ns-guiddef-guid) specified, then [**ConvertStringSecurityDescriptorToSecurityDescriptor**](/windows/desktop/api/Sddl/nf-sddl-convertstringsecuritydescriptortosecuritydescriptora) converts **ace\_type** to ACCESS\_ALLOWED\_ACE\_TYPE.

 

</dd> <dt>

<span id="ace_flags"></span><span id="ACE_FLAGS"></span>**ace\_flags**
</dt> <dd>

A string that indicates the value of the **AceFlags** member of the [**ACE\_HEADER**](/windows/desktop/api/Winnt/ns-winnt-ace_header) structure. The ACE flags string can be a concatenation of the following strings defined in Sddl.h.



| ACE flags string | Constant in Sddl.h       | AceFlag value                 |
|------------------|--------------------------|-------------------------------|
| "CI"             | SDDL\_CONTAINER\_INHERIT | CONTAINER\_INHERIT\_ACE       |
| "OI"             | SDDL\_OBJECT\_INHERIT    | OBJECT\_INHERIT\_ACE          |
| "NP"             | SDDL\_NO\_PROPAGATE      | NO\_PROPAGATE\_INHERIT\_ACE   |
| "IO"             | SDDL\_INHERIT\_ONLY      | INHERIT\_ONLY\_ACE            |
| "ID"             | SDDL\_INHERITED          | INHERITED\_ACE                |
| "SA"             | SDDL\_AUDIT\_SUCCESS     | SUCCESSFUL\_ACCESS\_ACE\_FLAG |
| "FA"             | SDDL\_AUDIT\_FAILURE     | FAILED\_ACCESS\_ACE\_FLAG     |



 

</dd> <dt>

<span id="rights"></span><span id="RIGHTS"></span>**rights**
</dt> <dd>

A string that indicates the [access rights](access-rights-and-access-masks.md) controlled by the ACE. This string can be a hexadecimal string representation of the access rights, such as "0x7800003F", or it can be a concatenation of the following strings.



### Generic access rights

| Access rights string | Constant in Sddl.h | Access right value |
|----------------------|--------------------|--------------------|
| "GA"                 | SDDL\_GENERIC\_ALL | GENERIC\_ALL       |
| "GR"                 | SDDL\_GENERIC\_READ | GENERIC\_READ     |
| "GW"                 | SDDL\_GENERIC\_WRITE | GENERIC\_WRITE |
| "GX"                 | SDDL\_GENERIC\_EXECUTE | GENERIC\_EXECUTE |


### Standard access rights

| Access rights string | Constant in Sddl.h | Access right value |
|----------------------|--------------------|--------------------|
| "RC"                 | SDDL\_READ\_CONTROL | READ\_CONTROL      |
| "SD"                 | SDDL\_STANDARD\_DELETE | DELETE          |
| "WD"                 | SDDL\_WRITE\_DAC | WRITE\_DAC            |
| "WO"                 | SDDL\_WRITE\_OWNER | WRITE\_OWNER        |

### Directory service object access rights

| Access rights string | Constant in Sddl.h | Access right value |
|----------------------|--------------------|--------------------|
| "RP"                 | SDDL\_READ\_PROPERTY | ADS\_RIGHT\_DS\_READ\_PROP |
| "WP"                 | SDDL\_WRITE\_PROPERTY | ADS\_RIGHT\_DS\_WRITE\_PROP |
| "CC"                 | SDDL\_CREATE\_CHILD | ADS\_RIGHT\_DS\_CREATE\_CHILD |
| "DC"                 | SDDL\_DELETE\_CHILD | ADS\_RIGHT\_DS\_DELETE\_CHILD |
| "LC"                 | SDDL\_LIST\_CHILDREN | ADS\_RIGHT\_ACTRL\_DS\_LIST |
| "SW"                 | SDDL\_SELF\_WRITE    | ADS\_RIGHT\_DS\_SELF |
| "LO"                  | SDDL\_LIST\_OBJECT | ADS\_RIGHT\_DS\_LIST\_OBJECT |
| "DT"                 | SDDL\_DELETE\_TREE | ADS\_RIGHT\_DS\_DELETE\_TREE |
| "CR"                  | SDDL\_CONTROL\_ACCESS | ADS\_RIGHT\_DS\_CONTROL\_ACCESS |

### File access rights

| Access rights string | Constant in Sddl.h | Access right value |
|----------------------|--------------------|--------------------|
| "FA"                 | SDDL\_FILE\_ALL    | FILE\_ALL\_ACCESS   |
| "FR"                 | SDDL\_FILE\_READ   | FILE\_GENERIC\_READ |
| "FW"                 | SDDL\_FILE\_WRITE  | FILE\_GENERIC\_WRITE |
| "FX"                 | SDDL\_FILE\_EXECUTE | FILE\_GENERIC\_EXECUTE |


### Registry key access rights

| Access rights string | Constant in Sddl.h | Access right value |
|----------------------|--------------------|--------------------|
| "KA"                 | SDDL\_KEY\_ALL     | KEY\_ALL\_ACCESS   |
| "KR"                 | SDDL\_KEY\_READ    | KEY\_READ          |
| "KW"                 | SDDL\_KEY\_WRITE   | KEY\_WRITE         |
| "KX"                 | SDDL\_KEY\_EXECUTE | KEY\_EXECUTE       |

### Mandatory label rights

| Access rights string | Constant in Sddl.h | Access right value |
|----------------------|--------------------|--------------------|
| "NR"                 | SDDL\_NO\_READ\_UP | SYSTEM\_MANDATORY\_LABEL\_NO\_READ\_UP |
| "NW"                 | SDDL\_NO\_WRITE\_UP | SYSTEM\_MANDATORY\_LABEL\_NO\_WRITE\_UP |
| "NX"                 | SDDL\_NO\_EXECUTE\_UP | SYSTEM\_MANDATORY\_LABEL\_NO\_EXECUTE\_UP |
</dd> <dt>

<span id="object_guid"></span><span id="OBJECT_GUID"></span>**object\_guid**
</dt> <dd>

A string representation of a GUID that indicates the value of the **ObjectType** member of an object-specific ACE structure, such as [**ACCESS\_ALLOWED\_OBJECT\_ACE**](/windows/desktop/api/Winnt/ns-winnt-access_allowed_object_ace). The GUID string uses the format returned by the [**UuidToString**](/windows/desktop/api/rpcdce/nf-rpcdce-uuidtostring) function.

The following table lists some commonly used object GUIDs.



| Rights and GUID                         | Permission      |
|-----------------------------------------|-----------------|
| CR;ab721a53-1e2f-11d0-9819-00aa0040529b | Change password |
| CR;00299570-246d-11d0-a768-00aa006e0529 | Reset password  |



 

</dd> <dt>

<span id="inherit_object_guid"></span><span id="INHERIT_OBJECT_GUID"></span>**inherit\_object\_guid**
</dt> <dd>

A string representation of a GUID that indicates the value of the **InheritedObjectType** member of an object-specific ACE structure. The GUID string uses the [**UuidToString**](/windows/desktop/api/rpcdce/nf-rpcdce-uuidtostring) format.

</dd> <dt>

<span id="account_sid"></span><span id="ACCOUNT_SID"></span>**account\_sid**
</dt> <dd>

[SID string](sid-strings.md) that identifies the [trustee](trustees.md) of the ACE.

</dd> <dt>

<span id="resource_attribute"></span><span id="RESOURCE_ATTRIBUTE"></span>**resource\_attribute**
</dt> <dd>

\[OPTIONAL\] The resource\_attribute is only for resource ACEs and is optional. A string that indicates the data type. The resource attribute ace data type can be one of the following data types defined in Sddl.h.

The "\#" sign is synonymous with "0" in resource attributes. For example, D:AI(XA;OICI;FA;;;WD;(OctetStringType==\#1\#2\#3\#\#)) is equivalent to and interpreted as D:AI(XA;OICI;FA;;;WD;(OctetStringType==\#01020300)).

**Windows Server 2008 R2, Windows 7, Windows Server 2008, Windows Vista and Windows Server 2003:** Resource attributes are not available.



| Resource attribute ace data type string | Constant in Sddl.h | Data type        |
|-----------------------------------------|--------------------|------------------|
| "TI"                                    | SDDL\_INT          | Signed integer   |
| "TU"                                    | SDDL\_UINT         | Unsigned integer |
| "TS"                                    | SDDL\_WSTRING      | Wide string      |
| "TD"                                    | SDDL\_SID          | SID              |
| "TX"                                    | SDDL\_BLOB         | Octet string     |
| "TB"                                    | SDDL\_BOOLEAN      | Boolean          |



 

</dd> </dl>

The following example shows an ACE string for an access-allowed ACE. It is not an object-specific ACE, so it has no information in the **object\_guid** and **inherit\_object\_guid** fields. The **ace\_flags** field is also empty, which indicates that none of the ACE flags are set.


```C++
(A;;RPWPCCDCLCSWRCWDWOGA;;;S-1-1-0)
```



The ACE string shown above describes the following ACE information.


```C++
AceType:       0x00 (ACCESS_ALLOWED_ACE_TYPE)
AceFlags:      0x00
Access Mask:   0x100e003f
                    READ_CONTROL
                    WRITE_DAC
                    WRITE_OWNER
                    GENERIC_ALL
                    Other access rights(0x0000003f)
Ace Sid      : (S-1-1-0)
```



The following example shows a file classified with resource claims for Windows and Structured Query Language (SQL) with Secrecy set to High Business Impact.


```C++
(RA;CI;;;;S-1-1-0; ("Project",TS,0,"Windows","SQL")) 
(RA;CI;;;;S-1-1-0; ("Secrecy",TU,0,3))
```



The ACE string shown above describes the following ACE information.


```C++
AceType:       0x12 (SYSTEM_RESOURCE_ATTRIBUTE_ACE_TYPE)
AceFlags:      0x1  (SDDL_CONTAINER_INHERIT)
Access Mask:   0x0
Ace Sid      : (S-1-1-0)
Resource Attributes: Project has the strings Windows and SQL, Secrecy has the unsigned int value of 3
```



For more information, see [Security Descriptor String Format](security-descriptor-string-format.md) and [SID Strings](sid-strings.md). For conditional ACEs, see [Security Descriptor Definition Language for Conditional ACEs](security-descriptor-definition-language-for-conditional-aces-.md).

## Related topics

<dl> <dt>

[\[MS-DTYP\]: Security Descriptor Description Language](/openspecs/windows_protocols/ms-dtyp/4f4251cc-23b6-44b6-93ba-69688422cb06)
</dt> </dl>

