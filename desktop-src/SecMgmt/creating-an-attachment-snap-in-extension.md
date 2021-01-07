---
description: An attachment snap-in extension provides an interface that users can use to change service-specific configuration settings.
ms.assetid: 6f2dc372-dee4-4793-b943-395c0587ed5e
title: Creating an Attachment Snap-in Extension
ms.topic: article
ms.date: 05/31/2018
---

# Creating an Attachment Snap-in Extension

An attachment snap-in extension provides an interface that users can use to change service-specific configuration settings. The attachment snap-in extension must fulfill the MMC requirements to be a valid snap-in extension. For more information on those requirements, see the [Microsoft Management Console](/previous-versions/windows/desktop/mmc/microsoft-management-console-start-page) documentation.

In addition to the interfaces required by MMC, an attachment snap-in extension must implement the COM interface [**ISceSvcAttachmentPersistInfo**](/windows/desktop/api/Scesvc/nn-scesvc-iscesvcattachmentpersistinfo). The Security Configuration snap-ins call methods of this interface to determine whether the configuration data has changed, and if so, to update the security database. The attachment snap-in must store any configuration changes until the Security Configuration snap-ins retrieves that data.

An attachment snap-in extension must provide the following functionality:

-   [Display Configuration and Analysis Information](displaying-configuration-and-analysis-information.md)
-   [Modify Configuration Information in the User Interface](modifying-configuration-information-in-the-user-interface.md)
-   [Modify Configuration Information in the Security Database](modifying-configuration-information-in-the-database.md)

To assist your snap-in extension in performing these tasks, the Security Configuration snap-ins implement a COM interface, [**ISceSvcAttachmentData**](/windows/desktop/api/Scesvc/nn-scesvc-iscesvcattachmentdata), which provides methods your snap-in extension can call in order to initialize itself and query information from the security database.

After you have created your attachment snap-in extension, you must register it with the Security Configuration snap-ins as described in [Registering an Attachment Snap-in Extension](registering-an-attachment-snap-in-extension.md).

 

 
