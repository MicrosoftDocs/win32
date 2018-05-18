---
title: MSFT\_FSRMFMJCondition class
description: Represents the file management job conditions.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'deb5be80-4255-4d56-8db5-31239e2872ef'
ms.prod: 'windows-server-dev'
ms.technology: 'file-server-resource-manager'
ms.tgt_platform: multiple
keywords: ["MSFT_FSRMFMJCondition class File Server Resource Manager", "MSFT_FSRMFMJCondition class File Server Resource Manager , described"]
topic_type:
- apiref
api_name:
- MSFT_FSRMFMJCondition
- MSFT_FSRMFMJCondition.Property
- MSFT_FSRMFMJCondition.Condition
- MSFT_FSRMFMJCondition.Value
- MSFT_FSRMFMJCondition.DateOffset
api_location:
- SrmSvc.dll
api_type:
- DllExport
---

# MSFT\_FSRMFMJCondition class

Represents the file management job conditions.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("FSRMWmiProvider")]
class MSFT_FSRMFMJCondition
{
  string Property;
  uint32 Condition;
  string Value;
  sint32 DateOffset;
};
```

## Members

The **MSFT\_FSRMFMJCondition** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_FSRMFMJCondition** class has these methods.



| Method                                                                 | Description                                                |
|:-----------------------------------------------------------------------|:-----------------------------------------------------------|
| [**CreateFMJCondition**](msft-fsrmfmjcondition-createfmjcondition.md) | Creates an **MSFT\_FSRMFMJCondition** instance.<br/> |



 

### Properties

The **MSFT\_FSRMFMJCondition** class has these properties.

<dl> <dt>

**Condition**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Required.

<dt>

<span id="Equal"></span><span id="equal"></span><span id="EQUAL"></span>

<span id="Equal"></span><span id="equal"></span><span id="EQUAL"></span>**Equal** (1)


</dt> <dd>

The property condition is met if the property value is equal to a specified value.

</dd> <dt>

<span id="NotEqual"></span><span id="notequal"></span><span id="NOTEQUAL"></span>

<span id="NotEqual"></span><span id="notequal"></span><span id="NOTEQUAL"></span>**NotEqual** (2)


</dt> <dd>

The property condition is met if the property value is not equal to a specified value.

</dd> <dt>

<span id="GreaterThan"></span><span id="greaterthan"></span><span id="GREATERTHAN"></span>

<span id="GreaterThan"></span><span id="greaterthan"></span><span id="GREATERTHAN"></span>**GreaterThan** (3)


</dt> <dd>

The property condition is met if the property value is greater than to a specified value.

</dd> <dt>

<span id="LessThan"></span><span id="lessthan"></span><span id="LESSTHAN"></span>

<span id="LessThan"></span><span id="lessthan"></span><span id="LESSTHAN"></span>**LessThan** (4)


</dt> <dd>

The property condition is met if the property value is less than to a specified value.

</dd> <dt>

<span id="Contain"></span><span id="contain"></span><span id="CONTAIN"></span>

<span id="Contain"></span><span id="contain"></span><span id="CONTAIN"></span>**Contain** (5)


</dt> <dd>

The property condition is met if the property value contains the specified value.

</dd> <dt>

<span id="Exist"></span><span id="exist"></span><span id="EXIST"></span>

<span id="Exist"></span><span id="exist"></span><span id="EXIST"></span>**Exist** (6)


</dt> <dd>

The property condition is met if the property value exists.

</dd> <dt>

<span id="NotExist"></span><span id="notexist"></span><span id="NOTEXIST"></span>

<span id="NotExist"></span><span id="notexist"></span><span id="NOTEXIST"></span>**NotExist** (7)


</dt> <dd>

The property condition is met if the property value does not exist.

</dd> <dt>

<span id="StartWith"></span><span id="startwith"></span><span id="STARTWITH"></span>

<span id="StartWith"></span><span id="startwith"></span><span id="STARTWITH"></span>**StartWith** (8)


</dt> <dd>

The property condition is met if the property value starts with the specified value.

</dd> <dt>

<span id="EndWith"></span><span id="endwith"></span><span id="ENDWITH"></span>

<span id="EndWith"></span><span id="endwith"></span><span id="ENDWITH"></span>**EndWith** (9)


</dt> <dd>

The property condition is met if the property value ends with the specified value.

</dd> <dt>

<span id="ContainedIn"></span><span id="containedin"></span><span id="CONTAINEDIN"></span>

<span id="ContainedIn"></span><span id="containedin"></span><span id="CONTAINEDIN"></span>**ContainedIn** (10)


</dt> <dd>

The property condition is met if the property value is contained in the specified value.

</dd> <dt>

<span id="PrefixOf"></span><span id="prefixof"></span><span id="PREFIXOF"></span>

<span id="PrefixOf"></span><span id="prefixof"></span><span id="PREFIXOF"></span>**PrefixOf** (11)


</dt> <dd>

The property condition is met if the property value is a prefix of the specified value.

</dd> <dt>

<span id="SuffixOf"></span><span id="suffixof"></span><span id="SUFFIXOF"></span>

<span id="SuffixOf"></span><span id="suffixof"></span><span id="SUFFIXOF"></span>**SuffixOf** (12)


</dt> <dd>

The property condition is met if the property value is a suffix of the specified value.

</dd> <dt>

<span id="MatchesPattern"></span><span id="matchespattern"></span><span id="MATCHESPATTERN"></span>

<span id="MatchesPattern"></span><span id="matchespattern"></span><span id="MATCHESPATTERN"></span>**MatchesPattern** (13)


</dt> <dd>

The property condition is met if the property value matches the specified pattern. The pattern format is a semicolon-separated list of wildcard patterns. For example "\*.exe;\*.com".

</dd> </dl>

</dd> <dt>

**DateOffset**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

An integer offset from the date value. Optional. The default value is 0.

</dd> <dt>

**Property**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A string up to 1KB in size. Required.

<dt>




</dt> <dd>

The name of a valid classification property on the server.

</dd> <dt>

File.Name
</dt> <dd></dd> <dt>

File.DateCreated
</dt> <dd></dd> <dt>

File.DateLastModified
</dt> <dd></dd> <dt>

File.DateLastAccessed
</dt> <dd></dd> </dl>

</dd> <dt>

**Value**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A string less than 1KB in size. The default is an empty string.

<dt>

A classification property name that is not a **DateTime** property. Must be compatible with the property definition.
</dt> <dd></dd> <dt>

A classification property name that is a **DateTime** property.
</dt> <dd>

-   A valid **FileTime**
-   File.DateCreated
-   File.DateLastModified
-   File.DateLastAccessed
-   Date.Now

</dd> <dt>

File.Name
</dt> <dd>

Strings with wildcards of '\*' and '?' separated by a semicolon.

</dd> <dt>

File.DateCreated
</dt> <dd>

A positive integer.

</dd> <dt>

File.DateLastModified
</dt> <dd>

A positive integer.

</dd> <dt>

File.DateLastAccessed
</dt> <dd>

A positive integer.

</dd> </dl>

</dd> </dl>

## Remarks

When the **Property** property refers to a classification property, the type of the classification property determines which **Condition** property values are acceptable. See the **Type** property of [**MSFT\_FSRMClassificationPropertyDefinition**](msft-fsrmclassificationpropertydefinition.md).



|             |         |        |       |             |              |             |             |          |
|-------------|---------|--------|-------|-------------|--------------|-------------|-------------|----------|
|             | Integer | String | YesNo | OrderedList | SingleChoice | MultiChoice | MultiString | DateTime |
| Equal       | Yes     | Yes    | Yes   | Yes         | Yes          | Yes         | Yes         | Yes      |
| NotEqual    | Yes     | Yes    | Yes   | Yes         | Yes          | Yes         | Yes         | Yes      |
| Exist       | Yes     | Yes    | Yes   | Yes         | Yes          | Yes         | Yes         | Yes      |
| NotExist    | Yes     | Yes    | Yes   | Yes         | Yes          | Yes         | Yes         | Yes      |
| Contains    | No      | Yes    | No    | No          | No           | Yes         | Yes         | No       |
| ContainedIn | No      | Yes    | No    | No          | No           | No          | No          | No       |
| LessThan    | Yes     | Yes    | No    | Yes         | No           | No          | No          | Yes      |
| GreaterThan | Yes     | Yes    | No    | Yes         | No           | No          | No          | Yes      |
| StartsWith  | No      | Yes    | No    | No          | No           | No          | No          | No       |
| EndsWith    | No      | Yes    | No    | No          | No           | No          | No          | No       |
| PrefixOf    | No      | Yes    | No    | No          | No           | No          | No          | No       |
| SuffixOf    | No      | Yes    | No    | No          | No           | No          | No          | No       |



 

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\FSRM<br/>                                                 |
| MOF<br/>                      | <dl> <dt>MSFT\_FSRM.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SrmSvc.dll</dt> </dl>     |



## See also

<dl> <dt>

[FSRM WMI Classes](fsrm-wmi-classes.md)
</dt> </dl>

 

 





