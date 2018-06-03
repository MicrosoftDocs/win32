---
title: MSFT\_FSRMClassificationPropertyDefinition class
description: Represents a classification property definition.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2221a226-60cd-45db-86c1-eae11ad41ff0
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- MSFT_FSRMClassificationPropertyDefinition class File Server Resource Manager
- MSFT_FSRMClassificationPropertyDefinition class File Server Resource Manager , described
topic_type:
- apiref
api_name:
- MSFT_FSRMClassificationPropertyDefinition
- MSFT_FSRMClassificationPropertyDefinition.Name
- MSFT_FSRMClassificationPropertyDefinition.DisplayName
- MSFT_FSRMClassificationPropertyDefinition.Description
- MSFT_FSRMClassificationPropertyDefinition.Type
- MSFT_FSRMClassificationPropertyDefinition.PossibleValue
- MSFT_FSRMClassificationPropertyDefinition.Parameters
- MSFT_FSRMClassificationPropertyDefinition.Flags
- MSFT_FSRMClassificationPropertyDefinition.AppliesTo
api_location:
- SrmSvc.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_FSRMClassificationPropertyDefinition class

Represents a classification property definition.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("FSRMWmiProvider")]
class MSFT_FSRMClassificationPropertyDefinition
{
  string                               Name;
  string                               DisplayName;
  string                               Description;
  uint32                               Type;
  MSFT_FSRMClassificationPropertyValue PossibleValue[];
  string                               Parameters[] = {};
  uint32                               Flags[];
  uint32                               AppliesTo[];
};
```

## Members

The **MSFT\_FSRMClassificationPropertyDefinition** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_FSRMClassificationPropertyDefinition** class has these methods.



| Method                                                             | Description                                                                                                 |
|:-------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------|
| [**Update**](msft-fsrmclassificationpropertydefinition-update.md) | Forces an update of the global classification property definitions from Active Directory if any.<br/> |



 

### Properties

The **MSFT\_FSRMClassificationPropertyDefinition** class has these properties.

<dl> <dt>

**AppliesTo**
</dt> <dd> <dl> <dt>

Data type: **uint32** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Flags that indicate what a FSRM property definition can be applied to.

<dt>

<span id="Files"></span><span id="files"></span><span id="FILES"></span>

<span id="Files"></span><span id="files"></span><span id="FILES"></span>**Files** (1)


</dt> <dd>

The Classification Property Definition applies to files.

</dd> <dt>

<span id="Folders"></span><span id="folders"></span><span id="FOLDERS"></span>

<span id="Folders"></span><span id="folders"></span><span id="FOLDERS"></span>**Folders** (2)


</dt> <dd>

The Classification Property Definition applies to folders.

</dd> </dl>

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

""

An optional string up to 1KB in length. The default value is an empty string.

</dd> <dt>

**DisplayName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

An optional string up to 100 characters in length. The value must be unique for classification property definitions on the server.

</dd> <dt>

**Flags**
</dt> <dd> <dl> <dt>

Data type: **uint32** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Flags that describe the classification property definition.

<dt>

<span id="Global"></span><span id="global"></span><span id="GLOBAL"></span>

<span id="Global"></span><span id="global"></span><span id="GLOBAL"></span>**Global** (1)


</dt> <dd>

The FSRM property definition is defined globally, using group policy.

</dd> <dt>

<span id="Deprecated"></span><span id="deprecated"></span><span id="DEPRECATED"></span>

<span id="Deprecated"></span><span id="deprecated"></span><span id="DEPRECATED"></span>**Deprecated** (2)


</dt> <dd>

The FSRM property definition is deprecated.

</dd> <dt>

<span id="Secure"></span><span id="secure"></span><span id="SECURE"></span>

<span id="Secure"></span><span id="secure"></span><span id="SECURE"></span>**Secure** (4)


</dt> <dd>

The FSRM property definition is a secure type.

</dd> </dl>

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A unique string up to 100 characters in length. Required.

</dd> <dt>

**Parameters**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

An array of strings formatted as "&lt;name&gt;=&lt;value&gt;", as accepted by the COM API for property definitions. The default value is an empty list.

</dd> <dt>

**PossibleValue**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_FSRMClassificationPropertyValue**](msft-fsrmclassificationpropertyvalue.md)** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**MSFT\_FSRMClassificationPropertyValue**](msft-fsrmclassificationpropertyvalue.md)")
</dt> </dl>

An array of classification property values in the form of instances of the [**MSFT\_FSRMClassificationPropertyValue**](msft-fsrmclassificationpropertyvalue.md) class. The default value is an empty list.

</dd> <dt>

**Type**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Describes the type of the classification property definition.

<dt>

<span id="OrderedList"></span><span id="orderedlist"></span><span id="ORDEREDLIST"></span>

<span id="OrderedList"></span><span id="orderedlist"></span><span id="ORDEREDLIST"></span>**OrderedList** (1)


</dt> <dd>

A classification property that defines an ordered list of possible string values, one of which may be assigned to the property.

The aggregation policy for this type is to use the order in which the items are added to the list to determine which value to use if the property exists and contains a value that is different from the rule's value. For example, if the list contains "HBI", "MBI", and "LBI", and one source specifies "MBI" and the other source specifies "HBI", the property value is set to "HBI" because it appears before "MBI" in the list.

You can use the following comparison operators with this type: Equal, Not equal, Greater than, Less than, Exists, and Not exists.

</dd> <dt>

<span id="MultiChoice"></span><span id="multichoice"></span><span id="MULTICHOICE"></span>

<span id="MultiChoice"></span><span id="multichoice"></span><span id="MULTICHOICE"></span>**MultiChoice** (2)


</dt> <dd>

A classification property that defines a list of possible string values, one or more of which may be assigned to the property. Use the vertical bar character (\|) to delimit the strings.

The aggregation policy for this type is to concatenate the values from each source, consolidating any duplicates. For example, if the list of possible values contains "Cat1", "Cat2", "Cat3", and "Cat4", and one source specifies "Cat3" and another source specifies "Cat1", the property value is set to "Cat1\|Cat3".

You can use the following comparison operators with this type: Equal, Not equal, Contains, Contained in, Exists, and Not exists.

</dd> <dt>

<span id="SingleChoice"></span><span id="singlechoice"></span><span id="SINGLECHOICE"></span>

<span id="SingleChoice"></span><span id="singlechoice"></span><span id="SINGLECHOICE"></span>**SingleChoice** (3)


</dt> <dd>

A classification property that defines a list of possible string values, only one of which may be assigned to the property.

No aggregation is available for this type.

You can use the following comparison operators with this type: Equal, Not equal, Exists, and Not exists.

</dd> <dt>

<span id="String"></span><span id="string"></span><span id="STRING"></span>

<span id="String"></span><span id="string"></span><span id="STRING"></span>**String** (4)


</dt> <dd>

A classification property that contains an arbitrary string value.

The aggregation policy is to fail if two sources do not specify the same value.

You can use the following comparison operators with this type: Equal, Not equal, Greater than, Less than, Contains, Contained in, Start with, End with, Prefix of, Suffix of, Exists, and Not exists.

</dd> <dt>

<span id="MultiString"></span><span id="multistring"></span><span id="MULTISTRING"></span>

<span id="MultiString"></span><span id="multistring"></span><span id="MULTISTRING"></span>**MultiString** (5)


</dt> <dd>

A classification property that contains one or more arbitrary string values. Use the vertical bar character (\|) to delimit the strings.

The aggregation policy is to concatenate the values from each source, consolidating any duplicates. For example if one source specifies "String1\|String2" and another source specifies "String1\|String3", the property value is set to "String1\|String2\|String3".

You can use the following comparison operators with this type: Equal, Not equal, Contains, Contained in, Exists, and Not exists.

</dd> <dt>

<span id="Integer"></span><span id="integer"></span><span id="INTEGER"></span>

<span id="Integer"></span><span id="integer"></span><span id="INTEGER"></span>**Integer** (6)


</dt> <dd>

A classification property that contains a decimal integer value expressed as a string.

The aggregation policy is to fail if two sources do not specify the same value.

You can use the following comparison operators with this type: Equal, Not equal, Greater than, Less than, Exists, and Not exists.

</dd> <dt>

<span id="YesNo"></span><span id="yesno"></span><span id="YESNO"></span>

<span id="YesNo"></span><span id="yesno"></span><span id="YESNO"></span>**YesNo** (7)


</dt> <dd>

A classification property that contains a Boolean value expressed as a string. Use a string value of "0" for **False** or a string value of "1" for **True**.

The aggregation policy is to perform a logical **OR** on the values from each source. For example, if one source specifies **True** and another source specifies **False**, the property value is set to **True**. If two sources both specify **False**, the property value is set to **False**.

You can use the following comparison operators with this type: Equal, Not equal, Exists, and Not exists.

</dd> <dt>

<span id="DateTime"></span><span id="datetime"></span><span id="DATETIME"></span>

<span id="DateTime"></span><span id="datetime"></span><span id="DATETIME"></span>**DateTime** (8)


</dt> <dd>

A classification property that contains a date value. The date value is a 64-bit decimal number (see [**FILETIME**](https://msdn.microsoft.com/library/windows/desktop/ms724284)) expressed as a string.

The aggregation policy is to fail if two sources do not specify the same value.

You can use the following comparison operators with this type: Equal, Not equal, Greater than, Less than, Exists, and Not exists.

</dd> </dl>

</dd> </dl>

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

[FSRM WMI Classes](fsrm-wmi-classes.md)
</dt> <dt>

[**MSFT\_FSRMClassificationPropertyValue**](msft-fsrmclassificationpropertyvalue.md)
</dt> </dl>

 

 





