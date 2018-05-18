---
title: MSISCSITARGET\_iSCSIConfigurationCapabilities class
description: Defines the capabilities of a CIM\_iSCSIConfigurationService.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '15472831-255c-4a48-8cad-26a3d716e8e5'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSISCSITARGET_iSCSIConfigurationCapabilities class iSCSI Software Target API", "MSISCSITARGET_iSCSIConfigurationCapabilities class iSCSI Software Target API , described"]
topic_type:
- apiref
api_name:
- MSISCSITARGET_iSCSIConfigurationCapabilities
- MSISCSITARGET_iSCSIConfigurationCapabilities.Caption
- MSISCSITARGET_iSCSIConfigurationCapabilities.Description
- MSISCSITARGET_iSCSIConfigurationCapabilities.InstanceID
- MSISCSITARGET_iSCSIConfigurationCapabilities.ElementName
- MSISCSITARGET_iSCSIConfigurationCapabilities.iSCSIProtocolEndpointCreationSupported
- MSISCSITARGET_iSCSIConfigurationCapabilities.IdentifierSelectionSupported
- MSISCSITARGET_iSCSIConfigurationCapabilities.iSCSINodeCreationSupported
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
---

# MSISCSITARGET\_iSCSIConfigurationCapabilities class

Defines the capabilities of a **CIM\_iSCSIConfigurationService**.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Static, Experimental, Version("1.0.0")]
class MSISCSITARGET_iSCSIConfigurationCapabilities : CIM_iSCSIConfigurationCapabilities
{
  string  Caption;
  string  Description;
  string  InstanceID;
  string  ElementName;
  boolean iSCSIProtocolEndpointCreationSupported = FALSE;
  boolean IdentifierSelectionSupported = FALSE;
  boolean iSCSINodeCreationSupported = FALSE;
};
```

## Members

The **MSISCSITARGET\_iSCSIConfigurationCapabilities** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSISCSITARGET\_iSCSIConfigurationCapabilities** class has these properties.

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

**IdentifierSelectionSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If false, the implementation chooses the Identifier for the iSCSIProtocolEndpoint and the Identifier cannot be supplied as a parameter to CreateiSCSIProtocolEndpoint and MUST be NULL.

This property is inherited from [**CIM\_iSCSIConfigurationCapabilities**](cim-iscsiconfigurationcapabilities.md).

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

**iSCSINodeCreationSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

iSCSI Nodes are modeled by instances of SCSIProtocolController. If true, this property indicates that iSCSI Nodes may be dynamically created and deleted in a NetworkEntity. If false, iSCSI Nodes are pre-existing and statically defined within the Entity.

This property is inherited from [**CIM\_iSCSIConfigurationCapabilities**](cim-iscsiconfigurationcapabilities.md).

</dd> <dt>

**iSCSIProtocolEndpointCreationSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

iSCSI Ports are modeled by instances of iSCSIProtocolEndpoints. If true, this property indicates that iSCSIProtocolEndpoints may be dynamically created and deleted in a Node. If false, iSCSIProtocolEndpoints are preexisting and statically defined within the Node.

This property is inherited from [**CIM\_iSCSIConfigurationCapabilities**](cim-iscsiconfigurationcapabilities.md).

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

[**CIM\_iSCSIConfigurationCapabilities**](cim-iscsiconfigurationcapabilities.md)
</dt> <dt>

[iSCSI Target Server Reference](https://msdn.microsoft.com/library/hh830439)
</dt> <dt>

[**CIM\_Capabilities**](cim-capabilities.md)
</dt> <dt>

[**CIM\_ComputerSystem**](https://msdn.microsoft.com/library/aa387219)
</dt> <dt>

[**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871)
</dt> <dt>

[**CIM\_SCSIProtocolController**](https://msdn.microsoft.com/library/cc136905)
</dt> </dl>

 

 





