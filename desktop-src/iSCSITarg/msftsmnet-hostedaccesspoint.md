---
title: MSFTSMNET\_HostedAccessPoint class
description: Associates service access points (SAPs) to the system on which they are hosted.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: fa179fbd-77a5-4a1d-a66a-1c077679d48a
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFTSMNET_HostedAccessPoint class iSCSI Software Target API
- MSFTSMNET_HostedAccessPoint class iSCSI Software Target API , described
topic_type:
- apiref
api_name:
- MSFTSMNET_HostedAccessPoint
- MSFTSMNET_HostedAccessPoint.Antecedent
- MSFTSMNET_HostedAccessPoint.Dependent
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFTSMNET\_HostedAccessPoint class

Associates service access points (SAPs) to the system on which they are hosted. This association is a one-to-many association.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("MSiSCSITargetProv"), Association, Version("1.0.0")]
class MSFTSMNET_HostedAccessPoint : CIM_HostedAccessPoint
{
  CIM_System             REF Antecedent;
  CIM_ServiceAccessPoint REF Dependent;
};
```

## Members

The **MSFTSMNET\_HostedAccessPoint** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFTSMNET\_HostedAccessPoint** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_System**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Min**](https://msdn.microsoft.com/library/aa393650) (1), [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The hosting System.

This property is inherited from [**CIM\_HostedAccessPoint**](cim-hostedaccesspoint.md).

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ServiceAccessPoint**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Weak**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The SAPs that are hosted on this System.

This property is inherited from [**CIM\_HostedAccessPoint**](cim-hostedaccesspoint.md).

</dd> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_HostedAccessPoint**](cim-hostedaccesspoint.md)
</dt> <dt>

[iSCSI Target Server Reference](https://msdn.microsoft.com/library/hh830439)
</dt> </dl>

 

 





