---
title: Msvm\_FailoverIndication class
description: Represents information about a failover.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '10aebfc6-4c17-4940-96d0-3b3ab1305205'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Msvm_FailoverIndication class", "Msvm_FailoverIndication class, described"]
topic_type:
- apiref
api_name:
- Msvm_FailoverIndication
- Msvm_FailoverIndication.SECURITY_DESCRIPTOR
- Msvm_FailoverIndication.TIME_CREATED
- Msvm_FailoverIndication.IndicationIdentifier
- Msvm_FailoverIndication.CorrelatedIndications
- Msvm_FailoverIndication.IndicationTime
- Msvm_FailoverIndication.OtherSeverity
- Msvm_FailoverIndication.IndicationFilterName
- Msvm_FailoverIndication.SequenceContext
- Msvm_FailoverIndication.SequenceNumber
- Msvm_FailoverIndication.HostedElement
- Msvm_FailoverIndication.HostedElementFormat
- Msvm_FailoverIndication.OtherHostedElementFormat
- Msvm_FailoverIndication.HostingSystem
- Msvm_FailoverIndication.HostingSystemFormat
- Msvm_FailoverIndication.OtherHostingSystemFormat
- Msvm_FailoverIndication.PreviousHostingSystem
- Msvm_FailoverIndication.PreviousHostingSystemFormat
- Msvm_FailoverIndication.OtherPreviousHostingSystemFormat
- Msvm_FailoverIndication.FailoverType
- Msvm_FailoverIndication.OtherFailoverType
- Msvm_FailoverIndication.PerceivedSeverity
- Msvm_FailoverIndication.OtherPerceivedSeverity
api_location:
- VMMS.exe
api_type:
- DllExport
---

# Msvm\_FailoverIndication class

