---
description: This topic provides a step-by-step examination of the requirements to build a DLL file that implements a handler to be used with Sync Center. This information is valid as of Windows Vista.
title: Developing a Windows Sync Center Handler
ms.topic: article
ms.date: 05/31/2018
ms.assetid: 66b40f81-9515-4190-8ced-44f20bb9df86
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# Developing a Windows Sync Center Handler

This topic provides a step-by-step examination of the requirements to build a DLL file that implements a handler to be used with Sync Center. This information is valid as of Windows Vista.

-   [The Windows Synchronization Experience Before Vista](#the-windows-synchronization-experience-before-vista)
-   [Sync Center APIs](#sync-center-apis)
    -   [Essential Interfaces](#essential-interfaces)

## The Windows Synchronization Experience Before Vista

Windows XP provided a [Synchronization Manager](syncmgr-start-page.md) (mobsync.exe). Many devices such as mp3 players, cell phones, and cameras also provided their own synchronization interfaces rather than using the Synchronization Manager. This resulted in an inconsistent and noncentralized user experience.

The new Sync Center feature provided in Windows Vista has several advantages over the older Synchronization Manager.

-   Better discoverability
-   Less need for direct user action
-   Does not block other operations
-   Better visualization of the synchronization progress
-   Easier to understand development model

## Sync Center APIs

Sync Center communicates with handlers through a number of Component Object Model (COM) interfaces. Not all of these interfaces are needed to implement a Sync Center handler. This topic has been broken into two sections. The first section explains the essential COM interfaces that every handler must support, and the second section examines the optional COM interfaces and looks at the reasons that a handler would support them.

-   [Essential Interfaces](#essential-interfaces)

### Essential Interfaces

All Sync Center handlers must support the following interfaces:

-   [**ISyncMgrHandler**](/windows/desktop/api/Syncmgr/nn-syncmgr-isyncmgrhandler)
-   [**ISyncMgrHandlerInfo**](/windows/desktop/api/Syncmgr/nn-syncmgr-isyncmgrhandlerinfo)
-   [**ISyncMgrSyncItemContainer**](/windows/desktop/api/Syncmgr/nn-syncmgr-isyncmgrsyncitemcontainer)
-   [**IEnumSyncMgrSyncItems**](/windows/desktop/api/Syncmgr/nn-syncmgr-ienumsyncmgrsyncitems)
-   [**ISyncMgrSyncItem**](/windows/desktop/api/Syncmgr/nn-syncmgr-isyncmgrsyncitem)
-   [**ISyncMgrSyncItemInfo**](/windows/desktop/api/Syncmgr/nn-syncmgr-isyncmgrsynciteminfo)

[**ISyncMgrSyncItem**](/windows/desktop/api/Syncmgr/nn-syncmgr-isyncmgrsyncitem) and [**ISyncMgrSyncItemInfo**](/windows/desktop/api/Syncmgr/nn-syncmgr-isyncmgrsynciteminfo) are used to describe a single sync item involved in the synchronization to the Sync Center. A sync item generally represents either a particular data type (such as images) or a particular location of data.

Sync items that represent different data locations allow for very specific synchronizations. The granularity of the location is up to the handler author, but care should be taken in the design. If there are too few sync items (locations), then the user is restricted in their ability to sync only certain data. At the other extreme, too much granularity can become unmanageable.

If a handler supports more than one data type or multiple data locations, then it needs to support more than one sync item object. An example might be a personal data assistant (PDA) that allows the user to sync contacts, calendar items and documents. These three data types would need to be represented by three unique objects that each expose the [**ISyncMgrSyncItem**](/windows/desktop/api/Syncmgr/nn-syncmgr-isyncmgrsyncitem) and [**ISyncMgrSyncItemInfo**](/windows/desktop/api/Syncmgr/nn-syncmgr-isyncmgrsynciteminfo) interfaces.

The [**IEnumSyncMgrSyncItems**](/windows/desktop/api/Syncmgr/nn-syncmgr-ienumsyncmgrsyncitems) interface provides a mechanism to enumerate through a handler's sync items. To retrieve this enumerator, Sync Center calls the [**ISyncMgrSyncItemContainer::GetSyncItemEnumerator**](/windows/desktop/api/Syncmgr/nf-syncmgr-isyncmgrsyncitemcontainer-getsyncitemenumerator) method exposed by the handler. [**ISyncMgrSyncItemContainer**](/windows/desktop/api/Syncmgr/nn-syncmgr-isyncmgrsyncitemcontainer) also contains two other methods that the Sync Center can use to retrieve information about the handler's sync items:

-   [**GetSyncItem**](/windows/desktop/api/Syncmgr/nf-syncmgr-isyncmgrsyncitemcontainer-getsyncitem) returns a specific sync item.
-   [**GetSyncItemCount**](/windows/desktop/api/Syncmgr/nf-syncmgr-isyncmgrsyncitemcontainer-getsyncitemcount) returns the number of sync items supported by the handler.

[**ISyncMgrHandler**](/windows/desktop/api/Syncmgr/nn-syncmgr-isyncmgrhandler) and [**ISyncMgrHandlerInfo**](/windows/desktop/api/Syncmgr/nn-syncmgr-isyncmgrhandlerinfo) are used to describe the properties of the hander and launch the actual synchronization. [**ISyncMgrHandler::Synchronize**](/windows/desktop/api/Syncmgr/nf-syncmgr-isyncmgrhandler-synchronize) is where the handler code carries out the synchronization and provides feedback on progress and any issues that occur.

Many of the interface methods do not need to be fully implemented. Sync Center provides a certain amount of default information. The interfaces allow a handler to override this information and provide custom information to display, if needed.

 

 



