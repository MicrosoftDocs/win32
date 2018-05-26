---
title: CIM\_SwitchesAmong class
description: Represents a switch service, which switches frames between switch ports.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3693e171-ed60-468e-93f4-42909b35a0ba
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_SwitchesAmong class
- CIM_SwitchesAmong class, described
topic_type:
- apiref
api_name:
- CIM_SwitchesAmong
- CIM_SwitchesAmong.Antecedent
- CIM_SwitchesAmong.Dependent
api_location:
- VMMS.exe
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_SwitchesAmong class

Represents a switch service, which switches frames between switch ports.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Abstract, Version("2.6.0"), UMLPackagePath("CIM::Network::SwitchingBridging")]
class CIM_SwitchesAmong : CIM_ForwardsAmong
{
  CIM_SwitchPort    REF Antecedent;
  CIM_SwitchService REF Dependent;
};
```

## Members

The **CIM\_SwitchesAmong** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_SwitchesAmong** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_SwitchPort**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent")
</dt> </dl>

A reference to the switch port.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_SwitchService**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent"), [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

A reference to the switching service.

</dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**CIM\_ForwardsAmong**](cim-forwardsamong.md)
</dt> <dt>

[Failover Clustering Hyper-V WMI Provider](failover-clustering-hyper-v-wmi-provider-portal.md)
</dt> </dl>

 

 





