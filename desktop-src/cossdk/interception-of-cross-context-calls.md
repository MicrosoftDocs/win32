---
description: When an object is activated in a given context, subsequent calls to or from it, within the context, are handled differently than calls across the context boundary.
ms.assetid: 9e234b41-f269-4674-adc4-12018277a14b
title: Interception of Cross-Context Calls
ms.topic: article
ms.date: 05/31/2018
---

# Interception of Cross-Context Calls

When an object is activated in a given context, subsequent calls to or from it, within the context, are handled differently than calls across the context boundary. Calls across the context boundary are handled with lightweight proxies. These proxies handle whatever mediation is required to adjust the run-time environment from one that accommodates the caller to one that accommodates the callee. This process is known as *interception*.

Cross-context call interception is necessary because objects in different contexts have different run-time requirements—this is precisely the reason for contexts. COM+ intercepts any object references that you pass as method parameters and automatically converts them to proxies so that they are usable in the new context.

If you share object references across context boundaries by other means—for example, in global variables—you should always use [**CoMarshalInterface**](/windows/desktop/api/combaseapi/nf-combaseapi-comarshalinterface) and [**CoUnmarshalInterface**](/windows/desktop/api/combaseapi/nf-combaseapi-counmarshalinterface). These functions can translate an object reference into a proxy usable in a different context. Never share a raw object reference across context boundaries.

The behavior of calls across context can have unwanted consequences in the case of objects exposing interfaces that cannot be marshaled. In this circumstance, you are likely to want to insist that the object that cannot be marshaled be activated only in the context of its caller and never in its own context. You can do this by selecting the **Must be activated in caller's context** option on the **Activation** tab of the component **Properties** page. (See [Enforcing Activation in the Caller's Context](enforcing-activation-in-the-caller-s-context.md) for step-by-step instructions.)

## Related topics

<dl> <dt>

[Context activation](context-activation.md)
</dt> </dl>

 

 
