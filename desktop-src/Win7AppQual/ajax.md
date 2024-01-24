---
description: AJAX
ms.assetid: F9907D49-F9FE-406A-BF5F-17C61706ADC1
title: AJAX
ms.topic: article
ms.date: 05/31/2018
---

# AJAX

AJAX features in Windows Internet Explorer 8 like **XDomainRequest (XDR)** and Cross-Document Messaging (XDM) have native properties that might conflict with existing custom properties.

Windows Internet Explorer exposes new properties for certain AJAX features, such as Cross-Document Messaging (XDM), even in Compatibility View. If you add custom properties to the event object, they might conflict with these new properties, such as **source**.

The following code example works in older versions of Internet Explorer but not in newer versions because new features use the **source** property.


```JScript
event.source = myObject;
```



The following code example shows how you can change this object to remain compatible.


```JScript
event.mySource = myObject;// Read-only in IE8, use mySource instead
```



## Related topics

<dl> <dt>

[Fixing Compatibility Issues in Web Applications by Using Compatibility View](remediating-web-applications-and-add-ons.md)
</dt> </dl>

 

 



