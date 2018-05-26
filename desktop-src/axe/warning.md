---
title: Warning element
description: Describes a warning.
ms.assetid: 87DE42C6-E829-465E-B595-D527F53ED8AF
keywords:
- Warning element Access Execution Engine
topic_type:
- apiref
api_name:
- Warning
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Warning element

Describes a warning.

## Usage

``` syntax
<Warning>
  child elements
</Warning>
```

## Attributes

There are no attributes.

## Child elements



| Element                               | Description                                                                            |
|---------------------------------------|----------------------------------------------------------------------------------------|
| [**Hresult**](hresult.md)<br/> | An **HRESULT** value for the warning. This element is required.<br/> <br/> |
| [**Message**](message.md)<br/> | Describes the warning. This element is required.<br/> <br/>                |



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

 

 





