---
description: Each service executes in the security context of a user account.
ms.assetid: a0e48918-6957-4288-a188-d65198b38c16
title: Service User Accounts
ms.topic: article
ms.date: 05/31/2018
---

# Service User Accounts

Each service executes in the security context of a user account. The user name and password of an account are specified by the [**CreateService**](/windows/desktop/api/Winsvc/nf-winsvc-createservicea) function at the time the service is installed. The user name and password can be changed by using the [**ChangeServiceConfig**](/windows/desktop/api/Winsvc/nf-winsvc-changeserviceconfiga) function. You can use the [**QueryServiceConfig**](/windows/desktop/api/Winsvc/nf-winsvc-queryserviceconfiga) function to get the user name (but not the password) associated with a service object. The service control manager (SCM) automatically loads the user profile.

When starting a service, the SCM logs on to the account associated with the service. If the log on is successful, the system produces an access token and attaches it to the new service process. This token identifies the service process in all subsequent interactions with securable objects (objects that have a security descriptor associated with them). For example, if the service tries to open a handle to a pipe, the system compares the service's access token to the pipe's security descriptor before granting access.

The SCM does not maintain the passwords of service user accounts. If a password is expired, the logon fails and the service fails to start. The system administrator who assigns accounts to services can create accounts with passwords that never expire. The administrator can also manage accounts with passwords that expire by using a [service configuration program](service-configuration-programs.md) to periodically change the passwords.

If a service needs to recognize another service before sharing its information, the second service can either use the same account as the first service, or it can run in an account belonging to an alias that is recognized by the first service. Services that need to run in a distributed manner across the network should run in domain-wide accounts.

You can specify one of the following special accounts instead of specifying a user account for the service:

-   [LocalService](localservice-account.md)
-   [NetworkService](networkservice-account.md)
-   [LocalSystem](localsystem-account.md)

 

 



