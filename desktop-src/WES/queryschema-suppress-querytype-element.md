---
title: Suppress (QueryType) Element
description: An XPath query that identifies the events to exclude from the query result set.
ms.assetid: 41304a3c-bde1-49c3-8cb3-e95fc428bd96
keywords:
- Suppress element EventLog
topic_type:
- apiref
api_name:
- Suppress
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Suppress (QueryType) Element

An XPath query that identifies the events to exclude from the query result set.

``` syntax
<xs:element name="Suppress">
    <xs:complexType
        mixed="true"
    >
        <xs:attribute name="Path"
            type="anyURI"
         />
    </xs:complexType>
</xs:element>
```

The **Suppress** element is defined by the [**QueryType**](queryschema-querytype-complextype.md) complex type.

## Attributes



| Name | Type   | Description                                                                              |
|------|--------|------------------------------------------------------------------------------------------|
| Path | anyURI | The name of the channel or the path to the log file that contains the events.<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

**Parent element**
</dt> <dt>

[**Query (QueryListType)**](queryschema-query-querylisttype-element.md)
</dt> </dl>

 

 





