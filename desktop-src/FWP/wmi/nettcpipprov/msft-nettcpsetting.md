---
description: Represents the TCP parameter setting for the Microsoft TCP/IP (Internet Protocol Suite) WMIv2 provider.
ms.assetid: 408e1916-7aee-49c7-84e0-4c675ba2cf8d
title: MSFT\_NetTCPSetting class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetTCPSetting
- MSFT_NetTCPSetting.InstanceID
- MSFT_NetTCPSetting.Caption
- MSFT_NetTCPSetting.Description
- MSFT_NetTCPSetting.ElementName
- MSFT_NetTCPSetting.CommonName
- MSFT_NetTCPSetting.PolicyKeywords
- MSFT_NetTCPSetting.SystemCreationClassName
- MSFT_NetTCPSetting.SystemName
- MSFT_NetTCPSetting.PolicyRuleCreationClassName
- MSFT_NetTCPSetting.PolicyRuleName
- MSFT_NetTCPSetting.CreationClassName
- MSFT_NetTCPSetting.PolicyActionName
- MSFT_NetTCPSetting.DoActionLogging
- MSFT_NetTCPSetting.SettingName
- MSFT_NetTCPSetting.MinRto
- MSFT_NetTCPSetting.InitialCongestionWindow
- MSFT_NetTCPSetting.CwndRestart
- MSFT_NetTCPSetting.MemoryPressureProtection
- MSFT_NetTCPSetting.CongestionProvider
- MSFT_NetTCPSetting.AutoTuningLevelLocal
- MSFT_NetTCPSetting.EcnCapability
- MSFT_NetTCPSetting.Timestamps
- MSFT_NetTCPSetting.InitialRto
- MSFT_NetTCPSetting.ScalingHeuristics
- MSFT_NetTCPSetting.DynamicPortRangeStartPort
- MSFT_NetTCPSetting.DynamicPortRangeNumberOfPorts
- MSFT_NetTCPSetting.AutoTuningLevelGroupPolicy
- MSFT_NetTCPSetting.AutoTuningLevelEffective
- MSFT_NetTCPSetting.DelayedAckTimeout
- MSFT_NetTCPSetting.DelayedAckFrequency
- MSFT_NetTCPSetting.AutomaticUseCustom
- MSFT_NetTCPSetting.NonSackRttResiliency
- MSFT_NetTCPSetting.ForceWS
- MSFT_NetTCPSetting.MaxSynRetransmissions
- MSFT_NetTCPSetting.AutoReusePortRangeStartPort
- MSFT_NetTCPSetting.AutoReusePortRangeNumberOfPorts
api_type: 
- DllExport
api_location: 
- NetTCPIP.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetTCPSetting class

