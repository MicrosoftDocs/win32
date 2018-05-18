---
title: MSFT\_SMFabricToSwitch class
description: Represents a relationship between a Windows Fabric storage service and a switch.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'e5ce3dd0-a99f-48c7-a406-bf715dfaeb60'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_SMFabricToSwitch class", "MSFT_SMFabricToSwitch class, described"]
topic_type:
- apiref
api_name:
- MSFT_SMFabricToSwitch
- MSFT_SMFabricToSwitch.Parent
- MSFT_SMFabricToSwitch.Child
api_location:
- StorageService.dll
api_type:
- DllExport
---

# MSFT\_SMFabricToSwitch class

Represents a relationship between a Windows Fabric storage service and a switch.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, dynamic, provider("WMIStorage")]
class MSFT_SMFabricToSwitch
{
  MSFT_SMFabric REF Parent;
  MSFT_SMSwitch REF Child;
};
```

## Members

The **MSFT\_SMFabricToSwitch** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SMFabricToSwitch** class has these properties.

<dl> <dt>

**Child**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_SMSwitch**](msft-smswitch.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to the [**MSFT\_SMSwitch**](msft-smswitch.md) object that represents the switch in the relationship.

</dd> <dt>

**Parent**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_SMFabric**](msft-smfabric.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to the [**MSFT\_SMFabric**](msft-smfabric.md) object that represents the Windows Fabric storage service in the relationship.

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

 

 





