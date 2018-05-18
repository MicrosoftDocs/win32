---
title: MSFTSM\_WSManCommunicationMechanism class
description: Describes an access mechanism for a MSFTSM\_ObjectManager instance. It describes a protocol and data encoding that can be used for communication.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'cbf3cdef-6301-47d6-a22e-2298675f63c4'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFTSM_WSManCommunicationMechanism class iSCSI Software Target API", "MSFTSM_WSManCommunicationMechanism class iSCSI Software Target API , described"]
topic_type:
- apiref
api_name:
- MSFTSM_WSManCommunicationMechanism
- MSFTSM_WSManCommunicationMechanism.Caption
- MSFTSM_WSManCommunicationMechanism.Description
- MSFTSM_WSManCommunicationMechanism.ElementName
- MSFTSM_WSManCommunicationMechanism.InstallDate
- MSFTSM_WSManCommunicationMechanism.OperationalStatus
- MSFTSM_WSManCommunicationMechanism.StatusDescriptions
- MSFTSM_WSManCommunicationMechanism.Status
- MSFTSM_WSManCommunicationMechanism.HealthState
- MSFTSM_WSManCommunicationMechanism.EnabledState
- MSFTSM_WSManCommunicationMechanism.OtherEnabledState
- MSFTSM_WSManCommunicationMechanism.RequestedState
- MSFTSM_WSManCommunicationMechanism.EnabledDefault
- MSFTSM_WSManCommunicationMechanism.TimeOfLastStateChange
- MSFTSM_WSManCommunicationMechanism.SystemCreationClassName
- MSFTSM_WSManCommunicationMechanism.SystemName
- MSFTSM_WSManCommunicationMechanism.CreationClassName
- MSFTSM_WSManCommunicationMechanism.Name
- MSFTSM_WSManCommunicationMechanism.CommunicationMechanism
- MSFTSM_WSManCommunicationMechanism.OtherCommunicationMechanismDescription
- MSFTSM_WSManCommunicationMechanism.FunctionalProfilesSupported
- MSFTSM_WSManCommunicationMechanism.FunctionalProfileDescriptions
- MSFTSM_WSManCommunicationMechanism.MultipleOperationsSupported
- MSFTSM_WSManCommunicationMechanism.AuthenticationMechanismsSupported
- MSFTSM_WSManCommunicationMechanism.AuthenticationMechanismDescriptions
- MSFTSM_WSManCommunicationMechanism.Version
- MSFTSM_WSManCommunicationMechanism.AdvertiseTypes
- MSFTSM_WSManCommunicationMechanism.AdvertiseTypeDescriptions
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
---

# MSFTSM\_WSManCommunicationMechanism class

