---
description: Specifies a key word for an MFTrace provider.
ms.assetid: 1ce4a5ee-c053-4d31-a984-dc11acebbf2a
title: keyword element
ms.topic: reference
ms.date: 05/31/2018
---

# keyword element

Specifies a key word for an [MFTrace](mftrace.md) provider.

## Usage

``` syntax
<keyword
  ID = "CDATA"/>
```

## Attributes



| Attribute         | Type             | Required       | Description                                             |
|-------------------|------------------|----------------|---------------------------------------------------------|
| **ID**<br/> | CDATA<br/> | Yes<br/> | The name or mask of the key word<br/> <br/> |



## Child elements

There are no child elements.

## Parent elements



| Element                                   |
|-------------------------------------------|
| [**mfdetours**](mfdetours.md)<br/> |
| [**provider**](provider.md)<br/>   |



## Remarks

For the [**mfdetours**](mfdetours.md) element, the valid key words are listed in the topic [MFTrace Keywords](mftrace-keywords.md).

For the [**provider**](provider.md) element, the key words depend on the event provider. You can use the Wevtutil.exe utility to list the key words for a given provider.

## Element information



|              |     |
|--------------|-----|
| Can be empty | Yes |



## See also

<dl> <dt>

[MFTrace Configuration File](mftrace-configuration-file.md)
</dt> <dt>

[MFTrace Keywords](mftrace-keywords.md)
</dt> </dl>

 

 




