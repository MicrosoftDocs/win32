---
description: There are several functions that change the installation of product components and features. The following describes how to change features and components.
ms.assetid: 840656f9-ea85-49e7-8842-f779228c30d6
title: Working with Features and Components
ms.topic: article
ms.date: 05/31/2018
---

# Working with Features and Components

There are several functions that change the installation of product [components and features](components-and-features.md). The following describes how to change features and components.

**To change the installation of features and components**

1.  Set the installation level for a component or feature by calling the [**MsiSetInstallLevel**](/windows/desktop/api/Msiquery/nf-msiquery-msisetinstalllevel) function.

    Each feature in a package is assigned an installation level in the [Feature table](feature-table.md). If the installation level of a feature is lower than the level set by [**MsiSetInstallLevel**](/windows/desktop/api/Msiquery/nf-msiquery-msisetinstalllevel), the feature is selected for installation. After **MsiSetInstallLevel** is called, you can explicitly change whether a feature is installed.

2.  Determine which states are available for a specified feature by calling the [**MsiGetFeatureValidStates**](/windows/desktop/api/Msiquery/nf-msiquery-msigetfeaturevalidstatesa) function.
3.  Obtain the disk space requirements for a specified feature and its child features by calling the [**MsiGetFeatureCost**](/windows/desktop/api/Msiquery/nf-msiquery-msigetfeaturecosta) function.
4.  Obtain the current state of a feature or component by calling the [**MsiGetFeatureState**](/windows/desktop/api/Msiquery/nf-msiquery-msigetfeaturestatea) function or the [**MsiGetComponentState**](/windows/desktop/api/Msiquery/nf-msiquery-msigetcomponentstatea) function.
5.  Change the state of the feature or component with the [**MsiSetFeatureState**](/windows/desktop/api/Msiquery/nf-msiquery-msisetfeaturestatea) function or the [**MsiSetComponentState**](/windows/desktop/api/Msiquery/nf-msiquery-msisetcomponentstatea) function.

 

 