Describes an access mechanism for a [**MSFTSM\_ObjectManager**](msftsm-objectmanager.md) instance. It describes a protocol and data encoding that can be used for communication.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Version("1.0.0"), provider("MSiSCSITargetProv")]
class MSFTSM_WSManCommunicationMechanism : CIM_ObjectManagerCommunicationMechanism
{
  string   Caption;
  string   Description;
  string   ElementName;
  datetime InstallDate;
  uint16   OperationalStatus[];
  string   StatusDescriptions[];
  string   Status;
  uint16   HealthState;
  uint16   EnabledState = 5;
  string   OtherEnabledState;
  uint16   RequestedState = 12;
  uint16   EnabledDefault = 2;
  datetime TimeOfLastStateChange;
  string   SystemCreationClassName;
  string   SystemName;
  string   CreationClassName;
  string   Name;
  uint16   CommunicationMechanism;
  string   OtherCommunicationMechanismDescription;
  uint16   FunctionalProfilesSupported[];
  string   FunctionalProfileDescriptions[];
  boolean  MultipleOperationsSupported;
  uint16   AuthenticationMechanismsSupported[];
  string   AuthenticationMechanismDescriptions[];
  string   Version;
  uint16   AdvertiseTypes[];
  string   AdvertiseTypeDescriptions[];
};
```

## Members

The **MSFTSM\_WSManCommunicationMechanism** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFTSM\_WSManCommunicationMechanism** class has these methods.



| Method                                                                              | Description                                                                                                                                                                                              |
|:------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**RequestStateChange**](msftsm-wsmancommunicationmechanism-requeststatechange.md) | Requests that the state of the element be changed to the specified value.<br/> This method is inherited from the [**CIM\_EnabledLogicalElement**](https://msdn.microsoft.com/library/mt446063) class.<br/> |



 

### Properties

The **MSFTSM\_WSManCommunicationMechanism** class has these properties.

<dl> <dt>

**AdvertiseTypeDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_ObjectManagerCommunicationMechanism.AdvertiseTypes")
</dt> </dl>

A free-form string providing additional information related to the AdvertiseType. A description MUST be provided when the AdvertiseType is 1, "Other". An entry in this array corresponds to the entry in the AdvertiseTypes array at the same index. It is not expected that additional descriptions are needed if the Type is set to "Not Advertised" or "SLP". However, as the SLP template expands, or as other advertisement mechanisms are defined, support for additional descriptions may be needed. This array is defined to support this.

This property is inherited from [**CIM\_ObjectManagerCommunicationMechanism**](cim-objectmanagercommunicationmechanism.md).

</dd> <dt>

**AdvertiseTypes**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650), [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_ObjectManagerCommunicationMechanism.AdvertiseTypeDescriptions")
</dt> </dl>

This property signifies the advertisement for this access point. . It is used by the advertising services of the WBEM infrastructure to determine what should be advertised, via what mechanisms. The property is an array so that the communicationMechansim MAY be advertised using several mechanisms. Note: If this property is null/uninitialized, this is equivalent to specifying the value 2, "Not Advertised".

This property is inherited from [**CIM\_ObjectManagerCommunicationMechanism**](cim-objectmanagercommunicationmechanism.md).

<dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Not_Advertised"></span><span id="not_advertised"></span><span id="NOT_ADVERTISED"></span>

**Not Advertised** (2)


</dt> <dd></dd> <dt>

<span id="SLP"></span><span id="slp"></span>

**SLP** (3)


</dt> <dd></dd> </dl>

</dd> <dt>

**AuthenticationMechanismDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_ObjectManagerCommunicationMechanism.AuthenticationMechanismsSupported")
</dt> </dl>

Free-form strings providing descriptions of the supported mechanisms. Entries in this array are correlated with those in the AuthenticationMechanismsSupported array. An entry in this Descriptions array MUST be provided when 1, "Other", is specified in AuthenticationMechanismsSupported.

This property is inherited from [**CIM\_ObjectManagerCommunicationMechanism**](cim-objectmanagercommunicationmechanism.md).

</dd> <dt>

**AuthenticationMechanismsSupported**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650), [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_ObjectManagerCommunicationMechanism.AuthenticationMechanismDescriptions")
</dt> </dl>

Enumerated array describing the types of authentication supported by the ObjectManager, using the encoding/protocol. specified in the property, CommunicationMechanism. The defined values represent the authentication defined in the DMTF document, Specification for CIM Operations over HTTP.

This property is inherited from [**CIM\_ObjectManagerCommunicationMechanism**](cim-objectmanagercommunicationmechanism.md).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

**None** (2)


</dt> <dd></dd> <dt>

<span id="Basic"></span><span id="basic"></span><span id="BASIC"></span>

**Basic** (3)


</dt> <dd></dd> <dt>

<span id="Digest"></span><span id="digest"></span><span id="DIGEST"></span>

**Digest** (4)


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

**CommunicationMechanism**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_ObjectManagerCommunicationMechanism.OtherCommunicationMechanismDescription")
</dt> </dl>

CommunicationMechanism describes an encoding and protocol which can be used to communicate with the server. ObjectManager, the specified string should be indicated. If Other is used, the value for OtherCommunicationMechanismDescription must not be null.

This property is inherited from [**CIM\_ObjectManagerCommunicationMechanism**](cim-objectmanagercommunicationmechanism.md).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="CIM-XML"></span><span id="cim-xml"></span>

**CIM-XML** (2)


</dt> <dd></dd> <dt>

<span id="SM-CLP"></span><span id="sm-clp"></span>

**SM-CLP** (3)


</dt> <dd></dd> <dt>

<span id="WS-Management"></span><span id="ws-management"></span><span id="WS-MANAGEMENT"></span>

**WS-Management** (4)


</dt> <dd></dd> <dt>

<span id="WSDM"></span><span id="wsdm"></span>

**WSDM** (5)


</dt> <dd></dd> </dl>

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

CreationClassName indicates the name of the class or the subclass used in the creation of an instance. When used with the other key properties of this class, this property allows all instances of this class and its subclasses to be uniquely identified.

This property is inherited from [**CIM\_ServiceAccessPoint**](cim-serviceaccesspoint.md).

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

**EnabledDefault**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

An enumerated value indicating an administrator's default or startup configuration for the Enabled State of an element. By default, the element is "Enabled" (value=2).

This property is inherited from [**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).

<dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** (2)


</dt> <dd></dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** (3)


</dt> <dd></dd> <dt>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>

**Not Applicable** (5)


</dt> <dd></dd> <dt>

<span id="Enabled_but_Offline"></span><span id="enabled_but_offline"></span><span id="ENABLED_BUT_OFFLINE"></span>

**Enabled but Offline** (6)


</dt> <dd></dd> <dt>

<span id="No_Default"></span><span id="no_default"></span><span id="NO_DEFAULT"></span>

**No Default** (7)


</dt> <dd></dd> <dt>

<span id="Quiesce"></span><span id="quiesce"></span><span id="QUIESCE"></span>

**Quiesce** (9)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>10–32767</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>32768–65535</dd> </dl>

</dd> <dt>

**EnabledState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_EnabledLogicalElement.OtherEnabledState")
</dt> </dl>

EnabledState is an integer enumeration that indicates the enabled and disabled states of an element. It can also indicate the transitions between these requested states. For example, shutting down (value=4) and starting (value=10) are transient states between enabled and disabled. The following text briefly summarizes the various enabled and disabled states: Enabled (2) indicates that the element is or could be executing commands, will process any queued commands, and queues new requests. Disabled (3) indicates that the element will not execute commands and will drop any new requests. Shutting Down (4) indicates that the element is in the process of going to a Disabled state. Not Applicable (5) indicates the element does not support being enabled or disabled. Enabled but Offline (6) indicates that the element might be completing commands, and will drop any new requests. Test (7) indicates that the element is in a test state. Deferred (8) indicates that the element might be completing commands, but will queue any new requests. Quiesce (9) indicates that the element is enabled but in a restricted mode. Starting (10) indicates that the element is in the process of going to an Enabled state. New requests are queued.

This property is inherited from [**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** (2)


</dt> <dd></dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** (3)


</dt> <dd></dd> <dt>

<span id="Shutting_Down"></span><span id="shutting_down"></span><span id="SHUTTING_DOWN"></span>

**Shutting Down** (4)


</dt> <dd></dd> <dt>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>

**Not Applicable** (5)


</dt> <dd></dd> <dt>

<span id="Enabled_but_Offline"></span><span id="enabled_but_offline"></span><span id="ENABLED_BUT_OFFLINE"></span>

**Enabled but Offline** (6)


</dt> <dd></dd> <dt>

<span id="In_Test"></span><span id="in_test"></span><span id="IN_TEST"></span>

**In Test** (7)


</dt> <dd></dd> <dt>

<span id="Deferred"></span><span id="deferred"></span><span id="DEFERRED"></span>

**Deferred** (8)


</dt> <dd></dd> <dt>

<span id="Quiesce"></span><span id="quiesce"></span><span id="QUIESCE"></span>

**Quiesce** (9)


</dt> <dd></dd> <dt>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>

**Starting** (10)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>11–32767</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>32768–65535</dd> </dl>

</dd> <dt>

**FunctionalProfileDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_ObjectManagerCommunicationMechanism.FunctionalProfilesSupported")
</dt> </dl>

Free-form strings providing descriptions of the supported operations of the object manager. Entries in the array are correlated with those in the ProfilesSupported array. An entry in this Descriptions array MUST be provided when 1, "Other", is specified in the FunctionalProfilesSupported array.

This property is inherited from [**CIM\_ObjectManagerCommunicationMechanism**](cim-objectmanagercommunicationmechanism.md).

</dd> <dt>

**FunctionalProfilesSupported**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650), [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_ObjectManagerCommunicationMechanism.FunctionalProfileDescriptions")
</dt> </dl>

Enumerated array describing the types of operations supported by the ObjectManager, using this encoding/protocol. The enumeration is based on the Functional Profiles defined for conformance in the DMTF document, Specification for CIM Operations over HTTP.

This property is inherited from [**CIM\_ObjectManagerCommunicationMechanism**](cim-objectmanagercommunicationmechanism.md).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Basic_Read"></span><span id="basic_read"></span><span id="BASIC_READ"></span>

**Basic Read** (2)


</dt> <dd></dd> <dt>

<span id="Basic_Write"></span><span id="basic_write"></span><span id="BASIC_WRITE"></span>

**Basic Write** (3)


</dt> <dd></dd> <dt>

<span id="Schema_Manipulation"></span><span id="schema_manipulation"></span><span id="SCHEMA_MANIPULATION"></span>

**Schema Manipulation** (4)


</dt> <dd></dd> <dt>

<span id="Instance_Manipulation"></span><span id="instance_manipulation"></span><span id="INSTANCE_MANIPULATION"></span>

**Instance Manipulation** (5)


</dt> <dd></dd> <dt>

<span id="Association_Traversal"></span><span id="association_traversal"></span><span id="ASSOCIATION_TRAVERSAL"></span>

**Association Traversal** (6)


</dt> <dd></dd> <dt>

<span id="Query_Execution"></span><span id="query_execution"></span><span id="QUERY_EXECUTION"></span>

**Query Execution** (7)


</dt> <dd></dd> <dt>

<span id="Qualifier_Declaration"></span><span id="qualifier_declaration"></span><span id="QUALIFIER_DECLARATION"></span>

**Qualifier Declaration** (8)


</dt> <dd></dd> <dt>

<span id="Indications"></span><span id="indications"></span><span id="INDICATIONS"></span>

**Indications** (9)


</dt> <dd></dd> </dl>

</dd> <dt>

**HealthState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the current health of the element. This attribute expresses the health of this element but not necessarily that of its sub-components.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

The following values have been defined:

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)


</dt> <dd>

The implementation cannot report on **HealthState** at this time.

</dd> <dt>

<span id="OK"></span><span id="ok"></span>

<span id="OK"></span><span id="ok"></span>**OK** (5)


</dt> <dd>

The element is fully functional and is operating within normal operational parameters and without error.

</dd> <dt>

<span id="Degraded_Warning"></span><span id="degraded_warning"></span><span id="DEGRADED_WARNING"></span>

<span id="Degraded_Warning"></span><span id="degraded_warning"></span><span id="DEGRADED_WARNING"></span>**Degraded/Warning** (10)


</dt> <dd>

The element is in working order and all functionality is provided. However, the element is not working to the best of its abilities. For example, the element might not be operating at optimal performance or it might be reporting recoverable errors

</dd> <dt>

<span id="Minor_failure"></span><span id="minor_failure"></span><span id="MINOR_FAILURE"></span>

<span id="Minor_failure"></span><span id="minor_failure"></span><span id="MINOR_FAILURE"></span>**Minor failure** (15)


</dt> <dd>

All functionality is available but some might be degraded.

</dd> <dt>

<span id="Major_failure"></span><span id="major_failure"></span><span id="MAJOR_FAILURE"></span>

<span id="Major_failure"></span><span id="major_failure"></span><span id="MAJOR_FAILURE"></span>**Major failure** (20)


</dt> <dd>

The element is failing. It is possible that some or all of the functionality of this component is degraded or not working.

</dd> <dt>

<span id="Critical_failure"></span><span id="critical_failure"></span><span id="CRITICAL_FAILURE"></span>

<span id="Critical_failure"></span><span id="critical_failure"></span><span id="CRITICAL_FAILURE"></span>**Critical failure** (25)


</dt> <dd>

The element is non-functional and recovery might not be possible.

</dd> <dt>

<span id="Non-recoverable_error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span>

<span id="Non-recoverable_error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span>**Non-recoverable error** (30)


</dt> <dd>

The element has completely failed, and recovery is not possible. All functionality provided by this element has been lost.

</dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved**


</dt> <dd>

DMTF has reserved the unused portion of the continuum for additional HealthStates in the future.

</dd> </dl>

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|ComponentID\|001.5")
</dt> </dl>

Indicates when the object was installed. The lack of a value does not indicate that the object is not installed.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**MultipleOperationsSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

Boolean indicating whether the ObjectManager supports multiple operation requests (TRUE) or only simple requests (FALSE).

This property is inherited from [**CIM\_ObjectManagerCommunicationMechanism**](cim-objectmanagercommunicationmechanism.md).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The Name property uniquely identifies the ServiceAccessPoint and provides an indication of the functionality that is managed. This functionality is described in more detail in the Description property of the object.

This property is inherited from [**CIM\_ServiceAccessPoint**](cim-serviceaccesspoint.md).

</dd> <dt>

**OperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_ManagedSystemElement.StatusDescriptions")
</dt> </dl>

Contains indicators of the current status of the element. The first value of **OperationalStatus** should contain the primary status for the element.

> [!Note]  
> **OperationalStatus** replaces the deprecated **Status** property. Due to the widespread use of the existing **Status** property in management applications, Microsoft strongly recommends that providers or instrumentation provide both the **Status** and **OperationalStatus** properties. When instrumented, **Status** (because it is single-valued) should also provide the primary status of the element.

 

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

The following values have been defined:

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)


</dt> <dd>

Indicates the implementation cannot report on **OperationalStatus** at this time.

</dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)


</dt> <dd>

Indicates an undefined state.

</dd> <dt>

<span id="OK"></span><span id="ok"></span>

<span id="OK"></span><span id="ok"></span>**OK** (2)


</dt> <dd>

Indicates full functionality without errors.

</dd> <dt>

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>**Degraded** (3)


</dt> <dd>

Indicates the element is working and all functionality is provided. However, the element is not working to the best of its abilities. For example, the element might not be operating at optimal performance or it might be reporting recoverable errors

</dd> <dt>

<span id="Stressed"></span><span id="stressed"></span><span id="STRESSED"></span>

<span id="Stressed"></span><span id="stressed"></span><span id="STRESSED"></span>**Stressed** (4)


</dt> <dd>

Indicates that the element is functioning, but needs attention. Overload and overheated are examples of **Stressed** states.

</dd> <dt>

<span id="Predictive_Failure"></span><span id="predictive_failure"></span><span id="PREDICTIVE_FAILURE"></span>

<span id="Predictive_Failure"></span><span id="predictive_failure"></span><span id="PREDICTIVE_FAILURE"></span>**Predictive Failure** (5)


</dt> <dd>

Indicates that an element is functioning nominally but predicting a failure in the near future.

</dd> <dt>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>**Error** (6)


</dt> <dd>

Indicates that an error has occurred.

</dd> <dt>

<span id="Non-Recoverable_Error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span>

<span id="Non-Recoverable_Error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span>**Non-Recoverable Error** (7)


</dt> <dd>

A non-recoverable error has occurred.

</dd> <dt>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>**Starting** (8)


</dt> <dd>

The job is starting.

</dd> <dt>

<span id="Stopping"></span><span id="stopping"></span><span id="STOPPING"></span>

<span id="Stopping"></span><span id="stopping"></span><span id="STOPPING"></span>**Stopping** (9)


</dt> <dd>

The job is stopping.

</dd> <dt>

<span id="Stopped"></span><span id="stopped"></span><span id="STOPPED"></span>

<span id="Stopped"></span><span id="stopped"></span><span id="STOPPED"></span>**Stopped** (10)


</dt> <dd>

The element has been intentionally stopped.

</dd> <dt>

<span id="In_Service"></span><span id="in_service"></span><span id="IN_SERVICE"></span>

<span id="In_Service"></span><span id="in_service"></span><span id="IN_SERVICE"></span>**In Service** (11)


</dt> <dd>

Indicates the element is being configured, maintained, cleaned, or otherwise administered.

</dd> <dt>

<span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span>

<span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span>**No Contact** (12)


</dt> <dd>

Indicates that the monitoring system has knowledge of this element, but has never been able to establish communications with it.

</dd> <dt>

<span id="Lost_Communication"></span><span id="lost_communication"></span><span id="LOST_COMMUNICATION"></span>

<span id="Lost_Communication"></span><span id="lost_communication"></span><span id="LOST_COMMUNICATION"></span>**Lost Communication** (13)


</dt> <dd>

Indicates that the job is known to exist and has been contacted successfully in the past, but is currently unreachable.

</dd> <dt>

<span id="Aborted"></span><span id="aborted"></span><span id="ABORTED"></span>

<span id="Aborted"></span><span id="aborted"></span><span id="ABORTED"></span>**Aborted** (14)


</dt> <dd>

Indicates the job stopped in an unexpected way. The state and configuration of the job might need to be updated.

</dd> <dt>

<span id="Dormant"></span><span id="dormant"></span><span id="DORMANT"></span>

<span id="Dormant"></span><span id="dormant"></span><span id="DORMANT"></span>**Dormant** (15)


</dt> <dd>

Indicates that the job is inactive.

</dd> <dt>

<span id="Supporting_Entity_in_Error"></span><span id="supporting_entity_in_error"></span><span id="SUPPORTING_ENTITY_IN_ERROR"></span>

<span id="Supporting_Entity_in_Error"></span><span id="supporting_entity_in_error"></span><span id="SUPPORTING_ENTITY_IN_ERROR"></span>**Supporting Entity in Error** (16)


</dt> <dd>

Indicates that an element on which this job depends is in error. This element may be **OK** but is unable to function because of the state of a dependent element. An example is a network service or endpoint that cannot function due to lower-layer networking problems.

</dd> <dt>

<span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span>

<span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span>**Completed** (17)


</dt> <dd>

Indicates that the job has completed its operation. This value should be combined with either **OK**, **Error**Error, or **Degraded** so that a client can tell if the complete operation **Completed** with **OK** (passed), Completed with **Error** (failed), or Completed with **Degraded** (the operation finished, but it did not complete OK or did not report an error).

</dd> <dt>

<span id="Power_Mode"></span><span id="power_mode"></span><span id="POWER_MODE"></span>

<span id="Power_Mode"></span><span id="power_mode"></span><span id="POWER_MODE"></span>**Power Mode** (18)


</dt> <dd>

"Power Mode" indicates that the element has additional power model information contained in the associated PowerManagementService association.

</dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved**


</dt> <dd>

DMTF has reserved this portion of the range for additional *OperationalStatus* values in the future.

</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>**Vendor Reserved**


</dt> <dd>

Microsoft has reserved the unused portion of the range for additional *OperationalStatus* values in the future.

</dd> </dl>

</dd> <dt>

**OtherCommunicationMechanismDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_ObjectManagerCommunicationMechanism.CommunicationMechanism")
</dt> </dl>

A free-form string providing a description of the supported protocols when 1, "Other", is specified in the CommunicationMechanism.

This property is inherited from [**CIM\_ObjectManagerCommunicationMechanism**](cim-objectmanagercommunicationmechanism.md).

</dd> <dt>

**OtherEnabledState**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_EnabledLogicalElement.EnabledState")
</dt> </dl>

A string that describes the enabled or disabled state of the element when the EnabledState property is set to 1 ("Other"). This property must be set to null when EnabledState is any value other than 1.

This property is inherited from [**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).

</dd> <dt>

**RequestedState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_EnabledLogicalElement.EnabledState")
</dt> </dl>

RequestedState is an integer enumeration that indicates the last requested or desired state for the element. The actual state of the element is represented by EnabledState. This property is provided to compare the last requested and current enabled or disabled states. Note that when EnabledState is set to 5 ("Not Applicable"), then this property has no meaning. By default, the RequestedState of the element is 5 ("No Change"). Refer to the EnabledState property description for explanations of the values in the RequestedState enumeration. Offline (6) indicates that the element has been requested to transition to the Enabled but Offline EnabledState. It should be noted that there are two new values in RequestedState that build on the statuses of EnabledState. These are "Reboot" (10) and "Reset" (11). Reboot refers to doing a "Shut Down" and then moving to an "Enabled" state. Reset indicates that the element is first "Disabled" and then "Enabled". The distinction between requesting "Shut Down" and "Disabled" should also be noted. Shut Down requests an orderly transition to the Disabled state, and might involve removing power, to completely erase any existing state. The Disabled state requests an immediate disabling of the element, such that it will not execute or accept any commands or processing requests. This property is set as the result of a method invocation (such as Start or StopService on CIM\_Service), or can be overridden and defined as WRITEable in a subclass. The method approach is considered superior to a WRITEable property, because it allows an explicit invocation of the operation and the return of a result code. A particular instance of EnabledLogicalElement might not support RequestedStateChange. If this occurs, the value 12 ("Not Applicable") is used.

This property is inherited from [**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).

<dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** (2)


</dt> <dd></dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** (3)


</dt> <dd></dd> <dt>

<span id="Shut_Down"></span><span id="shut_down"></span><span id="SHUT_DOWN"></span>

**Shut Down** (4)


</dt> <dd></dd> <dt>

<span id="No_Change"></span><span id="no_change"></span><span id="NO_CHANGE"></span>

**No Change** (5)


</dt> <dd></dd> <dt>

<span id="Offline"></span><span id="offline"></span><span id="OFFLINE"></span>

**Offline** (6)


</dt> <dd></dd> <dt>

<span id="Test"></span><span id="test"></span><span id="TEST"></span>

**Test** (7)


</dt> <dd></dd> <dt>

<span id="Deferred"></span><span id="deferred"></span><span id="DEFERRED"></span>

**Deferred** (8)


</dt> <dd></dd> <dt>

<span id="Quiesce"></span><span id="quiesce"></span><span id="QUIESCE"></span>

**Quiesce** (9)


</dt> <dd></dd> <dt>

<span id="Reboot"></span><span id="reboot"></span><span id="REBOOT"></span>

**Reboot** (10)


</dt> <dd></dd> <dt>

<span id="Reset"></span><span id="reset"></span><span id="RESET"></span>

**Reset** (11)


</dt> <dd></dd> <dt>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>

**Not Applicable** (12)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>13–32767</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>32768–65535</dd> </dl>

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("CIM\_ManagedSystemElement.OperationalStatus"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (10)
</dt> </dl>

Contains a string indicating the primary status of the object.

> [!Note]  
> This property is deprecated and replaced by the **OperationalStatus** property. If you choose to use the **Status** property for backward compatibility it should be secondary to the **OperationalStatus** property.

 

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

<dt>



 ("OK")


</dt> <dd></dd> <dt>



 ("Error")


</dt> <dd></dd> <dt>



 ("Degraded")


</dt> <dd></dd> <dt>



 ("Unknown")


</dt> <dd></dd> <dt>



 ("Pred Fail")


</dt> <dd></dd> <dt>



 ("Starting")


</dt> <dd></dd> <dt>



 ("Stopping")


</dt> <dd></dd> <dt>



 ("Service")


</dt> <dd></dd> <dt>



 ("Stressed")


</dt> <dd></dd> <dt>



 ("NonRecover")


</dt> <dd></dd> <dt>



 ("No Contact")


</dt> <dd></dd> <dt>



 ("Lost Comm")


</dt> <dd></dd> <dt>



 ("Stopped")


</dt> <dd></dd> </dl>

</dd> <dt>

**StatusDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_ManagedSystemElement.OperationalStatus")
</dt> </dl>

Contains strings describing the corresponding values in the **OperationalStatus** array. For example, if an element in **OperationalStatus** contains the value **Stopping**, then the element at the same array index in this property may contain an explanation as to why an object is being stopped.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**SystemCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Propagated**](https://msdn.microsoft.com/library/aa393650) ("CIM\_System.CreationClassName"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The CreationClassName of the scoping System.

This property is inherited from [**CIM\_ServiceAccessPoint**](cim-serviceaccesspoint.md).

</dd> <dt>

**SystemName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Propagated**](https://msdn.microsoft.com/library/aa393650) ("CIM\_System.Name"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The Name of the scoping System.

This property is inherited from [**CIM\_ServiceAccessPoint**](cim-serviceaccesspoint.md).

</dd> <dt>

**TimeOfLastStateChange**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The date or time when the EnabledState of the element last changed. If the state of the element has not changed and this property is populated, then it must be set to a 0 interval value. If a state change was requested, but rejected or not yet processed, the property must not be updated.

This property is inherited from [**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).

</dd> <dt>

**Version**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

Provides the protocol version for this service access point. Version information MUST be in the form of M.N, where M is a numeric that describes the Major version and N is a numeric that describes the minor version.

This property is inherited from [**CIM\_ObjectManagerCommunicationMechanism**](cim-objectmanagercommunicationmechanism.md).

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

[**CIM\_ObjectManagerCommunicationMechanism**](cim-objectmanagercommunicationmechanism.md)
</dt> <dt>

[iSCSI Target Server Reference](https://msdn.microsoft.com/library/hh830439)
</dt> </dl>

 

 