Represents the TCP parameter setting for the Microsoft TCP/IP (Internet Protocol Suite) WMIv2 provider.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[UMLPackagePath("CIM::Policy"), ClassVersion("1.0.0"), dynamic, provider("nettcpip"), AMENDMENT]
class MSFT_NetTCPSetting : CIM_PolicyAction
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
  string  SettingName;
  uint32  MinRto;
  uint32  InitialCongestionWindow;
  uint8   CwndRestart;
  uint8   MemoryPressureProtection;
  uint8   CongestionProvider;
  uint8   AutoTuningLevelLocal;
  uint8   EcnCapability;
  uint8   Timestamps;
  uint32  InitialRto;
  uint8   ScalingHeuristics;
  uint16  DynamicPortRangeStartPort;
  uint16  DynamicPortRangeNumberOfPorts;
  uint8   AutoTuningLevelGroupPolicy;
  uint8   AutoTuningLevelEffective;
  uint32  DelayedAckTimeout;
  uint8   DelayedAckFrequency;
  uint8   AutomaticUseCustom;
  uint8   NonSackRttResiliency;
  uint8   ForceWS;
  uint8   MaxSynRetransmissions;
  uint16  AutoReusePortRangeStartPort;
  uint16  AutoReusePortRangeNumberOfPorts;
};
```

## Members

The **MSFT\_NetTCPSetting** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetTCPSetting** class has these properties.

<dl> <dt>

**AutomaticUseCustom**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets and sets a value that indicates whether the automatic template setting specifies custom or default templates. This property can contain one of the following values.



| Value                                                                                                                                                                                                                           | Meaning                                                                    |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| <span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span><dl> <dt>**Disabled**</dt> <dt>0</dt> </dl> | The automatic template setting specifies the default templates.<br/> |
| <span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span><dl> <dt>**Enabled**</dt> <dt>1</dt> </dl>     | The automatic template setting specifies custom templates.<br/>      |



 

</dd> <dt>

**AutoReusePortRangeNumberOfPorts**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Number of ports starting from the **AutoReusePortRangeStartPort** property for automatic reuse port range.

**Windows 8.1, Windows Server 2012 R2, Windows 8 and Windows Server 2012:  **

This property is not supported before Windows 10 and Windows Server 2016.

</dd> <dt>

**AutoReusePortRangeStartPort**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Starting automatic reuse port number between 1025 and 65535.

**Windows 8.1, Windows Server 2012 R2, Windows 8 and Windows Server 2012:  **

This property is not supported before Windows 10 and Windows Server 2016.

</dd> <dt>

**AutoTuningLevelEffective**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets a value that indicates whether the auto tunning level is determined by group policy or a local setting.



| Value                                                                                                                                                                                                                                       | Meaning                                                             |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| <span id="Local"></span><span id="local"></span><span id="LOCAL"></span><dl> <dt>**Local**</dt> <dt>0</dt> </dl>                         | The auto tunning level is determined by a local setting.<br/> |
| <span id="GroupPolicy"></span><span id="grouppolicy"></span><span id="GROUPPOLICY"></span><dl> <dt>**GroupPolicy**</dt> <dt>1</dt> </dl> | The auto tunning level is determined by group policy.<br/>    |



 

</dd> <dt>

**AutoTuningLevelGroupPolicy**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets and sets the auto tunning level for group policy. This parameter can contain one of the following values.



| Value                                                                                                                                                                                                                                                           | Meaning                                                 |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| <span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span><dl> <dt>**Disabled**</dt> <dt>0</dt> </dl>                                 | The auto tunning level is disabled.<br/>          |
| <span id="HighlyRestricted"></span><span id="highlyrestricted"></span><span id="HIGHLYRESTRICTED"></span><dl> <dt>**HighlyRestricted**</dt> <dt>1</dt> </dl> | The auto tunning level is highly restricted.<br/> |
| <span id="Restricted"></span><span id="restricted"></span><span id="RESTRICTED"></span><dl> <dt>**Restricted**</dt> <dt>2</dt> </dl>                         | The auto tunning level is restricted.<br/>        |
| <span id="Normal"></span><span id="normal"></span><span id="NORMAL"></span><dl> <dt>**Normal**</dt> <dt>3</dt> </dl>                                         | The auto tunning level is normal.<br/>            |
| <span id="Experimental"></span><span id="experimental"></span><span id="EXPERIMENTAL"></span><dl> <dt>**Experimental**</dt> <dt>4</dt> </dl>                 | The auto tunning level is experimental.<br/>      |



 

</dd> <dt>

**AutoTuningLevelLocal**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets and sets the local auto tuning level. This property contains one of the following values.



| Value                                                                                                                                                                                                                                                           | Meaning                      |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------|
| <span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span><dl> <dt>**Disabled**</dt> <dt>0</dt> </dl>                                 |                              |
| <span id="HighlyRestricted"></span><span id="highlyrestricted"></span><span id="HIGHLYRESTRICTED"></span><dl> <dt>**HighlyRestricted**</dt> <dt>1</dt> </dl> | Highly Restricted<br/> |
| <span id="Restricted"></span><span id="restricted"></span><span id="RESTRICTED"></span><dl> <dt>**Restricted**</dt> <dt>2</dt> </dl>                         |                              |
| <span id="Normal"></span><span id="normal"></span><span id="NORMAL"></span><dl> <dt>**Normal**</dt> <dt>3</dt> </dl>                                         |                              |
| <span id="Experimental"></span><span id="experimental"></span><span id="EXPERIMENTAL"></span><dl> <dt>**Experimental**</dt> <dt>4</dt> </dl>                 |                              |



 

</dd> <dt>

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

**CongestionProvider**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets and sets the TCP congestion provider setting. This property contains one of the following values.



| Value                                                                                                                                                                                                                       | Meaning                           |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| <span id="Default"></span><span id="default"></span><span id="DEFAULT"></span><dl> <dt>**Default**</dt> <dt>0</dt> </dl> |                                   |
| <span id="CTCP"></span><span id="ctcp"></span><dl> <dt>**CTCP**</dt> <dt>2</dt> </dl>                                    | Compound TCP (CTCP)<br/>    |
| <span id="DCTCP"></span><span id="dctcp"></span><dl> <dt>**DCTCP**</dt> <dt>3</dt> </dl>                                 | Datacenter TCP (DCTCP)<br/> |



 

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

**CwndRestart**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets and sets a value that indicates whether a congested window is restarted. This property contains one of the following values.



| Value                                                                                                                                                                                                                           | Meaning                                         |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| <span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span><dl> <dt>**Disabled**</dt> <dt>0</dt> </dl> | A congested window is not restarted.<br/> |
| <span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span><dl> <dt>**Enabled**</dt> <dt>1</dt> </dl>     | A congested window is restarted.<br/>     |



 

</dd> <dt>

**DelayedAckFrequency**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets and sets number of unresolved acknowledgments (ACK) that will cause the ACK timer to be ignored. This parameter value can range from 1 to 255.

</dd> <dt>

**DelayedAckTimeout**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets and sets the TCP delayed ACK timeout, in milliseconds. This property can contain a value from 10 to 600.

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

Gets and sets the number of ports in the dynamic port range.

</dd> <dt>

**DynamicPortRangeStartPort**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets and sets the starting port of the dynamic port range. The property can contain a value between 1 and 65535.

</dd> <dt>

**EcnCapability**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets and sets the Explicit Congestion Notification (ECN) feature. This property contains one of the following values.



| Value                                                                                                                                                                                                                           | Meaning                     |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|
| <span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span><dl> <dt>**Disabled**</dt> <dt>0</dt> </dl> | ECN is disabled.<br/> |
| <span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span><dl> <dt>**Enabled**</dt> <dt>1</dt> </dl>     | ECN is enabled.<br/>  |



 

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

**ForceWS**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets and sets a value indicates whether forced window scaling is enabled.

**Windows 8 and Windows Server 2012:** This property is not supported before Windows 8.1 and Windows Server 2012 R2.



| Value                                                                                                                                                                                                                           | Meaning                                       |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| <span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span><dl> <dt>**Disabled**</dt> <dt>0</dt> </dl> | Forced window scaling is disabled.<br/> |
| <span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span><dl> <dt>**Enabled**</dt> <dt>1</dt> </dl>     | Forced window scaling is enabled.<br/>  |



 

</dd> <dt>

**InitialCongestionWindow**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets and sets the maximum segment size of the initial congestion window. The property value can range from 2 to 64.

</dd> <dt>

**InitialRto**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets and sets the retransmit timeout, in milliseconds. The default value for this property is 3000.

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

**MaxSynRetransmissions**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets and sets the number of times to attempt to reestablish a connection with SYN packetes. This property can contain a value that ranges from 2 to 8.

**Windows 8 and Windows Server 2012:** This property is not supported before Windows 8.1 and Windows Server 2012 R2.

</dd> <dt>

**MemoryPressureProtection**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets and sets the memory pressure protection setting. This property contains one of the following values.



| Value                                                                                                                                                                                                                           | Meaning                                                                        |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| <span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span><dl> <dt>**Disabled**</dt> <dt>0</dt> </dl> | Disable memory pressure protection.<br/>                                 |
| <span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span><dl> <dt>**Enabled**</dt> <dt>1</dt> </dl>     | Enable memory pressure protection.<br/>                                  |
| <span id="Default"></span><span id="default"></span><span id="DEFAULT"></span><dl> <dt>**Default**</dt> <dt>2</dt> </dl>     | Restore the memory pressure protection state to the system default.<br/> |



 

</dd> <dt>

**MinRto**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets and sets the TCP retransmission timeout, in milliseconds. The property value can range from 20 milliseconds to 300 milliseconds.

</dd> <dt>

**NonSackRttResiliency**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets and sets a value that enables Round-Trip Time (RTT) resiliency for clients that do not support Selective Acknowledgment (SACK).

**Windows 8 and Windows Server 2012:** This property is not supported before Windows 8.1 and Windows Server 2012 R2.



| Value                                                                                                                                                                                                                           | Meaning                                                                 |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| <span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span><dl> <dt>**Disabled**</dt> <dt>0</dt> </dl> | Disable RTT resiliency for clients that do not support SACK.<br/> |
| <span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span><dl> <dt>**Enabled**</dt> <dt>1</dt> </dl>     | Enable RTT resiliency for clients that do not support SACK.<br/>  |



 

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

**ScalingHeuristics**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets and sets a value that indicates whether window scaling heuristics are enabled.



| Value                                                                                                                                                                                                                           | Meaning                                           |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| <span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span><dl> <dt>**Disabled**</dt> <dt>0</dt> </dl> | Window scaling heuristics is disabled.<br/> |
| <span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span><dl> <dt>**Enabled**</dt> <dt>1</dt> </dl>     | Window scaling heuristics is enabled.<br/>  |



 

</dd> <dt>

**SettingName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the name of the setting. This property contains one of the following values.

-   DatacenterCustom
-   InternetCustom
-   Datacenter
-   Compat
-   Internet
-   Automatic

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

</dd> <dt>

**Timestamps**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets and sets the RFC timestamp setting. This property contains one of the following values.



| Value                                                                                                                                                                                                                           | Meaning                                 |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| <span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span><dl> <dt>**Disabled**</dt> <dt>0</dt> </dl> | Disable RFC 1323 timestamps.<br/> |
| <span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span><dl> <dt>**Enabled**</dt> <dt>1</dt> </dl>     | Enable RFC 1323 timestamps.<br/>  |



 

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                          |
| MOF<br/>                      | <dl> <dt>NetTCPIP.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetTCPIP.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_PolicyAction**](cim-policyaction.md)
</dt> <dt>

[NetTCPIP Provider Classes](net-tcpip-classes.md)
</dt> </dl>

 

