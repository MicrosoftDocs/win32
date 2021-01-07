---
description: To publish a product, component, or feature, use one of the publishing actions.
ms.assetid: 2c395d81-4f46-444e-a275-7a5d806e473c
title: Publishing Products, Features, and Components
ms.topic: article
ms.date: 05/31/2018
---

# Publishing Products, Features, and Components

To [publish](components-and-features.md) a product, component, or feature, use one of the publishing actions. The [PublishProduct action](publishproduct-action.md) registers the product information with the system. After executing the PublishProduct action, publish the components with the [PublishComponents action](publishcomponents-action.md), which in turn uses the [PublishComponent table](publishcomponent-table.md) to determine the components that are set as advertised. To publish on a per-feature basis, invoke the [PublishFeatures action](publishfeatures-action.md). This action uses the [FeatureComponents table](featurecomponents-table.md) as data to resolve which features are advertised.

There are also two corresponding actions that unpublish a feature or a component: the [UnpublishComponents action](unpublishcomponents-action.md) and the [UnpublishFeatures action](unpublishfeatures-action.md).

 

 



