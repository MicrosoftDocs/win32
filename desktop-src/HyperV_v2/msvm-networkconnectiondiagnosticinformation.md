---
Description: Provides information about the network connectivity for a virtual machine.
ms.assetid: 59503c1b-203b-46ec-8a65-f21a746f170f
title: Msvm\_NetworkConnectionDiagnosticInformation class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Msvm\_NetworkConnectionDiagnosticInformation class

Provides information about the network connectivity for a virtual machine.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[AMENDMENT]
class Msvm_NetworkConnectionDiagnosticInformation
{
  uint32 RoundTripTime;
};
```

## Members

The **Msvm\_NetworkConnectionDiagnosticInformation** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_NetworkConnectionDiagnosticInformation** class has these properties.

<dl> <dt>

**RoundTripTime**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The round trip time for the ping request.

</dd> </dl>

## Requirements



|                                     |                                                                                                         |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1703 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                          |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



 

 




