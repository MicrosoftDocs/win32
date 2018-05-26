---
Description: Creating BYOT Objects
ms.assetid: 16b68ce2-46b2-4e35-bf92-f132dcb354e3
title: Creating BYOT Objects
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Creating BYOT Objects

A new BYOT object creates objects with manual transactions. The two interfaces, [**ICreateWithTransactionEx**](/windows/win32/ComSvcs/nn-comsvcs-icreatewithtransactionex?branch=master) and [**ICreateWithTipTransactionEx**](/windows/win32/ComSvcs/nn-comsvcs-icreatewithtiptransactionex?branch=master), have a single method, **CreateInstance**, which take an **ITransaction** interface pointer and TIP URL, respectively. [**CreateInstance**](/windows/win32/ComSvcs/nf-comsvcs-icreatewithtransactionex-createinstance?branch=master) returns an interface pointer to the newly created object, which is enlisted within the specified transaction.

When an object with a manual transaction is released, COM+ does not attempt to commit the transaction. The transaction is controlled explicitly by the external transaction manager that dispensed the transaction under which this object had been created.

> [!Note]  
> The Byot.ByotServerEx object needs to be imported into a COM+ application.

 

 

 



