---
description: Contains a list of trace providers for MFTrace.
ms.assetid: ee483f0a-5a90-4150-ada4-0b63ae312523
title: providers element
ms.topic: reference
ms.date: 05/31/2018
---

# providers element

Contains a list of trace providers for [MFTrace](mftrace.md).

## Usage

``` syntax
<providers>
  child elements
</providers>
```

## Attributes

There are no attributes.

## Child elements



| Element                                   | Description                                                                                                      |
|-------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| [**mfdetours**](mfdetours.md)<br/> | Specifies the Media Foundation Detours provider, which traces Media Foundation API calls.<br/> <br/> |
| [**provider**](provider.md)<br/>   | Specifies a trace provider (ETW or WPP).<br/> <br/>                                                  |



### Child element sequence

``` syntax
(
  mfdetours?, 
  provider*
)
```

## Parent elements

There are no parent elements.

## Element information



|              |     |
|--------------|-----|
| Can be empty | Yes |



## See also

<dl> <dt>

[MFTrace Configuration File](mftrace-configuration-file.md)
</dt> </dl>

 

 




