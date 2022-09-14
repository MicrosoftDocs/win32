---
description: Is the root element of an WSDAPI code generator XML script file.
ms.assetid: '3d40172b-6ba1-4e42-9a1a-519c8e88c2b1'
title: wsdCodeGen element
ms.topic: article
ms.date: 05/31/2018
---

# wsdCodeGen element

Is the root element of an WSDAPI code generator XML script file.

## Usage

``` syntax
<wsdCodeGen
  ConfigFileVersion = "Any character string.">
  child elements
</wsdCodeGen>
```

## Attributes



| Attribute                        | Type                             | Required       | Description                                                                                  |
|----------------------------------|----------------------------------|----------------|----------------------------------------------------------------------------------------------|
| **ConfigFileVersion**<br/> | Any character string.<br/> | Yes<br/> | The version of the configuration file. The only valid value is "1.0".<br/> <br/> |



## Child elements



| Element                                                         | Description                                                                                                                                                                                                                 |
|-----------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**autoStatic**](autostatic.md)<br/>                     | Indicates whether or not WsdCodeGen should try to automatically flag certain generated fields as static. This is enabled by default.<br/> <br/>                                                                 |
| [**file**](file.md)<br/>                                 | Directs the code generator to generate a file.<br/> <br/>                                                                                                                                                       |
| [**hostMetadata**](hostmetadata.md)<br/>                 | The hosting metadata for the device to be implemented. This element is used for device implementations (hosts) only.<br/> <br/>                                                                                 |
| [**layerNumber**](layernumber.md)<br/>                   | The number of the code layer to be generated. Layer numbers are used in runtime tables to distinguish one layer of code for another. WSDAPI itself uses generated code that has a layer number of 0.<br/> <br/> |
| [**layerPrefix**](layerprefix.md)<br/>                   | The prefix to use in the generated code to assure uniqueness of generated symbols. WSDAPI uses the prefix "WSD".<br/> <br/>                                                                                     |
| [**macro**](macro.md)<br/>                               | Defines text or CDATA to be reused by the [**include**](include.md) element.<br/> <br/>                                                                                                                        |
| [**nameSpace**](namespace.md)<br/>                       | Describes a namespace to be used for code generation.<br/> <br/>                                                                                                                                                |
| [**relationshipMetadata**](relationshipmetadata.md)<br/> | Describes the host and hosted metadata for the device.<br/> <br/>                                                                                                                                               |
| [**thisModelMetadata**](thismodelmetadata.md)<br/>       | The manufacturer and model metadata for the device to be implemented. This element is used for device implementations (hosts) only.<br/> <br/>                                                                  |
| [**wsdl**](wsdl.md)<br/>                                 | Specifies a WSDL file to process for contract information.<br/> <br/>                                                                                                                                           |
| [**xsd**](xsd.md)<br/>                                   | Specifies an XSD file to process for contract information.<br/> <br/>                                                                                                                                           |



### Child element sequence

``` syntax
(
  layerNumber?, 
  layerPrefix?, 
  autoStatic?, 
  hostMetadata?, 
  thisModelMetadata?, 
  nameSpace*, 
  wsdl*, 
  xsd*, 
  file*, 
  macro*, 
  relationshipMetadata*
)
```

## Parent elements

There are no parent elements.

## Remarks

In general, [**file**](file.md) elements should occur last because they generate code which uses data specified by the other elements.

## Element information



| Label | Value |
|-------------------------------------|---------------|
| Minimum supported system<br/> | Windows Vista |
| Can be empty                        | Yes           |



 

 




