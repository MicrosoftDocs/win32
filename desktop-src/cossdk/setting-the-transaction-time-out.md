---
description: You can manually set the time-out for transactions by using the Component Services administrative tool, or you can programmatically configure the time-out by using the COM+ administration interfaces.
ms.assetid: f7a35bdf-ea6d-40ea-b3c0-c2a3ae2276c4
title: Setting the Transaction Time-Out
ms.topic: article
ms.date: 05/31/2018
---

# Setting the Transaction Time-Out

You can manually set the time-out for transactions by using the Component Services administrative tool, or you can programmatically configure the time-out by using the [COM+ administration interfaces](com--administration-interfaces.md). The time-out can be configured at the local computer level and also for individual components.

**To set the transaction time-out for the local computer by using the Component Services administrative tool**

1.  In the console tree, right-click the local computer you want to configure and then click **Properties**.

2.  In the computer properties dialog box, click the **Options** tab.

3.  Under **Transaction Timeout**, enter the transaction time-out in seconds. The default time-out is 60 seconds.

4.  Click **OK**.

**To set the transaction time-out for a component by using the Component Services administrative tool**

1.  In the console tree, right-click the component you want to configure and then click **Properties**.

2.  In the component properties dialog box, click the **Transactions** tab.

3.  Check the box labeled **Override global transaction timeout value**.

    > [!Note]  
    > You cannot check the box to override the global transaction time-out value if the **Transaction support** is set to **Disabled**, **Not Supported**, or **Supported**.

     

4.  Under **Transaction Timeout**, enter the transaction time-out in seconds. The default time-out is 0 seconds, which means that the component will never cause the transaction to time out.

5.  Click **OK**.

## Related topics

<dl> <dt>

[Managing Automatic Transactions in COM+](managing-automatic-transactions-in-com-.md)
</dt> </dl>

 

 