Represents information about a failover.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Indication, AMENDMENT]
class Msvm_FailoverIndication : CIM_ProcessIndication
{
  uint8    SECURITY_DESCRIPTOR[];
  uint64   TIME_CREATED;
  string   IndicationIdentifier;
  string   CorrelatedIndications[];
  datetime IndicationTime;
  string   OtherSeverity;
  string   IndicationFilterName;
  string   SequenceContext;
  sint64   SequenceNumber;
  string   HostedElement;
  uint16   HostedElementFormat;
  string   OtherHostedElementFormat;
  string   HostingSystem;
  uint16   HostingSystemFormat;
  string   OtherHostingSystemFormat;
  string   PreviousHostingSystem;
  uint16   PreviousHostingSystemFormat;
  string   OtherPreviousHostingSystemFormat;
  uint16   FailoverType;
  string   OtherFailoverType;
  uint16   PerceivedSeverity;
  string   OtherPerceivedSeverity;
};
```

## Members

The **Msvm\_FailoverIndication** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_FailoverIndication** class has these properties.

<dl> <dt>

**CorrelatedIndications**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("Recommendation.ITU\|X733.Correlated notifications"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_Indication**](cim-indication.md).**IndicationIdentifier**")
</dt> </dl>

A array that contains **IndicationIdentifier** values of notifications that are related this one.

This property is inherited from [**CIM\_Indication**](cim-indication.md).

</dd> <dt>

**FailoverType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The type of failover.

The possible values are:

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)


</dt> <dd>

The failover type is unknown.

</dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)


</dt> <dd>

The type is defined by the **OtherFailoverType** property.

</dd> <dt>

<span id="Unplanned"></span><span id="unplanned"></span><span id="UNPLANNED"></span>

<span id="Unplanned"></span><span id="unplanned"></span><span id="UNPLANNED"></span>**Unplanned** (2)


</dt> <dd>

The failover resulted from the failure of the element referenced by the **PreviousHostingSystem** property.

</dd> </dl>

</dd> <dt>

**HostedElement**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("**Msvm\_FailoverIndication**.**HostedElementFormat**")
</dt> </dl>

The identifying information of the instance that has failed over from one hosting system to another. This property contains the path of the instance, encoded as a string if the instance is modeled in the CIM Schema. If the instance is not a CIM instance, this property contains the name of the entity. The path or name is formatted according the **HostedElementFormat** property.

</dd> <dt>

**HostedElementFormat**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("**Msvm\_FailoverIndication**.**HostedElement**", "**Msvm\_FailoverIndication**.**OtherHostedElementFormat**")
</dt> </dl>

The format of the **HostedElement** property.

The possible values are:

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)


</dt> <dd>

The format is unknown.

</dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)


</dt> <dd>

The format is defined by the **OtherHostedElementFormat** property.

</dd> <dt>

<span id="CIMObjectPath"></span><span id="cimobjectpath"></span><span id="CIMOBJECTPATH"></span>

<span id="CIMObjectPath"></span><span id="cimobjectpath"></span><span id="CIMOBJECTPATH"></span>**CIMObjectPath** (2)


</dt> <dd>

This format is *&lt;ClassName&gt;*.*&lt;Prop1&gt;*="*&lt;Value1&gt;*",*&lt;Prop2&gt;*="*&lt;Value2&gt;*",*...*.

</dd> </dl>

</dd> <dt>

**HostingSystem**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("**Msvm\_FailoverIndication**.**HostingSystemFormat**")
</dt> </dl>

The identifying information of the instance that hosts the element referenced by **HostedElement**. This property contains the path of the instance, encoded as a string if the instance is modeled in the CIM Schema. If the instance is not a CIM instance, this property contains the name of the entity. The path or name is formatted according the **HostingSystemFormat** property.

</dd> <dt>

**HostingSystemFormat**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("**Msvm\_FailoverIndication**.**HostingSystem**", "**Msvm\_FailoverIndication**.**OtherHostingSystemFormat**")
</dt> </dl>

The format of the **PreviousHostingSystem** property.

The possible values are:

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)


</dt> <dd>

The format is unknown.

</dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)


</dt> <dd>

The format is defined by the **OtherHostingSystemFormat** property.

</dd> <dt>

<span id="CIMObjectPath"></span><span id="cimobjectpath"></span><span id="CIMOBJECTPATH"></span>

<span id="CIMObjectPath"></span><span id="cimobjectpath"></span><span id="CIMOBJECTPATH"></span>**CIMObjectPath** (2)


</dt> <dd>

This format is *&lt;ClassName&gt;*.*&lt;Prop1&gt;*="*&lt;Value1&gt;*",*&lt;Prop2&gt;*="*&lt;Value2&gt;*",*...*.

</dd> </dl>

</dd> <dt>

**IndicationFilterName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_IndicationFilter.Name")
</dt> </dl>

The identifier of the indication filter that processes the indication. The sending service sets this property. This property correlates with the **Name** property of the **CIM\_IndicationFilter** object. The value of **IndicationFilterName** should use the following format:

-   *&lt;OrgID&gt;*:*&lt;LocalID&gt;*
-   *&lt;OrgID&gt;* must include a copyrighted, trademarked, or unique name that is owned by the business entity that owns the object.
-   *&lt;OrgID&gt;* must not contain a colon (:)
-   *&lt;LocalID&gt;* a unique identifier chosen by the business entity that owns the object.

This property is inherited from [**CIM\_Indication**](cim-indication.md).

</dd> <dt>

**IndicationIdentifier**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("Recommendation.ITU\|X733.Notification identifier")
</dt> </dl>

An identifier of the indication. This property can be used as a key value in the **CorrelatedIndications** property array. Therefore, **IndicationIdentifier** should be a unique value within the namespace of this class instance.

To ensure that **IndicationIdentifier** is unique, it should use the following format:

-   *&lt;OrgID&gt;*:*&lt;LocalID&gt;*
-   *&lt;OrgID&gt;* must include a copyrighted, trademarked, or unique name that is owned by the business entity that owns the object.
-   *&lt;OrgID&gt;* must not contain a colon (:)
-   *&lt;LocalID&gt;* a unique identifier chosen by the business entity that owns the object.
-   For DMTF-defined instances, *&lt;OrgID&gt;* should be set to "CIM".

This property is inherited from [**CIM\_Indication**](cim-indication.md).

</dd> <dt>

**IndicationTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time and date when the indication was created. The property can be set to **NULL** if the entity that created the indication is not capable of determining this information.

> [!Note]  
> The **IndicationTime** value can be the same for indications that are generated in rapid succession.

 

This property is inherited from [**CIM\_Indication**](cim-indication.md).

</dd> <dt>

**OtherFailoverType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("**Msvm\_FailoverIndication**.**PreviousHostingSystemFormat**")
</dt> </dl>

A description of the value for the **FailoverType** property when it is set to "1" (other). For other values of **FailoverType**, **OtherFailoverType** must be set to **NULL**.

</dd> <dt>

**OtherHostedElementFormat**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("**Msvm\_FailoverIndication**.**HostedElementFormat**")
</dt> </dl>

A description of the value for the **HostedElementFormat** property when it is set to "1" (other). For other values of **HostedElementFormat**, **OtherHostedElementFormat** must be set to **NULL**.

</dd> <dt>

**OtherHostingSystemFormat**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("**Msvm\_FailoverIndication**.**HostingSystemFormat**")
</dt> </dl>

A description of the value for the **HostingSystemFormat** property when it is set to "1" (other). For other values of **HostingSystemFormat**, **OtherHostingSystemFormat** must be set to **NULL**.

</dd> <dt>

**OtherPerceivedSeverity**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("**Msvm\_FailoverIndication**.**PerceivedSeverity**")
</dt> </dl>

A description of the value for the **PerceivedSeverity** property when it is set to "1" (other). For other values of **PerceivedSeverity**, **OtherPerceivedSeverity** must be set to **NULL**.

</dd> <dt>

**OtherPreviousHostingSystemFormat**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("**Msvm\_FailoverIndication**.**PreviousHostingSystemFormat**")
</dt> </dl>

A description of the value for the **PreviousHostingSystemFormat** property when it is set to "1" (other). For other values of **PreviousHostingSystemFormat**, **OtherPreviousHostingSystemFormat** must be set to **NULL**.

</dd> <dt>

**OtherSeverity**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_AlertIndication**](cim-alertindication.md).**PerceivedSeverity**")
</dt> </dl>

The severity of the indication from the notifier's point of view when **PerceivedSeverity** is set to "1" (Other).

This property is inherited from [**CIM\_Indication**](cim-indication.md).

</dd> <dt>

**PerceivedSeverity**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650), [**Override**](https://msdn.microsoft.com/library/aa393650) ("PerceivedSeverity")
</dt> </dl>

The severity of the failover indication from the notifier's point of view.

The possible values are:

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Information"></span><span id="information"></span><span id="INFORMATION"></span>

**Information** (2)


</dt> <dd></dd> <dt>

<span id="Degraded_Warning"></span><span id="degraded_warning"></span><span id="DEGRADED_WARNING"></span>

**Degraded/Warning** (3)


</dt> <dd></dd> <dt>

<span id="Minor"></span><span id="minor"></span><span id="MINOR"></span>

**Minor** (4)


</dt> <dd></dd> <dt>

<span id="Major"></span><span id="major"></span><span id="MAJOR"></span>

**Major** (5)


</dt> <dd></dd> <dt>

<span id="Critical"></span><span id="critical"></span><span id="CRITICAL"></span>

**Critical** (6)


</dt> <dd></dd> <dt>

<span id="Fatal_NonRecoverable"></span><span id="fatal_nonrecoverable"></span><span id="FATAL_NONRECOVERABLE"></span>

**Fatal/NonRecoverable** (7)


</dt> <dd></dd> </dl>

</dd> <dt>

**PreviousHostingSystem**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("**Msvm\_FailoverIndication**.**HostingSystemFormat**")
</dt> </dl>

The identifying information of the instance that hosts the element referenced by **HostedElement**. This property contains the path of the instance, encoded as a string if the instance is modeled in the CIM Schema. If the instance is not a CIM instance, this property contains the name of the entity. The path or name is formatted according the **PreviousHostingSystemFormat** property.

</dd> <dt>

**PreviousHostingSystemFormat**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("**Msvm\_FailoverIndication**.**PreviousHostingSystem**", "**Msvm\_FailoverIndication**.**OtherPreviousHostingSystemFormat**")
</dt> </dl>

The format of the **PreviousHostingSystem** property.

The possible values are:

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)


</dt> <dd>

The format is unknown.

</dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)


</dt> <dd>

The format is defined by the **OtherPreviousHostingSystemFormat** property.

</dd> <dt>

<span id="CIMObjectPath"></span><span id="cimobjectpath"></span><span id="CIMOBJECTPATH"></span>

<span id="CIMObjectPath"></span><span id="cimobjectpath"></span><span id="CIMOBJECTPATH"></span>**CIMObjectPath** (2)


</dt> <dd>

This format is *&lt;ClassName&gt;*.*&lt;Prop1&gt;*="*&lt;Value1&gt;*",*&lt;Prop2&gt;*="*&lt;Value2&gt;*",*...*.

</dd> </dl>

</dd> <dt>

**SECURITY\_DESCRIPTOR**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Descriptor used by the event provider to determine which users can receive the event. This property is inherited from [**\_\_Event**](https://msdn.microsoft.com/library/aa394634). For more information about constants used to set this security descriptor, see [WMI Security Constants](https://msdn.microsoft.com/library/aa394576).

</dd> <dt>

**SequenceContext**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_Indication**](cim-indication.md).**SequenceNumber**")
</dt> </dl>

The sequence context of the sequence identifier for the indication. If a service does not support sequence identifiers for indications, this property should be set to **NULL**. If the indication is redelivered, this property remains the same.

> [!Note]  
> The sequence identifier for the indication enables a listener to identify duplicate indications when the service attempts to redeliver indications, reorder indications that arrive out of order, and detect lost indications.

 

To ensure that **SequenceContext** is unique, it should use the following format:

-   *indication-service-name*\#*cim-service-start-id* \#*listener-destination-creation-time*
-   *indication-service-name* is the value of the **Name** property of the **CIM\_IndicationService** instance that delivers the indication.
-   *cim-service-start-id* is an identifier that uniquely identifies the start operation of a service. For example, this could be a timestamp of the start time, or a counter that increases for each start or restart of the service.
-   *listener-destination-creation-time* is a timestamp of the creation time of the **CIM\_ListenerDestination** instance representing the listener destination.nSince this format is only a recommendation, CIM clients shall treat the value as an opaque identifier for the sequence context and shall not rely on this format.

This property is inherited from [**CIM\_Indication**](cim-indication.md).

</dd> <dt>

**SequenceNumber**
</dt> <dd> <dl> <dt>

Data type: **sint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_Indication**](cim-indication.md).**SequenceContext**")
</dt> </dl>

The sequence number of the sequence identifier for the indication.

> [!Note]  
> The sequence identifier for the indication enables a listener to identify duplicate indications when the service attempts to redeliver indications, reorder indications that arrive out of order, and detect lost indications.

 

The sequence number has the following characteristics:

-   The sequence number is reset to "0" whenever the **SequenceContext** value changes.
-   Whenever the listener destination receives a new indication, the sequence number is increased by "1".
-   The sequence number wraps to "0" when the value range is exceeded.
-   If the indication is redelivered, the **SequenceNumber** remains the same.

This property is inherited from [**CIM\_Indication**](cim-indication.md).

</dd> <dt>

**TIME\_CREATED**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Unique value that indicates the time at which the event was generated. This is a 64-bit value that represents the number of 100-nanosecond intervals after January 1, 1601. The information is in the Coordinated Universal Times (UTC) format. This property is inherited from [**\_\_Event**](https://msdn.microsoft.com/library/aa394634).

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**CIM\_ProcessIndication**](cim-processindication.md)
</dt> <dt>

[Failover Clustering Hyper-V WMI Provider](failover-clustering-hyper-v-wmi-provider-portal.md)
</dt> </dl>

 

 





