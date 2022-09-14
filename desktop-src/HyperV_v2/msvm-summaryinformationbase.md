---
description: Used in the GetSummaryInformation method in the Msvm\_VirtualSystemManagementService class to quickly retrieve common information related to a virtual system or snapshot.
ms.assetid: f8daa387-d812-4f44-bf5f-e0a0c18c6db8
title: Msvm_SummaryInformationBase class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_SummaryInformationBase
- Msvm_SummaryInformationBase.InstanceID
- Msvm_SummaryInformationBase.CreationTime
- Msvm_SummaryInformationBase.ElementName
- Msvm_SummaryInformationBase.EnabledState
- Msvm_SummaryInformationBase.OtherEnabledState
- Msvm_SummaryInformationBase.HealthState
- Msvm_SummaryInformationBase.Name
- Msvm_SummaryInformationBase.Notes
- Msvm_SummaryInformationBase.Version
- Msvm_SummaryInformationBase.NumberOfProcessors
- Msvm_SummaryInformationBase.OperationalStatus
- Msvm_SummaryInformationBase.StatusDescriptions
- Msvm_SummaryInformationBase.UpTime
- Msvm_SummaryInformationBase.EnhancedSessionModeState
- Msvm_SummaryInformationBase.VirtualSwitchNames
- Msvm_SummaryInformationBase.VirtualSystemSubType
- Msvm_SummaryInformationBase.HostComputerSystemName
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_SummaryInformationBase class

Used in the [**GetSummaryInformation**](getsummaryinformation-msvm-virtualsystemmanagementservice.md) method in the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class to quickly retrieve common information related to a virtual system or snapshot.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_SummaryInformationBase : CIM_View
{
  string   InstanceID;
  DateTime CreationTime;
  string   ElementName;
  uint16   EnabledState;
  string   OtherEnabledState;
  uint16   HealthState;
  string   Name;
  string   Notes;
  string   Version;
  uint16   NumberOfProcessors;
  uint16   OperationalStatus[];
  string   StatusDescriptions[];
  uint64   UpTime;
  uint16   EnhancedSessionModeState;
  string   VirtualSwitchNames[];
  string   VirtualSystemSubType;
  string   HostComputerSystemName;
};
```

## Members

The **Msvm\_SummaryInformationBase** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_SummaryInformationBase** class has these properties.

<dl> <dt>

**CreationTime**
</dt> <dd> <dl> <dt>

Data type: **DateTime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time at which the virtual system or snapshot was created.

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("CIM\_ManagedElement.ElementName")
</dt> </dl>

The friendly name for the virtual system or snapshot.

</dd> <dt>

**EnabledState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The current state of the virtual system or snapshot.

</dd> <dt>

**EnhancedSessionModeState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether or not enhanced mode connections are allowed by the host and if allowed, whether or not they are available to the virtual machine.

<dt>

<span id="Allowed_and_available"></span><span id="allowed_and_available"></span><span id="ALLOWED_AND_AVAILABLE"></span>

**Allowed and available** (2)


</dt> <dd></dd> <dt>

<span id="Not_allowed"></span><span id="not_allowed"></span><span id="NOT_ALLOWED"></span>

**Not allowed** (3)


</dt> <dd></dd> <dt>

<span id="Allowed_but_not_available"></span><span id="allowed_but_not_available"></span><span id="ALLOWED_BUT_NOT_AVAILABLE"></span>

**Allowed but not available** (6)


</dt> <dd></dd> </dl>

</dd> <dt>

**HealthState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The current health state for the virtual system. This property is not valid for instances of [**Msvm\_SummaryInformation**](msvm-summaryinformation.md) representing a virtual system snapshot.

</dd> <dt>

**HostComputerSystemName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the computer hosting this virtual machine.

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("CIM\_ManagedElement.InstanceID"), [**Key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

InstanceID is an optional property that may be used to opaquely and uniquely identify an instance of this class within the scope of the instantiating Namespace. Various subclasses of this class may override this property to make it required, or a key. Such subclasses may also modify the preferred algorithms for ensuring uniqueness that are defined below.

To ensure uniqueness within the NameSpace, the value of InstanceID should be constructed using the following "preferred" algorithm:

&lt;OrgID&gt;:&lt;LocalID&gt;

Where &lt;OrgID&gt; and &lt;LocalID&gt; are separated by a colon (:), and where &lt;OrgID&gt; must include a copyrighted, trademarked, or otherwise unique name that is owned by the business entity that is creating or defining the InstanceID or that is a registered ID assigned to the business entity by a recognized global authority. (This requirement is similar to the \<Schema Name>\\_\<Class Name> structure of Schema class names.) In addition, to ensure uniqueness, &lt;OrgID&gt; must not contain a colon (:). When using this algorithm, the first colon to appear in InstanceID must appear between &lt;OrgID&gt; and &lt;LocalID&gt;.

&lt;LocalID&gt; is chosen by the business entity and should not be reused to identify different underlying (real-world) elements. If not null and the above "preferred" algorithm is not used, the defining entity must assure that the resulting InstanceID is not reused across any InstanceIDs produced by this or other providers for the NameSpace of this instance.

If not set to null for DMTF-defined instances, the "preferred" algorithm must be used with the &lt;OrgID&gt; set to CIM.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The unique name for the virtual system or snapshot.

</dd> <dt>

**Notes**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The notes associated with the virtual system or snapshot.

</dd> <dt>

**NumberOfProcessors**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total number of virtual processors allocated to the virtual system or snapshot.

</dd> <dt>

**OperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](/windows/desktop/WmiSdk/standard-qualifiers) ("Indexed")
</dt> </dl>

The current status of the element.

</dd> <dt>

**OtherEnabledState**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string that describes the enabled or disabled state of the element when the **EnabledState** property is set to 1 ("Other"). This property must be set to null when **EnabledState** is any value other than 1.

</dd> <dt>

**StatusDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](/windows/desktop/WmiSdk/standard-qualifiers) ("Indexed")
</dt> </dl>

Strings that describe the various **OperationalStatus** array values.

</dd> <dt>

**UpTime**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The amount of time since the virtual system was last booted. This property is not valid for instances of [**Msvm\_SummaryInformation**](msvm-summaryinformation.md) representing a virtual system snapshot.

</dd> <dt>

**Version**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The version of the virtual system in a format of "major.minor"; for example, "2.0".

</dd> <dt>

**VirtualSwitchNames**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](/windows/desktop/WmiSdk/standard-qualifiers) ("Indexed")
</dt> </dl>

Strings that list the friendly names of the virtual switches the VM is connected to.

</dd> <dt>

**VirtualSystemSubType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The subtype of the virtual system.

<dt>

<span id="Microsoft_Hyper-V_SubType_1"></span><span id="microsoft_hyper-v_subtype_1"></span><span id="MICROSOFT_HYPER-V_SUBTYPE_1"></span>

**Microsoft:Hyper-V:SubType:1** ("Microsoft:Hyper-V:SubType:1")


</dt> <dd></dd> <dt>

<span id="Microsoft_Hyper-V_SubType_2"></span><span id="microsoft_hyper-v_subtype_2"></span><span id="MICROSOFT_HYPER-V_SUBTYPE_2"></span>

**Microsoft:Hyper-V:SubType:2** ("Microsoft:Hyper-V:SubType:2")


</dt> <dd></dd> </dl>

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1703 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                          |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_View**](cim-view.md)
</dt> </dl>

 

