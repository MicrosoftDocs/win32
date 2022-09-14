---
description: Creating BYOT Objects
ms.assetid: 16b68ce2-46b2-4e35-bf92-f132dcb354e3
title: Creating BYOT Objects
ms.topic: article
ms.date: 05/31/2018
---

# Creating BYOT Objects

A new BYOT object creates objects with manual transactions. The two interfaces, [**ICreateWithTransactionEx**](/windows/desktop/api/ComSvcs/nn-comsvcs-icreatewithtransactionex) and [**ICreateWithTipTransactionEx**](/windows/desktop/api/ComSvcs/nn-comsvcs-icreatewithtiptransactionex), have a single method, **CreateInstance**, which take an **ITransaction** interface pointer and TIP URL, respectively. [**CreateInstance**](/windows/desktop/api/ComSvcs/nf-comsvcs-icreatewithtransactionex-createinstance) returns an interface pointer to the newly created object, which is enlisted within the specified transaction.

When an object with a manual transaction is released, COM+ does not attempt to commit the transaction. The transaction is controlled explicitly by the external transaction manager that dispensed the transaction under which this object had been created.

> [!Note]  
> The Byot.ByotServerEx object needs to be imported into a COM+ application.

 

 

 



