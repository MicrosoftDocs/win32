---
description: The user can start a service with the Services control panel utility. The user can specify arguments for the service in the Start parameters field. A service control program can start a service and specify its arguments with the StartService function.
ms.assetid: 72f51b38-d62c-4400-a38d-b9a0e90e9db4
title: Starting Services on Demand
ms.topic: article
ms.date: 05/31/2018
---

# Starting Services on Demand

The user can start a service with the Services control panel utility. The user can specify arguments for the service in the **Start parameters** field. A service control program can start a service and specify its arguments with the [**StartService**](/windows/desktop/api/Winsvc/nf-winsvc-startservicea) function.

When the service is started, the SCM performs the following steps:

-   Retrieve the account information stored in the database.
-   Log on the service account.
-   Load the user profile.
-   Create the service in the suspended state.
-   Assign the logon token to the process.
-   Allow the process to execute.

 

 



