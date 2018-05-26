---
Description: Synchronizes files and directories in the Offline Files cache with their corresponding copies in the applicable network shared folders.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 179331f4-6e2a-4604-855c-9237a0cb8554
ms.prod: windows-server-dev
ms.technology: offline-files
ms.tgt_platform: multiple
title: Synchronize method of the Win32\_OfflineFilesCache class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Synchronize method of the Win32\_OfflineFilesCache class

Synchronizes files and directories in the Offline Files cache with their corresponding copies in the applicable network shared folders.

## Syntax


```mof
uint32 Synchronize(
  [in] string Paths[],
  [in] uint32 Flags
);
```



## Parameters

<dl> <dt>

*Paths* \[in\]
</dt> <dd>

Array of strings, each of which contains the fully qualified UNC path of a file or directory to be synchronized.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

Flags to control the behavior of the entire sync operation. Behaviors such as sync direction (in, out), the pinning of LNK targets, and the pinning of new files, are controlled through these flags. The following list describes the meaning of each flag.

<dt>

<span id="OfflineFilesSyncControlFlagFillSparse"></span><span id="offlinefilessynccontrolflagfillsparse"></span><span id="OFFLINEFILESSYNCCONTROLFLAGFILLSPARSE"></span>

<span id="OfflineFilesSyncControlFlagFillSparse"></span><span id="offlinefilessynccontrolflagfillsparse"></span><span id="OFFLINEFILESSYNCCONTROLFLAGFILLSPARSE"></span>**OfflineFilesSyncControlFlagFillSparse** (0x00000001)


</dt> <dd>

Fill sparse files in the cache. Setting this flag results in an enumeration of the local copies in the cache. Any sparsely cached files that are found are filled so that they are no longer sparse. Sparsely cached files are not available for offline use. For more information, see the Sparse property of the [**Win32\_OfflineFilesItem**](win32-offlinefilesitem.md) class.

</dd> <dt>

<span id="OfflineFilesSyncControlFlagSyncIn"></span><span id="offlinefilessynccontrolflagsyncin"></span><span id="OFFLINEFILESSYNCCONTROLFLAGSYNCIN"></span>

<span id="OfflineFilesSyncControlFlagSyncIn"></span><span id="offlinefilessynccontrolflagsyncin"></span><span id="OFFLINEFILESSYNCCONTROLFLAGSYNCIN"></span>**OfflineFilesSyncControlFlagSyncIn** (0x00000002)


</dt> <dd>

Sync remote changes from the server to the local cache. Setting this flag automatically sets the **OfflineFilesSyncControlFlagFillSparse** flag as well.

</dd> <dt>

<span id="OfflineFilesSyncControlFlagSyncOut"></span><span id="offlinefilessynccontrolflagsyncout"></span><span id="OFFLINEFILESSYNCCONTROLFLAGSYNCOUT"></span>

<span id="OfflineFilesSyncControlFlagSyncOut"></span><span id="offlinefilessynccontrolflagsyncout"></span><span id="OFFLINEFILESSYNCCONTROLFLAGSYNCOUT"></span>**OfflineFilesSyncControlFlagSyncOut** (0x00000004)


</dt> <dd>

Sync changes from the local cache to the server.

</dd> <dt>

<span id="OfflineFilesSyncControlFlagPinNewFiles"></span><span id="offlinefilessynccontrolflagpinnewfiles"></span><span id="OFFLINEFILESSYNCCONTROLFLAGPINNEWFILES"></span>

<span id="OfflineFilesSyncControlFlagPinNewFiles"></span><span id="offlinefilessynccontrolflagpinnewfiles"></span><span id="OFFLINEFILESSYNCCONTROLFLAGPINNEWFILES"></span>**OfflineFilesSyncControlFlagPinNewFiles** (0x00000008)


</dt> <dd>

Pin new files found on the server inside pinned directories. This flag is ignored if the **OfflineFilesSyncControlFlagSyncIn** flag is not set.

</dd> <dt>

<span id="OfflineFilesSyncControlFlagPinLinkTargets"></span><span id="offlinefilessynccontrolflagpinlinktargets"></span><span id="OFFLINEFILESSYNCCONTROLFLAGPINLINKTARGETS"></span>

