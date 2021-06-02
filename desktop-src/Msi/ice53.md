---
description: ICE53 checks for entries in the Registry table that write private installer information or policy values to the system registry.
ms.assetid: f5afca1f-bd36-4f95-a62a-f6b2e37238a6
title: ICE53
ms.topic: article
ms.date: 05/31/2018
---

# ICE53

ICE53 checks for entries in the Registry table that write private installer information or policy values to the system registry.

## Result

ICE53 posts a warning if the Registry table specifies writing internal or policy information to the registry.

## Example

ICE53 posts the following warning for the example shown.

``` syntax
Registry Key 'Registry1' writes Installer internal or policy information.
```

[Registry Table](registry-table.md) (partial)



| Registry             | Root         | Key                                                                                                   |
|----------------------|--------------|-------------------------------------------------------------------------------------------------------|
| Registry1<br/> | 1<br/> | **Software**\\**Policies**\\**Microsoft**\\**Windows**\\**Installer**\\**DisableRollback**<br/> |



 

Registry table row 'Registry1' writes a system policy value in the registry that affects the installation of all packages. Depending on the package, it may be possible to disable rollback for this package alone by setting the [**DISABLEROLLBACK**](-disablerollback.md) property in the [Property table](property-table.md). See [Rollback Installation](rollback-installation.md).

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 




