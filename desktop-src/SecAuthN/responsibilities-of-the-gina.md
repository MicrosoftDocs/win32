---
description: Lists and explains the responsibilities of the GINA.
ms.assetid: 5cffe4a6-6475-441e-bf81-f3cbcf1fee3f
title: Responsibilities of the GINA
ms.topic: article
ms.date: 05/31/2018
---

# Responsibilities of the GINA

> [!Note]  
> GINA DLLs are ignored in Windows Vista.

 

A [*GINA*](../secgloss/g-gly.md) DLL has the following responsibilities:

-   SAS monitoring

    The GINA is responsible for recognizing a [*secure attention sequence*](../secgloss/s-gly.md) (SAS), monitoring for SAS events, and notifying Winlogon when a SAS has occurred. Note that there can be more than one SAS defined, and the set of defined SASs can change over time. For example, there can be one set of SASs when [*Winlogon*](../secgloss/w-gly.md) is in the logged-off state and another set when it is in the logged-on state.

    Winlogon provides services to assist the GINA in using the CTRL+ALT+DEL SAS.

-   SAS processing

    One reason for making the GINA replaceable is to provide alternative identification and authentication mechanisms. To do this, the GINA must present all user interfaces resulting from the recognition of a SAS. When no user is logged on, the GINA is responsible for presenting identification and authentication options as well as any other permissible options that are not authenticated. When a user is logged on, the GINA is responsible for presenting the relevant options to the user as well as taking whatever actions are deemed appropriate. For example, in a system that includes a [*smart card*](../secgloss/s-gly.md), it may be appropriate to automatically lock the workstation if the user removes the smart card.

-   Shell activation

    When a user logs on, the GINA is responsible for creating one or more initial processes for that user. (In this documentation, it is assumed that these initial processes present an interface to the user. However, the processes can actually be any processes and do not necessarily have to interact with the user.) These processes are referred to as the *user shell* or just the *shell*. As part of shell activation, the GINA must assign the newly logged-on user's token to the processes. Winlogon provides a service to assist the GINA in assigning the token.

 

 
