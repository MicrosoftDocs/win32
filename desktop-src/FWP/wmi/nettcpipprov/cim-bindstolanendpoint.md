---
description: This association makes explicit the dependency of a SAP or protocol endpoint on an underlying LAN endpoint, on the same system.
ms.assetid: a24168ee-9100-44ee-8877-c3fb1952f4b5
title: CIM_BindsToLANEndpoint WMI class
ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_BindsToLANEndpoint
- CIM_BindsToLANEndpoint.Antecedent
- CIM_BindsToLANEndpoint.Dependent
- CIM_BindsToLANEndpoint.FrameType
api_type: 
- DllExport
api_location: 
- netTCPIP.dll
ROBOTS: INDEX,FOLLOW
---

# CIM\_BindsToLANEndpoint WMI class

This association makes explicit the dependency of a SAP or protocol endpoint on an underlying LAN endpoint, on the same system.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, UMLPackagePath("CIM::Network::ProtocolEndpoints"), Version("2.6.0"), AMENDMENT]
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

Qualifiers: [**key**](/windows/win32/wmisdk/key-qualifier), [**Override**](/windows/win32/wmisdk/standard-qualifiers) ("Antecedent")
</dt> </dl>

The underlying [**CIM\_LANEndpoint**](cim-lanendpoint.md), which is depended upon.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ServiceAccessPoint**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/win32/wmisdk/key-qualifier), [**Override**](/windows/win32/wmisdk/standard-qualifiers) ("Dependent")
</dt> </dl>

A [**CIM\_ServiceAccessPoint**](cim-serviceaccesspoint.md) containing the **AccessPoint** or **ProtocolEndpoint** dependent on the LAN endpoint.

</dd> <dt>

**FrameType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This describes the framing method for the upper layer SAP or Endpoint that is bound to the LAN endpoint. Note that "Raw802.3" is only known to be used with the IPX protocol.

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Ethernet"></span><span id="ethernet"></span><span id="ETHERNET"></span>**Ethernet** (1)
</dt> <dt>

<span id="802.2"></span>**802.2** (2)
</dt> <dt>

<span id="SNAP"></span><span id="snap"></span>**SNAP** (3)
</dt> <dt>

<span id="Raw802.3"></span><span id="raw802.3"></span><span id="RAW802.3"></span>**Raw802.3** (4)
</dt> </dl>

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\standardcimv2<br/>                                                          |
| MOF<br/>                      | <dl> <dt>NetTCPIP.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetTCPIP.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_BindsTo**](cim-bindsto.md)
</dt> </dl>

 

