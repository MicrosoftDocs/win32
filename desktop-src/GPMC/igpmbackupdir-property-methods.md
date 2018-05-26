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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# IGPMBackupDir Property Methods

The property method of the [**IGPMBackupDir**](/windows/previous-versions/Gpmgmt/nn-gpmgmt-igpmbackupdir?branch=master) interface gets the property that is described in the following table. For a general discussion of property methods, see [**Interface Property Methods**](https://msdn.microsoft.com/library/aa746378) in the Active Directory Service Interfaces (ADSI) documentation.

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

[**IGPMBackupDir**](/windows/previous-versions/Gpmgmt/nn-gpmgmt-igpmbackupdir?branch=master)
</dt> <dt>

[**IGPMBackup**](/windows/previous-versions/Gpmgmt/nn-gpmgmt-igpmbackup?branch=master)
</dt> <dt>

[**IGPMBackupCollection**](/windows/previous-versions/Gpmgmt/nn-gpmgmt-igpmbackupcollection?branch=master)
</dt> </dl>

 

 





