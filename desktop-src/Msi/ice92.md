---
description: ICE92 verifies that a component without a Component Id GUID is not also specified as a permanent component.
ms.assetid: 5fe8a844-3f96-4b19-baa6-24e2405aff30
title: ICE92
ms.topic: article
ms.date: 05/31/2018
---

# ICE92

ICE92 verifies that a component without a Component Id GUID is not also specified as a permanent component. This ICE custom action checks the [Component Table](component-table.md) for components without a [GUID](guid.md) specified in the ComponentId field and verifies that the **msidbComponentAttributesPermanent** flag has not been set in the Attributes field. ICE92 also verifies that no component has both the **msidbComponentAttributesPermanent** and **msidbComponentAttributesUninstallOnSupersedence** attributes.

If the ComponentId column is null, the installer does not register the component and the component cannot be removed or repaired by the installer.

## Result

ICE92 posts the following error.



| ICE92 error                                                          | Description                                                                                                                                                    |
|----------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| The Component '\[1\]' has no ComponentId and is marked as permanent. | The entry for this component in the Component table has null in the ComponentId column and has **msidbComponentAttributesPermanent** in the Attributes column. |



 

ICE92 posts the following warning.



| ICE92 warning                                                                                                                                                           | Description                                                                                                                                                                                                 |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| The Component '\[1\]' is marked as permanent and uninstall-on-supersedence. The uninstall-on-supersedence attribute will be ignored because the component is permanent. | The entry for this component in the [Component table](component-table.md) has both the **msidbComponentAttributesPermanent** and **msidbComponentAttributesUninstallOnSupersedence** attributes specified. |



 

## Example

ICE92 reports the following error for the example:

``` syntax
The Component 'Component1' has no ComponentId and is marked as permanent.
```

[Component Table](component-table.md) (partial)



| Component  | ComponentId | Directory\_ | Attributes | KeyPath |
|------------|-------------|-------------|------------|---------|
| Component1 |             | DirectoryA  | 16         | FileA   |



 

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



