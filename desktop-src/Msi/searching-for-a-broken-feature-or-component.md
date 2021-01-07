---
description: The installer can increase application resiliency by automatically reinstalling damaged components.
ms.assetid: aa565e34-f89d-4d26-945d-67b439586523
title: Searching for a Broken Feature or Component
ms.topic: article
ms.date: 05/31/2018
---

# Searching for a Broken Feature or Component

The installer can increase application [resiliency](resiliency.md) by automatically reinstalling damaged components. Specifically, the installer reinstalls a component or feature if it finds that the file or registry key specified in the KeyPath column of the [Component table](component-table.md) is missing.

If the KeyPath of a feature's component is damaged in the source, or if there is an error in how the KeyPath is authored in the database, the installer may attempt to open an installation package and reinstall the feature each time the feature's shortcut is activated.

To determine the cause of repeated attempts to reinstall a feature or application, check the Event Log for two entries such as the following.

``` syntax
Detection of product 'MyProduct', feature 'MyFeature' failed during
 request for component 'MyComponent'
Detection of product 'MyProduct', feature 'MyFeature', component
 'MyComponent' failed
```

The first message states which component in the product's package was being installed. This is the component referenced in the Component\_ column of the [Shortcut table](shortcut-table.md).

The second message states which component is failing detection. This is the component with the missing or damaged KeyPath that's triggering the reinstall.

 

 



