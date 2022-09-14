---
title: ActiveX Controls Architecture
description: ActiveX controls technology builds on a foundation of many lower-level objects and interfaces in OLE. The exact interfaces available on a control vary with its capabilities. This section takes a closer look at the capabilities a control might provide.
ms.assetid: 42959a11-8bfb-4f7e-ba27-5dc1ed49cdaa
ms.topic: article
ms.date: 05/31/2018
---

# ActiveX Controls Architecture

ActiveX controls technology builds on a foundation of many lower-level objects and interfaces in OLE. The exact interfaces available on a control vary with its capabilities. This section takes a closer look at the capabilities a control might provide.

ActiveX controls are used to provide the building blocks for creating user interfaces in applications. For example, a button that initiates some action in the container application when it is clicked is a simple control. The following aspects are involved in providing these user interface building blocks:

-   A control can be embedded within its container client to support some user interface activity within the client. Thus, a control needs to provide a visual representation of itself when it is embedded within the container and needs to provide a way to save its state, for example, its property values and its position within its container. The client must support being a container with objects embedded in it.
-   By activating the control using a keyboard or mouse, the end user initiates some action in the client application. Thus, a control must respond to keyboard activity and must be able to communicate with its client so it can notify its container of its activities and trigger events in the client.
-   The client also typically provides a programming language through which the end user can initiate actions provided by the control's properties and methods. Thus, a control must support automation and some set of design-time versus run-time features as well.

As a result of its role in providing user interface building blocks, a control typically supports features in the following areas using OLE technologies as indicated:

<dl> <dt>

<span id="Properties_and_methods"></span><span id="properties_and_methods"></span><span id="PROPERTIES_AND_METHODS"></span>Properties and methods
</dt> <dd>

Like any OLE object, a control can provide much of its functionality through a set of incoming interfaces with properties and methods. The container can supply additional ambient properties, and it can support extending the control's properties through aggregation. These features rest on OLE automation, property pages, connectable objects, and ActiveX control technologies.

</dd> <dt>

<span id="Events"></span><span id="events"></span><span id="EVENTS"></span>Events
</dt> <dd>

In addition to providing properties and methods, an ActiveX control can also provide outgoing interfaces to notify its client of events. The client must support handling of these events. These features use OLE automation and connectable objects.

</dd> <dt>

<span id="Visual_representation"></span><span id="visual_representation"></span><span id="VISUAL_REPRESENTATION"></span>Visual representation
</dt> <dd>

A control can support positioning and displaying itself within its container. The container positions the control and determines its size. These features use compound document technology, including OLE drag and drop technology.

</dd> <dt>

<span id="Keyboard_handling"></span><span id="keyboard_handling"></span><span id="KEYBOARD_HANDLING"></span>Keyboard handling
</dt> <dd>

A control can respond to keyboard accelerators so the end-user can initiate actions performed by the control. The container manages keyboard activity for all its embedded controls. These features use control and compound document technologies.

</dd> <dt>

<span id="Persistence"></span><span id="persistence"></span><span id="PERSISTENCE"></span>Persistence
</dt> <dd>

A control can save its state. The client manages the persistence of its embedded controls. These features use structured storage and object persistence technologies.

</dd> <dt>

<span id="Registration_and_licensing"></span><span id="registration_and_licensing"></span><span id="REGISTRATION_AND_LICENSING"></span>Registration and licensing
</dt> <dd>

A control typically supports self-registration and creates a set of registry entries when it is instantiated. A control can also be licensed to help prevent unauthorized use.

</dd> </dl>

Most of these features involve both the control and its client container.

## Related topics

<dl> <dt>

[ActiveX Controls](activex-controls.md)
</dt> </dl>

 

 




