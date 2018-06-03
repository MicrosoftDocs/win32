---
Description: Enables or disables the Offline Files feature.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a51147d3-ac7b-4a4b-8fcb-b9785f0bca9c
ms.prod: windows-server-dev
ms.technology: offline-files
ms.tgt_platform: multiple
title: Enable method of the Win32\_OfflineFilesCache class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Enable method of the Win32\_OfflineFilesCache class

Enables or disables the Offline Files feature.

## Syntax


```mof
uint32 Enable(
  [in]  boolean Enable,
  [out] boolean RebootRequired
);
```



## Parameters

<dl> <dt>

*Enable* \[in\]
</dt> <dd>

Specify **TRUE** to enable Offline Files, or **FALSE** to disable.

</dd> <dt>

*RebootRequired* \[out\]
</dt> <dd>

Receives **TRUE** if a system restart is necessary to apply the desired configuration, or **FALSE** otherwise.

</dd> </dl>

## Return value

This method returns either a [WMI return code](https://msdn.microsoft.com/library/aa394574) or a [system error code](https://msdn.microsoft.com/library/windows/desktop/ms681381).

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

 

 




