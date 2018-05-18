---
Description: Creating BYOT Objects
ms.assetid: '16b68ce2-46b2-4e35-bf92-f132dcb354e3'
title: Creating BYOT Objects
---

# Creating BYOT Objects

A new BYOT object creates objects with manual transactions. The two interfaces, [**ICreateWithTransactionEx**](icreatewithtransactionex.md) and [**ICreateWithTipTransactionEx**](icreatewithtiptransactionex.md), have a single method, **CreateInstance**, which take an **ITransaction** interface pointer and TIP URL, respectively. [**CreateInstance**](icreatewithtransactionex-createinstance.md) returns an interface pointer to the newly created object, which is enlisted within the specified transaction.

When an object with a manual transaction is released, COM+ does not attempt to commit the transaction. The transaction is controlled explicitly by the external transaction manager that dispensed the transaction under which this object had been created.

> [!Note]  
> The Byot.ByotServerEx object needs to be imported into a COM+ application.

 

 

 



