---
title: MsftSil\_ComputerIdentity class
description: The MsftSil\_ComputerIdentity WMI class encapsulates identification properties of a computer.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '7e5be55b-5a21-41df-84dc-9f9a349b134d'
ms.prod: 'windows-server-dev'
ms.technology:
- 'software-inventory-logging'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MsftSil_ComputerIdentity class Software Inventory Logging", "MsftSil_ComputerIdentity class Software Inventory Logging , described"]
topic_type:
- apiref
api_name:
- MsftSil_ComputerIdentity
- MsftSil_ComputerIdentity.ID
- MsftSil_ComputerIdentity.UUID
- MsftSil_ComputerIdentity.VMGUID
- MsftSil_ComputerIdentity.Name
- MsftSil_ComputerIdentity.HypervisorHostName
api_location:
- SILProvider.dll
api_type:
- DllExport
---

# MsftSil\_ComputerIdentity class

The **MsftSil\_ComputerIdentity** WMI class encapsulates identification properties of a computer.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("silprovider"), AMENDMENT]
class MsftSil_ComputerIdentity : MsftSil_Data
{
  string ID;
  string UUID;
  string VMGUID;
  string Name;
  string HypervisorHostName;
};
```

## Members

The **MsftSil\_ComputerIdentity** class has these types of members:

-   [Properties](#properties)

### Properties

The **MsftSil\_ComputerIdentity** class has these properties.

<dl> <dt>

**HypervisorHostName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the computer running the hypervisor that hosts this computer.

</dd> <dt>

**ID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The ID of the computer.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of this computer.

</dd> <dt>

**UUID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The **GUID** of the computer.

</dd> <dt>

**VMGUID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The **GUID** used to identify the virtual machine hosting this computer.

</dd> </dl>

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                          |
| Namespace<br/>                | Root\\InventoryLogging<br/>                                                          |
| MOF<br/>                      | <dl> <dt>SILProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SILProvider.dll</dt> </dl> |



 

 





