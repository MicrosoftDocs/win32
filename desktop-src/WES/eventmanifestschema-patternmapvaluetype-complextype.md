---
title: PatternMapValueType Complex Type
description: Not used. Defines the regular expressions used to find a matching string in the message string and alter it.
ms.assetid: 2ae8a268-64c0-45d1-8339-988b13d884a3
keywords:
- PatternMapValueType complex type EventLog
topic_type:
- apiref
api_name:
- PatternMapValueType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# PatternMapValueType Complex Type

Not used. Defines the regular expressions used to find a matching string in the message string and alter it.

``` syntax
<xs:complexType name="PatternMapValueType">
    <xs:simpleContent>
        <xs:extension
            base="string"
        >
            <xs:attribute name="name"
                type="string"
                use="required"
             />
            <xs:attribute name="value"
                type="string"
                use="required"
             />
        </xs:extension>
    </xs:simpleContent>
</xs:complexType>
```

## Attributes



| Name  | Type   | Description                                                                                               |
|-------|--------|-----------------------------------------------------------------------------------------------------------|
| name  | string | The regular expression used to find a matching string in the message string.<br/>                   |
| value | string | The regular expression used to alter the matching string that was found in the message string.<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





