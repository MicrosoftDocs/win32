---
description: Identifies the root node of the counters section of an instrumentation manifest.
ms.assetid: f16f432b-466f-4a3c-bc1b-e80b876a2511
title: counters Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- kbSyntax
api_name: 
api_type: 
api_location: 
---

# counters Element

Identifies the root node of the counters section of an instrumentation manifest.

``` syntax
<xs:element name="counters"
    type="man:counters"
>
    <xs:key name="uniqueprovGUID">
        <xs:selector
            xpath="./man:provider"
         />
        <xs:field
            xpath="@providerGuid"
         />
    </xs:key>
    <xs:key name="uniqueCounterSetGUID">
        <xs:selector
            xpath="./man:provider/man:counterSet"
         />
        <xs:field
            xpath="@guid"
         />
    </xs:key>
    <xs:key name="uniqueCounterSetURI">
        <xs:selector
            xpath="./man:provider/man:counterSet"
         />
        <xs:field
            xpath="@uri"
         />
    </xs:key>
    <xs:key name="uniqueCounterSetName">
        <xs:selector
            xpath="./man:provider/man:counterSet"
         />
        <xs:field
            xpath="@name"
         />
    </xs:key>
    <xs:key name="uniqueCounterSetSymbol">
        <xs:selector
            xpath="./man:provider/man:counterSet"
         />
        <xs:field
            xpath="@symbol"
         />
    </xs:key>
    <xs:unique name="uniqueCounterSymbol">
        <xs:selector
            xpath="./man:provider/man:counterSet/man:counter"
         />
        <xs:field
            xpath="@symbol"
         />
    </xs:unique>
    <xs:key name="uniqueCounterURI">
        <xs:selector
            xpath="./man:provider/man:counterSet/man:counter"
         />
        <xs:field
            xpath="@uri"
         />
    </xs:key>
</xs:element>
```

## Remarks

This element's parent node is the [**instrumentation**](/windows/desktop/WES/eventmanifestschema-instrumentationtype-complextype) element of the manifest.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

