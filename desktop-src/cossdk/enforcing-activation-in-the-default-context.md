---
description: A configured COM component is usually activated in its own context; that is, COM+ references the components catalog information to provide any configured services.
ms.assetid: 09dc7165-22b1-4eca-9591-d83e85556f3f
title: Enforcing Activation in the Default Context
ms.topic: article
ms.date: 05/31/2018
---

# Enforcing Activation in the Default Context

A configured COM component is usually activated in its own context; that is, COM+ references the component's catalog information to provide any configured services. However, you can choose to activate a configured component in the default context. A base COM component—a registered component that has no COM+ catalog information—is usually activated in the default context.

Activating a COM component in the default context provides three major performance benefits, as follows:

-   You save system resources by limiting the number of contexts that are created.
-   You increase performance by limiting the number of cross-context calls. Because calls across contexts require marshaling, it is much faster for a COM object activated in the default context to make calls to other objects in the default context. The performance in this case (of calls within the same context) is similar to that of calling a subroutine.
-   You can import older COM applications into COM+ and run them without a problem. For example, you may have several older COM applications implemented under the assumption that it was allowable to pass object references within an apartment without marshaling the references. These COM applications do not work when imported into COM+ because the object references are passed across context boundaries. However, you can make this type of COM application run when imported if you use the Component Services administrative tool to mark all the classes in the application as **Must be activated in the default context**.

The major disadvantage to activating a configured component in the default context is that COM+ does not provide any of the component's configured services. There is a trade-off between enhanced performance and the ability to use COM+ services.

For example, assume that a COM component does not require any COM+ services (such as [Transactions](com--transactions.md), [Just-in-Time Activation](com--just-in-time-activation.md), [Events](com--events.md), [Queued Components](com--queued-components.md), [Synchronization](com--synchronization.md), or [Object Pooling](com--object-pooling.md)) and that the component makes a number of calls to other COM components that may be activated in the default context. In this case, it would be a good idea to activate the calling component in the default context.

If the COM component requires COM+ services, it cannot be marked as **Must be activated in the default context**. In addition, there is no real performance gain if a COM object activated in the default context makes a number of calls to objects in other contexts. (For more detail, see [Contexts](com--contexts.md).)

**To enforce activation in the default context**

1.  In the details pane of the Component Services administrative tool, right-click the component (located within the **Components** folder of any selected COM+ application) that you want to activate in the default context and then click **Properties**.

2.  In the component properties dialog box, click the **Activation** tab.

3.  Select the **Must be activated in the default context**check box.

4.  Click **OK**.

> [!Note]  
> When you run a configured component in the default context, COM+ does not activate any of the configured services for that component. These services are available again when you uncheck the **Must be activated in the default context**check box and subsequently run the configured component in its own context.

 

## Related topics

<dl> <dt>

[COM+ Just-in-Time Activation Concepts](com--just-in-time-activation-concepts.md)
</dt> <dt>

[Enforcing Activation in the Caller's Context](enforcing-activation-in-the-caller-s-context.md)
</dt> </dl>

 

 



