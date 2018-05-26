---
Description: Query the smart card database. They can provide a list of smart cards supplied by a specific user, the interfaces and primary service provider of a specific card, the reader groups defined for the system, and the readers within a set of reader groups.
ms.assetid: a30cbb99-522c-4752-bfcd-75be608785f1
title: Smart Card Database Query Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Smart Card Database Query Functions

The following functions query the [*smart card database*](security.s_gly#-security-smart-card-database-gly). They can provide a list of smart cards supplied by a specific user, the interfaces and [*primary service provider*](security.p_gly#-security-primary-service-provider-gly) of a specific card, the [*reader groups*](security.r_gly#-security-reader-group-gly) defined for the system, and the [*readers*](security.r_gly#-security-reader-gly) within a set of reader groups.

When you use these functions, you can query the complete smart card database, or you can narrow the search by setting the [*resource manager context*](security.r_gly#-security-resource-manager-context-gly). The resource manager context is set by calling [**SCardEstablishContext**](/windows/win32/Winscard/nf-winscard-scardestablishcontext?branch=master) before calling a query function.

> [!Note]  
> Without a specified context, some information may still be inaccessible due to security restrictions.

 



| Topic                                                  | Description                                                                                                                                                                          |
|--------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SCardGetProviderId**](/windows/win32/Winscard/nf-winscard-scardgetproviderida?branch=master)       | Retrieve the identifier (GUID) of the [*primary service provider*](security.p_gly#-security-primary-service-provider-gly) for the given card. |
| [**SCardListCards**](/windows/win32/Winscard/nf-winscard-scardlistcardsa?branch=master)               | Retrieve a list of cards previously introduced to the system by a specific user.                                                                                                     |
| [**SCardListInterfaces**](/windows/win32/Winscard/nf-winscard-scardlistinterfacesa?branch=master)     | Retrieve the identifiers (GUIDs) of the interfaces supplied by a given card.                                                                                                         |
| [**SCardListReaderGroups**](/windows/win32/Winscard/nf-winscard-scardlistreadergroupsa?branch=master) | Retrieve a list of reader groups that have previously been introduced to the system.                                                                                                 |
| [**SCardListReaders**](/windows/win32/Winscard/nf-winscard-scardlistreadersa?branch=master)           | Retrieve the list of readers within a set of named reader groups.                                                                                                                    |



 

 

 



