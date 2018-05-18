---
Description: Setting the Done Bit
ms.assetid: 'badd3b5a-ce6f-4be7-9dd8-a3b17344b185'
title: Setting the Done Bit
---

# Setting the Done Bit

COM+ will deactivate a JIT-activated object based on the status of a context property, the done bit, as follows:

-   When the done bit is set to True, COM+ deactivates the object when the current method call returns.
-   When the done bit is set to False, the object remains active when the current method call returns.

By default, the done bit is set to False when an object is created and its context initialized. (Any JIT-activated object is created in its own context so that it has its own done bit to set.) However, you can change this default setting on a per-method basis by using the auto-done property. You can set the done bit in the following ways:

-   Using [**IContextState**](icontextstate.md)
-   Using [**IObjectContext**](iobjectcontext.md)
-   Using the auto-done property

## Using IContextState

You can use [**IContextState::SetDeactivateOnReturn**](icontextstate-setdeactivateonreturn.md) to set the done bit to True or False.

You can use [**IContextState::GetDeactivateOnReturn**](icontextstate-getdeactivateonreturn.md) to get the current status of the done bit from the object context.

## Using IObjectContext

You can use the following methods on [**IObjectContext**](iobjectcontext.md) to set the done bit while simultaneously setting the consistent bit used for voting in transactions:

-   [**SetComplete**](iobjectcontext-setcomplete.md) signals both that you are done and that you vote to commit the current transaction. It sets both the done bit and the consistent bit to True.
-   [**SetAbort**](iobjectcontext-setabort.md) signals that you are done and dooms the current transaction. It sets the done bit to True and the consistent bit to False.
-   [**EnableCommit**](iobjectcontext-enablecommit.md) signals that you are not done but that you vote to commit the transaction. It sets the done bit to False and the consistent bit to True.
-   [**DisableCommit**](iobjectcontext-disablecommit.md) signals that you are not done and that you vote not to commit the transaction at this time, usually because the state is inconsistent. It sets both the done bit and the consistent bit to False.

## Related topics

<dl> <dt>

[COM+ Just-in-Time Activation Concepts](com--just-in-time-activation-concepts.md)
</dt> <dt>

[Enabling JIT Activation for a Component](enabling-jit-activation-for-a-component.md)
</dt> <dt>

[Object Pooling and COM+ JIT Activation](object-pooling-and-com--jit-activation.md)
</dt> <dt>

[Transactions and COM+ JIT Activation](transactions-and-com--jit-activation.md)
</dt> </dl>

 

 



