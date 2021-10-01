---
description: CIM\_Indication is the abstract base class for all notifications about changes in schema objects, and schema object data, events detected by providers and instrumentation. Subclasses of CIM\_Indication represent specific types of notifications.
ms.assetid: 85a70425-7b32-449c-9fc0-1cfbf34d9187
title: CIM_Indication class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_Indication
- CIM_Indication.IndicationIdentifier
- CIM_Indication.CorrelatedIndications
- CIM_Indication.IndicationTime
- CIM_Indication.PerceivedSeverity
- CIM_Indication.OtherSeverity
- CIM_Indication.IndicationFilterName
- CIM_Indication.SequenceContext
- CIM_Indication.SequenceNumber
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# CIM\_Indication class

**CIM\_Indication** is the abstract base class for all notifications about changes in schema objects, and schema object data, events detected by providers and instrumentation. Subclasses of **CIM\_Indication** represent specific types of notifications.

## Syntax

``` syntax
[Indication, Version("2.24.0"), UMLPackagePath("CIM::Event"), AMENDMENT]
class CIM_Indication : __ExtrinsicEvent
{
  string   IndicationIdentifier;
  string   CorrelatedIndications[];
  datetime IndicationTime;
  uint16   PerceivedSeverity;
  string   OtherSeverity;
  string   IndicationFilterName;
  string   SequenceContext;
  sint64   SequenceNumber;
};
```

## Members

The **CIM\_Indication** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_Indication** class has these properties.

<dl> <dt>

**CorrelatedIndications**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("Recommendation.ITU\|X733.Correlated notifications"), [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("**CIM\_Indication**.**IndicationIdentifier**")
</dt> </dl>

A array that contains **IndicationIdentifier** values of notifications that are related this one.

</dd> <dt>

**IndicationFilterName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("CIM\_IndicationFilter.Name")
</dt> </dl>

The identifier of the indication filter that processes the indication. The sending service sets this property. This property correlates with the **Name** property of the **CIM\_IndicationFilter** object. The value of **IndicationFilterName** should use the following format:

-   *&lt;OrgID&gt;*:*&lt;LocalID&gt;*
-   *&lt;OrgID&gt;* must include a copyrighted, trademarked, or unique name that is owned by the business entity that owns the object.
-   *&lt;OrgID&gt;* must not contain a colon (:)
-   *&lt;LocalID&gt;* a unique identifier chosen by the business entity that owns the object.

</dd> <dt>

**IndicationIdentifier**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("Recommendation.ITU\|X733.Notification identifier")
</dt> </dl>

An identifier of the indication. This property can be used as a key value in the **CorrelatedIndications** property array. Therefore, **IndicationIdentifier** should be a unique value within the namespace of this class instance.

To ensure that **IndicationIdentifier** is unique, it should use the following format:

-   *&lt;OrgID&gt;*:*&lt;LocalID&gt;*
-   *&lt;OrgID&gt;* must include a copyrighted, trademarked, or unique name that is owned by the business entity that owns the object.
-   *&lt;OrgID&gt;* must not contain a colon (:)
-   *&lt;LocalID&gt;* a unique identifier chosen by the business entity that owns the object.
-   For DMTF-defined instances, *&lt;OrgID&gt;* should be set to "CIM".

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

 

</dd> <dt>

**OtherSeverity**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("[**CIM\_AlertIndication**](cim-alertindication.md).**PerceivedSeverity**")
</dt> </dl>

The severity of the indication from the notifier's point of view when **PerceivedSeverity** is set to "1" (Other).

</dd> <dt>

**PerceivedSeverity**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("Recommendation.ITU\|X733.Perceived severity")
</dt> </dl>

The severity of the indication from the notifier's point of view.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)


</dt> <dd>

the Perceived Severity of the indication is unknown or indeterminate.

</dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)


</dt> <dd>

Indicates that the Severity's value can be found in the **OtherSeverity** property.

</dd> <dt>

<span id="Information"></span><span id="information"></span><span id="INFORMATION"></span>

