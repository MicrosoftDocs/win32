---
Description: To enable your application to work with the Synchronization Manager you must implement a Component Object Model (COM) object to handle synchronization notifications that you receive from SyncMgr.
title: Using Synchronization Manager from a Program
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using Synchronization Manager from a Program

To enable your application to work with the Synchronization Manager you must implement a Component Object Model (COM) object to handle synchronization notifications that you receive from SyncMgr. Your application's handler performs the synchronization for the items that you handle. Included in your handler, you must implement the [**ISyncMgrSynchronize**](/windows/win32/Mobsync/nn-mobsync-isyncmgrsynchronize?branch=master) interface. Also, you must provide an enumerator object and [**ISyncMgrEnumItems**](/windows/win32/mobsync/nn-mobsync-isyncmgrenumitems?branch=master) for any separate items that your application can synchronize.

SyncMgr implements [**ISyncMgrSynchronizeCallback**](/windows/win32/mobsync/nn-mobsync-isyncmgrsynchronizecallback?branch=master) and [**ISyncMgrSynchronizeInvoke**](/windows/win32/Mobsync/nn-mobsync-isyncmgrsynchronizeinvoke?branch=master).

The SyncMgr calls methods in your [**ISyncMgrSynchronize**](/windows/win32/Mobsync/nn-mobsync-isyncmgrsynchronize?branch=master) to get information on the items that your application handles and information on the handler that you provide for synchronizing these items.

At runtime, the synchronization process follows these steps.

1.  SyncMgr notifies your application that it is time for synchronization to occur for one of the items that your application handles by calling your [**ISyncMgrSynchronize::Initialize**](/windows/win32/Mobsync/nf-mobsync-isyncmgrsynchronize-initialize?branch=master) method.
2.  SyncMgr calls [**ISyncMgrSynchronize::EnumSyncMgrItems**](/windows/win32/Mobsync/nf-mobsync-isyncmgrsynchronize-enumsyncmgritems?branch=master) to obtain the [**ISyncMgrEnumItems**](/windows/win32/mobsync/nn-mobsync-isyncmgrenumitems?branch=master) interface for the items handled by your application.
3.  SyncMgr calls [**ISyncMgrSynchronize::SetProgressCallback**](/windows/win32/Mobsync/nf-mobsync-isyncmgrsynchronize-setprogresscallback?branch=master) to provide your handler with the interface pointer for the [**ISyncMgrSynchronizeCallback**](/windows/win32/mobsync/nn-mobsync-isyncmgrsynchronizecallback?branch=master) interface. Your handler uses this interface to call back to the SyncMgr during synchronization.
4.  SyncMgr then calls your [**ISyncMgrSynchronize::PrepareForSync**](/windows/win32/Mobsync/nf-mobsync-isyncmgrsynchronize-prepareforsync?branch=master) method to give your handler a chance to display any user interface element that is necessary before synchronization begins. For example, an email application may display a user logon dialog.
5.  Your handler calls [**ISyncMgrSynchronizeCallback::EnableModeless**](/windows/win32/Mobsync/nf-mobsync-isyncmgrsynchronizecallback-enablemodeless?branch=master) before and after displaying any user interface elements. Your handler calls [**ISyncMgrSynchronizeCallback::PrepareForSyncCompleted**](/windows/win32/Mobsync/nf-mobsync-isyncmgrsynchronizecallback-prepareforsynccompleted?branch=master) when you are done.
6.  SyncMgr calls your [**ISyncMgrSynchronize::Synchronize**](/windows/win32/Mobsync/nf-mobsync-isyncmgrsynchronize-synchronize?branch=master) method to start the synchronization.

During the synchronization process, SyncMgr continues to call methods in your [**ISyncMgrSynchronize**](/windows/win32/Mobsync/nn-mobsync-isyncmgrsynchronize?branch=master) interface. It can send your handler errors, progress, and notifications. It can also enumerate through the items that your application handles or allow your application to show properties for the items.

Your handler calls methods in [**ISyncMgrSynchronizeCallback**](/windows/win32/mobsync/nn-mobsync-isyncmgrsynchronizecallback?branch=master) to determine if an item should be skipped, to log errors, and to post progress information during the synchronization process.

For further information, see the related reference pages for the interfaces involved.

When the synchronization is completed, your handler calls [**ISyncMgrSynchronizeCallback::SynchronizeCompleted**](/windows/win32/Mobsync/nf-mobsync-isyncmgrsynchronizecallback-synchronizecompleted?branch=master).

 

 



