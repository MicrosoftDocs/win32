---
Description: Manage the smart card database, updating the database by using a specified resource manager context.
ms.assetid: a2f457e1-c042-42e7-9071-cf0edd68e27a
title: Smart Card Database Management Functions
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Smart Card Database Management Functions

The following functions manage the [*smart card database*](security.s_gly#-security-smart-card-database-gly), updating the database by using a specified [*resource manager context*](security.r_gly#-security-resource-manager-context-gly).

> [!Note]  
> Database security is maintained by placing access restrictions on the database, rather than by adding security mechanisms to the [*smart card subsystem*](security.s_gly#-security-smart-card-subsystem-gly).

 



| Topic                                                            | Description                                                                                                                                                             |
|------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SCardAddReaderToGroup**](/windows/desktop/api/Winscard/nf-winscard-scardaddreadertogroupa)           | Add a [*reader*](security.r_gly#-security-reader-gly) to a [*reader group*](security.r_gly#-security-reader-group-gly). |
| [**SCardForgetCardType**](/windows/desktop/api/Winscard/nf-winscard-scardforgetcardtypea)               | Remove a smart card from the system.                                                                                                                                    |
| [**SCardForgetReader**](/windows/desktop/api/Winscard/nf-winscard-scardforgetreadera)                   | Remove a reader from the system.                                                                                                                                        |
| [**SCardForgetReaderGroup**](/windows/desktop/api/Winscard/nf-winscard-scardforgetreadergroupa)         | Remove a reader group from the system.                                                                                                                                  |
| [**SCardIntroduceCardType**](/windows/desktop/api/Winscard/nf-winscard-scardintroducecardtypea)         | Introduce a new card to the system.                                                                                                                                     |
| [**SCardIntroduceReader**](/windows/desktop/api/Winscard/nf-winscard-scardintroducereadera)             | Introduce a new reader to the system.                                                                                                                                   |
| [**SCardIntroduceReaderGroup**](/windows/desktop/api/Winscard/nf-winscard-scardintroducereadergroupa)   | Introduce a new reader group to the system.                                                                                                                             |
| [**SCardRemoveReaderFromGroup**](/windows/desktop/api/Winscard/nf-winscard-scardremovereaderfromgroupa) | Remove a reader from a reader group.                                                                                                                                    |



 

 

 



