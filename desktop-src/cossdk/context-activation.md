---
description: In COM+, every COM object is created with an associated context.
ms.assetid: e5602af2-5852-4c34-a792-6742e90b7d41
title: Context Activation
ms.topic: article
ms.date: 05/31/2018
---

# Context Activation

In COM+, every COM object is created with an associated context. This means that either a new context must be created and initialized or an appropriate existing context is used. This process is known as *activation*. In COM+, an object is activated either in its own context or in that of its creator (an object that has requested that the object be activated—for example, by calling [**CoCreateInstance**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstance)).

In some circumstances, such as with [object pooling](com--object-pooling.md), an object is activated without being created from scratch. In this case, a running instance is activated within a context. Over its lifetime, it may be repeatedly activated in different contexts.

The basic mechanism is the same in either case—an object is associated with a context and that context is properly initialized to represent the run-time needs of the object.

## Flowing of Context Properties

When an object is being activated in response to a creation request from another object, COM+ needs to mediate between them to properly activate the downstream object. COM+ has to compare the context of the caller with the configuration of the called component and then decide where to activate the downstream component and how to initialize its context properties.

To discover the component's configuration, COM+ looks it up in the COM+ class registration database, which is optimized for extremely fast run-time lookups. (This is determined by how you configured a component when installing it into a COM+ application.) The component's configuration is then examined against the state of the caller's context properties.

In some cases, the configuration is consistent with the context of the caller and the component can be activated within the caller's context. This can happen only if the caller's context satisfies all the run-time requirements of the new object.

When the downstream component cannot be activated within the caller's context, it is activated in its own context in an appropriate apartment. When this occurs, certain context properties may flow from caller to callee. For example, if the caller is associated with a transaction and the callee supports transactions, the new object gets its own context (to vote in the transaction, it needs to have its own consistent flag) and inherits the caller's transaction ID and activity ID (which reside within the same transaction and synchronization domain).

## Ignored Context Properties

Depending on how a component is configured, some context properties may play no role in determining whether it is activated in the creator's context or its own context. For example, the Transactions Disabled and Synchronization Disabled settings, indicating the presence of a transaction or a synchronization domain, will play no role whatsoever in the component's activation. These properties are fundamentally ignored when context is flowed. Or if a component uses only process-level access checking, its security context property is ignored—the component's security configuration will never play a role in its activation.

## Forcing Activation in the Caller's Context

In some circumstances, you might want an object to be activated only in its caller's context—that is, never activated in its own context. For example, you might want to control the object's behavior when it's called across a context boundary.

You can ensure that an object cannot be activated in its own context by selecting the **Must be activated in callers context** option on the **Activation** tab of the component **Properties** page, using the Component Services administrative tool. (See [Enforcing Activation in the Caller's Context](enforcing-activation-in-the-caller-s-context.md) for step-by-step instructions.) When you select this option, if the object cannot be activated in the caller's context, [**CoCreateInstance**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstance) fails, returning CO\_E\_ATTEMPT\_TO\_CREATE\_OUTSIDE\_CLIENT\_CONTEXT.

## Default Context

Default contexts exist to support unconfigured components—that is, COM components not installed in COM+ applications and not registered in the COM+ class registration database. If unconfigured components have a compatible threading model, they are activated in the caller's context. Otherwise, they are activated in a default context in the appropriate apartment. Each apartment has a default context to support COM objects that do not use COM+ services.

## Hooking Activation

By implementing [**IObjectControl::Activate**](/windows/desktop/api/ComSvcs/nf-comsvcs-iobjectcontrol-activate) and [**IObjectControl::Deactivate**](/windows/desktop/api/ComSvcs/nf-comsvcs-iobjectcontrol-deactivate), you can hook activation and deactivation together to perform special initialization in the new context. These methods are called by COM+ at certain points in an object's lifecycle, when the object is configured to use JIT-activation or object pooling. See [COM+ Just-in-Time Activation](com--just-in-time-activation.md) and [COM+ Object Pooling](com--object-pooling.md) for more detail.

## Related topics

<dl> <dt>

[Interception of Cross-Context Calls](interception-of-cross-context-calls.md)
</dt> </dl>

 

 