<span id="OfflineFilesSyncControlFlagPinLinkTargets"></span><span id="offlinefilessynccontrolflagpinlinktargets"></span><span id="OFFLINEFILESSYNCCONTROLFLAGPINLINKTARGETS"></span>**OfflineFilesSyncControlFlagPinLinkTargets** (0x00000010)


</dt> <dd>

Applicable only if the **OfflineFilesSyncControlFlagPinNewFiles** flag is set. Normally, when a shell link (type LNK) is pinned, its target is not automatically pinned. When this flag is set, pinning a LNK file automatically pins its target if the target is a file. If the target is a directory, the target is never pinned automatically.

</dd> <dt>

<span id="OfflineFilesSyncControlFlagPinForUser"></span><span id="offlinefilessynccontrolflagpinforuser"></span><span id="OFFLINEFILESSYNCCONTROLFLAGPINFORUSER"></span>

<span id="OfflineFilesSyncControlFlagPinForUser"></span><span id="offlinefilessynccontrolflagpinforuser"></span><span id="OFFLINEFILESSYNCCONTROLFLAGPINFORUSER"></span>**OfflineFilesSyncControlFlagPinForUser** (0x00000020)


</dt> <dd>

Applicable only if the **OfflineFilesSyncControlFlagPinNewFiles** flag is set. Pins the items for the calling user. This is the flag typically set for a caller of this method. It is important to note that Offline Files does not support a true per-user notion of pinning. When an item is pinned for a user, it is pinned for all users of that machine. However, the ability to access that pinned file depends on the user's access rights to that file computed while online.

</dd> <dt>

<span id="OfflineFilesSyncControlFlagPinForUser_Policy"></span><span id="offlinefilessynccontrolflagpinforuser_policy"></span><span id="OFFLINEFILESSYNCCONTROLFLAGPINFORUSER_POLICY"></span>

<span id="OfflineFilesSyncControlFlagPinForUser_Policy"></span><span id="offlinefilessynccontrolflagpinforuser_policy"></span><span id="OFFLINEFILESSYNCCONTROLFLAGPINFORUSER_POLICY"></span>**OfflineFilesSyncControlFlagPinForUser\_Policy** (0x00000040)


</dt> <dd>

Applicable only if the **OfflineFilesSyncControlFlagPinNewFiles** flag is set. Pins the items for per-user policy. This differs from the **OfflineFilesSyncControlFlagPinForUser** flag in that this flag cannot be modified by the user through the Offline Files user interface. Internally, Offline Files sets this flag when items are pinned by its Group Policy extension.

</dd> <dt>

<span id="OfflineFilesSyncControlFlagPinForAll"></span><span id="offlinefilessynccontrolflagpinforall"></span><span id="OFFLINEFILESSYNCCONTROLFLAGPINFORALL"></span>

<span id="OfflineFilesSyncControlFlagPinForAll"></span><span id="offlinefilessynccontrolflagpinforall"></span><span id="OFFLINEFILESSYNCCONTROLFLAGPINFORALL"></span>**OfflineFilesSyncControlFlagPinForAll** (0x00000080)


</dt> <dd>

Applicable only if the **OfflineFilesSyncControlFlagPinNewFiles** flag is set. Pins the items for all users of the local machine. While the pinned state applies to all users, the ability to access a pinned file depends on the user's access rights to that file computed while online.

</dd> <dt>

<span id="OfflineFilesSyncControlFlagLowPriority"></span><span id="offlinefilessynccontrolflaglowpriority"></span><span id="OFFLINEFILESSYNCCONTROLFLAGLOWPRIORITY"></span>

<span id="OfflineFilesSyncControlFlagLowPriority"></span><span id="offlinefilessynccontrolflaglowpriority"></span><span id="OFFLINEFILESSYNCCONTROLFLAGLOWPRIORITY"></span>**OfflineFilesSyncControlFlagLowPriority** (0x00000200)


</dt> <dd>

This flag is reserved for future use.

</dd> <dt>

