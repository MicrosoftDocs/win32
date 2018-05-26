---
Description: Defines the utilization thresholds for an IP address range, subnet mask, or block.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 28346333-9c47-47ad-a9d2-9eca006f953b
ms.prod: windows-server-dev
ms.technology:
- internet-protocol-address-management
- windows-management-instrumentation
ms.tgt_platform: multiple
title: MSFT\_IPAM\_IPAddressUtilizationThreshold class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_IPAM\_IPAddressUtilizationThreshold class

Defines the utilization thresholds for an IP address range, subnet mask, or block.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[UMLPackagePath("CIM::Core::CoreElements"), ClassVersion("1.0.0"), dynamic, provider("IPAMServerPSProvider"), AMENDMENT]
class MSFT_IPAM_IPAddressUtilizationThreshold : CIM_ManagedElement
{
  string Caption;
  string Description;
  string ElementName;
  string InstanceID;
  uint32 UnderUtilizationThreshold;
  uint32 OverUtilizationThreshold;
};
```

## Members

The **MSFT\_IPAM\_IPAddressUtilizationThreshold** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_IPAM\_IPAddressUtilizationThreshold** class has these methods.



| Method                                                                                                                   | Description                                                                                   |
|:-------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------|
| [**SetIpamAddressUtilizationThreshold**](setipamaddressutilizationthreshold-msft-ipam-ipaddressutilizationthreshold.md) | Updates the utilization thresholds for an IP address range, subnet mask, or block.<br/> |



 

### Properties

The **MSFT\_IPAM\_IPAddressUtilizationThreshold** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

The Caption property is a short textual description (one- line string) of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Description property provides a textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties, identity data, and description information.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (InstanceID), [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

InstanceID is an optional property that may be used to opaquely and uniquely identify an instance of this class within the scope of the instantiating Namespace. Various subclasses of this class may override this property to make it required, or a key. Such subclasses may also modify the preferred algorithms for ensuring uniqueness that are defined below.

To ensure uniqueness within the NameSpace, the value of InstanceID should be constructed using the following "preferred" algorithm:

&lt;OrgID&gt;:&lt;LocalID&gt;

Where &lt;OrgID&gt; and &lt;LocalID&gt; are separated by a colon (:), and where &lt;OrgID&gt; must include a copyrighted, trademarked, or otherwise unique name that is owned by the business entity that is creating or defining the InstanceID or that is a registered ID assigned to the business entity by a recognized global authority. (This requirement is similar to the &lt;Schema Name&gt;\_&lt;Class Name&gt; structure of Schema class names.) In addition, to ensure uniqueness, &lt;OrgID&gt; must not contain a colon (:). When using this algorithm, the first colon to appear in InstanceID must appear between &lt;OrgID&gt; and &lt;LocalID&gt;.

&lt;LocalID&gt; is chosen by the business entity and should not be reused to identify different underlying (real-world) elements. If not null and the above "preferred" algorithm is not used, the defining entity must assure that the resulting InstanceID is not reused across any InstanceIDs produced by this or other providers for the NameSpace of this instance.

If not set to null for DMTF-defined instances, the "preferred" algorithm must be used with the &lt;OrgID&gt; set to CIM.

</dd> <dt>

**OverUtilizationThreshold**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The threshold percentage that indicates whether an IP address range, subnet, or block is overutilized.

</dd> <dt>

**UnderUtilizationThreshold**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The threshold percentage that indicates whether an IP address range, subnet, or block is underutilized.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                   |
| Namespace<br/>                | Root\\Microsoft\\IPAM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>IPAMServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IPAMServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ManagedElement**](cim-managedelement.md)
</dt> <dt>

[IPAM Server WMI Provider Reference](ipam-server-wmi-provider-reference.md)
</dt> </dl>

 

 




