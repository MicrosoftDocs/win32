---
description: ICE59 checks that advertised shortcuts belong to components that are installed by the target feature of the shortcut.
ms.assetid: 9cd19137-792d-4fde-92d2-7d96942448d6
title: ICE59
ms.topic: article
ms.date: 05/31/2018
---

# ICE59

ICE59 checks that advertised shortcuts belong to components that are installed by the target feature of the shortcut.

Errors reported by ICE59 generally lead to the following behavior:

1.  The advertised shortcut will launch the Windows Installer to install the feature listed in the Target column.
2.  But because the [FeatureComponents table](featurecomponents-table.md) does not map the target feature to the component containing the shortcut, the keyfile of the component (which is activated by the shortcut) is not installed.
3.  Therefore the shortcut is broken and will not do anything.

## Result

ICE59 posts an error if an advertised shortcut does not belong to the components that are installed by the target feature of the shortcut.

## Example

ICE59 reports the following error for the example shown:

``` syntax
The shortcut ShortcutB activates component ComponentB and advertises feature FeatureA, but there is no mapping between FeatureA and ComponentB in the FeatureComponents table.
```

In this case, ShortcutB advertises FeatureA, and when activated, starts the key file of ComponentB. Yet ComponentB is never installed by FeatureA, so even after the installation-on-demand phase completes, the target of the shortcut does not exist.

To fix this error, add a row to the [FeatureComponents table](featurecomponents-table.md) that associates FeatureA and ComponentB.

[Shortcut Table](shortcut-table.md) (partial)



| Shortcut  | Target   | Component\_ |
|-----------|----------|-------------|
| ShortcutB | FeatureA | ComponentB  |



 

[FeatureComponents Table](featurecomponents-table.md)



| Feature\_ | Component\_ |
|-----------|-------------|
| FeatureA  | ComponentA  |



 

[Feature Table](feature-table.md) (partial)



| Feature  | Level |
|----------|-------|
| FeatureA | 10    |



 

[Component Table](component-table.md) (partial)



| Component  | KeyPath |
|------------|---------|
| ComponentA | FileA   |
| ComponentB | FileB   |



 

[File Table](file-table.md) (partial)



| File  | Component\_ | Sequence |
|-------|-------------|----------|
| FileA | ComponentA  | 1        |
| FileB | ComponentB  | 2        |



 

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



