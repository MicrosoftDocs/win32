---
title: MSFTSM\_HostedService class
description: Associates a CIM\_Service with the MSFTSM\_System on which the service is implemented.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '9eca9192-0a4c-4474-b095-e42154208196'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFTSM_HostedService class iSCSI Software Target API", "MSFTSM_HostedService class iSCSI Software Target API , described"]
topic_type:
- apiref
api_name:
- MSFTSM_HostedService
- MSFTSM_HostedService.Antecedent
- MSFTSM_HostedService.Dependent
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
---

# MSFTSM\_HostedService class

Associates a [**CIM\_Service**](https://msdn.microsoft.com/library/aa388442) with the [**MSFTSM\_System**](msftsm-system.md) on which the service is implemented. This is a one-to-many association. A system can host many services, and services are weak with respect to their hosting system. A service is hosted on the system where the logical devices or software features that implement the service are located.

The **MSFTSM\_HostedService** class represents a service that is hosted on a single system. The **CIM\_ApplicationSystem** is used to represent a service that is hosted across multiple systems.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Version("1.0.0"), Provider("MSiSCSITargetProv")]
class MSFTSM_HostedService : CIM_HostedService
{
  CIM_System  REF Antecedent;
  CIM_Service REF Dependent;
};
```

## Members

The **MSFTSM\_HostedService** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFTSM\_HostedService** class has these properties.

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

This property is inherited from [**CIM\_HostedService**](cim-hostedservice.md).

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Service**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Weak**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The Service hosted on the System.

This property is inherited from [**CIM\_HostedService**](cim-hostedservice.md).

</dd> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_HostedService**](cim-hostedservice.md)
</dt> <dt>

[iSCSI Target Server Reference](https://msdn.microsoft.com/library/hh830439)
</dt> </dl>

 

 





