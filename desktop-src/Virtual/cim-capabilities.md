---
title: CIM\_Capabilities class
description: An abstract class for subclasses that describes the abilities of an associated managed element, and the potential of the abilities.
ms.assetid: '3e4ae38d-651b-4f0e-bcd0-1bfd70b416b8'
keywords: ["CIM_Capabilities class Hyper-V", "CIM_Capabilities class Hyper-V , described"]
topic_type:
- apiref
api_name:
- CIM_Capabilities
- CIM_Capabilities.Caption
- CIM_Capabilities.Description
- CIM_Capabilities.InstanceID
- CIM_Capabilities.ElementName
api_location:
- Root\virtualization
api_type:
- Schema
---

# CIM\_Capabilities class

An abstract class for subclasses that describes the abilities of an associated managed element, and the potential of the abilities. For example, a capability can describe the maximum number of VLANs that can be supported on a system using a subclass of **CIM\_Capabilities**.

Capabilities are tied to the elements which they describe using a [**CIM\_ElementCapabilities**](cim-elementcapabilities.md) class association. A **CIM\_Capabilities** object must be associated with a [**CIM\_ManagedElement**](cim-managedelement.md) object, however, the **CIM\_Capabilities** object cannot be associated with more than one manage element. This class does not indicate what is configured or operational. Instead, it indicates what can and cannot exist, be defined, or be used. It is possible to describe both supported and excluded abilities and functions (capabilities and limitations) using this class.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract, Version("2.11.0"), AMENDMENT]
class CIM_Capabilities : CIM_ManagedElement
{
  string Caption;
  string Description;
  string InstanceID;
  string ElementName;
};
```

## Members

The **CIM\_Capabilities** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **CIM\_Capabilities** class has these methods.



| Method                                                            | Description                                                                                                                |
|:------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------|
| [**CreateGoalSettings**](cim-capabilities-creategoalsettings.md) | Creates a set of supported SettingData elements, from two sets of SettingData elements, provided by the caller.<br/> |



 

### Properties

The **CIM\_Capabilities** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

A short textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650), [**Override**](https://msdn.microsoft.com/library/aa393650) ("ElementName")
</dt> </dl>

The user friendly name for this class instance. In addition, the user friendly name can be used as a index property for a query. This value does not have to be unique within its namespace.

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Uniquely and opaquely identifies an instance of this class within the scope of the containing namespace.

> \[!Important\]
>
> In order to ensure uniqueness within the namespace, the value of the **InstanceID** property should be constructed in the following pattern: *OrgID*:*LocalID*
>
> *OrgID* must include a copyrighted, trademarked or otherwise unique name that is owned by the business entity that defines the **InstanceID**, or be a registered ID that is assigned by a recognized global authority. This pattern is similar to the structure of schema class names. In addition, to ensure uniqueness, the first colon in **InstanceID** must be between the *OrgID* and*LocalID*. Therefore the *OrgID* must not contain a colon (':').
>
> *LocalID* is chosen by the business entity and should not be re-used to identify different underlying real-world elements.
>
> If the above pattern is not used, the defining entity must assure that the resultant **InstanceID** value is not re-used across any **InstanceID** properties that are produced by this provider or other providers for this namespace.
>
> For Distributed Management Task Force (DMTF) defined instances, the pattern must be used with the *OrgID* set to CIM.

 

</dd> </dl>

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012 R2<br/>                                                                    |
| Namespace<br/>                | Root\\virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ManagedElement**](cim-managedelement.md)
</dt> </dl>

 

 





