---
description: ICE41 validates that the entries in the Class and Extension tables refer to entries in the Component table that implement the class object or extension of the component.
ms.assetid: 43572322-ba23-4f99-be34-e572d4c6e3eb
title: ICE41
ms.topic: article
ms.date: 05/31/2018
---

# ICE41

ICE41 validates that the entries in the [Class](class-table.md) and [Extension](extension-table.md) tables refer to entries in the [Component table](component-table.md) that implement the class object or extension of the component.

## Result

ICE41 posts an error if there is a feature that does not contain the component implementing the class object or extension.

## Example

ICE41 reports the following errors for the example shown.



| ICE41 error                                                                                                                                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Class {00000000-0000-0000-0000-0000000000000} references feature Feature2 and component Component1, but the that Component is not associated with that Feature in the FeatureComponents table. | There is a feature that does not contain the component implementing the class object. This means that the installer does not install the component with the feature and that advertising may not work as expected. To fix this error, change the entry in the Feature\_ column of the [Class table](class-table.md) entry to reference a feature that installs component listed in the Component\_ column or change the feature and component associated in the [FeatureComponents table](featurecomponents-table.md).<br/>          |
| Extension .yip references feature Feature1 and component Component2, but the that Component is not associated with that Feature in the FeatureComponents table.                                | There is a feature that does not contain the component implementing the extension. This means that the installer does not install the component with the feature and that advertising may not work as expected. To fix this error, change the entry in the Feature\_ column of the [Extension table](extension-table.md) entry to reference a feature that installs the component listed in the Component\_ column or change the feature and component associated in the [FeatureComponents table](featurecomponents-table.md).<br/> |



 

[FeatureComponents Table](featurecomponents-table.md) (partial)



| Feature\_ |
|-----------|
| Feature1  |
| Feature2  |



 

[Class Table](class-table.md) (partial)



| CLSID                                  | Component\_ | Feature\_ |
|----------------------------------------|-------------|-----------|
| {00000000-0000-0000-0000-000000000000} | Component1  | Feature2  |



 

[Class Table](class-table.md) (partial)



| Extension | Component\_ | Feature\_ |
|-----------|-------------|-----------|
| .yip      | Component2  | Feature1  |



 

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 




