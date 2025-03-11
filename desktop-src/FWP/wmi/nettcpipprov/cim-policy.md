---
description: An abstract class defining the common properties of the policy managed elements derived from CIM\_Policy.
ms.assetid: a87d754a-5e32-4f36-aabb-83ffcd113a9d
title: CIM\_Policy class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_Policy
- CIM_Policy.InstanceID
- CIM_Policy.Caption
- CIM_Policy.Description
- CIM_Policy.ElementName
- CIM_Policy.CommonName
- CIM_Policy.PolicyKeywords
api_type: 
- DllExport
api_location: 
- netTCPIP.dll
ROBOTS: INDEX,FOLLOW
---

# CIM\_Policy class

An abstract class defining the common properties of the policy managed elements derived from CIM\_Policy. The subclasses are used to create rules and groups of rules that work together to form a coherent set of policies within an administrative domain or set of domains.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[UMLPackagePath("CIM::Policy"), Abstract, Version("2.6.0"), AMENDMENT]
class CIM_Policy : CIM_ManagedElement
{
  string InstanceID;
  string Caption;
  string Description;
  string ElementName;
  string CommonName;
  string PolicyKeywords[];
};
```

## Members

The **CIM\_Policy** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_Policy** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/win32/wmisdk/standard-qualifiers) (64)
</dt> </dl>

Contains a short textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**CommonName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A user-friendly name of this policy-related object.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides a textual description of the object.

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
</dt> </dl>

Uniquely and opaquely identifies an instance of this class within the scope of the containing Namespace.

> \[!Important\]In order to ensure uniqueness within the Namespace, the value of **InstanceID** should be constructed in the following pattern:
>
> *OrgID*:*LocalID*
>
> *OrgID* must include a copyrighted, trademarked or otherwise unique name that is owned by the business entity defining the **InstanceID**, or be a registered ID that is assigned by a recognized global authority. This is similar to the structure of Schema class names. In addition, to ensure uniqueness the first colon in **InstanceID** must be between the *OrgID* and*LocalID*. Therefor the *OrgID* must not contain a colon (':').
>
> *LocalID* is chosen by the business entity and should not be re-used to identify different underlying real-world elements.
>
> If the preceding pattern is not used, the defining entity must assure that the resultant **InstanceID** is not re-used across any **InstanceID**s produced by this or other providers for this Namespace.
>
> For Distributed Management Task Force (DMTF) defined instances, the pattern must be used with the *OrgID* set to CIM.

 

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**PolicyKeywords**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array of keywords for characterizing / categorizing policy objects. Keywords are of one of two types:

-   Keywords defined in this and other MOFs, or in DMTF white papers. These keywords provide a vendor- independent, installation-independent way of characterizing policy objects.
-   Installation-dependent keywords for characterizing policy objects. Examples include 'Engineering', 'Billing', and 'Review in December 2000'.

This MOF defines the following keywords: **UNKNOWN**, **CONFIGURATION**, **USAGE**, **SECURITY**, **SERVICE**, **MOTIVATIONAL**, **INSTALLATION**, and **EVENT**. These concepts are self-explanatory and are further discussed in the SLA/Policy White Paper. One additional keyword is defined: **POLICY**. The role of this keyword is to identify policy-related instances that may not be otherwise identifiable, in some implementations. The keyword **POLICY** is NOT mutually exclusive of the other keywords specified above.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\standardcimv2<br/>                                                          |
| MOF<br/>                      | <dl> <dt>NetTCPIP.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetTCPIP.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ManagedElement**](cim-managedelement.md)
</dt> </dl>

 

