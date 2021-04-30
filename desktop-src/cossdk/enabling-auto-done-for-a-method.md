---
description: You can enable the auto-done feature for any method exposed by a component for which COM+ JIT activation is enabled. If JIT activation is disabled, auto-done is unavailable.
ms.assetid: d699b85c-441f-4ea6-8d03-d1fa9a8a357f
title: Enabling Auto-Done for a Method
ms.topic: article
ms.date: 05/31/2018
---

# Enabling Auto-Done for a Method

You can enable the auto-done feature for any method exposed by a component for which COM+ JIT activation is enabled. If JIT activation is disabled, auto-done is unavailable.

You should enable auto-done only for a method that has intentionally been written to take advantage of it because this feature can potentially change the expected behavior of the method.

When you enable auto-done, you are changing the default behavior of both JIT activation and automatic transactions for that method. You may want to use this feature because it can remove the necessity to explicitly declare consistency and doneness. This can instead be done by simply returning an HRESULT when auto-done is enabled. Essentially, when you enable auto-done, you are instructing COM+ to do the following:

-   Set the done bit to True by default on the context in which the object runs whenever this method is called.
-   Inspect the HRESULT returned by the method; if it indicates SUCCESS or FAILURE, set the consistency bit accordingly. This can result in an automatic call to [**IObjectContext::SetComplete**](/windows/desktop/api/ComSvcs/nf-comsvcs-iobjectcontext-setcomplete) or [**IObjectContext::SetAbort**](/windows/desktop/api/ComSvcs/nf-comsvcs-iobjectcontext-setabort), depending also on what the method does internally.

**To enable auto-done for a method**

1.  In the details pane of the Component Services administrative tool, right-click the method that you want to configure and then click **Properties**.

2.  In the method properties dialog box, click the **General** tab.

3.  To enable auto-done, select the **Automatically deactivate this object when this method returns** check box. If the check box is unavailable, you must first enable JIT Activation for the component. (See[Enabling JIT Activation for a Component](enabling-jit-activation-for-a-component.md) for detailed instructions.)

4.  Click **OK**.

## Related topics

<dl> <dt>

[COM+ Just-in-Time Activation Concepts](com--just-in-time-activation-concepts.md)
</dt> <dt>

[Enabling JIT Activation for a Component](enabling-jit-activation-for-a-component.md)
</dt> <dt>

[Setting the Done Bit](setting-the-done-bit.md)
</dt> </dl>

 

 



