---
description: Enforcing Activation in the Callers Context
ms.assetid: bb228f39-0e04-497a-8404-18f7bc027bea
title: Enforcing Activation in the Callers Context
ms.topic: article
ms.date: 05/31/2018
---

# Enforcing Activation in the Caller's Context

You can control whether an object gets activated in its own context. When you use the Component Services administrative tool to require component activation in the caller's context, the following occurs when COM+ activates an instance of the component in a context:

-   The object is activated in the creator's context if possible.
-   Object activation fails if it requires its own context; CO\_E\_ATTEMPT\_TO\_CREATE\_OUTSIDE\_CLIENT\_CONTEXT is returned.

Whether or not the object requires its own context depends on its configuration relative to the current state of the caller's context properties. For more detail, see [COM+ Contexts](com--contexts.md).

You would want to control activation at that fine a level if some aspect of your object would not function properly if it has its own context. For example, if the component does not support marshaling and it has its own context, any calls to it will fail because cross-context calls are intercepted and a lightweight marshal performed.

**To enforce activation in the caller's context**

1.  In the details pane of the Component Services administrative tool, right-click the component (located within the **Components** folder of any selected COM+ application) for which you are setting activation properties and then click **Properties**.

2.  In the component properties dialog box, click the **Activation** tab.

3.  Select the **Must be activated in the callers context** check box.

4.  Click **OK**.

## Related topics

<dl> <dt>

[COM+ Just-in-Time Activation Concepts](com--just-in-time-activation-concepts.md)
</dt> <dt>

[Enforcing Activation in the Default Context](enforcing-activation-in-the-default-context.md)
</dt> </dl>

 

 



