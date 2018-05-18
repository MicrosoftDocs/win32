---
title: MSISCSITARGET\_HostedAccessPoint class
description: Defines an association between a Service Access Point (SAP) and the System on which it is provided.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '005e68cd-9480-435d-97f5-8747935526ea'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSISCSITARGET_HostedAccessPoint class iSCSI Software Target API", "MSISCSITARGET_HostedAccessPoint class iSCSI Software Target API , described"]
topic_type:
- apiref
api_name:
- MSISCSITARGET_HostedAccessPoint
- MSISCSITARGET_HostedAccessPoint.Antecedent
- MSISCSITARGET_HostedAccessPoint.Dependent
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
---

# MSISCSITARGET\_HostedAccessPoint class

Defines an association between a Service Access Point (SAP) and the System on which it is provided. The cardinality of this association is one-to-many and is weak with respect to the System. Each System can host many SAPs.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("MSiSCSITargetProv"), Association, Version("1.0.0")]
class MSISCSITARGET_HostedAccessPoint : CIM_HostedAccessPoint
{
  CIM_System             REF Antecedent;
  CIM_ServiceAccessPoint REF Dependent;
};
```

## Members

The **MSISCSITARGET\_HostedAccessPoint** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSISCSITARGET\_HostedAccessPoint** class has these properties.

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
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_HostedAccessPoint**](cim-hostedaccesspoint.md)
</dt> <dt>

[iSCSI Target Server Reference](https://msdn.microsoft.com/library/hh830439)
</dt> <dt>

[**CIM\_HostedAccessPoint**](https://msdn.microsoft.com/library/aa387858)
</dt> </dl>

 

 





