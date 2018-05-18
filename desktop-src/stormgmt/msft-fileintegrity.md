---
title: MSFT\_FileIntegrity class
description: Represents the file integrity state for a file.
ms.assetid: '1CDF98E4-3E19-4324-AE61-15F2FEF94BBA'
keywords: ["MSFT_FileIntegrity class Windows Storage Management API", "MSFT_FileIntegrity class Windows Storage Management API , described"]
topic_type:
- apiref
api_name:
- MSFT_FileIntegrity
- MSFT_FileIntegrity.FileName
- MSFT_FileIntegrity.Enabled
- MSFT_FileIntegrity.Enforced
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
---

# MSFT\_FileIntegrity class

Represents the file integrity state for a file.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
class MSFT_FileIntegrity
{
  String  FileName;
  Boolean Enabled;
  Boolean Enforced;
};
```

## Members

The **MSFT\_FileIntegrity** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_FileIntegrity** class has these methods.



| Method                                      | Description                                                                 |
|:--------------------------------------------|:----------------------------------------------------------------------------|
| [**Get**](msft-fileintegrity-get.md)       | Retrieves the file integrity information for the specified file.<br/> |
| [**Repair**](msft-fileintegrity-repair.md) | Scrubs the data for the specified file.<br/>                          |
| [**Set**](msft-fileintegrity-set.md)       | Sets the file integrity state for the specified file.<br/>            |



 

### Properties

The **MSFT\_FileIntegrity** class has these properties.

<dl> <dt>

**Enabled**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies whether integrity streams are enabled for this file.

</dd> <dt>

**Enforced**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies whether integrity streams are enforced for this file.

</dd> <dt>

**FileName**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the file.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



 

 





