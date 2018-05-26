---
title: CreateFMJCondition method of the MSFT\_FSRMFMJCondition class
description: Creates an MSFT\_FSRMFMJCondition instance.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 56c507a6-be3c-4a51-8db0-3dccea8071b1
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- CreateFMJCondition method File Server Resource Manager
- CreateFMJCondition method File Server Resource Manager , MSFT_FSRMFMJCondition class
- MSFT_FSRMFMJCondition class File Server Resource Manager , CreateFMJCondition method
topic_type:
- apiref
api_name:
- MSFT_FSRMFMJCondition.CreateFMJCondition
api_location:
- SrmSvc.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CreateFMJCondition method of the MSFT\_FSRMFMJCondition class

Creates an [**MSFT\_FSRMFMJCondition**](msft-fsrmfmjcondition.md) instance.

## Syntax


```mof
uint64 CreateFMJCondition(
  [in]  string                Property,
  [in]  uint32                Condition,
  [in]  string                Value,
  [in]  sint32                DateOffset,
  [out] MSFT_FSRMFMJCondition FmjCondition
);
```



## Parameters

<dl> <dt>

*Property* \[in\]
</dt> <dd>

A string up to 1KB in size. Required.

<dt>




</dt> <dd>

The name of a valid classification property on the server. See the Remarks section for details concerning which property types are compatible with which *Condition* parameter values.

</dd> <dt>

File.Name
</dt> <dd></dd> <dt>

File.DateCreated
</dt> <dd></dd> <dt>

File.DateLastModified
</dt> <dd></dd> <dt>

File.DateLastAccessed
</dt> <dd></dd> </dl> </dd> <dt>

*Condition* \[in\]
</dt> <dd>

Describes the condition that must be matched for the file management job. Required.

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

</dd> </dl> </dd> <dt>

*Value* \[in\]
</dt> <dd>

A string less than 1KB in size. The default is an empty string. The *Value* parameter must not be empty unless the *Condition* parameter is "Exist" (6) or "NotExist" (7). The table shows the possible values to use for each of the *Property* parameter values.

This shows the types of vales to use for the *Value* parameter for each *Property* parameter

<dt>

A classification property name that is not a **DateTime** property.
</dt> <dd>

Must be compatible with the property definition.

</dd> <dt>

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

</dd> </dl> </dd> <dt>

*DateOffset* \[in\]
</dt> <dd>

An integer offset from the date value. Optional. The default value is 0.

</dd> <dt>

*FmjCondition* \[out\]
</dt> <dd>

Returns an instance of the [**MSFT\_FSRMFMJCondition**](msft-fsrmfmjcondition.md) class.

</dd> </dl>

## Remarks

When the *Property* parameter refers to a classification property, the type of the classification property determines which *Condition* values are acceptable. See the **Type** property of [**MSFT\_FSRMClassificationPropertyDefinition**](msft-fsrmclassificationpropertydefinition.md).



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
| Minimum supported server<br/> | Windows Server 2012<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\FSRM<br/>                                                 |
| MOF<br/>                      | <dl> <dt>MSFT\_FSRM.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SrmSvc.dll</dt> </dl>     |



## See also

<dl> <dt>

[**MSFT\_FSRMFMJCondition**](msft-fsrmfmjcondition.md)
</dt> </dl>

 

 





