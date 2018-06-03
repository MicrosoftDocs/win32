---
title: IGPMBackup Property Methods
description: The property methods of the IGPMBackup interface get the properties that are described in the following table. For a general discussion of property methods, see Interface Property Methods in the Active Directory Service Interfaces (ADSI) documentation.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5393a50a-ce4c-436d-9e86-2f9540652d6a
ms.prod: windows-server-dev
ms.technology: group-policy
ms.tgt_platform: multiple
keywords:
- IGPMBackup Property Methods GPMC
topic_type:
- apiref
api_name:
- IGPMBackup Property Methods
- IGPMBackup.BackupDir
- IGPMBackup.get_BackupDir
- IGPMBackup.Comment
- IGPMBackup.get_Comment
- IGPMBackup.GPODisplayName
- IGPMBackup.get_GPODisplayName
- IGPMBackup.GPODomain
- IGPMBackup.get_GPODomain
- IGPMBackup.GPOID
- IGPMBackup.get_GPOID
- IGPMBackup.ID
- IGPMBackup.get_ID
- IGPMBackup.Timestamp
- IGPMBackup.get_Timestamp
api_location:
- Gpmgmt.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IGPMBackup Property Methods

The property methods of the [**IGPMBackup**](/previous-versions/windows/desktop/api/Gpmgmt/nn-gpmgmt-igpmbackup) interface get the properties that are described in the following table. For a general discussion of property methods, see [Interface Property Methods](https://msdn.microsoft.com/library/aa746378) in the Active Directory Service Interfaces (ADSI) documentation.

## Properties

<dl> <dt>

**BackupDir**
</dt> <dd> <dl>

The directory in which the [**GPMBackup**](/previous-versions/windows/desktop/api/Gpmgmt/nn-gpmgmt-igpmbackup) object exists.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **String**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_BackupDir(
  [out] BSTR* pVal
);
```


</dt> </dl> </dd> <dt>

**Comment**
</dt> <dd> <dl>

Comment associated with the [**GPMBackup**](/previous-versions/windows/desktop/api/Gpmgmt/nn-gpmgmt-igpmbackup) object.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **String**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Comment(
  [out] BSTR* pVal
);
```


</dt> </dl> </dd> <dt>

**GPODisplayName**
</dt> <dd> <dl>

Friendly display name of the backed-up Group Policy object (GPO). More than one GPO can have the same friendly name. GPOs are identified in the directory service by the ID (GUID), not by the friendly name.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **String**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_GPODisplayName(
  [out] BSTR* pVal
);
```


</dt> </dl> </dd> <dt>

**GPODomain**
</dt> <dd> <dl>

Name of the domain in which the GPO existed when it was backed up. This is a full Domain Name System (DNS) name, such as example.microsoft.com.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **String**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_GPODomain(
  [out] BSTR* pVal
);
```


</dt> </dl> </dd> <dt>

**GPOID**
</dt> <dd> <dl>

ID of the backed-up GPO.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **String**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_GPOID(
  [out] BSTR* pVal
);
```


</dt> </dl> </dd> <dt>

**ID**
</dt> <dd> <dl>

GUID that uniquely identifies the [**GPMBackup**](/previous-versions/windows/desktop/api/Gpmgmt/nn-gpmgmt-igpmbackup) object within its backup directory.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **String**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_ID(
  [out] BSTR* pVal
);
```


</dt> </dl> </dd> <dt>

**Timestamp**
</dt> <dd> <dl>

Date and time when the [**GPMBackup**](/previous-versions/windows/desktop/api/Gpmgmt/nn-gpmgmt-igpmbackup) object was created, in local time.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **Date**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Timestamp(
  [out] DATE* pVal
);
```


</dt> </dl> </dd> </dl>

 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Header<br/>                   | <dl> <dt>Gpmgmt.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Gpmgmt.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Gpmgmt.dll</dt> </dl> |
| IID<br/>                      | IID\_IGPMBackup is defined as D8A16A35-3B0D-416B-8D02-4DF6F95A7119<br/>         |



## See also

<dl> <dt>

[**IGPMBackup**](/previous-versions/windows/desktop/api/Gpmgmt/nn-gpmgmt-igpmbackup)
</dt> <dt>

[**IGPMBackupCollection**](/previous-versions/windows/desktop/api/Gpmgmt/nn-gpmgmt-igpmbackupcollection)
</dt> <dt>

[**IGPMBackupDir**](/previous-versions/windows/desktop/api/Gpmgmt/nn-gpmgmt-igpmbackupdir)
</dt> </dl>

 

 





