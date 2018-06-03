---
title: MSFT\_FSRMMgmtProperty class
description: Represents a FSRM management property which is a classification property that includes \ 0034;Folders \ 0034; (2) in its MSFT\_FSRMClassificationPropertyDefinition.AppliesTo property and whose MSFT\_FSRMClassificationPropertyDefinition.Flags property does not include the \ 0034;Secure \ 0034; (4) value.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 50047152-7f78-4871-9880-9ebaf51296e2
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- MSFT_FSRMMgmtProperty class File Server Resource Manager
- MSFT_FSRMMgmtProperty class File Server Resource Manager , described
topic_type:
- apiref
api_name:
- MSFT_FSRMMgmtProperty
- MSFT_FSRMMgmtProperty.Namespace
- MSFT_FSRMMgmtProperty.Exists
- MSFT_FSRMMgmtProperty.PropertyValue
api_location:
- SrmSvc.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_FSRMMgmtProperty class

Represents a FSRM management property which is a classification property that includes "Folders" (2) in its [**MSFT\_FSRMClassificationPropertyDefinition.AppliesTo**](msft-fsrmclassificationpropertydefinition.md) property and whose **MSFT\_FSRMClassificationPropertyDefinition.Flags** property does not include the "Secure" (4) value.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("FSRMWmiProvider")]
class MSFT_FSRMMgmtProperty
{
  string                     Namespace;
  boolean                    Exists;
  MSFT_FSRMMgmtPropertyValue PropertyValue[];
};
```

## Members

The **MSFT\_FSRMMgmtProperty** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_FSRMMgmtProperty** class has these methods.



| Method                                                                 | Description                                                                  |
|:-----------------------------------------------------------------------|:-----------------------------------------------------------------------------|
| [**DeleteMgmtProperty**](msft-fsrmmgmtproperty-deletemgmtproperty.md) | Deletes a FSRM management property.<br/>                               |
| [**GetMgmtProperty**](msft-fsrmmgmtproperty-getmgmtproperty.md)       | Retrieves management properties that meet the specified criteria.<br/> |
| [**SetMgmtProperty**](msft-fsrmmgmtproperty-setmgmtproperty.md)       | Sets a FSRM management property.<br/>                                  |



 

### Properties

The **MSFT\_FSRMMgmtProperty** class has these properties.

<dl> <dt>

**Exists**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the local path exists.

</dd> <dt>

**Namespace**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string representing a local path to a folder. Must not exceed the value of **MAX\_PATH**. Required.

</dd> <dt>

**PropertyValue**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_FSRMMgmtPropertyValue** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**MSFT\_FSRMMgmtPropertyValue**](msft-fsrmmgmtpropertyvalue.md)")
</dt> </dl>

An array of instances of the [**MSFT\_FSRMMgmtPropertyValue**](msft-fsrmmgmtpropertyvalue.md) class representing the management property values.

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

[**MSFT\_FSRMClassificationPropertyDefinition**](msft-fsrmclassificationpropertydefinition.md)
</dt> </dl>

 

 





