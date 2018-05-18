---
Description: 'To enable your application to work with the Synchronization Manager you must implement a Component Object Model (COM) object to handle synchronization notifications that you receive from SyncMgr.'
title: Using Synchronization Manager from a Program
---

# Using Synchronization Manager from a Program

To enable your application to work with the Synchronization Manager you must implement a Component Object Model (COM) object to handle synchronization notifications that you receive from SyncMgr. Your application's handler performs the synchronization for the items that you handle. Included in your handler, you must implement the [**ISyncMgrSynchronize**](syncmgr-isyncmgrsynchronize.md) interface. Also, you must provide an enumerator object and [**ISyncMgrEnumItems**](syncmgr-isyncmgrenumitems.md) for any separate items that your application can synchronize.

SyncMgr implements [**ISyncMgrSynchronizeCallback**](syncmgr-isyncmgrsynchronizecallback.md) and [**ISyncMgrSynchronizeInvoke**](syncmgr-isyncmgrsynchronizeinvoke.md).

The SyncMgr calls methods in your [**ISyncMgrSynchronize**](syncmgr-isyncmgrsynchronize.md) to get information on the items that your application handles and information on the handler that you provide for synchronizing these items.

At runtime, the synchronization process follows these steps.

1.  SyncMgr notifies your application that it is time for synchronization to occur for one of the items that your application handles by calling your [**ISyncMgrSynchronize::Initialize**](syncmgr-isyncmgrsynchronize-initialize.md) method.
2.  SyncMgr calls [**ISyncMgrSynchronize::EnumSyncMgrItems**](syncmgr-isyncmgrsynchronize-enumsyncmgritems.md) to obtain the [**ISyncMgrEnumItems**](syncmgr-isyncmgrenumitems.md) interface for the items handled by your application.
3.  SyncMgr calls [**ISyncMgrSynchronize::SetProgressCallback**](syncmgr-isyncmgrsynchronize-setprogresscallback.md) to provide your handler with the interface pointer for the [**ISyncMgrSynchronizeCallback**](syncmgr-isyncmgrsynchronizecallback.md) interface. Your handler uses this interface to call back to the SyncMgr during synchronization.
4.  SyncMgr then calls your [**ISyncMgrSynchronize::PrepareForSync**](syncmgr-isyncmgrsynchronize-prepareforsync.md) method to give your handler a chance to display any user interface element that is necessary before synchronization begins. For example, an email application may display a user logon dialog.
5.  Your handler calls [**ISyncMgrSynchronizeCallback::EnableModeless**](syncmgr-isyncmgrsynchronizecallback-enablemodeless.md) before and after displaying any user interface elements. Your handler calls [**ISyncMgrSynchronizeCallback::PrepareForSyncCompleted**](syncmgr-isyncmgrsynchronizecallback-prepareforsynccompleted.md) when you are done.
6.  SyncMgr calls your [**ISyncMgrSynchronize::Synchronize**](syncmgr-isyncmgrsynchronize-synchronize.md) method to start the synchronization.

During the synchronization process, SyncMgr continues to call methods in your [**ISyncMgrSynchronize**](syncmgr-isyncmgrsynchronize.md) interface. It can send your handler errors, progress, and notifications. It can also enumerate through the items that your application handles or allow your application to show properties for the items.

Your handler calls methods in [**ISyncMgrSynchronizeCallback**](syncmgr-isyncmgrsynchronizecallback.md) to determine if an item should be skipped, to log errors, and to post progress information during the synchronization process.

For further information, see the related reference pages for the interfaces involved.

When the synchronization is completed, your handler calls [**ISyncMgrSynchronizeCallback::SynchronizeCompleted**](syncmgr-isyncmgrsynchronizecallback-synchronizecompleted.md).

 

 



