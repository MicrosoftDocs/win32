---
description: Is used in the registration of permanent event consumers to relate an instance of the \_\_EventConsumer to an instance of \_\_EventFilter.
ms.assetid: e6a06161-0f1c-4754-ac34-263ccf7bf10d
ms.tgt_platform: multiple
title: '__FilterToConsumerBinding class'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- __FilterToConsumerBinding
- All
- All
- All
- All
- All
- All
- All
api_type: 
- Schema
api_location: 
- All
---

# \_\_FilterToConsumerBinding class

The **\_\_FilterToConsumerBinding** system class is used in the registration of permanent event consumers to relate an instance of the [**\_\_EventConsumer**](--eventconsumer.md) to an instance of [**\_\_EventFilter**](--eventfilter.md).**\_\_FilterToConsumerBinding** is an association class.

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
class __FilterToConsumerBinding : __IndicationRelated
{
  __EventConsumer REF Consumer;
  uint8               CreatorSID[];
  boolean             DeliverSynchronously = False;
  uint32              DeliveryQoS;
  __EventFilter   REF Filter;
  boolean             MaintainSecurityContext = False;
  boolean             SlowDownProviders = False;
};
```

## Members

The **\_\_FilterToConsumerBinding** class has these types of members:

-   [Properties](#properties)

### Properties

The **\_\_FilterToConsumerBinding** class has these properties.

<dl> <dt>

**Consumer**
</dt> <dd> <dl> <dt>

Data type: **\_\_EventConsumer**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Key**](standard-qualifiers.md)
</dt> </dl>

Reference to an instance of [**\_\_EventConsumer**](--eventconsumer.md) that represents the object path to a logical consumer, the recipient of an event. A logical consumer is an instance of a class derived from **\_\_EventConsumer**.

</dd> <dt>

**CreatorSID**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

Security identifier (SID) that uniquely identifies the user who created the binding. Depending on the operating system, WMI stores the Administrator SID or the SID of the user that creates an instance of **\_\_FilterToConsumerBinding**. For more information, see [Binding an Event Filter with a Logical Consumer](binding-an-event-filter-with-a-logical-consumer.md) and [Monitoring and Responding to Events with Standard Consumers](monitoring-and-responding-to-events-with-standard-consumers.md).

</dd> <dt>

**DeliverSynchronously**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Obsolete. Instead use the **DeliveryQoS** property in place of this property, because if **DeliverSynchronously** is set to **True** it overrides the setting of the **DeliveryQoS** property.

</dd> <dt>

**DeliveryQoS**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Quality of service for a subscription. If the **DeliverSynchronously** property is set to **True**, it overrides the setting of the **DeliveryQoS** property.

<dt>

<span id="WMIMSG_FLAG_QOS_SYNCHRONOUS"></span><span id="wmimsg_flag_qos_synchronous"></span>

<span id="WMIMSG_FLAG_QOS_SYNCHRONOUS"></span><span id="wmimsg_flag_qos_synchronous"></span>**WMIMSG\_FLAG\_QOS\_SYNCHRONOUS** (0)


</dt> <dd>

Synchronous delivery

**False**. The event is delivered to the logical consumer synchronously.

</dd> <dt>

<span id="WMIMSG_FLAG_QOS_EXPRESS"></span><span id="wmimsg_flag_qos_express"></span>

<span id="WMIMSG_FLAG_QOS_EXPRESS"></span><span id="wmimsg_flag_qos_express"></span>**WMIMSG\_FLAG\_QOS\_EXPRESS** (1)


</dt> <dd>

Express delivery

**True**. The event is delivered to the logical consumer asynchronously.

</dd> </dl>

</dd> <dt>

**Filter**
</dt> <dd> <dl> <dt>

Data type: **\_\_EventFilter**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Key**](standard-qualifiers.md)
</dt> </dl>

Reference to an instance of [**\_\_EventFilter**](--eventfilter.md) that represents the object path to an event filter which is a query that specifies the type of event to be received.

</dd> <dt>

**MaintainSecurityContext**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **True**, the events are delivered in the same security context that the provider was in when it provided them.

> [!Note]  
> Only a consumer implemented as a DLL (an in-process consumer) can receive events in the security context of the provider. For more information about in-process providers and security, see [Provider Hosting and Security](provider-hosting-and-security.md). For more information and examples, see replace:[Receiving Events Securely](receiving-events-securely.md).

 

</dd> <dt>

**SlowDownProviders**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **True**, providers are slowed down if this consumer cannot keep up.

</dd> </dl>

## Remarks

The **\_\_FilterToConsumerBinding** class is derived from [**\_\_IndicationRelated**](--indicationrelated.md), which has no properties.

Permanent event consumers use the **\_\_FilterToConsumerBinding** system class to bind event filters to final consumers. After the filter and consumer are bound together, WMI can forward events that match the filter to the corresponding consumer.

## Examples

The [Create Permanent WMI Event registration to monitor files](https://Gallery.TechNet.Microsoft.Com/Create-Permenant-WMI-Event-f67ce5c2) PowerShell example on TechNet Gallery uses **\_\_FilterToConsumerBinding** as part of a complex script to set up a permanent WMI event registration.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |
| Namespace<br/>                | All WMI namespaces<br/>  |



## See also

<dl> <dt>

[**\_\_IndicationRelated**](--indicationrelated.md)
</dt> <dt>

[WMI System Classes](wmi-system-classes.md)
</dt> <dt>

[Monitoring and Responding to Events with Standard Consumers](monitoring-and-responding-to-events-with-standard-consumers.md)
</dt> <dt>

[Monitoring Events](monitoring-events.md)
</dt> <dt>

[Creating an Event Filter](creating-an-event-filter.md)
</dt> <dt>

[Securing WMI Events](securing-wmi-events.md)
</dt> </dl>

 

 




