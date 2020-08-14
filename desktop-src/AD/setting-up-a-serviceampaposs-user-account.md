---
title: Setting up a Service's User Account
description: Your service installer can suggest a default logon account for a service instance and allow the administrator to select the default account or specify a different one.
ms.assetid: 37285c23-8922-4da5-9f0b-922ea5e5794e
ms.tgt_platform: multiple
keywords:
- Setting up a Service's User Account AD
ms.topic: article
ms.date: 05/31/2018
---

# Setting up a Service's User Account

Your service installer can suggest a default logon account for a service instance and allow the administrator to select the default account or specify a different one. If the administrator selects a user account, rather than the LocalSystem account, the account must exist before you call the [**CreateService**](/windows/desktop/api/winsvc/nf-winsvc-createservicea) function to install an instance of the service on a host server. For more information and a code example that can be used to create a new domain user object in Active Directory Domain Services, see [Creating a User](creating-a-user.md).

Ideally, each instance of a service, whether a host-based or replicable service, should have its own domain user account. Using separate accounts for each service instance is more secure than having multiple instances share the same account. Also, using separate accounts makes it possible to audit the activities of each service instance.

When your installer suggests a default logon account, it should specify the name of a new account to be created for the new service instance. The account name could be composed from the same elements used to compose a service principal name, such as the service class, host computer, and service name. For more information, see [Service Principal Names](service-principal-names.md). Typically, you create the account in the Users container on the domain of the host computer.

You must generate a password for each account. For more information about how to write a tool that automates the task of updating service account passwords, see [Changing the Password on a Service's User Account](changing-the-password-on-a-serviceampaposs-user-account.md).

 

 