---
description: Enabling JIT Activation for a Component
ms.assetid: ccf7c98b-8b1a-431d-b417-83f79734f691
title: Enabling JIT Activation for a Component
ms.topic: article
ms.date: 05/31/2018
---

# Enabling JIT Activation for a Component

You should configure a component to be JIT activated only when it is correctly written to support the COM+ Just-in-Time (JIT) Activation service. If a component is deactivated between method calls, it will lose any associated state. Given the default behavior of JIT Activation, this is unlikely to occur when you don't expect it to, but you should be aware of a component's requirements prior to changing its configuration and of the expectations of clients that will be calling the component.

> [!Note]  
> If a component is configured to require transactions, the COM+ JIT Activation service is enabled automatically. You cannot disable it in this case. For more detail, see [Configuring Transactions](configuring-transactions.md).

 

When you enable JIT Activation for a component, its synchronization attribute is set to required for that component. You cannot change the synchronization setting in this case. For more detail, see [Synchronization Dependencies](synchronization-dependencies.md).

**To enable JIT Activation**

1.  In the details pane of the Component Services administrative tool, right-click the component that you want to configure and then click **Properties**.

2.  In the component properties dialog box, click the **Activation** tab.

3.  To enable JIT activation for the component, select the **Enable Just In Time Activation** check box.

4.  Click **OK**.

When you have enabled JIT Activation for a component, you have the option of enabling the auto-done feature for any method exposed by that component. See [Enabling Auto-Done for a Method](enabling-auto-done-for-a-method.md) for more information.

## Related topics

<dl> <dt>

[Enabling Auto-Done for a Method](enabling-auto-done-for-a-method.md)
</dt> <dt>

[Setting the Done Bit](setting-the-done-bit.md)
</dt> </dl>

 

 