<span id="OfflineFilesSyncControlFlagAsyncProgress"></span><span id="offlinefilessynccontrolflagasyncprogress"></span><span id="OFFLINEFILESSYNCCONTROLFLAGASYNCPROGRESS"></span>

<span id="OfflineFilesSyncControlFlagAsyncProgress"></span><span id="offlinefilessynccontrolflagasyncprogress"></span><span id="OFFLINEFILESSYNCCONTROLFLAGASYNCPROGRESS"></span>**OfflineFilesSyncControlFlagAsyncProgress** (0x00000400)


</dt> <dd>

Progress is reported to the progress interface asynchronously with the actual operations. If this flag is not set, progress is reported synchronously with each operation.

</dd> <dt>

<span id="OfflineFilesSyncControlFlagInteractive"></span><span id="offlinefilessynccontrolflaginteractive"></span><span id="OFFLINEFILESSYNCCONTROLFLAGINTERACTIVE"></span>

<span id="OfflineFilesSyncControlFlagInteractive"></span><span id="offlinefilessynccontrolflaginteractive"></span><span id="OFFLINEFILESSYNCCONTROLFLAGINTERACTIVE"></span>**OfflineFilesSyncControlFlagInteractive** (0x00000800)


</dt> <dd>

Set this flag if the operation is allowed to display user interface elements as necessary. An example is the system's credential-request dialog.

</dd> <dt>

<span id="OfflineFilesSyncControlFlagConsole"></span><span id="offlinefilessynccontrolflagconsole"></span><span id="OFFLINEFILESSYNCCONTROLFLAGCONSOLE"></span>

<span id="OfflineFilesSyncControlFlagConsole"></span><span id="offlinefilessynccontrolflagconsole"></span><span id="OFFLINEFILESSYNCCONTROLFLAGCONSOLE"></span>**OfflineFilesSyncControlFlagConsole** (0x00001000)


</dt> <dd>

All interactions are directed to the console.

</dd> <dt>

<span id="OfflineFilesSyncControlFlagSkipSuspendedDirs"></span><span id="offlinefilessynccontrolflagskipsuspendeddirs"></span><span id="OFFLINEFILESSYNCCONTROLFLAGSKIPSUSPENDEDDIRS"></span>

<span id="OfflineFilesSyncControlFlagSkipSuspendedDirs"></span><span id="offlinefilessynccontrolflagskipsuspendeddirs"></span><span id="OFFLINEFILESSYNCCONTROLFLAGSKIPSUSPENDEDDIRS"></span>**OfflineFilesSyncControlFlagSkipSuspendedDirs** (0x00002000)


</dt> <dd>

Set this flag if you want the sync operation to not sync suspended directory trees. It is recommended that this flag is set when the sync operation has not been invoked interactively and intentionally by a user.

</dd> <dt>

<span id="OfflineFilesSyncControlFlagBackground"></span><span id="offlinefilessynccontrolflagbackground"></span><span id="OFFLINEFILESSYNCCONTROLFLAGBACKGROUND"></span>

<span id="OfflineFilesSyncControlFlagBackground"></span><span id="offlinefilessynccontrolflagbackground"></span><span id="OFFLINEFILESSYNCCONTROLFLAGBACKGROUND"></span>**OfflineFilesSyncControlFlagBackground** (0x00010000)


</dt> <dd>

Set this flag if you want the sync operation to avoid sharing violations in the event that an application opens a file that is currently open for the sync operation. When that scenario occurs and this flag is set, the sync operation will "back off" and not finish for that particular file at that time. This flag is primarily used by the Offline Files service for internal operations.

</dd> </dl>

Note that **OfflineFilesSyncControlCrKeepLocal**, **OfflineFilesSyncControlCrKeepRemote**, and **OfflineFilesSyncControlCrKeepLatest** are not flag values. If you want all sync conflicts to be resolved in a "keep local", "keep remote" or "keep latest" manner, set one (and only one) of the following values to specify a conflict resolution policy. If no conflict resolution policy is specified, conflicts will remain unresolved and may be viewed in the Sync Center Conflicts folder.

<dt>

