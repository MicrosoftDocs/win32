---
description: Represents the UDP parameter setting for the Microsoft TCP/IP WMI v2 provider.
ms.assetid: 84f51eec-7acf-4f54-b591-0e09971358ff
title: MSFT\_NetUDPSetting class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetUDPSetting
- MSFT_NetUDPSetting.InstanceID
- MSFT_NetUDPSetting.Caption
- MSFT_NetUDPSetting.Description
- MSFT_NetUDPSetting.ElementName
- MSFT_NetUDPSetting.CommonName
- MSFT_NetUDPSetting.PolicyKeywords
- MSFT_NetUDPSetting.SystemCreationClassName
- MSFT_NetUDPSetting.SystemName
- MSFT_NetUDPSetting.PolicyRuleCreationClassName
- MSFT_NetUDPSetting.PolicyRuleName
- MSFT_NetUDPSetting.CreationClassName
- MSFT_NetUDPSetting.PolicyActionName
- MSFT_NetUDPSetting.DoActionLogging
- MSFT_NetUDPSetting.DynamicPortRangeStartPort
- MSFT_NetUDPSetting.DynamicPortRangeNumberOfPorts
api_type: 
- DllExport
api_location: 
- NetTCPIP.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetUDPSetting class

Represents the UDP parameter setting for the Microsoft TCP/IP WMI v2 provider.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[UMLPackagePath("CIM::Policy"), ClassVersion("1.0.0"), dynamic, provider("nettcpip"), AMENDMENT]
class MSFT_NetUDPSetting : CIM_PolicyAction
{
  string  InstanceID;
  string  Caption;
  string  Description;
  string  ElementName;
  string  CommonName;
  string  PolicyKeywords[];
  string  SystemCreationClassName;
  string  SystemName;
  string  PolicyRuleCreationClassName;
  string  PolicyRuleName;
  string  CreationClassName;
  string  PolicyActionName;
  boolean DoActionLogging;
  uint16  DynamicPortRangeStartPort;
  uint16  DynamicPortRangeNumberOfPorts;
};
```

## Members

The **MSFT\_NetUDPSetting** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetUDPSetting** class has these properties.

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

This property is inherited from [**CIM\_Policy**](cim-policy.md).

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/win32/wmisdk/key-qualifier), [**MaxLen**](/windows/win32/wmisdk/standard-qualifiers) (256)
</dt> </dl>

Indicates the name of the class or the subclass used in the creation of an instance. When used with the other key properties of this class, this property allows all instances of this class and its subclasses to be uniquely identified.

This property is inherited from [**CIM\_PolicyAction**](cim-policyaction.md).

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

**DoActionLogging**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Causes a log message to be generated when the action is performed.

This property is inherited from [**CIM\_PolicyAction**](cim-policyaction.md).

</dd> <dt>

**DynamicPortRangeNumberOfPorts**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The number of ports in the dynamic port range, which starts from the value of **DynamicPortRangeStartPort**.

</dd> <dt>

**DynamicPortRangeStartPort**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The port number for the start of the dynamic port range. The value must be between 1 and 65535.

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

**PolicyActionName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/win32/wmisdk/key-qualifier), [**MaxLen**](/windows/win32/wmisdk/standard-qualifiers) (256)
</dt> </dl>

A user-friendly name of this policy action.

This property is inherited from [**CIM\_PolicyAction**](cim-policyaction.md).

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

This property is inherited from [**CIM\_Policy**](cim-policy.md).

</dd> <dt>

**PolicyRuleCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/win32/wmisdk/key-qualifier), [**MaxLen**](/windows/win32/wmisdk/standard-qualifiers) (256)
</dt> </dl>

For a rule-specific policy action, the **CreationClassName** of the policy rule object with which this Action is associated. For a reusable policy action, a special value, 'NO RULE', should be used to indicate that this Action is reusable and not associated with a single policy rule.

This property is inherited from [**CIM\_PolicyAction**](cim-policyaction.md).

</dd> <dt>

**PolicyRuleName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/win32/wmisdk/key-qualifier), [**MaxLen**](/windows/win32/wmisdk/standard-qualifiers) (256)
</dt> </dl>

For a rule-specific policy action, the name of the policy rule object with which this Action is associated. For a reusable policy action, a special value, 'NO RULE', should be used to indicate that this Action is reusable and not associated with a single policy rule.

This property is inherited from [**CIM\_PolicyAction**](cim-policyaction.md).

</dd> <dt>

**SystemCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/win32/wmisdk/key-qualifier), [**MaxLen**](/windows/win32/wmisdk/standard-qualifiers) (256)
</dt> </dl>

The name of the class or the subclass used in the creation of the System object in whose scope this policy action is defined.

This property helps to identify the System object in whose scope this instance of policy action exists. For a rule-specific policy action, this is the System in whose context the policy rule is defined. For a reusable policy action, this is the instance of PolicyRepository (which is a subclass of System) that holds the Action.

Note that this property, and the analogous property **SystemName**, do not represent propagated keys from an instance of the class System. Instead, they are properties defined in the context of this class, which repeat the values from the instance of System to which this policy action is related, either directly via the policy action InPolicyRepository association or indirectly via the PolicyActionInPolicyRule aggregation.

This property is inherited from [**CIM\_PolicyAction**](cim-policyaction.md).

</dd> <dt>

**SystemName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/win32/wmisdk/key-qualifier), [**MaxLen**](/windows/win32/wmisdk/standard-qualifiers) (256)
</dt> </dl>

The name of the System object in whose scope this policy action is defined.

This property completes the identification of the System object in whose scope this instance of policy action exists. For a rule-specific policy action, this is the System in whose context the policy rule is defined. For a reusable policy action, this is the instance of PolicyRepository (which is a subclass of System) that holds the Action.

This property is inherited from [**CIM\_PolicyAction**](cim-policyaction.md).

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                          |
| MOF<br/>                      | <dl> <dt>NetTCPIP.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetTCPIP.dll</dt> </dl> |



 

