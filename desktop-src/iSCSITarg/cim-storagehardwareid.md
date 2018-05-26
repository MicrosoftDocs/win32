---
title: CIM\_StorageHardwareID class
description: CIM\_StorageHardwareID is a hardware ID that serves as an authorization subject. Example are host controller IDs that serve as authorization subjects in disk array LUN Masking.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 66fb046c-d9fa-4486-8f10-510abc9c890f
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_StorageHardwareID class iSCSI Software Target API
- CIM_StorageHardwareID class iSCSI Software Target API , described
topic_type:
- apiref
api_name:
- CIM_StorageHardwareID
- CIM_StorageHardwareID.Caption
- CIM_StorageHardwareID.Description
- CIM_StorageHardwareID.ElementName
- CIM_StorageHardwareID.InstanceID
- CIM_StorageHardwareID.CurrentlyAuthenticated
- CIM_StorageHardwareID.StorageID
- CIM_StorageHardwareID.IDType
- CIM_StorageHardwareID.OtherIDType
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_StorageHardwareID class

CIM\_StorageHardwareID is a hardware ID that serves as an authorization subject. Example are host controller IDs that serve as authorization subjects in disk array LUN Masking.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Version("2.13.0"), UMLPackagePath("CIM::User::StorageHardwareID")]
class CIM_StorageHardwareID : CIM_Identity
{
  string  Caption;
  string  Description;
  string  ElementName;
  string  InstanceID;
  boolean CurrentlyAuthenticated = FALSE;
  string  StorageID;
  uint16  IDType;
  string  OtherIDType;
};
```

## Members

The **CIM\_StorageHardwareID** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_StorageHardwareID** class has these properties.

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

**CurrentlyAuthenticated**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Boolean indicating whether this Identity has been authenticated, and is currently known within the scope of an AuthenticationService or authority. By default, authenticity SHOULD NOT be assumed. This property is set and cleared by the security infrastructure, and should only be readable within the management infrastructure. Note that its value, alone, may not be sufficient to determine authentication/ authorization, in that properties of an Identity subclass (such as a security token or computer hardware port/ communication details) may be required by the security infrastructure.

This property is inherited from [**CIM\_Identity**](cim-identity.md).

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
</dt> </dl>

Contains a user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties, identity data, and description information.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**IDType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StorageHardwareID.StorageID")
</dt> </dl>

The type of the ID property. iSCSI IDs may use one of three iSCSI formats - iqn, eui, or naa. This three letter format is the name prefix; so a single iSCSI type is provided here, the prefix can be used to further refine the format.

<dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="PortWWN"></span><span id="portwwn"></span><span id="PORTWWN"></span>

**PortWWN** (2)


</dt> <dd></dd> <dt>

<span id="NodeWWN"></span><span id="nodewwn"></span><span id="NODEWWN"></span>

**NodeWWN** (3)


</dt> <dd></dd> <dt>

<span id="Hostname"></span><span id="hostname"></span><span id="HOSTNAME"></span>

**Hostname** (4)


</dt> <dd></dd> <dt>

<span id="iSCSI_Name"></span><span id="iscsi_name"></span><span id="ISCSI_NAME"></span>

**iSCSI Name** (5)


</dt> <dd></dd> <dt>

<span id="SwitchWWN"></span><span id="switchwwn"></span><span id="SWITCHWWN"></span>

**SwitchWWN** (6)


</dt> <dd></dd> </dl>

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Within the scope of the instantiating Namespace, InstanceID opaquely and uniquely identifies an instance of this class. In order to ensure uniqueness within the NameSpace, the value of InstanceID SHOULD be constructed using the following 'preferred' algorithm:

&lt;OrgID&gt;:&lt;LocalID&gt;

Where &lt;OrgID&gt; and &lt;LocalID&gt; are separated by a colon ':', and where &lt;OrgID&gt; MUST include a copyrighted, trademarked or otherwise unique name that is owned by the business entity creating/defining the InstanceID, or is a registered ID that is assigned to the business entity by a recognized global authority. (This is similar to the &lt;Schema Name&gt;\_&lt;Class Name&gt; structure of Schema class names.) In addition, to ensure uniqueness &lt;OrgID&gt; MUST NOT contain a colon (':'). When using this algorithm, the first colon to appear in InstanceID MUST appear between &lt;OrgID&gt; and &lt;LocalID&gt;.

&lt;LocalID&gt; is chosen by the business entity and SHOULD not be re-used to identify different underlying (real-world) elements. If the above 'preferred' algorithm is not used, the defining entity MUST assure that the resultant InstanceID is not re-used across any InstanceIDs produced by this or other providers for this instance's NameSpace.

For DMTF defined instances, the 'preferred' algorithm MUST be used with the &lt;OrgID&gt; set to 'CIM'.

This property is inherited from [**CIM\_Identity**](cim-identity.md).

</dd> <dt>

**OtherIDType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The ID type when IDType is "Other".

</dd> <dt>

**StorageID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StorageHardwareID.IDType")
</dt> </dl>

The hardware worldwide unique ID.

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

[**CIM\_Identity**](cim-identity.md)
</dt> </dl>

 

 





