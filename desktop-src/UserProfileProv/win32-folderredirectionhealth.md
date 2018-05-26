---
Description: Represents the health status of a redirected user folder.
ms.assetid: 7EC65CB4-44FE-47AA-8584-9AAA15ABD551
title: Win32\_FolderRedirectionHealth class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Win32\_FolderRedirectionHealth class

Represents the health status of a redirected user folder.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class Win32_FolderRedirectionHealth
{
  string   OfflineFileNameFolderGUID;
  boolean  Redirected;
  boolean  OfflineAccessEnabled;
  DATETIME LastSuccessfulSyncTime;
  DATETIME LastSyncTime;
  uint8    LastSyncStatus;
  uint8    HealthStatus;
};
```

## Members

The **Win32\_FolderRedirectionHealth** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_FolderRedirectionHealth** class has these properties.

<dl> <dt>

**HealthStatus**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The health status of the folder.

The possible values are.

<dl> <dt>

<span id="Healthy"></span><span id="healthy"></span><span id="HEALTHY"></span>**Healthy** (0)
</dt> <dt>

<span id="Caution"></span><span id="caution"></span><span id="CAUTION"></span>**Caution** (1)
</dt> <dt>

<span id="Unhealthy"></span><span id="unhealthy"></span><span id="UNHEALTHY"></span>**Unhealthy** (2)
</dt> </dl>

</dd> <dt>

**LastSuccessfulSyncTime**
</dt> <dd> <dl> <dt>

Data type: **DATETIME**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The last time the folder was successfully synchronized with the Offline Files cache.

</dd> <dt>

**LastSyncStatus**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The status of the last attempt to synchronize the folder to the Offline Files cache.

The possible values are.

<dl> <dt>

<span id="Success"></span><span id="success"></span><span id="SUCCESS"></span>**Success** (0)
</dt> <dt>

<span id="Conflict"></span><span id="conflict"></span><span id="CONFLICT"></span>**Conflict** (1)
</dt> <dt>

<span id="Warning"></span><span id="warning"></span><span id="WARNING"></span>**Warning** (2)
</dt> <dt>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>**Error** (3)
</dt> </dl>

</dd> <dt>

**LastSyncTime**
</dt> <dd> <dl> <dt>

Data type: **DATETIME**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The last time an attempt was made to synchronize the folder with the Offline Files cache.

</dd> <dt>

**OfflineAccessEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether offline access is enabled on the folder. **True** if offline access is enabled; otherwise **false**.

</dd> <dt>

**OfflineFileNameFolderGUID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The **GUID** of the folder.

</dd> <dt>

**Redirected**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether the folder is redirected. **True** if this folder is redirected; otherwise **false**.

</dd> </dl>

## Requirements



|                                     |                                                                                                       |
|-------------------------------------|-------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                  |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                                |
| MOF<br/>                      | <dl> <dt>UserProfileWmiProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Profprov.dll</dt> </dl>               |



## See also

<dl> <dt>

[UserProfileProvider Provider Classes](userprofileprovider-provider-classes.md)
</dt> </dl>

 

 




