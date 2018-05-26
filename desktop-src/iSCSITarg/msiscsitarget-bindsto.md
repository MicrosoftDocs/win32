---
title: MSISCSITARGET\_BindsTo class
description: Associates a CIM\_ServiceAccessPoint class, as the requestor of protocol services, to a CIM\_ProtocolEndpoint class.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a27ea588-5057-40e2-b876-eb0ad4a4bc5b
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSISCSITARGET_BindsTo class iSCSI Software Target API
- MSISCSITARGET_BindsTo class iSCSI Software Target API , described
topic_type:
- apiref
api_name:
- MSISCSITARGET_BindsTo
- MSISCSITARGET_BindsTo.Antecedent
- MSISCSITARGET_BindsTo.Dependent
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSISCSITARGET\_BindsTo class

Associates a [**CIM\_ServiceAccessPoint**](https://msdn.microsoft.com/library/aa388447) class, as the requestor of protocol services, to a [**CIM\_ProtocolEndpoint**](https://msdn.microsoft.com/library/cc136899) class.

Typically, this association is established between a [**CIM\_ServiceAccessPoint**](https://msdn.microsoft.com/library/aa388447) class and a [**CIM\_ProtocolEndpoint**](https://msdn.microsoft.com/library/cc136899) class on a single system. Because a **CIM\_ProtocolEndpoint** class is a child of the **CIM\_ServiceAccessPoint** class, this binding can be used to represent two layers in a stack of protocols. In this scenario, the **Dependent** property represents the upper layer, and the **Antecedent** property represents the lower layer.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, Provider("MSiSCSITargetProv"), Association, Version("1.0.0")]
class MSISCSITARGET_BindsTo : CIM_BindsTo
{
  CIM_ProtocolEndpoint   REF Antecedent;
  CIM_ServiceAccessPoint REF Dependent;
};
```

## Members

The **MSISCSITARGET\_BindsTo** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSISCSITARGET\_BindsTo** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ProtocolEndpoint**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A [**CIM\_ProtocolEndpoint**](https://msdn.microsoft.com/library/cc136899) containing the lower-level endpoint that is accessed by the SAP.

This property is inherited from [**CIM\_BindsTo**](cim-bindsto.md).

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ServiceAccessPoint**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A [**CIM\_ServiceAccessPoint**](https://msdn.microsoft.com/library/aa388447) containing the AccessPoint or ProtocolEndpoint that is dependent on the lower-level endpoint.

This property is inherited from [**CIM\_BindsTo**](cim-bindsto.md).

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

[**CIM\_BindsTo**](cim-bindsto.md)
</dt> <dt>

[iSCSI Target Server Reference](https://msdn.microsoft.com/library/hh830439)
</dt> </dl>

 

 