<span id="Information"></span><span id="information"></span><span id="INFORMATION"></span>**Information** (2)


</dt> <dd>

Information should be used when providing an informative response.

</dd> <dt>

<span id="Degraded_Warning"></span><span id="degraded_warning"></span><span id="DEGRADED_WARNING"></span>

<span id="Degraded_Warning"></span><span id="degraded_warning"></span><span id="DEGRADED_WARNING"></span>**Degraded/Warning** (3)


</dt> <dd>

Should be used when its appropriate to let the user decide if action is needed.

</dd> <dt>

<span id="Minor"></span><span id="minor"></span><span id="MINOR"></span>

<span id="Minor"></span><span id="minor"></span><span id="MINOR"></span>**Minor** (4)


</dt> <dd>

Action is needed, but the situation is not serious at this time.

</dd> <dt>

<span id="Major"></span><span id="major"></span><span id="MAJOR"></span>

<span id="Major"></span><span id="major"></span><span id="MAJOR"></span>**Major** (5)


</dt> <dd>

Action is needed NOW.

</dd> <dt>

<span id="Critical"></span><span id="critical"></span><span id="CRITICAL"></span>

<span id="Critical"></span><span id="critical"></span><span id="CRITICAL"></span>**Critical** (6)


</dt> <dd>

Action is needed NOW and the scope is broad (perhaps an imminent outage to a critical resource will result).

</dd> <dt>

<span id="Fatal_NonRecoverable"></span><span id="fatal_nonrecoverable"></span><span id="FATAL_NONRECOVERABLE"></span>

<span id="Fatal_NonRecoverable"></span><span id="fatal_nonrecoverable"></span><span id="FATAL_NONRECOVERABLE"></span>**Fatal/NonRecoverable** (7)


</dt> <dd>

an error occurred, but it's too late to take remedial action.

</dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved** (..)


</dt> <dd></dd> </dl>

</dd> <dt>

**SequenceContext**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("**CIM\_Indication**.**SequenceNumber**")
</dt> </dl>

The sequence context of the sequence identifier for the indication. If a service does not support sequence identifiers for indications, this property should be set to **NULL**. If the indication is redelivered, this property remains the same.

> [!Note]  
> The sequence identifier for the indication enables a listener to identify duplicate indications when the service attempts to redeliver indications, reorder indications that arrive out of order, and detect lost indications.

 

To ensure that **SequenceContext** is unique, it should use the following format:

-   *indication-service-name*\#*cim-service-start-id* \#*listener-destination-creation-time*
-   *indication-service-name* is the value of the **Name** property of the **CIM\_IndicationService** instance that delivers the indication.
-   *cim-service-start-id* is an identifier that uniquely identifies the start operation of a service. For example, this could be a timestamp of the start time, or a counter that increases for each start or restart of the service.
-   *listener-destination-creation-time* is a timestamp of the creation time of the **CIM\_ListenerDestination** instance representing the listener destination.nSince this format is only a recommendation, CIM clients shall treat the value as an opaque identifier for the sequence context and shall not rely on this format.

</dd> <dt>

**SequenceNumber**
</dt> <dd> <dl> <dt>

Data type: **sint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("**CIM\_Indication**.**SequenceContext**")
</dt> </dl>

The sequence number of the sequence identifier for the indication.

> [!Note]  
> The sequence identifier for the indication enables a listener to identify duplicate indications when the service attempts to redeliver indications, reorder indications that arrive out of order, and detect lost indications.

 

The sequence number has the following characteristics:

-   The sequence number is reset to "0" whenever the **SequenceContext** value changes.
-   Whenever the listener destination receives a new indication, the sequence number is increased by "1".
-   The sequence number wraps to "0" when the value range is exceeded.
-   If the indication is redelivered, the **SequenceNumber** remains the same.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                                  |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                       |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**\_\_ExtrinsicEvent**](/windows/desktop/WmiSdk/--extrinsicevent)
</dt> </dl>

 

