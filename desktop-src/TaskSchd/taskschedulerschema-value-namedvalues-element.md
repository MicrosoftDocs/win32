---
title: Value (namedValues) Element
description: Contains the value that is associated with a name in a name-value pair.
ms.assetid: d5582b55-0b9b-4fed-a425-9d15a1a62fb7
keywords:
- Value element Task Scheduler
topic_type:
- apiref
api_name:
- Value
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Value (namedValues) Element

Contains the value that is associated with a name in a name-value pair.

``` syntax
<xs:element name="Value"
    type="namedValue"
    minOccurs="1"
    maxOccurs="32"
 />
```

The **Value** element is defined by the [**namedValues**](taskschedulerschema-namedvalues-complextype.md) complex type.

## Parent element



| Element                                                                                              | Derived from                                                       | Description                                                                                                                                                                                                                                                                                                                                                                       |
|------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ValueQueries (eventTriggerType)**](taskschedulerschema-valuequeries-eventtriggertype-element.md) | [**namedValues**](taskschedulerschema-namedvalues-complextype.md) | Specifies a collection of named XPath queries. Each query in the collection is applied to the last matching event XML that is returned from the subscription query specified in the [**Subscription**](taskschedulerschema-subscription-eventtriggertype-element.md) element. The name of the query can be used as a variable in the message of a ShowMessage action.<br/> |



## Remarks

For C++ development, see [**Value Property of ITaskNamedValuePair**](/windows/desktop/api/taskschd/nf-taskschd-itasknamedvaluepair-get_value).

For script development, see [**TaskNamedValuePair.Value**](tasknamedvaluepair-value.md).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





