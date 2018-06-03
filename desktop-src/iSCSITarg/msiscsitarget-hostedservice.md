---
title: MSISCSITARGET\_HostedService class
description: Defines an association between a Service and the System on which the functionality is located.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e2644154-6368-4f36-b977-a6ac19431682
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSISCSITARGET_HostedService class iSCSI Software Target API
- MSISCSITARGET_HostedService class iSCSI Software Target API , described
topic_type:
- apiref
api_name:
- MSISCSITARGET_HostedService
- MSISCSITARGET_HostedService.Antecedent
- MSISCSITARGET_HostedService.Dependent
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSISCSITARGET\_HostedService class

Defines an association between a Service and the System on which the functionality is located.The cardinality of this association is one-to-many and is weak with respect to the System. Each System can host many services.

A Service is hosted on the System where the **CIM\_LogicalDevices** or **CIM\_SoftwareFeatures** that implement the [**CIM\_Service**](https://msdn.microsoft.com/library/aa388442) are located. This model does not represent services hosted across multiple systems.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("MSiSCSITargetProv"), Association, Version("1.0.0")]
class MSISCSITARGET_HostedService : CIM_HostedService
{
  CIM_System  REF Antecedent;
  CIM_Service REF Dependent;
};
```

## Members

The **MSISCSITARGET\_HostedService** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSISCSITARGET\_HostedService** class has these properties.

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
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_HostedService**](cim-hostedservice.md)
</dt> <dt>

[iSCSI Target Server Reference](https://msdn.microsoft.com/library/hh830439)
</dt> <dt>

[**CIM\_HostedService**](https://msdn.microsoft.com/library/aa387865)
</dt> <dt>

[**CIM\_Service**](https://msdn.microsoft.com/library/aa388442)
</dt> </dl>

 

 





