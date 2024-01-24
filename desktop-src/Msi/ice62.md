---
description: ICE62 performs extensive checks on the IsolatedComponent table for data that may cause unexpected behavior.
ms.assetid: 649d3989-8121-4303-aa3e-63bc6649f445
title: ICE62
ms.topic: article
ms.date: 05/31/2018
---

# ICE62

ICE62 performs extensive checks on the [IsolatedComponent table](isolatedcomponent-table.md) for data that may cause unexpected behavior.

Failure to fix an error reported by ICE62 can result in a failure of the isolated component system in a wide variety of ways. For example, if the SharedDllRefCount bit is not set for a shared component, the registration for the component could be removed when another application uses that ComponentId and is uninstalled.

## Result

ICE62 posts a warning or error when it finds data in the IsolatedComponent table that may produce unexpected behavior.

## Example

ICE62 reports the following errors and warning for the examples shown.

``` syntax
The component 'Component2' is listed as an isolated application 
component in the IsolatedComponent table, but the key path is not a file.
```

Component2 is listed as the application component for the isolation of component1. However, Component2 has a registry key path, and does not provide a valid executable path to use to isolate the component.

To fix this error, use a different component as the application for the isolated component Component1.

``` syntax
The component 'Component1' is listed as an isolated shared component in the 
IsolatedComponent table, but is not marked with the SharedDllRefCount component attribute.
```

Component1 is listed as an isolated shared component, but does not have the SharedDllRefCount bit set. This could result in the lifetime of the component being incorrect. If another application uses this component (isolated or not) and is uninstalled, the registration for the component is removed but this application's isolated copy remains. This causes repair and uninstall problems.

To fix this error, set the SharedDllRefCount bit for the component.

``` syntax
The isolated shared component 'Component1' is not installed by the same feature as 
(or a parent feature of) its isolated application component 'Component2' (which is installed by feature 'Feature2').
```

Component1 and Component2 are installed by different features. Component1 is installed by Feature1, and Component2 is installed by Feature2. Feature1 is not a parent of Feature2, hence it is possible for the application to be installed but not the isolated component, breaking the isolation.

To fix this error, add an entry to the FeatureComponents table linking Component1 to the same feature as (or a parent feature of) the feature that installs Component2.

``` syntax
WARNING: The isolated shared component 'Component1' (referenced in the IsolatedComponent table) 
is conditionalized. Isolated shared component conditions should never change from TRUE to FALSE after the first install of the product.
```

Component1 has a condition in the Component table. If this condition ever changes from TRUE to FALSE during the lifetime of an installation on a computer, the isolated component could be orphaned without registration information.

To fix this warning, remove the condition, or author the condition so that it can never change from TRUE to FALSE.

``` syntax
WARNING: The isolated shared component 'Component1' is shared by multiple applications 
(including 'Component2') that are installed to the directory 'TARGETDIR'.
WARNING: The isolated shared component 'Component1' is shared by multiple applications 
(including 'Component3') that are installed to the directory 'TARGETDIR'.
```

Component1 is isolated for both Component2 and Component3, and the two components are also installed to the same directory. The applications share an isolated component, but if one application is removed the shared component is removed as well causing the other applications to lose the isolated component.

To fix this warning, install the applications to different directories or check whether some of the applications truly require an isolated component.

[IsolatedComponent Table](isolatedcomponent-table.md)



| Component\_Shared | Component\_Application |
|-------------------|------------------------|
| Component1        | Component2             |
| Component1        | Component3             |



 

[Component Table](component-table.md)



| Component  | ComponentId | Directory\_ | Attributes | Condition   | KeyPath   |
|------------|-------------|-------------|------------|-------------|-----------|
| Component1 |             | Dir1        | 0          | MYCONDITION | File1     |
| Component2 |             | TARGETDIR   | 4          |             | Registry2 |
| Component3 |             | TARGETDIR   | 0          |             | File3     |



 

[FeatureComponentsTable](featurecomponents-table.md)



| Feature\_ | Component\_ |
|-----------|-------------|
| Feature1  | Component1  |
| Feature2  | Component2  |
| Feature1  | Component3  |



 

[Feature Table](feature-table.md) (partial)



| Feature  | Feature\_Parent |
|----------|-----------------|
| Feature1 |                 |
| Feature2 |                 |



 

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



