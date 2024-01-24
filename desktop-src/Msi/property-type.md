---
description: The Property Type of semantic type is one of the Key Format Types. This type consists of a foreign key into the Property table provided by the user.
ms.assetid: 819e4e90-0bc3-41ba-851d-1d4c52b6eeea
title: Property Type
ms.topic: article
ms.date: 05/31/2018
---

# Property Type

The Property Type of [semantic type](semantic-types.md) is one of the [Key Format Types](key-format-types.md). This type consists of a foreign key into the [Property table](property-table.md) provided by the user.

The merge tool must substitute a valid Windows Installer [Identifier](identifier.md) for items of this type. Mergemod.dll does not enforce this restriction and it is up to the merge tool to ensure that the user provides a valid key into the Property table. The primary keys of the Property table are the property names.

Null is a valid value for this type unless the msmConfigItemNonNullable has been included in the Attributes field of the [ModuleConfiguration table](moduleconfiguration-table.md).

The Property type may be used with the following kinds of ContextData.

**Null ContextData**

A configurable merge module may use this type to enable the user to provide a property name to a database table in the module. The merge tool substitutes the property's identifier into the templates in the Value column of the [ModuleSubstitution table](modulesubstitution-table.md). To specify a configurable item of this type, module authors should enter the name of the configurable item into the Name column, enter "1" into the Format column, enter "Property" into the Type column, and leave blank the ContextData column of the [ModuleConfiguration table](moduleconfiguration-table.md).

**Public ContextData**

A configurable merge module may use this type to enable the user to provide the name of a [public property](public-properties.md) to a database table in the module. The merge tool substitutes the property's identifier into the templates in the Value column of the [ModuleSubstitution table](modulesubstitution-table.md). To specify a configurable item of this type, module authors should enter the name of the configurable item into the Name column, enter "1" into the Format column, enter "Property" into the Type column, and enter "Public" into the ContextData column of the ModuleConfiguration table.

**Private ContextData**

A configurable merge module may use this type to enable the user to provide the name of a [private property](private-properties.md) to a database table in the module. The merge tool substitutes the property's identifier into the templates in the Value column of the [ModuleSubstitution table](modulesubstitution-table.md). To specify a configurable item of this type, module authors should enter the name of the configurable item into the Name column, enter "1" into the Format column, enter "Property" into the Type column, and enter "Private" into the ContextData column of the ModuleConfiguration table.

 

 



