---
title: MSFT\_SMProviderToSystem class
description: Represents a relationship between a storage provider and a system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 949dc838-1c18-42d6-8a84-40fc3af24882
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_SMProviderToSystem class
- MSFT_SMProviderToSystem class, described
topic_type:
- apiref
api_name:
- MSFT_SMProviderToSystem
- MSFT_SMProviderToSystem.Parent
- MSFT_SMProviderToSystem.Child
api_location:
- StorageService.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_SMProviderToSystem class

Represents a relationship between a storage provider and a system.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, dynamic, provider("WMIStorage")]
class MSFT_SMProviderToSystem
{
  MSFT_SMProvider REF Parent;
  MSFT_SMSystem   REF Child;
};
```

## Members

The **MSFT\_SMProviderToSystem** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SMProviderToSystem** class has these properties.

<dl> <dt>

**Child**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_SMSystem**](msft-smsystem.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to the object that represents the system.

</dd> <dt>

**Parent**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_SMProvider**](msft-smprovider.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to the object that represents the storage provider.

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[Windows Storage Management WMI Provider](windows-storage-management-wmi-provider-portal.md)
</dt> </dl>

 

 





