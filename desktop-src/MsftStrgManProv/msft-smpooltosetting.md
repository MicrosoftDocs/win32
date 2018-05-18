---
title: MSFT\_SMPoolToSetting class
description: Represents a relationship between a storage pool and a set of storage pool settings.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '428f77b0-8207-4bc2-8f5c-1540aed2be3c'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_SMPoolToSetting class", "MSFT_SMPoolToSetting class, described"]
topic_type:
- apiref
api_name:
- MSFT_SMPoolToSetting
- MSFT_SMPoolToSetting.Parent
- MSFT_SMPoolToSetting.Child
api_location:
- StorageService.dll
api_type:
- DllExport
---

# MSFT\_SMPoolToSetting class

Represents a relationship between a storage pool and a set of storage pool settings.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, dynamic, provider("WMIStorage")]
class MSFT_SMPoolToSetting
{
  MSFT_SMPool        REF Parent;
  MSFT_SMPoolSetting REF Child;
};
```

## Members

The **MSFT\_SMPoolToSetting** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SMPoolToSetting** class has these properties.

<dl> <dt>

**Child**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_SMPoolSetting**](msft-smpoolsetting.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to the object that represents the storage pool settings.

</dd> <dt>

**Parent**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_SMPool**](msft-smpool.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to the object that represents the storage pool.

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[Windows Storage Management WMI Provider](windows-storage-management-wmi-provider-portal.md)
</dt> </dl>

 

 





