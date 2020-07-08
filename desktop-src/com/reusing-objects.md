---
title: Reusing Objects
description: Reusing Objects
ms.assetid: 07055fea-bdfe-4c7a-be07-2edcbf609dd9
ms.topic: article
ms.date: 05/31/2018
---

# Reusing Objects

An important goal of any object model is to enable object authors to reuse and extend objects provided by others as pieces of their own implementations. One way to do this in Microsoft Visual C++ and other languages is by using *implementation inheritance*, which allows an object to inherit ("subclass") some of its functions from another object while overriding other functions.

The problem for systemwide object interaction using traditional implementation inheritance is that the contract (the interface) between objects in an implementation hierarchy is not clearly defined. In fact, it is implicit and ambiguous. When the parent or child object changes its implementation, the behavior of related components might become undefined or unstably implemented. In any single application, where the implementation can be managed by a single engineering team that updates all of the components at the same time, this is not always a major concern. In an environment where the components of one team are built through black-box reuse of other components built by other teams, this type of instability jeopardizes reuse. Additionally, implementation inheritance usually works only within process boundaries. This makes traditional implementation inheritance impractical for large, evolving systems composed of software components built by many engineering teams.

The key to building reusable components is to be able to treat the object as an opaque box. This means that the piece of code attempting to reuse another object knows nothing, and needs to know nothing, about the internal structure or implementation of the component being used. In other words, the code attempting to reuse a component depends on the behavior of the object and not its exact implementation.

To achieve black-box reusability, COM adopts other established reusability mechanisms such as *containment/delegation* and *aggregation*.

> [!NOTE]  
> For convenience, the object being reused is called the *inner object* and the object making use of that inner object is the *outer object*.

 

It is important to remember in both these mechanisms how the outer object appears to its clients. As far as the clients are concerned, both objects implement any interfaces to which the client can get a pointer. The client treats the outer object as an opaque box and therefore does not care, nor does it need to care, about the internal structure of the outer objectâ€”the client cares only about behavior.

For more information, see the following topics:

-   [Containment/Delegation](containment-delegation.md)
-   [Aggregation](aggregation.md)

 

 




