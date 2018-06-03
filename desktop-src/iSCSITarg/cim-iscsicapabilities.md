---
title: CIM\_iSCSICapabilities class
description: The capabilites for an iSCSI Network Entity.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 51e26ebd-7fb9-48cd-a538-a2cfd30a0532
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_iSCSICapabilities class iSCSI Software Target API
- CIM_iSCSICapabilities class iSCSI Software Target API , described
topic_type:
- apiref
api_name:
- CIM_iSCSICapabilities
- CIM_iSCSICapabilities.Caption
- CIM_iSCSICapabilities.Description
- CIM_iSCSICapabilities.InstanceID
- CIM_iSCSICapabilities.ElementName
- CIM_iSCSICapabilities.MinimumSpecificationVersionSupported
- CIM_iSCSICapabilities.MaximumSpecificationVersionSupported
- CIM_iSCSICapabilities.AuthenticationMethodsSupported
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CIM\_iSCSICapabilities class

The capabilites for an iSCSI Network Entity. An instance of this class will be associated by ElementCapabilities to a instance of ComputerSystem that represents the Network Entity. These capability properties are associated to a Network Entity/ComputerSystem since they affect all login negotiations on all iSCSI ProtocolEndpoints aggregated to the system.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract, Version("2.11.0"), UMLPackagePath("CIM::Network::iSCSI")]
class CIM_iSCSICapabilities : CIM_Capabilities
{
  string Caption;
  string Description;
  string InstanceID;
  string ElementName;
  uint8  MinimumSpecificationVersionSupported;
  uint8  MaximumSpecificationVersionSupported;
  uint16 AuthenticationMethodsSupported[];
};
```

## Members

The **CIM\_iSCSICapabilities** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_iSCSICapabilities** class has these properties.

<dl> <dt>

**AuthenticationMethodsSupported**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|IPS-AUTH-MIB.ipsAuthCredAuthMethod"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_iSCSIConnectionSettings.PrimaryAuthenticationMethod", "CIM\_iSCSIConnectionSettings.SecondaryAuthenticationMethod", "CIM\_iSCSIConnection.AuthenticationMethodUsed")
</dt> </dl>

An array containing a list of authentication methods supported by this Network Entity.

<dt>

<span id="_None"></span><span id="_none"></span><span id="_NONE"></span>

**(None** (2)


</dt> <dd></dd> <dt>

<span id="SRP"></span><span id="srp"></span>

**SRP** (3)


</dt> <dd></dd> <dt>

<span id="CHAP"></span><span id="chap"></span>

**CHAP** (4)


</dt> <dd></dd> <dt>

<span id="Kerberos"></span><span id="kerberos"></span><span id="KERBEROS"></span>

**Kerberos** (5)


</dt> <dd></dd> </dl>

</dd> <dt>

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

Contains a textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The user friendly name for this instance of Capabilities. In addition, the user friendly name can be used as a index property for a search of query. (Note: Name does not have to be unique within a namespace.)

This property is inherited from [**CIM\_Capabilities**](cim-capabilities.md).

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Within the scope of the instantiating Namespace, InstanceID opaquely and uniquely identifies an instance of this class. In order to ensure uniqueness within the NameSpace, the value of InstanceID SHOULD be constructed using the following 'preferred' algorithm: &lt;OrgID&gt;:&lt;LocalID&gt; Where &lt;OrgID&gt; and &lt;LocalID&gt; are separated by a colon ':', and where &lt;OrgID&gt; MUST include a copyrighted, trademarked or otherwise unique name that is owned by the business entity creating/defining the InstanceID, or is a registered ID that is assigned to the business entity by a recognized global authority (This is similar to the &lt;Schema Name&gt;\_&lt;Class Name&gt; structure of Schema class names.) In addition, to ensure uniqueness &lt;OrgID&gt; MUST NOT contain a colon (':'). When using this algorithm, the first colon to appear in InstanceID MUST appear between &lt;OrgID&gt; and &lt;LocalID&gt;. &lt;LocalID&gt; is chosen by the business entity and SHOULD not be re-used to identify different underlying (real-world) elements. If the above 'preferred' algorithm is not used, the defining entity MUST assure that the resultant InstanceID is not re-used across any InstanceIDs produced by this or other providers for this instance's NameSpace. For DMTF defined instances, the 'preferred' algorithm MUST be used with the &lt;OrgID&gt; set to 'CIM'.

This property is inherited from [**CIM\_Capabilities**](cim-capabilities.md).

</dd> <dt>

**MaximumSpecificationVersionSupported**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MinValue**](https://msdn.microsoft.com/library/aa393650) (0), [**MaxValue**](https://msdn.microsoft.com/library/aa393650) (255), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|ISCSI-MIB.iscsiInstVersionMax"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_iSCSICapabilities.MinimumSpecificationVersionSupported", "CIM\_iSCSIConnection.ActiveiSCSIVersion")
</dt> </dl>

The maximum version number of the iSCSI specification such that this iSCSI instance supports this maximum value, the minimum value indicated by the corresponding property MinimumSpecificationVersionSupported, and all versions in between.

</dd> <dt>

**MinimumSpecificationVersionSupported**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MinValue**](https://msdn.microsoft.com/library/aa393650) (0), [**MaxValue**](https://msdn.microsoft.com/library/aa393650) (255), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|iSCSI-MIB.iscsiInstVersionMin"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_iSCSICapabilities.MaximumSpecificationVersionSupported", "CIM\_iSCSIConnection.ActiveiSCSIVersion")
</dt> </dl>

The minimum version number of the iSCSI specification such that this iSCSI instance supports this minimum value, the maximum value indicated by the corresponding property MaximumSpecificationVersionSupported, and all versions in between.

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

[**CIM\_Capabilities**](cim-capabilities.md)
</dt> </dl>

 

 





