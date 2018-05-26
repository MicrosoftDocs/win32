---
title: Parent element
description: A single parent of the TestCase.
ms.assetid: 0AE240B0-3CCA-4810-9993-8B3C11326C37
keywords:
- Parent element Access Execution Engine
topic_type:
- apiref
api_name:
- Parent
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Parent element

A single parent of the [**TestCase**](testcase.md).

## Usage

``` syntax
<Parent>
  text
</Parent>
```

## Attributes

There are no attributes.

## Text value

The value of this node is a string that must match either the [**Key**](key.md) of another test case in the file, or identify a logical grouping relationship. For example, all test cases that represent intervals could have a parent intervals which does not match the key of any test case in the file but defines the logical grouping of intervals.

## Child elements

There are no child elements.

## Parent elements



| Element                                   | Description                                                                               |
|-------------------------------------------|-------------------------------------------------------------------------------------------|
| [**TestCases**](testcases.md)<br/> | A container for one or more [**TestCase**](testcase.md) elements.<br/> <br/> |



## Element information



|              |     |
|--------------|-----|
| Can be empty | Yes |



## See also

<dl> <dt>

[AXE Results Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449335)
</dt> </dl>

 

 





