---
description: ICE61 validates the Upgrade table of a Windows Installer database.
ms.assetid: 9f6834c6-74eb-4219-8111-7b722ea41a3a
title: ICE61
ms.topic: article
ms.date: 05/31/2018
---

# ICE61

ICE61 checks the upgrade table to ensure that the following conditions are true:

-   All ActionProperty properties are not pre-authored in the Property table.
-   All ActionProperty properties are Public Properties.
-   All ActionProperty properties are included in the [**SecureCustomProperties**](securecustomproperties.md) property.
-   All ActionProperty properties are unique to each record in the Upgrade table.
-   All VersionMax values are not less than the corresponding VersionMin values.
-   VersionMin and VersionMax values are valid product versions. See the [**ProductVersion**](productversion.md) property for the valid product version format.
-   No attempt is made to remove a newer or equal version of the current product.

Failure to fix a warning or error reported by ICE61 generally leads to problems in upgrading your application. Depending on the exact error, this could be anything from leaving files from the older version behind, deleting files from the older version even though they are needed by the new application, or complete failure of the upgrade.

## Result

ICE61 posts a warning or error if any of the above conditions are not true.

## Example

ICE61 reports the following errors and warning for the examples shown.

``` syntax
This product should remove only older versions of itself. The Maximum version is not less than the current product. (2.01.0000 2.01.0000)
```

In this case, the first row would try to remove a product of the same version. (VersionMax column is equal to the product version in the Property table).

To fix this error, use a version in the VersionMax column lower than the current version specified in the Property table. Remove the **msidbUpgradeAttributesVersionMaxInclusive** bit from the Attributes column if the VersionMax is equal to the current version. If the intent is only to detect the product and not remove it, adding the **msidbUpgradeAttributesOnlyDetect** bit to the Attributes column will also fix this error.

``` syntax
Upgrade.ActionProperty EnglishAPPFOUND must be added to the SecureCustomProperties property.
```

Unless the property is listed in the [**SecureCustomProperties**](securecustomproperties.md) property, the property is not passed to the server side of the install when the property is found.

To fix this error, add the property to [**SecureCustomProperties**](securecustomproperties.md).

``` syntax
Upgrade.ActionProperty EnglishAPPFOUND must not contain lowercase letters.
```

Upgrade properties must be public properties for the result to be passed to the server side of the installation.

To fix this error, use all uppercase letters in the property name.

``` syntax
Upgrade.ActionProperty OLDAPPFOUND may be used in only one record of the Upgrade table.
```

A property can only be used in one row of the Upgrade table.

To fix this error, use a different property for the second row.

``` syntax
Upgrade.VersionMax cannot be less than Upgrade.VersionMin. (OLDAPPFOUND)
```

The minimum version must be less than the maximum version.

To fix this error, check your version numbers for typos. If they are correct and you want to use the range between the two versions, switch them so that VersionMin is less than VersionMax.

[Property Table](property-table.md)



| Property                                                 | Value                                  |
|----------------------------------------------------------|----------------------------------------|
| [**UpgradeCode**](upgradecode.md)                       | {61AA4C55-E17F-11D2-93BB-0060089A76DB} |
| [**ProductVersion**](productversion.md)                 | 2.01.0000                              |
| [**SecureCustomProperties**](securecustomproperties.md) | OLDAPPFOUND                            |



 

[Upgrade Table](upgrade-table.md)



| UpgradeCode                            | VersionMin | VersionMax | Language | Attributes | Remove                | ActionProperty  |
|----------------------------------------|------------|------------|----------|------------|-----------------------|-----------------|
| {61AA4C55-E17F-11D2-93BB-0060089A76DB} |            | 2.01.0000  |          | 513        |                       | OLDAPPFOUND     |
| {61AA4C55-E17F-11D2-93BB-0060089A76DB} | 2.01.0001  | 2.01.0000  |          |            |                       | OLDAPPFOUND     |
| {C6CB4596-D8E8-D5A4-635F-9FE456D682EB} | 1.00.0000  | 2.00.0000  | 1033     |            | \[AppFeatureEnglish\] | EnglishAPPFOUND |



 

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



