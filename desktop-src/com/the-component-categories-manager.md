---
title: The Component Categories Manager
description: The Component Categories Manager
ms.assetid: bd43ef98-2299-4c8a-9f35-bf9aceb074ab
ms.topic: article
ms.date: 05/31/2018
---

# The Component Categories Manager

To facilitate the handling of component categories and to guarantee consistency of the registry, the system provides the Component Categories Manager, a COM object with a CLSID of CLSID\_StdComponentCategoriesMgr. This COM object provides the following interfaces:

-   [**ICatInformation**](/windows/desktop/api/ComCat/nn-comcat-icatinformation)
-   [**ICatRegister**](/windows/desktop/api/ComCat/nn-comcat-icatregister)

[**ICatInformation**](/windows/desktop/api/ComCat/nn-comcat-icatinformation) provides methods for obtaining information about the categories implemented or required by a certain class and provides information about the categories registered on a given machine.

[**ICatRegister**](/windows/desktop/api/ComCat/nn-comcat-icatregister) provides methods for registering and unregistering component category information in the registry. This includes both the human-readable names of categories and the categories implemented or required by a given component or class.

## Related topics

<dl> <dt>

[Associating Icons with a Category](associating-icons-with-a-category.md)
</dt> <dt>

[Categorizing by Component Capabilities](categorizing-by-component-capabilities.md)
</dt> <dt>

[Categorizing by Container Capabilities](categorizing-by-container-capabilities.md)
</dt> <dt>

[Default Classes and Associations](default-classes-and-associations.md)
</dt> <dt>

[Defining Component Categories](defining-component-categories.md)
</dt> </dl>

 

 




