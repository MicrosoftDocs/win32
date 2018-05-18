---
title: CIM\_BindsTo class
description: Represents an association where a CIM\_ServiceAccessPoint object requests protocol services from a CIM\_ProtocolEndpoint object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '0e73e7b8-5949-4ff1-b1fb-56c90fdd8626'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CIM_BindsTo class", "CIM_BindsTo class, described"]
topic_type:
- apiref
api_name:
- CIM_BindsTo
- CIM_BindsTo.Antecedent
- CIM_BindsTo.Dependent
api_location:
- VMMS.exe
api_type:
- DllExport
---

# CIM\_BindsTo class

Represents an association where a [**CIM\_ServiceAccessPoint**](cim-serviceaccesspoint.md) object requests protocol services from a [**CIM\_ProtocolEndpoint**](cim-protocolendpoint.md) object.

This association usually runs between service access points and endpoints on the same system. Because a [**CIM\_ProtocolEndpoint**](cim-protocolendpoint.md) is a kind of [**CIM\_ServiceAccessPoint**](cim-serviceaccesspoint.md), this binding can be used to establish a layering of two protocols, where the upper layer is represented by the **Dependent** property and the lower layer is represented by the **Antecedent** property.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Abstract, Version("2.10.0"), UMLPackagePath("CIM::Core::Service")]
class CIM_BindsTo : CIM_SAPSAPDependency
{
  CIM_ProtocolEndpoint   REF Antecedent;
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

The lower level endpoint that is accessed by the service access point.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ServiceAccessPoint**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

The access point or protocol endpoint that is dependent on the lower level endpoint.

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

[**CIM\_SAPSAPDependency**](cim-sapsapdependency.md)
</dt> <dt>

[Failover Clustering Hyper-V WMI Provider](failover-clustering-hyper-v-wmi-provider-portal.md)
</dt> </dl>

 

 





