---
title: Categorizing by Component Capabilities
description: Component categories can be used to display a subset of all of the installed components.
ms.assetid: 522af5d7-ba7b-4127-9cdb-48ef4d0f8e65
ms.topic: article
ms.date: 05/31/2018
---

# Categorizing by Component Capabilities

Component categories can be used to display a subset of all of the installed components. Each component category is identified by a GUID, referred to as a Category ID (CATID). Each CATID has a list of locale-tagged, human-readable names associated with it. A listing of the CATIDs and the human-readable names is stored in a well-known location in the registry.

For example, all components that implement the functionality for OLE document embedding can be classified within a component category. In the past, these objects would have been identified by the "Insertable" key in the registry. To use component categories instead, the following information would be added to the registry:

```
HKEY_CLASSES_ROOT\Component Categories\{40FC6ED3-2438-11cf-A3DB-080036F12502}
   (Default) = ""
   409 = "Embeddable Objects"
```

Each class that implements the functionality corresponding to a component category lists the category ID for that category within the CLSID key in the registry. Because a single component can support a wide range of functionality, components can belong to multiple component categories. For example, a particular OLE control might support all of the functionality required to participate as OLE document embedding, Microsoft Visual Basic data binding, and Internet functionality. Such a control would have the following information stored in its CLSID key in the registry:

``` syntax
;The CLSID for "My Super OLE Control" is {12345678-ABCD-4321-0101-00000000000C}HKEY_CLASSES_ROOT\CLSID\{12345678-ABCD-4321-0101-00000000000C}\Implemented Categories
;The CATID for "Insertable" is {40FC6ED3-2438-11cf-A3DB-080036F12502} HKEY_CLASSES_ROOT\CLSID\{12345678-ABCD-4321-0101-00000000000C}Implemented Categories\{40FC6ED3-2438-11cf-A3DB-080036F12502}
;The CATID for "Control" is {40FC6ED4-2438-11cf-A3DB-080036F12502} HKEY_CLASSES_ROOT\CLSID\{12345678-ABCD-4321-0101-00000000000C}Implemented Categories\{40FC6ED4-2438-11cf-A3DB-080036F12502}
;The CATID for an internet aware control is {...CATID_InternetAware...} HKEY_CLASSES_ROOT\CLSID\{12345678-ABCD-4321-0101-00000000000C}Implemented Categories\{...CATID_InternetAware...}
 
```

With this information, a container can enumerate the controls installed on a system and display only those controls that support the functionality required by the container. The use of component categories provides a way to categorize components by the implemented functionality of the component.

## Related topics

<dl> <dt>

[Associating Icons with a Category](associating-icons-with-a-category.md)
</dt> <dt>

[Categorizing by Container Capabilities](categorizing-by-container-capabilities.md)
</dt> <dt>

[Default Classes and Associations](default-classes-and-associations.md)
</dt> <dt>

[Defining Component Categories](defining-component-categories.md)
</dt> <dt>

[The Component Categories Manager](the-component-categories-manager.md)
</dt> </dl>

 

 




