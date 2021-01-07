---
description: People Near Me Stores
ms.assetid: 3f2aa9bd-49ca-4fa6-b718-7cbeeef857c7
title: People Near Me Stores
ms.topic: article
ms.date: 05/31/2018
---

# People Near Me Stores

Applications capable of [People Near Me](about-people-near-me.md) (PNM) can use the following data stores:

### Windows Address Book

The Windows Address Book stores information on contacts and their digital certificates. The '**Me**' contact, representing the currently logged in user, is also stored in the Windows Address Book.

### Certificate Store

The Certificate Store contains the self-signed certificate for the '**Me**' contact.

### Application Store

An application installer registers an application with PNM during the installation process. These are the objects that can be searched for by other users when attempting to connect to a user with a common application, such as a computer game. For each application, the Application Store contains the name of the application, a globally unique identifier (GUID), a scope of the application, a description, and a path to the executable file of the program. The scope of an application can be set to None (not advertised), People Near Me (advertised on the local subnet), Contacts (advertised just for contacts), or All (advertised on the local subnet and for contacts). The Application Store is located in the Windows Vista registry.

 

 



