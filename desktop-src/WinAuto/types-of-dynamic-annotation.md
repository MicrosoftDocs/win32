---
title: Types of Dynamic Annotation
description: There are three types of Dynamic Annotation supported in Microsoft Active Accessibility direct annotation, value-mapped annotation, and server annotation. Each type offers specific advantages, so it is important to understand the differences.
ms.assetid: 113fea65-982e-4291-9d60-bbb57282f3f4
ms.topic: article
ms.date: 05/31/2018
---

# Types of Dynamic Annotation

There are three types of Dynamic Annotation supported in Microsoft Active Accessibility: *direct annotation*, *value-mapped annotation*, and *server annotation*. Each type offers specific advantages, so it is important to understand the differences.

## Direct Annotation

Direct annotation is the simplest form of Dynamic Annotation. It is most applicable for accessible elements whose annotated property is not dependent upon the control's state and does not require the additional support provided by value-mapped annotation and server annotation. Direct annotation is used to override the value of one or more Microsoft Active Accessibility properties of an accessible element, and to override or add a Microsoft UI Automation property to the control. All annotations made in a Microsoft Active Accessibility property are reflected in the UI Automation translation as well as in the Microsoft Active Accessibility-to-UI Automation proxy. For more information, see [Direct Annotation](direct-annotation.md).

## Value Map Annotation

In addition to directly annotating [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) properties, there is often a need to convert a control-specific value into a string that can be understood by an end user. An example is the screen resolution slider control under the **Settings** tab on the **Display Properties** window (from **Control Panel**). While each slider position corresponds to a different resolution (for example, 640 x 480, 1024 x 768), the control has no knowledge of this relationship and cannot convey this information to Microsoft Active Accessibility.

Value-mapped annotation makes this task easier. Using this form of annotation, you can specify strings for slider values and specify roles, states, and descriptions for icons in list and tree views. For more information, see [Value Map Annotation](value-map-annotation.md).

## Server Annotation

Server annotation allows developers to register a callback object to service client requests for an element's annotated property. This callback object must implement the [**IAccPropServer**](/windows/desktop/api/oleacc/nn-oleacc-iaccpropserver) interface and be registered with Microsoft Active Accessibility annotation services. Once registered, it will be asked to service all client requests for that accessible element's property value.

One particularly useful feature of server annotation is that a server can be registered once to handle requests for a container and all of its children. So, for example, a single server can be set up once to handle requests for all the items is a list box. For more information, see [Server Annotation](server-annotation.md).

 

 




