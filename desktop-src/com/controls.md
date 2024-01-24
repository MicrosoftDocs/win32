---
title: Controls (COM)
description: Controls
ms.assetid: '73947c81-6727-4112-9da0-efa60360f458'
ms.topic: article
ms.date: 05/31/2018
---

# Controls (COM)

An ActiveX control is really just another term for OLE object or more specifically, COM object. In other words, a control, at the very least, is some COM object that supports the [**IUnknown**](/windows/desktop/api/Unknwn/nn-unknwn-iunknown) interface and is also self-registering. Through [**IUnknown::QueryInterface**](/windows/desktop/api/Unknwn/nf-unknwn-iunknown-queryinterface(q)) a container can manage the lifetime of the control as well as dynamically discover the full extent of a control's functionality based on the available interfaces. This allows a control to implement as little functionality as it needs to, instead of supporting a large number of interfaces that actually don't do anything. In short, this minimal requirement for nothing more than **IUnknown** allows any control to be as lightweight as it can.

In short, other than [**IUnknown**](/windows/desktop/api/Unknwn/nn-unknwn-iunknown) and self-registration, there are no other requirements for a control. There are, however, conventions that should be followed about what the support of an interface means in terms of functionality provided to the container by the control. This section then describes what it means for a control to actually support an interface, as well as methods, properties, and events that a control should provide as a baseline if it has occasion to support methods, properties, and events.

For more information, see the following topics:

-   [Self Registration for Controls](self-registration-for-controls.md)
-   [What Support for an Interface Means](what-support-for-an-interface-means.md)
-   [Persistence Interfaces](persistence-interfaces.md)
-   [Optional Methods in Control Interfaces](optional-methods-in-control-interfaces.md)
-   [Class Factory Options](class-factory-options.md)
-   [Exposing Properties through IDispatch](properties.md)
-   [Exposing Methods through IDispatch](exposing-methods-through-idispatch.md)
-   [Events in Controls](events-in-controls.md)
-   [Property Pages](property-pages.md)
-   [Ambient Properties for Controls](ambient-properties-for-controls.md)
-   [Using the Container's Functionality](using-the-container-s-functionality.md)

## Related topics

<dl> <dt>

[ActiveX Control and Control Container Guidelines](activex-control-and-control-container-guidelines.md)
</dt> </dl>

 

 




