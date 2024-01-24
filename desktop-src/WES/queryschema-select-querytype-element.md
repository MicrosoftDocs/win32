---
title: Select (QueryType) Element
description: An XPath query that identifies the events to include in the query result set.
ms.assetid: b6aa747b-3586-460b-b51c-52fb112739c3
keywords:
- Select element EventLog
topic_type:
- apiref
api_name:
- Select
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Select (QueryType) Element

An XPath query that identifies the events to include in the query result set.

``` syntax
<xs:element name="Select">
    <xs:complexType
        mixed="true"
    >
        <xs:attribute name="Path"
            type="anyURI"
         />
    </xs:complexType>
</xs:element>
```

The **Select** element is defined by the [**QueryType**](queryschema-querytype-complextype.md) complex type.

## Attributes



| Name | Type   | Description                                                                              |
|------|--------|------------------------------------------------------------------------------------------|
| Path | anyURI | The name of the channel or the path to the log file that contains the events.<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps \| UWP apps\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps \| UWP apps\]<br/> |



## See also

<dl> <dt>

**Parent element**
</dt> <dt>

[**Query (QueryListType)**](queryschema-query-querylisttype-element.md)
</dt> </dl>

 

 





