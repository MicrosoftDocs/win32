---
title: Msvm\_ComputerSystemSummaryInformation class
description: Associates a hosting computer system or a virtual machine with summary information.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '02cded9e-cfb0-4cf6-a861-79be36101fe6'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Msvm_ComputerSystemSummaryInformation class", "Msvm_ComputerSystemSummaryInformation class, described"]
topic_type:
- apiref
api_name:
- Msvm_ComputerSystemSummaryInformation
- Msvm_ComputerSystemSummaryInformation.Antecedent
- Msvm_ComputerSystemSummaryInformation.Dependent
api_location:
- VMMS.exe
api_type:
- DllExport
---

# Msvm\_ComputerSystemSummaryInformation class

Associates a hosting computer system or a virtual machine with summary information.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Dynamic, Association, Provider("VmmsWmiInstanceAndMethodProvider")]
class Msvm_ComputerSystemSummaryInformation : CIM_ElementView
{
  CIM_ComputerSystem          REF Antecedent;
  Msvm_SummaryInformationBase REF Dependent;
};
```

## Members

The **Msvm\_ComputerSystemSummaryInformation** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_ComputerSystemSummaryInformation** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ComputerSystem**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent")
</dt> </dl>

A [**CIM\_ComputerSystem**](cim-computersystem.md) reference to the hosting computer system or a virtual machine.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **Msvm\_SummaryInformationBase**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

An [**Msvm\_SummaryInformationBase**](msvm-summaryinformationbase.md) reference to the summary information.

</dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**CIM\_ElementView**](cim-elementview.md)
</dt> <dt>

[Failover Clustering Hyper-V WMI Provider](failover-clustering-hyper-v-wmi-provider-portal.md)
</dt> </dl>

 

 





