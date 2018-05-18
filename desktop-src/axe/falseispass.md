---
title: FalseIsPass element
description: Indicates that the MetricValue is considered to pass if its boolean value is false.
ms.assetid: 'CA715419-4D21-4FE5-B5A8-23AFACB9107A'
keywords: ["FalseIsPass element Access Execution Engine"]
topic_type:
- apiref
api_name:
- FalseIsPass
api_type:
- Schema
---

# FalseIsPass element

Indicates that the **MetricValue** is considered to pass if its boolean value is **false**. This is valid for boolean, numeric and string types. For integral numeric types, zero is considered false, and non-zero is true. For floating point types, zero and NaN are considered false, and all other values true. For string types, false is assumed if the string is null, empty (zero length) or consists of all white space characters.

## Usage

``` syntax
<FalseIsPass/>
```

## Attributes

There are no attributes.

## Child elements

There are no child elements.

## Parent elements

There are no parent elements.

## Element information



|              |     |
|--------------|-----|
| Can be empty | Yes |



 

 




