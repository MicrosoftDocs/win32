---
title: MSFT\_SMSystemToCapabilities class
description: Represents a relationship between a system and a set of system capabilities.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 587359db-0041-485c-9140-a4041ff1cfa3
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_SMSystemToCapabilities class
- MSFT_SMSystemToCapabilities class, described
topic_type:
- apiref
api_name:
- MSFT_SMSystemToCapabilities
- MSFT_SMSystemToCapabilities.Parent
- MSFT_SMSystemToCapabilities.Child
api_location:
- StorageService.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_SMSystemToCapabilities class

Represents a relationship between a system and a set of system capabilities.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, dynamic, provider("WMIStorage")]
class MSFT_SMSystemToCapabilities
{
  MSFT_SMSystem             REF Parent;
  MSFT_SMSystemCapabilities REF Child;
};
```

## Members

The **MSFT\_SMSystemToCapabilities** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SMSystemToCapabilities** class has these properties.

<dl> <dt>

**Child**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_SMSystemCapabilities**](msft-smsystemcapabilities.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to the object that represents the system capabilities in the relationship.

</dd> <dt>

**Parent**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_SMSystem**](msft-smsystem.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to the object that represents the system in the relationship.

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

 

 





