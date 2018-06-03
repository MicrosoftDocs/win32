---
title: TrueIsPass element
description: Indicates that the MetricValue is considered to pass if its boolean value is true.
ms.assetid: FFB16A4C-6429-4533-B3C4-882C06E84AE1
keywords:
- TrueIsPass element Access Execution Engine
topic_type:
- apiref
api_name:
- TrueIsPass
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# TrueIsPass element

Indicates that the **MetricValue** is considered to pass if its boolean value is **true**. This is valid for boolean, numeric and string types. For integral numeric types, zero is considered false, and non-zero is true. For floating point types, zero and NaN are considered false, and all other values true. For string types, false is assumed if the string is null, empty (zero length) or consists of all white space characters.

## Usage

``` syntax
<TrueIsPass/>
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



 

 




