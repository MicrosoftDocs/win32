---
Description: 'Unpins files, directories, and network shared folders from the Offline Files cache.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: 'ffc91765-1f11-4679-a532-7bb65c042598'
ms.prod: 'windows-server-dev'
ms.technology: 'offline-files'
ms.tgt_platform: multiple
title: 'Unpin method of the Win32\_OfflineFilesCache class'
---

# Unpin method of the Win32\_OfflineFilesCache class

Unpins files, directories, and network shared folders from the Offline Files cache. Pinning is called "Always Available Offline" in the Windows user interface.

When a file is unpinned, it is no longer guaranteed to be available offline. If the unpin operation removes all instances of pin information in that it is not pinned by Folder Redirection, Group Policy, or by the user and that item has no unsynchronized offline changes, it may be automatically removed from the cache at any time.

## Syntax


```mof
uint32 Unpin(
  [in] string  Paths[],
  [in] uint32  Flags,
  [in] boolean Deep
);
```



## Parameters

<dl> <dt>

*Paths* \[in\]
</dt> <dd>

Array of strings, each of which contains the qualified UNC path of a file or directory to be unpinned.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

Controls behavior of the unpin operation. May be one or more of the following flags.

<dt>

<span id="OfflineFilesPinControlFlagForUser"></span><span id="offlinefilespincontrolflagforuser"></span><span id="OFFLINEFILESPINCONTROLFLAGFORUSER"></span>

<span id="OfflineFilesPinControlFlagForUser"></span><span id="offlinefilespincontrolflagforuser"></span><span id="OFFLINEFILESPINCONTROLFLAGFORUSER"></span>**OfflineFilesPinControlFlagForUser** (0x00000020)


</dt> <dd>

Unpins the items for the calling user. This is the flag typically set for a caller of this function. It is important to note that Offline Files does not support a true per-user notion of pinning. When an item is unpinned for a user, it is pinned for all users of that machine. An item that is pinned with this flag can be unpinned by any user who has access to that file. The ability to access that pinned file depends on the user's access rights to that file computed while online.

</dd> <dt>

<span id="OfflineFilesPinControlFlagForUser_Policy"></span><span id="offlinefilespincontrolflagforuser_policy"></span><span id="OFFLINEFILESPINCONTROLFLAGFORUSER_POLICY"></span>

<span id="OfflineFilesPinControlFlagForUser_Policy"></span><span id="offlinefilespincontrolflagforuser_policy"></span><span id="OFFLINEFILESPINCONTROLFLAGFORUSER_POLICY"></span>**OfflineFilesPinControlFlagForUser\_Policy** (0x00000040)


</dt> <dd>

Unpins the items for per-user policy. This differs from the **OfflineFilesPinControlFlagForUser** flag in that this flag cannot be modified by the user through the Offline Files user interface. Internally, Offline Files sets this flag when items are unpinned by its Group Policy extension.

</dd> <dt>

<span id="OfflineFilesPinControlFlagForAll"></span><span id="offlinefilespincontrolflagforall"></span><span id="OFFLINEFILESPINCONTROLFLAGFORALL"></span>

<span id="OfflineFilesPinControlFlagForAll"></span><span id="offlinefilespincontrolflagforall"></span><span id="OFFLINEFILESPINCONTROLFLAGFORALL"></span>**OfflineFilesPinControlFlagForAll** (0x00000080)


</dt> <dd>

Unpins the items for all users of the local machine.

</dd> <dt>

<span id="OfflineFilesPinControlFlagLowPriority"></span><span id="offlinefilespincontrolflaglowpriority"></span><span id="OFFLINEFILESPINCONTROLFLAGLOWPRIORITY"></span>

<span id="OfflineFilesPinControlFlagLowPriority"></span><span id="offlinefilespincontrolflaglowpriority"></span><span id="OFFLINEFILESPINCONTROLFLAGLOWPRIORITY"></span>**OfflineFilesPinControlFlagLowPriority** (0x00000200)


</dt> <dd>

Reserved for future use.

</dd> <dt>

<span id="OfflineFilesPinControlFlagAsyncProgress"></span><span id="offlinefilespincontrolflagasyncprogress"></span><span id="OFFLINEFILESPINCONTROLFLAGASYNCPROGRESS"></span>

<span id="OfflineFilesPinControlFlagAsyncProgress"></span><span id="offlinefilespincontrolflagasyncprogress"></span><span id="OFFLINEFILESPINCONTROLFLAGASYNCPROGRESS"></span>**OfflineFilesPinControlFlagAsyncProgress** (0x00000400)


</dt> <dd>

Progress is reported to the progress interface asynchronously with respect to the actual operations. If this flag is not set, progress is reported synchronously with each operation.

</dd> <dt>

