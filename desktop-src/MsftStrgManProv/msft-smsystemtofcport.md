---
title: MSFT\_SMSystemToFCPort class
description: Represents a relationship between a system and a Fibre Channel (FC) port.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '81ededd7-a6c3-4eb2-bd53-63a9803ac5f2'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_SMSystemToFCPort class", "MSFT_SMSystemToFCPort class, described"]
topic_type:
- apiref
api_name:
- MSFT_SMSystemToFCPort
- MSFT_SMSystemToFCPort.Parent
- MSFT_SMSystemToFCPort.Child
api_location:
- StorageService.dll
api_type:
- DllExport
---

# MSFT\_SMSystemToFCPort class

Represents a relationship between a system and a Fibre Channel (FC) port.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, dynamic, provider("WMIStorage")]
class MSFT_SMSystemToFCPort
{
  MSFT_SMSystem REF Parent;
  MSFT_SMFCPort REF Child;
};
```

## Members

The **MSFT\_SMSystemToFCPort** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SMSystemToFCPort** class has these properties.

<dl> <dt>

**Child**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_SMFCPort**](msft-smfcport.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to the object that represents the Fibre Channel (FC) port in the relationship.

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
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[Windows Storage Management WMI Provider](windows-storage-management-wmi-provider-portal.md)
</dt> </dl>

 

 





