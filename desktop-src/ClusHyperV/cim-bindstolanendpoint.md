---
title: CIM\_BindsToLANEndpoint class
description: Represents an association where a CIM\_ServiceAccessPoint or CIM\_ProtocolEndpoint object depends on an underlying CIM\_LANEndpoint object on the same system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 83ac67a8-bbd3-4344-b069-c80aa9b3e678
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_BindsToLANEndpoint class
- CIM_BindsToLANEndpoint class, described
topic_type:
- apiref
api_name:
- CIM_BindsToLANEndpoint
- CIM_BindsToLANEndpoint.Antecedent
- CIM_BindsToLANEndpoint.Dependent
- CIM_BindsToLANEndpoint.FrameType
api_location:
- VMMS.exe
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_BindsToLANEndpoint class

Represents an association where a [**CIM\_ServiceAccessPoint**](cim-serviceaccesspoint.md) or [**CIM\_ProtocolEndpoint**](cim-protocolendpoint.md) object depends on an underlying [**CIM\_LANEndpoint**](cim-lanendpoint.md) object on the same system.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Abstract, Version("2.6.0"), UMLPackagePath("CIM::Network::ProtocolEndpoints")]
class CIM_BindsToLANEndpoint : CIM_BindsTo
{
  CIM_LANEndpoint        REF Antecedent;
  CIM_ServiceAccessPoint REF Dependent;
  uint16                     FrameType;
};
```

## Members

The **CIM\_BindsToLANEndpoint** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_BindsToLANEndpoint** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_LANEndpoint**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent")
</dt> </dl>

The underlying [**CIM\_LANEndpoint**](cim-lanendpoint.md) object.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ServiceAccessPoint**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

The [**CIM\_ServiceAccessPoint**](cim-serviceaccesspoint.md) or [**CIM\_ProtocolEndpoint**](cim-protocolendpoint.md) object that is dependent on the [**CIM\_LANEndpoint**](cim-lanendpoint.md).

</dd> <dt>

**FrameType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The framing method for the upper layer service access point or protocol endpoint.

> [!Note]  
> Raw802.3 is only known to be used with the IPX protocol.

 

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Ethernet"></span><span id="ethernet"></span><span id="ETHERNET"></span>

**Ethernet** (1)


</dt> <dd></dd> <dt>

<span id="802.2"></span>

**802.2** (2)


</dt> <dd></dd> <dt>

<span id="SNAP"></span><span id="snap"></span>

**SNAP** (3)


</dt> <dd></dd> <dt>

<span id="Raw802.3"></span><span id="raw802.3"></span><span id="RAW802.3"></span>

**Raw802.3** (4)


</dt> <dd></dd> </dl>

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

[**CIM\_BindsTo**](cim-bindsto.md)
</dt> <dt>

[Failover Clustering Hyper-V WMI Provider](failover-clustering-hyper-v-wmi-provider-portal.md)
</dt> </dl>

 

 





