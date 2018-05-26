---
title: Id element
description: A unique GUID identifier.
ms.assetid: 677D4CF9-84CA-4F36-B0AB-9521306B3DED
keywords:
- Id element Access Execution Engine
topic_type:
- apiref
api_name:
- Id
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Id element

A unique **GUID** identifier.

## Usage

``` syntax
<Id>
  text
</Id>
```

## Attributes

There are no attributes.

## Text value

A **GUID** identifier in registry format. Open and close braces are required.

## Child elements

There are no child elements.

## Parent elements



| Element                             | Description                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| [**AxeJob**](https://msdn.microsoft.com/library/windows/desktop/hh707420)<br/> | This node contains the entirety of the job used to generate a set of results.<br/> <br/> |



## Remarks

### Report Identity

Each report file has a unique identity. Report files do not receive a version.

Tools should write an **Id** element at the top of the report file so that the identity can be determined by a streaming XML reader.

Axe is responsible for writing this value in the aggregated job results file.

## Element information



|              |     |
|--------------|-----|
| Can be empty | Yes |



## See also

<dl> <dt>

[AXE Job Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449330)
</dt> <dt>

[AXE Results Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449335)
</dt> </dl>

 

 





