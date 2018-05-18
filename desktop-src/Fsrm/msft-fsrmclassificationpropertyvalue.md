---
title: MSFT\_FSRMClassificationPropertyValue class
description: Represents a classification property value.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'c48f0fef-0e0f-4fe4-b70c-6007f29210ea'
ms.prod: 'windows-server-dev'
ms.technology: 'file-server-resource-manager'
ms.tgt_platform: multiple
keywords: ["MSFT_FSRMClassificationPropertyValue class File Server Resource Manager", "MSFT_FSRMClassificationPropertyValue class File Server Resource Manager , described"]
topic_type:
- apiref
api_name:
- MSFT_FSRMClassificationPropertyValue
- MSFT_FSRMClassificationPropertyValue.Name
- MSFT_FSRMClassificationPropertyValue.DisplayName
- MSFT_FSRMClassificationPropertyValue.Description
- MSFT_FSRMClassificationPropertyValue.Id
api_location:
- SrmSvc.dll
api_type:
- DllExport
---

# MSFT\_FSRMClassificationPropertyValue class

Represents a classification property value.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("FSRMWmiProvider")]
class MSFT_FSRMClassificationPropertyValue
{
  string Name;
  string DisplayName;
  string Description;
  string Id;
};
```

## Members

The **MSFT\_FSRMClassificationPropertyValue** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_FSRMClassificationPropertyValue** class has these methods.



| Method                                                                                  | Description                                         |
|:----------------------------------------------------------------------------------------|:----------------------------------------------------|
| [**CreatePropertyValue**](msft-fsrmclassificationpropertyvalue-createpropertyvalue.md) | Creates a classification property value.<br/> |



 

### Properties

The **MSFT\_FSRMClassificationPropertyValue** class has these properties.

<dl> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Description of the property value.

</dd> <dt>

**DisplayName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Display name of the property value.

</dd> <dt>

**Id**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**GUID** in string form representing this property value.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Name of the property value.

</dd> </dl>

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

 

 





