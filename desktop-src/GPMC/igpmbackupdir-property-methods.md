---
title: IGPMBackupDir Property Methods
description: The property method of the IGPMBackupDir interface gets the property that is described in the following table. For a general discussion of property methods, see Interface Property Methods in the Active Directory Service Interfaces (ADSI) documentation.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 303bdd12-9c45-4722-a737-da318e84a735
ms.prod: windows-server-dev
ms.technology: group-policy
ms.tgt_platform: multiple
keywords:
- IGPMBackupDir Property Methods GPMC
topic_type:
- apiref
api_name:
- IGPMBackupDir Property Methods
- IGPMBackupDir.BackupDirectory
- IGPMBackupDir.get_BackupDirectory
api_location:
- Gpmgmt.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IGPMBackupDir Property Methods

The property method of the [**IGPMBackupDir**](/previous-versions/windows/desktop/api/Gpmgmt/nn-gpmgmt-igpmbackupdir) interface gets the property that is described in the following table. For a general discussion of property methods, see [**Interface Property Methods**](https://msdn.microsoft.com/library/aa746378) in the Active Directory Service Interfaces (ADSI) documentation.

## Properties

<dl> <dt>

**BackupDirectory**
</dt> <dd> <dl>

Full path of the file system directory for Group Policy object (GPO) backups.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **String**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_BackupDirectory(
  [out] BSTR* pVal
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
| IID<br/>                      | IID\_IGPMBackupDir is defined as B1568BED-0A93-4ACC-810F-AFE7081019B9<br/>      |



## See also

<dl> <dt>

[**IGPMBackupDir**](/previous-versions/windows/desktop/api/Gpmgmt/nn-gpmgmt-igpmbackupdir)
</dt> <dt>

[**IGPMBackup**](/previous-versions/windows/desktop/api/Gpmgmt/nn-gpmgmt-igpmbackup)
</dt> <dt>

[**IGPMBackupCollection**](/previous-versions/windows/desktop/api/Gpmgmt/nn-gpmgmt-igpmbackupcollection)
</dt> </dl>

 

 





