---
title: Error element
description: This element describes an error.
ms.assetid: '4207c9d3-6ebb-4968-a855-1c0f4afb8d4d'
keywords: ["Error element Access Execution Engine"]
topic_type:
- apiref
api_name:
- Error
api_type:
- Schema
---

# Error element

This element describes an error.

## Usage

``` syntax
<Error>
  child elements
</Error>
```

## Attributes

There are no attributes.

## Child elements



| Element                               | Description                                                                          |
|---------------------------------------|--------------------------------------------------------------------------------------|
| [**Hresult**](hresult.md)<br/> | An **HRESULT** value for the error. This element is required.<br/> <br/> |
| [**Message**](message.md)<br/> | Describes the error. This element is required.<br/> <br/>                |



### Child element sequence

``` syntax
(
  Hresult, 
  Message
)
```

## Parent elements



| Element                                                   | Description                                                                |
|-----------------------------------------------------------|----------------------------------------------------------------------------|
| [**ErrorsAndWarnings**](errorsandwarnings.md)<br/> | A container to hold assessment errors and warnings.<br/> <br/> |



## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Results Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449335)
</dt> </dl>

 

 





