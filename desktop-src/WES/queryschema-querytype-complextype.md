---
title: QueryType Complex Type
description: Defines a set of selector and suppressor queries that are used to include events in or exclude events from the result set.
ms.assetid: 223d0127-f097-45f8-8511-1a56d9c41e84
keywords:
- QueryType complex type EventLog
topic_type:
- apiref
api_name:
- QueryType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# QueryType Complex Type

Defines a set of selector and suppressor queries that are used to include events in or exclude events from the result set.

``` syntax
<xs:complexType name="QueryType">
    <xs:choice
        maxOccurs="unbounded"
    >
        <xs:element name="Select">
            <xs:complexType
                mixed="true"
            >
                <xs:attribute name="Path"
                    type="anyURI"
                 />
            </xs:complexType>
        </xs:element>
        <xs:element name="Suppress">
            <xs:complexType
                mixed="true"
            >
                <xs:attribute name="Path"
                    type="anyURI"
                 />
            </xs:complexType>
        </xs:element>
    </xs:choice>
    <xs:attribute name="Id"
        type="long"
        use="optional"
     />
    <xs:attribute name="Path"
        type="anyURI"
        use="optional"
     />
</xs:complexType>
```

## Child elements



| Element                                                    | Type | Description                                                                                                                                                                            |
|------------------------------------------------------------|------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Select**](queryschema-select-querytype-element.md)     |      | An XPath query that identifies the events to include in the query result set. Specify the XPath in the text body of this element. The XPath is limited to 32 expressions.<br/>   |
| [**Suppress**](queryschema-suppress-querytype-element.md) |      | An XPath query that identifies the events to exclude from the query result set. Specify the XPath in the text body of this element. The XPath is limited to 32 expressions.<br/> |



## Attributes



| Name | Type   | Description                                                                                                                                                                                         |
|------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Id   | long   | An identifier that uniquely identifies this query in your list of queries. The identifier is zero-based. You must specify an identifier if your query list contains more than one query.<br/> |
| Path | anyURI | The name of the channel or the path to the log file that contains the events.<br/>                                                                                                            |
| Path | anyURI | The name of the channel or the path to the log file that contains the events.<br/>                                                                                                            |
| Path | anyURI | Not used.<br/>                                                                                                                                                                                |



## Remarks

The query must have at least one select statement. For each suppress statement, there must be at least one select statement that specifies the same path. If the select and suppress query return the same events, the suppress statement takes precedence. If you select events from multiple sources, the events are returned in time stamp order. If you use the system time stamp and the rate of events is high, it is possible that more than one event will have the same time stamp. When this occurs, the ordering of events becomes ambiguous and the events may appear out of order.

If you specify a path for one of the queries in the list of queries, all of the queries must specify a path. If you do not specify a path for all of the queries, you must specify the path when calling the [**EvtQuery**](/windows/desktop/api/WinEvt/nf-winevt-evtquery) or [**EvtSubscribe**](/windows/desktop/api/WinEvt/nf-winevt-evtsubscribe) function.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





