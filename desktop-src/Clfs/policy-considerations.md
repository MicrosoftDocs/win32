---
Description: When working with CLFS Management policies, be aware of the following
ms.assetid: f2cc1da5-b957-4cfd-8fc4-b68a33079073
title: Policy Considerations
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Policy Considerations

When working with CLFS Management policies, be aware of the following:

-   There are default policies that are in effect until they are overwritten by client policies.
-   Client policies are not persistent; they are in effect until they are overwritten or until all log handles have been closed. When all log handles are closed, the log reverts to the default policies.
-   All clients are subject to the same policies, even if they are using other log streams.
-   A policy does not take effect immediately after it is installed; a specific log action triggers the change, such as adding a record.
-   You can only install one policy at a time.
-   Installing a policy overwrites the defaults.
-   You can only set one group of policies per physical log.
-   If more than one client updates a policy, the updates can overwrite each other and cause unexpected results. Therefore, managed clients must have consistent policies if those clients are going to share a physical log.
-   You can reset a policy to its default state by calling [**RemoveLogPolicy**](/windows/win32/Clfsmgmtw32/nf-clfsmgmtw32-removelogpolicy?branch=master).

 

 



