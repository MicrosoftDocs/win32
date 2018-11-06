---
Description: Query the smart card database. They can provide a list of smart cards supplied by a specific user, the interfaces and primary service provider of a specific card, the reader groups defined for the system, and the readers within a set of reader groups.
ms.assetid: a30cbb99-522c-4752-bfcd-75be608785f1
title: Smart Card Database Query Functions
ms.topic: article
ms.date: 05/31/2018
---

# Smart Card Database Query Functions

The following functions query the [*smart card database*](https://msdn.microsoft.com/en-us/library/ms721625(v=VS.85).aspx). They can provide a list of smart cards supplied by a specific user, the interfaces and [*primary service provider*](https://msdn.microsoft.com/en-us/library/ms721603(v=VS.85).aspx) of a specific card, the [*reader groups*](https://msdn.microsoft.com/en-us/library/ms721604(v=VS.85).aspx) defined for the system, and the [*readers*](https://msdn.microsoft.com/en-us/library/ms721604(v=VS.85).aspx) within a set of reader groups.

When you use these functions, you can query the complete smart card database, or you can narrow the search by setting the [*resource manager context*](https://msdn.microsoft.com/en-us/library/ms721604(v=VS.85).aspx). The resource manager context is set by calling [**SCardEstablishContext**](/windows/desktop/api/Winscard/nf-winscard-scardestablishcontext) before calling a query function.

> [!Note]  
> Without a specified context, some information may still be inaccessible due to security restrictions.

 



| Topic                                                  | Description                                                                                                                                                                          |
|--------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SCardGetProviderId**](/windows/desktop/api/Winscard/nf-winscard-scardgetproviderida)       | Retrieve the identifier (GUID) of the [*primary service provider*](https://msdn.microsoft.com/en-us/library/ms721603(v=VS.85).aspx) for the given card. |
| [**SCardListCards**](/windows/desktop/api/Winscard/nf-winscard-scardlistcardsa)               | Retrieve a list of cards previously introduced to the system by a specific user.                                                                                                     |
| [**SCardListInterfaces**](/windows/desktop/api/Winscard/nf-winscard-scardlistinterfacesa)     | Retrieve the identifiers (GUIDs) of the interfaces supplied by a given card.                                                                                                         |
| [**SCardListReaderGroups**](/windows/desktop/api/Winscard/nf-winscard-scardlistreadergroupsa) | Retrieve a list of reader groups that have previously been introduced to the system.                                                                                                 |
| [**SCardListReaders**](/windows/desktop/api/Winscard/nf-winscard-scardlistreadersa)           | Retrieve the list of readers within a set of named reader groups.                                                                                                                    |



 

 

 



