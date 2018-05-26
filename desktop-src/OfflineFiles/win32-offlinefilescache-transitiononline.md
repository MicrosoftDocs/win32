---
Description: Transitions an item online if possible.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: bcf3b602-6227-4bd0-84f6-ef436d396e4f
ms.prod: windows-server-dev
ms.technology: offline-files
ms.tgt_platform: multiple
title: TransitionOnline method of the Win32\_OfflineFilesCache class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# TransitionOnline method of the Win32\_OfflineFilesCache class

Transitions an item online if possible.

## Syntax


```mof
uint32 TransitionOnline(
  [in] string Path,
  [in] uint32 Flags
);
```



## Parameters

<dl> <dt>

*Path* \[in\]
</dt> <dd>

Fully qualified UNC path of the item to be transitioned online.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

One or more of the following flag values.

<dt>

<span id="OfflineFilesTransitionFlagInteractive"></span><span id="offlinefilestransitionflaginteractive"></span><span id="OFFLINEFILESTRANSITIONFLAGINTERACTIVE"></span>

<span id="OfflineFilesTransitionFlagInteractive"></span><span id="offlinefilestransitionflaginteractive"></span><span id="OFFLINEFILESTRANSITIONFLAGINTERACTIVE"></span>**OfflineFilesTransitionFlagInteractive** (0x00000001)


</dt> <dd>

Set this flag if the operation is allowed to display user interface elements as necessary. An example is the system's credential-request dialog.

</dd> <dt>

<span id="OfflineFilesTransitionFlagConsole"></span><span id="offlinefilestransitionflagconsole"></span><span id="OFFLINEFILESTRANSITIONFLAGCONSOLE"></span>

<span id="OfflineFilesTransitionFlagConsole"></span><span id="offlinefilestransitionflagconsole"></span><span id="OFFLINEFILESTRANSITIONFLAGCONSOLE"></span>**OfflineFilesTransitionFlagConsole** (0x00000002)


</dt> <dd>

This flag is ignored if the **OfflineFilesTransitionFlagInteractive** flag is not set. If the **OfflineFilesTransitionFlagInteractive** flag is set, this flag indicates that any UI produced should be directed to the console window associated with the process invoking the operation.

</dd> </dl> </dd> </dl>

## Return value

This method returns either a [WMI return code](https://msdn.microsoft.com/library/aa394574) or a [system error code](https://msdn.microsoft.com/library/windows/desktop/ms681381).

## Remarks

The entire scope of the item is transitioned online, not just the item. An item's scope is defined as the closest ancestor shared folder of the item.

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP1<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Version<br/>                  | [KB935553](http://go.microsoft.com/fwlink/p/?linkid=110521) on Windows Vista<br/>                |
| Namespace<br/>                | Root\\CIMv2<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Cscobj.h</dt> </dl>                    |
| MOF<br/>                      | <dl> <dt>OfflineFilesWmiProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CscObj.dll</dt> </dl>                  |



## See also

<dl> <dt>

[**Win32\_OfflineFilesCache**](win32-offlinefilescache.md)
</dt> </dl>

 

 




