---
title: MSFT\_FSRMClassificationRule class
description: Defines a classification rule.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 845fc1e8-d06a-4bc4-9529-0748cb488727
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- MSFT_FSRMClassificationRule class File Server Resource Manager
- MSFT_FSRMClassificationRule class File Server Resource Manager , described
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_FSRMClassificationRule class

Defines a classification rule. The rule defines the paths to which the rule applies, the classifier module to run on files in those paths, and the property and property value used to classify each file.

To create a classification rule, call the [**IFsrmClassificationManager::CreateRule**](/previous-versions/windows/desktop/api/FsrmPipeline/nf-fsrmpipeline-ifsrmclassificationmanager-createrule) method.

## Syntax

``` syntax
[dynamic, provider("FSRMWmiProvider")]
class MSFT_FSRMClassificationRule
{
  string   Name;
  string   Description;
  boolean  Disabled;
  string   Property;
  string   PropertyValue;
  string   Namespace[];
  uint32   ReevaluateProperty;
  string   ClassificationMechanism;
  string   Parameters[];
  datetime LastModified;
  uint32   Flags[];
  string   ContentRegularExpression[];
  string   ContentString[];
  string   ContentStringCaseSensitive[];
};
```

## Members

The **MSFT\_FSRMClassificationRule** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_FSRMClassificationRule** class has these properties.

<dl> <dt>

**ClassificationMechanism**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The name of a valid classification mechanism available on the server. Required. The value must be under 1KB.

</dd> <dt>

**ContentRegularExpression**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

A list of regular expressions to search for, provided to the content classifier. Optional. The list size must be under 25KB. Default value is an empty list.

</dd> <dt>

**ContentString**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

A list of strings to search for, provided to the content classifier. Optional. The list size must be under 25KB. Default value is an empty list.

</dd> <dt>

**ContentStringCaseSensitive**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

A list of case sensitive strings to search for, provided to the content classifier. Optional. The list size must be under 25KB. Default value is an empty list.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A string up to 1KB in size. Optional. The default value is an empty string.

</dd> <dt>

**Disabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Defines whether the rule is enabled or disabled. The default value is false.

</dd> <dt>

**Flags**
</dt> <dd> <dl> <dt>

Data type: **uint32** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

Array of flags describing the rule.

<dt>

<span id="Deprecated"></span><span id="deprecated"></span><span id="DEPRECATED"></span>

<span id="Deprecated"></span><span id="deprecated"></span><span id="DEPRECATED"></span>**Deprecated** (4096)


</dt> <dd>

The rule is deprecated.

</dd> <dt>

<span id="ClearManuallyClassifiedProperty"></span><span id="clearmanuallyclassifiedproperty"></span><span id="CLEARMANUALLYCLASSIFIEDPROPERTY"></span>

<span id="ClearManuallyClassifiedProperty"></span><span id="clearmanuallyclassifiedproperty"></span><span id="CLEARMANUALLYCLASSIFIEDPROPERTY"></span>**ClearManuallyClassifiedProperty** (2048)


</dt> <dd>

TBD

**Windows Server 2012:** This value is not supported before Windows Server 2012 R2.

</dd> <dt>

<span id="ClearAutomaticallyClassifiedProperty"></span><span id="clearautomaticallyclassifiedproperty"></span><span id="CLEARAUTOMATICALLYCLASSIFIEDPROPERTY"></span>

<span id="ClearAutomaticallyClassifiedProperty"></span><span id="clearautomaticallyclassifiedproperty"></span><span id="CLEARAUTOMATICALLYCLASSIFIEDPROPERTY"></span>**ClearAutomaticallyClassifiedProperty** (1024)


</dt> <dd>

TBD

**Windows Server 2012:** This value is not supported before Windows Server 2012 R2.

</dd> </dl>

</dd> <dt>

**LastModified**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The date for the last time the rule was modified.

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

**Namespace**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

A list of valid local folder paths on the server. Each string is not to exceed the **MAX\_PATH**value. Can be valid values for the **FolderUsage** classification property. If providing **FolderUsage** properties, the format "\[FolderUsage\_MS=*value*\]" must be used. The default value is an empty list.

</dd> <dt>

**Parameters**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

A list of strings formatted as "&lt;name&gt;=&lt;value&gt;", as accepted by the COM API for rule parameters. Optional. The default value is an empty list.

</dd> <dt>

**Property**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The name of a valid classification property that is available on the server. The value is required and limited to a size of 1KB.

</dd> <dt>

**PropertyValue**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The value to which the property is set upon successful classification. The value is optional and limited to a size of 4 KB. The default value is an empty string.

</dd> <dt>

**ReevaluateProperty**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Sets the evaluation policy of the rule. Optional.

<dt>

<span id="Never"></span><span id="never"></span><span id="NEVER"></span>

<span id="Never"></span><span id="never"></span><span id="NEVER"></span>**Never** (1)


</dt> <dd>

The rule is applied as a default value to the file if the property is not set on the file (if none of the storage modules returns the property). if the property is set on the file the rule is not reevaluated.

</dd> <dt>

<span id="Aggregate"></span><span id="aggregate"></span><span id="AGGREGATE"></span>

<span id="Aggregate"></span><span id="aggregate"></span><span id="AGGREGATE"></span>**Aggregate** (2)


</dt> <dd>

The rule is applied to the file considering default and existing values using aggregation rules.

</dd> <dt>

<span id="Overwrite"></span><span id="overwrite"></span><span id="OVERWRITE"></span>

<span id="Overwrite"></span><span id="overwrite"></span><span id="OVERWRITE"></span>**Overwrite** (3)


</dt> <dd>

The rule is applied to the file but default and existing values are ignored.

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
</dt> </dl>

 

 





