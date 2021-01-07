---
description: To enable your application to work with the Synchronization Manager you must implement a Component Object Model (COM) object to handle synchronization notifications that you receive from SyncMgr.
title: Using Synchronization Manager from a Program
ms.topic: article
ms.date: 05/31/2018
ms.assetid: bf18d493-0fe7-46e7-9686-f7ee75b3039b
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# Using Synchronization Manager from a Program

To enable your application to work with the Synchronization Manager you must implement a Component Object Model (COM) object to handle synchronization notifications that you receive from SyncMgr. Your application's handler performs the synchronization for the items that you handle. Included in your handler, you must implement the [**ISyncMgrSynchronize**](/windows/desktop/api/Mobsync/nn-mobsync-isyncmgrsynchronize) interface. Also, you must provide an enumerator object and [**ISyncMgrEnumItems**](/windows/desktop/api/mobsync/nn-mobsync-isyncmgrenumitems) for any separate items that your application can synchronize.

SyncMgr implements [**ISyncMgrSynchronizeCallback**](/windows/desktop/api/mobsync/nn-mobsync-isyncmgrsynchronizecallback) and [**ISyncMgrSynchronizeInvoke**](/windows/desktop/api/Mobsync/nn-mobsync-isyncmgrsynchronizeinvoke).

The SyncMgr calls methods in your [**ISyncMgrSynchronize**](/windows/desktop/api/Mobsync/nn-mobsync-isyncmgrsynchronize) to get information on the items that your application handles and information on the handler that you provide for synchronizing these items.

At runtime, the synchronization process follows these steps.

1.  SyncMgr notifies your application that it is time for synchronization to occur for one of the items that your application handles by calling your [**ISyncMgrSynchronize::Initialize**](/windows/desktop/api/Mobsync/nf-mobsync-isyncmgrsynchronize-initialize) method.
2.  SyncMgr calls [**ISyncMgrSynchronize::EnumSyncMgrItems**](/windows/desktop/api/Mobsync/nf-mobsync-isyncmgrsynchronize-enumsyncmgritems) to obtain the [**ISyncMgrEnumItems**](/windows/desktop/api/mobsync/nn-mobsync-isyncmgrenumitems) interface for the items handled by your application.
3.  SyncMgr calls [**ISyncMgrSynchronize::SetProgressCallback**](/windows/desktop/api/Mobsync/nf-mobsync-isyncmgrsynchronize-setprogresscallback) to provide your handler with the interface pointer for the [**ISyncMgrSynchronizeCallback**](/windows/desktop/api/mobsync/nn-mobsync-isyncmgrsynchronizecallback) interface. Your handler uses this interface to call back to the SyncMgr during synchronization.
4.  SyncMgr then calls your [**ISyncMgrSynchronize::PrepareForSync**](/windows/desktop/api/Mobsync/nf-mobsync-isyncmgrsynchronize-prepareforsync) method to give your handler a chance to display any user interface element that is necessary before synchronization begins. For example, an email application may display a user logon dialog.
5.  Your handler calls [**ISyncMgrSynchronizeCallback::EnableModeless**](/windows/desktop/api/Mobsync/nf-mobsync-isyncmgrsynchronizecallback-enablemodeless) before and after displaying any user interface elements. Your handler calls [**ISyncMgrSynchronizeCallback::PrepareForSyncCompleted**](/windows/desktop/api/Mobsync/nf-mobsync-isyncmgrsynchronizecallback-prepareforsynccompleted) when you are done.
6.  SyncMgr calls your [**ISyncMgrSynchronize::Synchronize**](/windows/desktop/api/Mobsync/nf-mobsync-isyncmgrsynchronize-synchronize) method to start the synchronization.

During the synchronization process, SyncMgr continues to call methods in your [**ISyncMgrSynchronize**](/windows/desktop/api/Mobsync/nn-mobsync-isyncmgrsynchronize) interface. It can send your handler errors, progress, and notifications. It can also enumerate through the items that your application handles or allow your application to show properties for the items.

Your handler calls methods in [**ISyncMgrSynchronizeCallback**](/windows/desktop/api/mobsync/nn-mobsync-isyncmgrsynchronizecallback) to determine if an item should be skipped, to log errors, and to post progress information during the synchronization process.

For further information, see the related reference pages for the interfaces involved.

When the synchronization is completed, your handler calls [**ISyncMgrSynchronizeCallback::SynchronizeCompleted**](/windows/desktop/api/Mobsync/nf-mobsync-isyncmgrsynchronizecallback-synchronizecompleted).

 

 



