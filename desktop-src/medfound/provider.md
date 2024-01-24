---
description: Specifies a trace provider (ETW or WPP) for MFTrace.
ms.assetid: '692cce3b-ebf5-4a49-8c37-48c8ef6caee7'
title: provider element
ms.topic: article
ms.date: 05/31/2018
---

# provider element

Specifies a trace provider (ETW or WPP) for [MFTrace](mftrace.md).

## Usage

``` syntax
<provider
  ID = "CDATA"
  level = "CDATA">
  child elements
</provider>
```

## Attributes



| Attribute            | Type             | Required       | Description                                              |
|----------------------|------------------|----------------|----------------------------------------------------------|
| **ID**<br/>    | CDATA<br/> | Yes<br/> | The name or GUID of the provider.<br/> <br/> |
| **level**<br/> | CDATA<br/> | Yes<br/> | The trace level.<br/> <br/>                  |



## Child elements



| Element                               |
|---------------------------------------|
| [**keyword**](keyword.md)<br/> |



### Child element sequence

``` syntax
keyword+
```

## Parent elements



| Element                                   |
|-------------------------------------------|
| [**providers**](providers.md)<br/> |



## Element information

:::row:::
    :::column:::
        Can be empty
    :::column-end:::
    :::column span="2":::
        No
    :::column-end:::
:::row-end:::

## See also

<dl> <dt>

[MFTrace Configuration File](mftrace-configuration-file.md)
</dt> </dl>

 

 




