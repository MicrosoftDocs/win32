---
description: ICEM06 checks for invalid direct references to features by the module.
ms.assetid: 63e63a60-53e5-4881-ad71-efeceb73a70e
title: ICEM06
ms.topic: article
ms.date: 05/31/2018
---

# ICEM06

ICEM06 checks for invalid direct references to features by the module.

Merge module ICEs are stored in a merge module .cub file called Mergemod.cub and not in the .cub file containing the ICEs used for package validation.

## Result

ICEM06 posts an error when the module database contains direct references to a feature. Feature information must be provided by the user of the module.

## Example

ICEM06 posts the following error messages for a module containing the database entries shown below.

``` syntax
The target of shortcut Shortcut1.GUID1 is not a property and not a null GUID. 
Modules may not directly reference features.
The row GUID2.LocalServer32.Component2 in the Class table has a feature reference 
that is not a null GUID. Modules may not directly reference features.
```

[Shortcut Table](shortcut-table.md) (partial)



| Shortcut          | Target                                 |
|-------------------|----------------------------------------|
| Shortcut1.*GUID1* | cmd.exe                                |
| Shortcut2.*GUID1* | \[MyProp\]                             |
| Shortcut3.*GUID1* | {00000000-0000-0000-0000-000000000000} |



 

[Class Table](class-table.md) (partial)



| CLSID   | Context       | Component\_ | Feature\_                              |
|---------|---------------|-------------|----------------------------------------|
| *GUID1* | LocalServer32 | Component1  | {00000000-0000-0000-0000-000000000000} |
| *GUID2* | LocalServer32 | Component2  | MyFeature                              |



 

ICEM06 reports the first error because the first record in the Shortcut table has an entry in the Target field that is not a property or a null GUID. A module cannot reference a feature directly. Feature information must be provided by the user of the module. To fix this error, references to a feature should be replaced by a null GUID.

ICEM06 reports the second error because the second record in the Class table has an entry in the Feature field that is not a null GUID. A module cannot reference a feature directly. Feature information must be provided by the user of the module. To fix this error, references to a feature should be replaced by a null GUID.

## Related topics

<dl> <dt>

[Merge Module ICE Reference](merge-module-ice-reference.md)
</dt> </dl>

 

 



