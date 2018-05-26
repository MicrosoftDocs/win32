---
title: CIM\_Identity class
description: An instance of an Identity represents a ManagedElement that acts as a security principal within the scope in which it is defined and authenticated.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: bd38f753-3a1b-4d10-9d2d-a35208a3cffc
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_Identity class iSCSI Software Target API
- CIM_Identity class iSCSI Software Target API , described
topic_type:
- apiref
api_name:
- CIM_Identity
- CIM_Identity.Caption
- CIM_Identity.Description
- CIM_Identity.ElementName
- CIM_Identity.InstanceID
- CIM_Identity.CurrentlyAuthenticated
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_Identity class

An instance of an Identity represents a ManagedElement that acts as a security principal within the scope in which it is defined and authenticated. (Note that the Identity's scope is specified using the association, CIM\_IdentityContext.) ManagedElements with Identities can be OrganizationalEntities, Services, Systems, etc. The ManagedElement 'behind' an Identity is described using the AssignedIdentity association.

Within a given security context, an Identity may be imparted a level of trust, usually based on its credentials. A trust level is defined using the CIM\_SecuritySensitivity class, and associated with Identity using CIM\_ElementSecuritySensitivity. Whether an Identity is currently authenticated is evaluated by checking the CurrentlyAuthenticated boolean property. This property is set and cleared by the security infrastructure, and should only be readable within the management infrastructure. The conditions which must be met/authenticated in order for an Identity's CurrentlyAuthenticated Boolean to be TRUE are defined using a subclass of PolicyCondition - AuthenticationCondition. The inheritance tree for AuthenticationCondition is defined in the CIM Policy Model.

Subclasses of Identity may include specific information related to a given AuthenticationService or authority (such as a security token or computer hardware port/communication details) that more specifically determine the authenticity of the Identity. An instance of Identity may be persisted even though it is not CurrentlyAuthenticated, in order to maintain static relationships to Roles, associations to accounting information, and policy data defining authentication requirements. Note however, when an Identity is not authenticated (CurrentlyAuthenticated = FALSE), then Privileges or rights SHOULD NOT be authorized. The lifetime, validity, and propagation of the Identity is dependent on a security infrastructure's policies.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Version("2.19.0"), UMLPackagePath("CIM::User::Identity")]
class CIM_Identity : CIM_ManagedElement
{
  string  Caption;
  string  Description;
  string  ElementName;
  string  InstanceID;
  boolean CurrentlyAuthenticated = FALSE;
};
```

## Members

The **CIM\_Identity** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_Identity** class has these properties.

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

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("InstanceID")
</dt> </dl>

Within the scope of the instantiating Namespace, InstanceID opaquely and uniquely identifies an instance of this class. In order to ensure uniqueness within the NameSpace, the value of InstanceID SHOULD be constructed using the following 'preferred' algorithm:

&lt;OrgID&gt;:&lt;LocalID&gt;

Where &lt;OrgID&gt; and &lt;LocalID&gt; are separated by a colon ':', and where &lt;OrgID&gt; MUST include a copyrighted, trademarked or otherwise unique name that is owned by the business entity creating/defining the InstanceID, or is a registered ID that is assigned to the business entity by a recognized global authority. (This is similar to the &lt;Schema Name&gt;\_&lt;Class Name&gt; structure of Schema class names.) In addition, to ensure uniqueness &lt;OrgID&gt; MUST NOT contain a colon (':'). When using this algorithm, the first colon to appear in InstanceID MUST appear between &lt;OrgID&gt; and &lt;LocalID&gt;.

&lt;LocalID&gt; is chosen by the business entity and SHOULD not be re-used to identify different underlying (real-world) elements. If the above 'preferred' algorithm is not used, the defining entity MUST assure that the resultant InstanceID is not re-used across any InstanceIDs produced by this or other providers for this instance's NameSpace.

For DMTF defined instances, the 'preferred' algorithm MUST be used with the &lt;OrgID&gt; set to 'CIM'.

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

[**CIM\_ManagedElement**](cim-managedelement.md)
</dt> </dl>

 

 





