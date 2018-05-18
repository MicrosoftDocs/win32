---
title: Hresult element
description: An HRESULT value for the error.
ms.assetid: 'CAD1750F-15EF-475A-825F-6BFB26722C51'
keywords: ["Hresult element Access Execution Engine"]
topic_type:
- apiref
api_name:
- Hresult
api_type:
- Schema
---

# Hresult element

An **HRESULT** value for the error.

## Usage

``` syntax
<Hresult>
  text
</Hresult>
```

## Attributes

There are no attributes.

## Text value

An **HRESULT** value. If the application has no **HRESULT** it should populate this field with the **E\_FAIL** (**\_HRESULT\_TYPEDEF\_**(0x80004005L)) error.

## Child elements

There are no child elements.

## Parent elements



| Element                               | Description                                 |
|---------------------------------------|---------------------------------------------|
| [**Error**](error.md)<br/>     | Describes an error.<br/> <br/>  |
| [**Warning**](warning.md)<br/> | Describes a warning.<br/> <br/> |



## Remarks

Applications should not put succeeding **HRESULT** in this field.

Applications should ignore a [**Warning**](warning.md) element with a success code in the **Hresult** element.

## Element information



|              |     |
|--------------|-----|
| Can be empty | Yes |



## See also

<dl> <dt>

[AXE Results Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449335)
</dt> </dl>

 

 