<span id="OfflineFilesPinControlFlagInteractive"></span><span id="offlinefilespincontrolflaginteractive"></span><span id="OFFLINEFILESPINCONTROLFLAGINTERACTIVE"></span>

<span id="OfflineFilesPinControlFlagInteractive"></span><span id="offlinefilespincontrolflaginteractive"></span><span id="OFFLINEFILESPINCONTROLFLAGINTERACTIVE"></span>**OfflineFilesPinControlFlagInteractive** (0x00000800)


</dt> <dd>

Set this flag if the operation is allowed to display user interface elements as necessary. An example is the system's credential-request dialog.

</dd> <dt>

<span id="OfflineFilesPinControlFlagConsole"></span><span id="offlinefilespincontrolflagconsole"></span><span id="OFFLINEFILESPINCONTROLFLAGCONSOLE"></span>

<span id="OfflineFilesPinControlFlagConsole"></span><span id="offlinefilespincontrolflagconsole"></span><span id="OFFLINEFILESPINCONTROLFLAGCONSOLE"></span>**OfflineFilesPinControlFlagConsole** (0x00001000)


</dt> <dd>

This flag is ignored if the **OfflineFilesPinControlFlagInteractive** flag is not set. If the **OfflineFilesPinControlFlagInteractive** flag is set, this flag indicates that any UI produced should be directed to the console window associated with the process invoking the operation.

</dd> <dt>

<span id="OfflineFilesPinControlFlagBackground"></span><span id="offlinefilespincontrolflagbackground"></span><span id="OFFLINEFILESPINCONTROLFLAGBACKGROUND"></span>

<span id="OfflineFilesPinControlFlagBackground"></span><span id="offlinefilespincontrolflagbackground"></span><span id="OFFLINEFILESPINCONTROLFLAGBACKGROUND"></span>**OfflineFilesPinControlFlagBackground** (0x00010000)


</dt> <dd>

Set this flag if you want the unpin operation to avoid sharing violations in the event that an application wishes to open a file that is currently open for the unpin operation. When that scenario occurs and this flag is set, the unpin operation will "back off" and not finish for that particular file at that time. This flag is primarily used by the Offline Files service for internal operations.

</dd> </dl> </dd> <dt>

*Deep* \[in\]
</dt> <dd>

If one or more of the paths provided refers to a directory or shared folder, this argument indicates whether all subdirectories are to be unpinned as well. If this parameter is **TRUE**, all subdirectories are unpinned recursively. If this parameter is **FALSE**, only files that are immediate children of the directory are unpinned.

</dd> </dl>

## Return value

This method returns either a [WMI return code](https://msdn.microsoft.com/library/aa394574) or a [system error code](https://msdn.microsoft.com/library/windows/desktop/ms681381).

## Remarks

To monitor progress, implement a WMI event sink to receive [**SWbem.OnProgress**](https://msdn.microsoft.com/library/aa393882) [event notifications](https://msdn.microsoft.com/library/aa393011). The *strMessage* parameter contains a text string that is encoded with the following colon-delimited format:

*Reason*:*Result*:*ResultText*:\[*Path*\]

<dl> <dt>

<span id="Reason"></span><span id="reason"></span><span id="REASON"></span>*Reason*
</dt> <dd>

Specifies the type of progress notification as one of the following values:

<dl> <dd>0: Begin; sent once at the start of the operation.</dd> <dd>1: End; sent once at the end of the operation.</dd> <dd>2: ItemBegin; sent at the start of processing each item.</dd> <dd>3: ItemResult. Sent at the end of processing each item.</dd> </dl> </dd> <dt>

<span id="Result"></span><span id="result"></span><span id="RESULT"></span>*Result*
</dt> <dd>

Specifies an **HRESULT** value. If the unpin operation succeeds, this value is zero.

</dd> <dt>

<span id="ResultText"></span><span id="resulttext"></span><span id="RESULTTEXT"></span>*ResultText*
</dt> <dd>

Specifies a Windows message text string to be associated with the *Result* value.

</dd> <dt>

<span id="Path"></span><span id="path"></span><span id="PATH"></span>*Path*
</dt> <dd>

A string containing the UNC path of the item. This is an empty string if *Reason* is zero (Begin) or 1 (End).

</dd> </dl>

If an unpin operation is canceled while in progress, files that have been unpinned up to that point will remain unpinned.

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Namespace<br/>                | Root\\CIMv2<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Cscobj.h</dt> </dl>                    |
| MOF<br/>                      | <dl> <dt>OfflineFilesWmiProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CscObj.dll</dt> </dl>                  |



## See also

<dl> <dt>

[**Win32\_OfflineFilesCache**](win32-offlinefilescache.md)
</dt> </dl>

 

 




