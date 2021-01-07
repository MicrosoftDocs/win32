---
description: The following sections describe using the built-in installer properties and additional properties defined by the package author.
ms.assetid: 5a2f1cd4-2bbd-414a-a814-8b9fdab434b4
title: Using Properties
ms.topic: article
ms.date: 05/31/2018
---

# Using Properties

The following sections describe using the built-in installer properties and additional properties defined by the package author. Properties can be either [public properties](public-properties.md) or [private properties](private-properties.md). Every property that needs to be defined upon initialization of the installer must have its name and initial value listed in the [Property table](property-table.md). Properties having a Null value are not listed in the Property table. You can get or set properties from programs and custom actions and set public properties from the command line. The installation process can be modified by using properties in conditional statements.

[Restrictions on Property Names](restrictions-on-property-names.md)

[Initialization of Property Values](initialization-of-property-values.md)

[Getting and Setting Properties](getting-and-setting-properties.md)

[Using Properties in Conditional Statements](using-properties-in-conditional-statements.md)

[Using a Directory Property in a Path](using-a-directory-property-in-a-path.md)

> [!Note]  
> Do not use properties for passwords or other information that must remain secure. The installer may write the value of a property authored into the Property table or created at runtime into a log or the system registry.

 

## Related topics

<dl> <dt>

[About Properties](about-properties.md)
</dt> <dt>

[Property Reference](property-reference.md)
</dt> </dl>

 

 



