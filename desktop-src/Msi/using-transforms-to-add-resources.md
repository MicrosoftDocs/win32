---
description: Resources that are needed for the customization of an application, such as corporate templates, can be deployed with the application by including a transform with the application's installation package.
ms.assetid: 3d9328d0-4d95-449c-bf2b-5487f7ba5971
title: Using Transforms to Add Resources
ms.topic: article
ms.date: 05/31/2018
---

# Using Transforms to Add Resources

Resources that are needed for the customization of an application, such as corporate templates, can be deployed with the application by including a transform with the application's installation package. The following rules should be followed when deploying resources, such as files, registry keys, or shortcuts, using a transform.

-   The transform should add one or more new components to the installation database to contain the additional resources. The transform should not add resources to a component that already exists in the installation.
-   The transform should add one or more new features to the installation database to contain these new components. These new features should not be the parents of any existing features, but new parent and child features may be introduced together. New features should be given names that are unique across all other transforms for this product. No two transforms should ever add a feature to this product that has the same name listed in the Feature column of the [Feature table](feature-table.md) and containing different components or resources.

 

 



