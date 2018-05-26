---
Description: Presents query and action capabilities associated with the online-offline transition behavior of Offline Files.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0d91475d-8483-42c6-89d7-19569c82e0d7
ms.prod: windows-server-dev
ms.technology: offline-files
ms.tgt_platform: multiple
title: Win32\_OfflineFilesConnectionInfo class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Win32\_OfflineFilesConnectionInfo class

Presents query and action capabilities associated with the online-offline transition behavior of Offline Files. An instance of this class is obtained through the **ConnectionInfo** property of the [**Win32\_OfflineFilesItem**](win32-offlinefilesitem.md) object.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[dynamic, provider("Win32_OfflineFilesProvider"), AMENDMENT]
class Win32_OfflineFilesConnectionInfo
{
  uint32 ConnectState;
  uint32 OfflineReason;
};
```

## Members

The **Win32\_OfflineFilesConnectionInfo** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_OfflineFilesConnectionInfo** class has these properties.

<dl> <dt>

**ConnectState**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Offline"></span><span id="offline"></span><span id="OFFLINE"></span>

**Offline** (1)


</dt> <dd></dd> <dt>

<span id="Online"></span><span id="online"></span><span id="ONLINE"></span>

**Online** (2)


</dt> <dd></dd> <dt>

<span id="Transparently_Cached"></span><span id="transparently_cached"></span><span id="TRANSPARENTLY_CACHED"></span>

**Transparently Cached** (3)


</dt> <dd></dd> <dt>

<span id="Partly_Transparently_Cached"></span><span id="partly_transparently_cached"></span><span id="PARTLY_TRANSPARENTLY_CACHED"></span>

**Partly Transparently Cached** (4)


</dt> <dd></dd> </dl>

Indicates whether the item is currently online or offline. If the item is offline, the **OfflineReason** property indicates why it is offline.

**Windows Server 2008, Windows Vista, Windows Server 2008 R2 and Windows 7:** 3 (Transparently Cached) and 4 (Partly Transparently Cached) are not supported before Windows Server 2012 and Windows 8

</dd> <dt>

**OfflineReason**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Not_applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>

**Not applicable** (1)


</dt> <dd></dd> <dt>

<span id="Working_offline"></span><span id="working_offline"></span><span id="WORKING_OFFLINE"></span>

**Working offline** (2)


</dt> <dd></dd> <dt>

<span id="Slow_connection"></span><span id="slow_connection"></span><span id="SLOW_CONNECTION"></span>

**Slow connection** (3)


</dt> <dd></dd> <dt>

<span id="Net_disconnected"></span><span id="net_disconnected"></span><span id="NET_DISCONNECTED"></span>

**Net disconnected** (4)


</dt> <dd></dd> <dt>

<span id="Need_to_sync_item"></span><span id="need_to_sync_item"></span><span id="NEED_TO_SYNC_ITEM"></span>

**Need to sync item** (5)


</dt> <dd></dd> <dt>

<span id="Item_suspended"></span><span id="item_suspended"></span><span id="ITEM_SUSPENDED"></span>

**Item suspended** (6)


</dt> <dd></dd> </dl>

If the item is offline (**ConnectState**=1 (**Offline**), this property indicates why it is offline.

</dd> </dl>

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

[Offline Files WMI Provider Reference](offline-files-wmi-provider-reference.md)
</dt> </dl>

 

 




