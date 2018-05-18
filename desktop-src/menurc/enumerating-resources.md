---
title: Enumerating Resources
description: This topic discusses the functions used to obtain lists of resources.
ms.assetid: '388deaa1-3b04-43fa-aad2-8b52376d570c'
---

# Enumerating Resources

In certain situations application developers may want to discover the resource contents of an unknown Portable Executable (PE) module. The Windows SDK provides resource enumeration functions that enable an application to obtain lists of resource types, names, and languages in a specified module. The [**EnumResourceTypes**](enumresourcetypes.md) and [**EnumResourceTypesEx**](enumresourcetypesex.md) functions provide a list of resource types found in the module, the [**EnumResourceNames**](enumresourcenames.md) and [**EnumResourceNamesEx**](enumresourcenamesex.md) functions provide the name of each resource within a given type, and the [**EnumResourceLanguages**](enumresourcelanguages.md) and [**EnumResourceLanguagesEx**](enumresourcelanguagesex.md) functions provide the language of each resource of a given name and type. These functions and their associated callback functions enable applications to create a list of all resources in a module. This process is described in [Creating a Resource List](using-resources.md#creating-a-resource-list).

 

 




