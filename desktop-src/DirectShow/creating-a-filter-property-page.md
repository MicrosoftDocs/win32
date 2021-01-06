---
description: Creating a Filter Property Page
ms.assetid: 028e2c4e-0241-4057-8514-d3e9b456ab6e
title: Creating a Filter Property Page
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Filter Property Page

This section describes how to create a property page for a custom DirectShow filter, using the [**CBasePropertyPage**](cbasepropertypage.md) class. The example code in this section shows all the steps needed to create a property page. The example shows a property page for a hypothetical video effect filter that supports a saturation property. The property page has a slider, which the user can move to adjust the filter's saturation level.

This section contains the following topics:

-   [Step 1. Define a Mechanism for Setting the Property](step-1--define-a-mechanism-for-setting-the-property.md)
-   [Step 2. Implement ISpecifyPropertyPages](step-2--implement-ispecifypropertypages.md)
-   [Step 3. Support QueryInterface](step-3--support-queryinterface.md)
-   [Step 4. Create the Property Page](step-4--create-the-property-page.md)
-   [Step 5. Store a Pointer to the Filter](step-5--store-a-pointer-to-the-filter.md)
-   [Step 6. Initialize the Dialog](step-6--initialize-the-dialog.md)
-   [Step 7. Handle Window Messages](step-7--handle-window-messages.md)
-   [Step 8. Apply Property Changes](step-8--apply-property-changes.md)
-   [Step 9. Disconnect the Property Page](step-9--disconnect-the-property-page.md)
-   [Step 10. Support COM Registration](step-10--support-com-registration.md)

## Related topics

<dl> <dt>

[Writing DirectShow Filters](writing-directshow-filters.md)
</dt> </dl>

 

 



