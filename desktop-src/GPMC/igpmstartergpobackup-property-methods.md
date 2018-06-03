---
title: IGPMStarterGPOBackup Property Methods
description: The property methods of the IGPMStarterGPOBackup interface get the properties described in the following table. For a general discussion of property methods, see Interface Property Methods in the ADSI documentation.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d12b7893-00d2-42cb-8fa4-b200a2d4b340
ms.prod: windows-server-dev
ms.technology: group-policy
ms.tgt_platform: multiple
keywords:
- IGPMStarterGPOBackup Property Methods GPMC
topic_type:
- apiref
api_name:
- IGPMStarterGPOBackup Property Methods
- IGPMStarterGPOBackup.BackupDir
- IGPMStarterGPOBackup.get_BackupDir
- IGPMStarterGPOBackup.Comment
- IGPMStarterGPOBackup.get_Comment
- IGPMStarterGPOBackup.DisplayName
- IGPMStarterGPOBackup.get_DisplayName
- IGPMStarterGPOBackup.Domain
- IGPMStarterGPOBackup.get_Domain
- IGPMStarterGPOBackup.StarterGPOID
- IGPMStarterGPOBackup.get_StarterGPOID
- IGPMStarterGPOBackup.ID
- IGPMStarterGPOBackup.get_ID
- IGPMStarterGPOBackup.Timestamp
- IGPMStarterGPOBackup.get_Timestamp
- IGPMStarterGPOBackup.Type
- IGPMStarterGPOBackup.get_Type
api_location:
- Gpmgmt.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IGPMStarterGPOBackup Property Methods

The property methods of the [**IGPMStarterGPOBackup**](/previous-versions/windows/desktop/api/Gpmgmt/nn-gpmgmt-igpmstartergpobackup) interface get the properties described in the following table. For a general discussion of property methods, see [Interface Property Methods](https://msdn.microsoft.com/library/aa746378) in the ADSI documentation.

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
  [out] BSTR* pbstrBackupDir
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
  [out] BSTR* pbstrComment
);
```


</dt> </dl> </dd> <dt>

**DisplayName**
</dt> <dd> <dl>

Friendly display name of the backed-up Starter GPO.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **String**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_DisplayName(
  [out] BSTR* pbstrDisplayName
);
```


</dt> </dl> </dd> <dt>

**Domain**
</dt> <dd> <dl>

Name of the domain in which the GPO existed when it was backed up. This is a full DNS name, such as, example.microsoft.com.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **String**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Domain(
  [out] BSTR* pbstrTemplateDomain
);
```


</dt> </dl> </dd> <dt>

**ID**
</dt> <dd> <dl>

GUID that uniquely identifies the [**GPMStarterGPOBackup**](/previous-versions/windows/desktop/api/Gpmgmt/nn-gpmgmt-igpmstartergpobackup) object within its backup directory.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **String**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_ID(
  [out] BSTR* pbstrID
);
```


</dt> </dl> </dd> <dt>

**StarterGPOID**
</dt> <dd> <dl>

ID of the backed-up Starter GPO.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **String**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_StarterGPOID(
  [out] BSTR* pbstrTemplateID
);
```


</dt> </dl> </dd> <dt>

**Timestamp**
</dt> <dd> <dl>

Date and time when the [**GPMStarterGPOBackup**](/previous-versions/windows/desktop/api/Gpmgmt/nn-gpmgmt-igpmstartergpobackup) object was created, in local time.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **Date**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Timestamp(
  [out] DATE* pTimestamp
);
```


</dt> </dl> </dd> <dt>

**Type**
</dt> <dd> <dl>

Type of backed-up [**GPMStarterGPO**](/previous-versions/windows/desktop/api/Gpmgmt/nn-gpmgmt-igpmstartergpobackup) object. The type of backed-up **GPMStarterGPO** is a system or custom Starter Group Policy object.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **Date**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Type(
  [out] GPMStarterGPOType* pType
);
```


</dt> </dl> </dd> </dl>

 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Gpmgmt.h</dt> </dl>     |
| IDL<br/>                      | <dl> <dt>Gpmgmt.idl</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Gpmgmt.dll</dt> </dl>   |
| IID<br/>                      | IID\_IGPMStarterGPOBackup is defined as 51D98EDA-A87E-43dd-B80A-0B66EF1938D6<br/> |



## See also

<dl> <dt>

[**IGPMStarterGPOBackup**](/previous-versions/windows/desktop/api/Gpmgmt/nn-gpmgmt-igpmstartergpobackup)
</dt> <dt>

[**IGPMBackupDirEx**](/previous-versions/windows/desktop/api/Gpmgmt/nn-gpmgmt-igpmbackupdirex)
</dt> <dt>

[**IGPMStarterGPOBackupCollection**](/previous-versions/windows/desktop/api/Gpmgmt/nn-gpmgmt-igpmstartergpobackupcollection)
</dt> </dl>

 

 





