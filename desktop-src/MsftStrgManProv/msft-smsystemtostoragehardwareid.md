---
title: MSFT\_SMSystemToStorageHardwareID class
description: Represents a relationship between a system and a storage hardware ID.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f0e7cfa0-9032-483c-b7ea-c76b46587573
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_SMSystemToStorageHardwareID class
- MSFT_SMSystemToStorageHardwareID class, described
topic_type:
- apiref
api_name:
- MSFT_SMSystemToStorageHardwareID
- MSFT_SMSystemToStorageHardwareID.Parent
- MSFT_SMSystemToStorageHardwareID.Child
api_location:
- StorageService.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_SMSystemToStorageHardwareID class

Represents a relationship between a system and a storage hardware ID.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, dynamic, provider("WMIStorage")]
class MSFT_SMSystemToStorageHardwareID
{
  MSFT_SMSystem            REF Parent;
  MSFT_SMStorageHardwareID REF Child;
};
```

## Members

The **MSFT\_SMSystemToStorageHardwareID** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SMSystemToStorageHardwareID** class has these properties.

<dl> <dt>

**Child**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_SMStorageHardwareID**](msft-smstoragehardwareid.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to the object that represents the storage hardware ID in the relationship.

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

 

 





