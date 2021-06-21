---
description: Specifies a localized version of the manufacturer name.
ms.assetid: e87de50f-60ec-4c18-b21c-81f7b6928752
title: manufacturerLS element
ms.topic: reference
ms.date: 05/31/2018
---

# manufacturerLS element

Specifies a localized version of the manufacturer name.

## Usage

``` syntax
<manufacturerLS
  Language = "language identifier string"
  Data = "localized manufacturer name string"/>
```

## Attributes



| Attribute               | Type                                          | Required       | Description                                                             |
|-------------------------|-----------------------------------------------|----------------|-------------------------------------------------------------------------|
| **Data**<br/>     | localized manufacturer name string<br/> | Yes<br/> | The localized manufacturer name.<br/> <br/>                 |
| **Language**<br/> | language identifier string<br/>         | Yes<br/> | The language of the localized manufacturer name.<br/> <br/> |



## Child elements

There are no child elements.

## Parent elements



| Element                                                   | Description                                                                                          |
|-----------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| [**thisModelMetadata**](thismodelmetadata.md)<br/> | Defines the manufacturer and model metadata for the device to be implemented.<br/> <br/> |



## Element information



| Label | Value |
|-------------------------------------|---------------|
| Minimum supported system<br/> | Windows Vista |
| Can be empty                        | Yes           |



 

 