<span id="OfflineFilesSyncControlCrKeepLocal"></span><span id="offlinefilessynccontrolcrkeeplocal"></span><span id="OFFLINEFILESSYNCCONTROLCRKEEPLOCAL"></span>

<span id="OfflineFilesSyncControlCrKeepLocal"></span><span id="offlinefilessynccontrolcrkeeplocal"></span><span id="OFFLINEFILESSYNCCONTROLCRKEEPLOCAL"></span>**OfflineFilesSyncControlCrKeepLocal** (0x10000000)


</dt> <dd>

Resolve all conflicts by copying the local computer copy to the server.

</dd> <dt>

<span id="OfflineFilesSyncControlCrKeepRemote"></span><span id="offlinefilessynccontrolcrkeepremote"></span><span id="OFFLINEFILESSYNCCONTROLCRKEEPREMOTE"></span>

<span id="OfflineFilesSyncControlCrKeepRemote"></span><span id="offlinefilessynccontrolcrkeepremote"></span><span id="OFFLINEFILESSYNCCONTROLCRKEEPREMOTE"></span>**OfflineFilesSyncControlCrKeepRemote** (0x20000000)


</dt> <dd>

Resolve all conflicts by copying the server copy to the local computer.

</dd> <dt>

<span id="OfflineFilesSyncControlCrKeepLatest"></span><span id="offlinefilessynccontrolcrkeeplatest"></span><span id="OFFLINEFILESSYNCCONTROLCRKEEPLATEST"></span>

<span id="OfflineFilesSyncControlCrKeepLatest"></span><span id="offlinefilessynccontrolcrkeeplatest"></span><span id="OFFLINEFILESSYNCCONTROLCRKEEPLATEST"></span>**OfflineFilesSyncControlCrKeepLatest** (0x30000000)


</dt> <dd>

Resolve all conflicts by copying with the latest last-change time. This resolution is sometimes called "last writer wins."

</dd> </dl> </dd> </dl>

## Return value

This method returns either a [WMI return code](https://msdn.microsoft.com/library/aa394574) or a [system error code](https://msdn.microsoft.com/library/windows/desktop/ms681381).

## Remarks

To monitor progress, implement a WMI event sink to receive [**SWbem.OnProgress**](https://msdn.microsoft.com/library/aa393882)[event notifications](https://msdn.microsoft.com/library/aa393011). The *strMessage* parameter contains a text string that is encoded with the following colon-delimited format:

*Reason*:*Result*:*ResultText*:\[*Path*\]

<dl> <dt>

<span id="Reason"></span><span id="reason"></span><span id="REASON"></span>*Reason*
</dt> <dd>

Specifies the type of progress notification as one of the following values:

<dl> <dd>0: Begin; sent once at the start of the operation.</dd> <dd>1: End; sent once at the end of the operation.</dd> <dd>2: ItemBegin; sent at the start of processing each item.</dd> <dd>3: ItemResult. Sent at the end of processing each item.</dd> </dl> </dd> <dt>

<span id="Result"></span><span id="result"></span><span id="RESULT"></span>*Result*
</dt> <dd>

Specifies an **HRESULT** value. If the sync operation succeeds, this value is zero.

</dd> <dt>

<span id="ResultText"></span><span id="resulttext"></span><span id="RESULTTEXT"></span>*ResultText*
</dt> <dd>

Specifies a Windows message text string to be associated with the *Result* value.

</dd> <dt>

<span id="Path"></span><span id="path"></span><span id="PATH"></span>*Path*
</dt> <dd>

A string containing the UNC path of the item. This is an empty string if *Reason* is zero (Begin) or 1 (End).

</dd> </dl>

If a sync operation is canceled while in progress, files that have been synchronized up to that point will remain synchronized.

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Namespace<br/>                | Root\\CIMv2<br/>                                                                                 |
| MOF<br/>                      | <dl> <dt>OfflineFilesWmiProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CscObj.dll</dt> </dl>                  |



## See also

<dl> <dt>

[**Win32\_OfflineFilesCache**](win32-offlinefilescache.md)
</dt> </dl>

 

 




