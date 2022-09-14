---
title: Containment/Delegation
description: The most common mechanism for object reuse in COM is containment/delegation.
ms.assetid: 56396c11-889a-4f28-8fa7-9e48c805c501
ms.topic: article
ms.date: 05/31/2018
---

# Containment/Delegation

The most common mechanism for object reuse in COM is *containment/delegation*. This type of reuse is a familiar concept found in most object-oriented languages and systems. The outer object, which needs to make use of the inner object, acts as an object client to the inner object. The outer object "contains" the inner object, and when the outer object requires the services of the inner object, the outer object explicitly delegates implementation to the inner object's methods. That is, the outer object uses the inner object's services to implement itself.

It is not necessary for the outer and inner objects to support the same interfaces, although it certainly is reasonable to contain an object that implements an interface that the outer object does not and implement the methods of the outer object simply as calls to the corresponding methods in the inner object. When the complexity of the outer and inner objects differs greatly, however, the outer object may implement some of the methods of its interfaces by delegating calls to interface methods implemented in the inner object.

It is simple to implement containment for an outer object. The outer object creates the inner objects it needs to use as any other client would. This is nothing new—the process is like a C++ object that itself contains a C++ string object that it uses to perform certain string functions, even if the outer object is not considered a string object in its own right. Then, using its pointer to the inner object, a call to a method in the outer object generates a call to an inner object method.

## Related topics

<dl> <dt>

[Aggregation](aggregation.md)
</dt> </dl>

 

 




