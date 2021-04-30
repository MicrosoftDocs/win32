---
description: The just-in-time (JIT) activation service enables COM+ to deactivate an object while a client still holds an active reference to that object.
ms.assetid: dbc7b257-8506-42c8-8a78-3474c6d4f4b6
title: COM+ Just-in-Time Activation Concepts
ms.topic: article
ms.date: 05/31/2018
---

# COM+ Just-in-Time Activation Concepts

The just-in-time (JIT) activation service enables COM+ to deactivate an object while a client still holds an active reference to that object. The next time the client calls a method on the object, which the client believes to be still active, the COM+ JIT activation service reactivates the object transparently to the client, just in time.

The main advantage of using COM + JIT activation is that you can enable clients to hold references to objects for as long as they need them, without necessarily tying up valuable server resources such as memory. Other important benefits include the following:

-   Using the COM+ JIT activation service greatly simplifies the programming model for the client because the client doesn't have to think about how it uses expensive server objects and server resources. Without JIT activation, clients can incur a significant penalty when they frequently need to call and release objects.
    > [!Note]  
    > You can refine this performance benefit further by using the [COM+ Object Pooling](com--object-pooling.md) service. By pooling JIT-activated objects, you can greatly speed object reactivation for clients while reusing whatever resources they might be holding, giving you more precise control over how much memory is used by a given object on the server. For more detail, see [Object Pooling and COM+ JIT Activation](object-pooling-and-com--jit-activation.md).

     

-   With distributed applications, an expensive network round-trip is required for the creation of every object, and the farther the client is from the server, the greater the costs of activating and marshaling the server object, opening the channel, and setting up the proxy and stub. By using the COM+ JIT activation service, you can minimize the frequency of object creation to significantly improve the performance of your application.
-   When you use COM+ JIT activation to activate those objects to which clients hold long-lived references but which they aren't necessarily using all the time, server memory is not always tied up keeping those objects alive. This can significantly increase the scalability of your application. The only performance hit that clients see is the time it takes COM+ to reactivate the object, usually just marginally more time than it takes to allocate memory for the object and substantially less than the network round-trip for remote object creation.

## Enabling COM+ JIT Activation

You can enable the COM+ JIT activation service for a component by using either the Component Services administrative tool or the Administrative functions. For details about how to do this, see [Enabling JIT Activation for a Component](enabling-jit-activation-for-a-component.md).

COM+ JIT activation can interact with other COM+ services, such as the following:

-   When your component requires transactions, JIT activation is automatically enabled for it. For greater detail, see [Transactions and COM+ JIT Activation](transactions-and-com--jit-activation.md).
-   When your component is enabled for JIT activation, synchronization is automatically set to required. This means that if two clients simultaneously call a JIT-activated component and a method call for one of them returns, causing the object to be deactivated, the other is not left stranded.

## How Deactivation Is Triggered

COM+ deactivates an object based on the status of the doneness bit on the object context. Your object can use this bit to signal whether it is done—that is, ready to be deactivated—during a given method call. For more information, see [Setting the Done Bit](setting-the-done-bit.md).

## Using the Auto-Done Property

Using the Component Services administrative tool, you can configure a method such that the object is automatically deactivated on method return. (See [Enabling Auto-Done for a Method](enabling-auto-done-for-a-method.md) for instructions about how to set this property.) By selecting this option, you can eliminate the repetitive method calls for voting in transactions. Because the default setting for the consistency bit is True, if you have changed the done bit to True as well and you take no action to change these settings, [**IObjectContext::SetComplete**](/windows/desktop/api/ComSvcs/nf-comsvcs-iobjectcontext-setcomplete) is called automatically after the method returns.

However, there is one caveat to this behavior: COM+ will examine the HRESULT that the method returns. If that HRESULT indicates failure, the consistency bit is set to False and the result is the same as if you had called [**IObjectContext::SetAbort**](/windows/desktop/api/ComSvcs/nf-comsvcs-iobjectcontext-setabort).

To summarize, if you select auto-done for a method and don't take any action to set any bits, and if an HRESULT(hr) is returned, the following applies:

-   If SUCCEEDS(hr), it is as though you called [**SetComplete**](/windows/desktop/api/ComSvcs/nf-comsvcs-iobjectcontext-setcomplete).
-   If FAILED(hr), it is as though you called [**SetAbort**](/windows/desktop/api/ComSvcs/nf-comsvcs-iobjectcontext-setabort).

## Using IObjectControl to Manage Object Activation and Deactivation

You can implement the [**IObjectControl**](/windows/desktop/api/ComSvcs/nn-comsvcs-iobjectcontrol) interface so that the COM+ runtime automatically manages deactivation and reactivation for your objects. When an object implements this interface, COM+ calls [**IObjectControl::Deactivate**](/windows/desktop/api/ComSvcs/nf-comsvcs-iobjectcontrol-deactivate) when it deactivates the object and [**IObjectControl::Activate**](/windows/desktop/api/ComSvcs/nf-comsvcs-iobjectcontrol-activate) when it reactivates it. These methods enable automatic context initialization on object activation and cleanup of state on deactivation.

If you are pooling objects that use COM+ JIT activation, it is highly recommended that you implement [**IObjectControl**](/windows/desktop/api/ComSvcs/nn-comsvcs-iobjectcontrol). For more detail, see [Object Pooling and COM+ JIT Activation](object-pooling-and-com--jit-activation.md).

## Statelessness and JIT Activation

Transactional objects are necessarily stateless because you cannot share state across a transaction boundary. Therefore, you would use JIT activation only when your object holds no state that would be lost on deactivation; otherwise, you violate the isolation of the transactions. Due to the natural use patterns of transactional objects—they do some unit of work and release the object when the transaction commits or aborts—JIT activation and automatic transactions are closely related. Configuring an object to require transactions enables COM+ JIT activation automatically.

## Related topics

<dl> <dt>

[COM+ Just-in-Time Activation Tasks](com--just-in-time-activation-tasks.md)
</dt> <dt>

[Object Pooling and COM+ JIT Activation](object-pooling-and-com--jit-activation.md)
</dt> <dt>

[Transactions and COM+ JIT Activation](transactions-and-com--jit-activation.md)
</dt> </dl>

 

 



