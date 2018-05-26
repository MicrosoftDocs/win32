---
title: CreateFMJAction method of the MSFT\_FSRMFMJAction class
description: Creates a new MSFT\_FSRMFMJAction instance.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d09b47d0-8a55-48ef-ac8c-35593a6cd9bd
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- CreateFMJAction method File Server Resource Manager
- CreateFMJAction method File Server Resource Manager , MSFT_FSRMFMJAction class
- MSFT_FSRMFMJAction class File Server Resource Manager , CreateFMJAction method
topic_type:
- apiref
api_name:
- MSFT_FSRMFMJAction.CreateFMJAction
api_location:
- SrmSvc.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CreateFMJAction method of the MSFT\_FSRMFMJAction class

Creates a new [**MSFT\_FSRMFMJAction**](msft-fsrmfmjaction.md) instance.

## Syntax


```mof
uint64 CreateFMJAction(
  [in]  uint32             Type,
  [in]  string             ExpirationFolder,
  [in]  boolean            RMSFolderOwner,
  [in]  string             RMSFullControlUser[],
  [in]  string             RMSReadUser[],
  [in]  string             RMSWriteUser[],
  [in]  string             RMSTemplate,
  [in]  string             Command,
  [in]  string             WorkingDirectory,
  [in]  string             CommandParameters,
  [in]  uint32             SecurityLevel = LocalService,
  [out] MSFT_FSRMFMJAction Action
);
```



## Parameters

<dl> <dt>

*Type* \[in\]
</dt> <dd>

Specifies the type of the action.

<dt>

<span id="Expiration"></span><span id="expiration"></span><span id="EXPIRATION"></span>

<span id="Expiration"></span><span id="expiration"></span><span id="EXPIRATION"></span>**Expiration** (1)


</dt> <dd>

The action is an expiration action.

</dd> <dt>

<span id="Custom"></span><span id="custom"></span><span id="CUSTOM"></span>

<span id="Custom"></span><span id="custom"></span><span id="CUSTOM"></span>**Custom** (2)


</dt> <dd>

The action is a custom action.

</dd> <dt>

<span id="RMS"></span><span id="rms"></span>

<span id="RMS"></span><span id="rms"></span>**RMS** (3)


</dt> <dd>

The action is a Rights Managed Services (RMS) action.

</dd> </dl> </dd> <dt>

*ExpirationFolder* \[in\]
</dt> <dd>

A string representing a path to a local or remote folder. Optional. Size must not exceed the value of **MAX\_PATH** (260).

This parameter is required when the *Type* parameter is 1 (Expiration).

</dd> <dt>

*RMSFolderOwner* \[in\]
</dt> <dd>

Add the **FolderOwner** to the full control list if **True**. Has no effect if no **FolderOwner** is available for the file.

This parameter is only examined when the *Type* parameter is 3 (RMS) and the *RMSTemplate* parameter is empty.

</dd> <dt>

*RMSFullControlUser* \[in\]
</dt> <dd>

An array of user email addresses to provide with full control. Each string must be less than 1KB in size.

This parameter is required when the *Type* parameter is 3 (RMS) and the *RMSTemplate* parameter is empty.

</dd> <dt>

*RMSReadUser* \[in\]
</dt> <dd>

An array of user email addresses to provide with read access. Each string must be less than 1KB in size.

This parameter is only examined when the *Type* parameter is 3 (RMS) and the *RMSTemplate* parameter is empty.

</dd> <dt>

*RMSWriteUser* \[in\]
</dt> <dd>

An array of user email addresses to provide with write access. Each string must be less than 1KB in size.

This parameter is only examined when the *Type* parameter is 3 (RMS) and the *RMSTemplate* parameter is empty.

</dd> <dt>

*RMSTemplate* \[in\]
</dt> <dd>

The name of an RMS template. Must be fewer than 1000 characters.

This parameter is required when the *Type* parameter is 3 (RMS) and the *RMSFullControlUser* parameter is empty.

</dd> <dt>

*Command* \[in\]
</dt> <dd>

A string that refers to a valid executable file. Must not exceed the length of **MAX\_PATH** (260). Required.

This parameter is required when the *Type* parameter is 2 (Custom).

</dd> <dt>

*WorkingDirectory* \[in\]
</dt> <dd>

A string that refers to a valid path to a folder. Must not exceed the length of **MAX\_PATH** (260). Optional. Remote paths are not supported. The default value is an empty string.

This parameter is only examined when the *Type* parameter is 2 (Custom).

</dd> <dt>

*CommandParameters* \[in\]
</dt> <dd>

A string up to 10KB in size.

This parameter is only examined when the *Type* parameter is 2 (Custom).

</dd> <dt>

*SecurityLevel* \[in\]
</dt> <dd>

The default value is 2 (LocalService).

This parameter is only examined when the *Type* parameter is 2 (Custom).

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

<span id="None"></span><span id="none"></span><span id="NONE"></span>**None** (0)


</dt> <dd>

The security level is not specified.

</dd> <dt>

<span id="NetworkService"></span><span id="networkservice"></span><span id="NETWORKSERVICE"></span>

<span id="NetworkService"></span><span id="networkservice"></span><span id="NETWORKSERVICE"></span>**NetworkService** (1)


</dt> <dd>

The action is run in the context of the [NetworkService Account](https://msdn.microsoft.com/library/windows/desktop/ms684272).

</dd> <dt>

<span id="LocalService"></span><span id="localservice"></span><span id="LOCALSERVICE"></span>

<span id="LocalService"></span><span id="localservice"></span><span id="LOCALSERVICE"></span>**LocalService** (2)


</dt> <dd>

The action is run in the context of the [LocalService Account](https://msdn.microsoft.com/library/windows/desktop/ms684188).

</dd> <dt>

<span id="LocalSystem"></span><span id="localsystem"></span><span id="LOCALSYSTEM"></span>

<span id="LocalSystem"></span><span id="localsystem"></span><span id="LOCALSYSTEM"></span>**LocalSystem** (3)


</dt> <dd>

The action is run in the context of the [LocalSystem Account](https://msdn.microsoft.com/library/windows/desktop/ms684190).

</dd> </dl> </dd> <dt>

*Action* \[out\]
</dt> <dd>

On output contains a new instance of the [**MSFT\_FSRMFMJAction**](msft-fsrmfmjaction.md) class.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\FSRM<br/>                                                 |
| MOF<br/>                      | <dl> <dt>MSFT\_FSRM.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SrmSvc.dll</dt> </dl>     |



## See also

<dl> <dt>

[**MSFT\_FSRMFMJAction**](msft-fsrmfmjaction.md)
</dt> </dl>

 

 





