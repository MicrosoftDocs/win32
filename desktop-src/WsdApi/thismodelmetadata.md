---
description: Defines the manufacturer and model metadata for the device to be implemented. This element is used for device implementations (hosts) only.
ms.assetid: 2ebd3092-39aa-469c-a8c9-23f373ba0e66
title: thisModelMetadata element
ms.topic: reference
ms.date: 05/31/2018
---

# thisModelMetadata element

Defines the manufacturer and model metadata for the device to be implemented. This element is used for device implementations (hosts) only.

## Usage

``` syntax
<thisModelMetadata>
  child elements
</thisModelMetadata>
```

## Attributes

There are no attributes.

## Child elements



| Element                                                     | Description                                                                                                                                                                        |
|-------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**manufacturer**](manufacturer.md)<br/>             | Name of the manufacturer. At least one of [**manufacturer**](manufacturer.md) or [**manufacturerLS**](manufacturerls.md) must be present in the metadata.<br/> <br/> |
| [**manufacturerLS**](manufacturerls.md)<br/>         | Localized version of the manufacturer name.<br/> <br/>                                                                                                                 |
| [**manufacturerURL**](manufacturerurl.md)<br/>       | Manufacturer URL address.<br/> <br/>                                                                                                                                   |
| [**modelName**](modelname.md)<br/>                   | Name of the device. At least one of [**modelName**](modelname.md) or [**modelNameLS**](modelnamels.md) must be present in the metadata.<br/> <br/>                   |
| [**modelNameLS**](modelnamels.md)<br/>               | Localized version of the device name.<br/> <br/>                                                                                                                       |
| [**modelNumber**](modelnumber.md)<br/>               | Model number of the device.<br/> <br/>                                                                                                                                 |
| [**modelURL**](modelurl.md)<br/>                     | URL address for the device model.<br/> <br/>                                                                                                                           |
| [**PnPXDeviceCategory**](pnpxdevicecategory.md)<br/> | PnP-X category to which the device belongs. <br/> <br/>                                                                                                                |
| [**presentationURL**](presentationurl.md)<br/>       | URL address of the device model's presentation data.<br/> <br/>                                                                                                        |



### Child element sequence

``` syntax
(
  manufacturer?, 
  manufacturerLS*, 
  manufacturerURL?, 
  modelName?, 
  modelNameLS*, 
  modelNumber, 
  modelURL?, 
  PnPXDeviceCategory?, 
  presentationURL?
)
```

## Parent elements



| Element                                     | Description                                                                          |
|---------------------------------------------|--------------------------------------------------------------------------------------|
| [**wsdCodeGen**](wsdcodegen.md)<br/> | The root element of an WSDAPI code generator XML script file.<br/> <br/> |



## Remarks

The manufacturer metadata matches the manufacturer metadata section described in the device profile (consult the device profile for details). The manufacturer name or at least one localized version of the manufacturer name must be provided. The model name or at least one localized version of the model name must be provided.

The [**thisModelMetadataDefinition**](thismodelmetadatadefinition.md) element is subsequently used to generate a C constant containing this information.

If a [**PnPXDeviceCategory**](pnpxdevicecategory.md) element is present, then at least one [**hosted**](hosted.md) element must contain both [**PnPXHardwareId**](pnpxhardwareid.md) and [**PnPXCompatibleId**](pnpxcompatibleid.md) elements. Similarly, if **PnPXHardwareId** and **PnPXCompatibleId** elements are present in a **hosted** element, a **PnPXDeviceCategory** element must be present inside the **thisModelMetadata** element.

## Element information



| Label | Value |
|-------------------------------------|---------------|
| Minimum supported system<br/> | Windows Vista |
| Can be empty                        | No            |



 

 




