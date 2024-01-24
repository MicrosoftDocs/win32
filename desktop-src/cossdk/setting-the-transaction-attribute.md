---
description: You can set transaction attributes manually by using the Component Services administrative tool, or you can add programmatic support for transactions when you write your component.
ms.assetid: b0d701c7-47ef-4034-873f-dd4428efb4c7
title: Setting the Transaction Attribute
ms.topic: article
ms.date: 05/31/2018
---

# Setting the Transaction Attribute

You can set transaction attributes manually by using the Component Services administrative tool, or you can add programmatic support for transactions when you write your component.

For more on transaction attribute values, see [Configuring Transactions](configuring-transactions.md).

**To set the attribute value by using the Component Services administrative tool**

1.  In the console tree, right-click the component you want to configure and then click **Properties**.

2.  In the component properties dialog box, click the **Transactions** tab.

3.  Under **Transaction support**, select the option for the value you want. The default value for all components is **Not Supported**.

4.  Click **OK**.

You must repeat this procedure for each component.

## To set the attribute value programmatically

Programmers using Microsoft Visual Basic can set the transaction attribute with **MTSTransactionMode**, a class module property for ActiveX DLL projects. Visual Basic maps your selection to the equivalent COM+ transaction attribute value and publishes the value in your component's type library.

The following table maps each **MTSTransactionMode** constant value to its equivalent COM+ transaction value.



| MTSTransactionMode constant         | COM+ transaction value             |
|-------------------------------------|------------------------------------|
| NotAnMTSObject (default)<br/> | Disabled<br/>                |
| NoTransactions<br/>           | Not Supported (default)<br/> |
| RequiresTransaction <br/>     | Required<br/>                |
| UsesTransaction <br/>         | Supported<br/>               |
| RequiresNewTransaction <br/>  | Requires New<br/>            |



 

The **MTSTransactionMode** property can also be accessed programmatically by using the COM+ Administration Library API.

 

 




