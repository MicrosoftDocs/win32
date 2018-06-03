---
title: CIM\_BindsTo class
description: This association establishes a ServiceAccessPoint as a requestor of protocol services from a ProtocolEndpoint.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 56b2aaef-02fc-43e7-b303-f03b0b489e7f
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_BindsTo class iSCSI Software Target API
- CIM_BindsTo class iSCSI Software Target API , described
topic_type:
- apiref
api_name:
- CIM_BindsTo
- CIM_BindsTo.Antecedent
- CIM_BindsTo.Dependent
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CIM\_BindsTo class

This association establishes a ServiceAccessPoint as a requestor of protocol services from a ProtocolEndpoint. Typically, this association runs between SAPs and endpoints on a single system. Because a ProtocolEndpoint is a kind of ServiceAccessPoint, this binding can be used to establish a layering of two protocols, with the upper layer represented by the Dependent and the lower layer represented by the Antecedent.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Abstract, Version("2.10.0"), UMLPackagePath("CIM::Core::Service")]
class CIM_BindsTo : CIM_SAPSAPDependency
{
  CIM_ProtocolEndpoint   REF Antecedent;
  CIM_ServiceAccessPoint REF Dependent;
};
```

## Members

The **CIM\_BindsTo** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_BindsTo** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ProtocolEndpoint**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent")
</dt> </dl>

A [**CIM\_ProtocolEndpoint**](https://msdn.microsoft.com/library/cc136899) containing the lower-level endpoint that is accessed by the SAP.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ServiceAccessPoint**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

A [**CIM\_ServiceAccessPoint**](https://msdn.microsoft.com/library/aa388447) containing the AccessPoint or ProtocolEndpoint that is dependent on the lower-level endpoint.

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

[**CIM\_SAPSAPDependency**](cim-sapsapdependency.md)
</dt> </dl>

 

 





