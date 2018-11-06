---
title: Default Classes and Associations
description: For certain categories, a single class can be associated as the default class.
ms.assetid: 9c48615b-ab10-44e4-a032-49d5ee0c9b01
ms.topic: article
ms.date: 05/31/2018
---

# Default Classes and Associations

For certain categories, a single class can be associated as the default class. The default class is selected whenever that particular category of object is required. While this may not be useful for all component categories, establishing a default class can be helpful when a particular class must be loaded from a list of possible classes without user intervention. Administrators define which class can be used by manipulating the registry.

To associate a default class with a category, introduce a CLSID key with the same CLSID as the CATID of the component category chosen as the default. Then add a TreatAs key to this key, using the value for the CLSID of the default class for the category. To use the default class for a component category, use [**CoCreateInstance**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstance) or [**CoGetClassObject**](/windows/desktop/api/combaseapi/nf-combaseapi-cogetclassobject), specifying the CATID for the CLSID parameter. This automatically redirects to the CLSID established as the default for this category. The registry entry is as follows:

```
HKEY_CLASSES_ROOT\CLSID
   {catid}
      TreatAs
          = default clsid
```

During installation, a component can check for the existence of any default class keys for its categories and present the user with options for overriding the current settings.

## Related topics

<dl> <dt>

[Associating Icons with a Category](associating-icons-with-a-category.md)
</dt> <dt>

[Categorizing by Component Capabilities](categorizing-by-component-capabilities.md)
</dt> <dt>

[Categorizing by Container Capabilities](categorizing-by-container-capabilities.md)
</dt> <dt>

[Defining Component Categories](defining-component-categories.md)
</dt> <dt>

[The Component Categories Manager](the-component-categories-manager.md)
</dt> </dl>

 

 




