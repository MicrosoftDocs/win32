---
description: Specifies a localized version of the device name.
ms.assetid: 67ebbca0-bdb2-4a6e-98d8-3d8d1029884f
title: modelNameLS element
ms.topic: reference
ms.date: 05/31/2018
---

# modelNameLS element

Specifies a localized version of the device name.

## Usage

``` syntax
<modelNameLS
  Language = "language identifier string"
  Data = "localized model name string"/>
```

## Attributes



| Attribute               | Type                                   | Required       | Description                                                      |
|-------------------------|----------------------------------------|----------------|------------------------------------------------------------------|
| **Data**<br/>     | localized model name string<br/> | Yes<br/> | The localized model name.<br/> <br/>                 |
| **Language**<br/> | language identifier string<br/>  | Yes<br/> | The language of the localized model name.<br/> <br/> |



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



 

 




