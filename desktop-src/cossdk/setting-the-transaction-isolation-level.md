---
description: You can manually set the transaction isolation level of components by using the Component Services administrative tool, or you can programmatically configure the transaction isolation level for a component by using the COM+ administration interfaces.
ms.assetid: 3ef5b805-334d-4803-be67-00c9e35cdcc6
title: Setting the Transaction Isolation Level
ms.topic: article
ms.date: 05/31/2018
---

# Setting the Transaction Isolation Level

You can manually set the transaction isolation level of components by using the Component Services administrative tool, or you can programmatically configure the transaction isolation level for a component by using the [COM+ administration interfaces](com--administration-interfaces.md).

For more on transaction isolation levels, see [Configuring Transaction Isolation Levels](configuring-transaction-isolation-levels.md).

**To set the transaction isolation level by using the Component Services administrative tool**

1.  In the console tree, right-click the component you want to configure and then click **Properties**.

2.  In the component properties dialog box, click the **Transactions** tab.

3.  Under **Transaction Isolation Level**, select the value you want from the drop-down box. The default value for all components is **Serialized**.

    > [!Note]  
    > If either **Disabled** or **Not Supported** is selected under **Transaction support**, you cannot set the transaction isolation level.

     

4.  Click **OK**.

You must repeat this procedure for each component.

## Related topics

<dl> <dt>

[Configuring Transaction Isolation Levels](configuring-transaction-isolation-levels.md)
</dt> </dl>

 

 



