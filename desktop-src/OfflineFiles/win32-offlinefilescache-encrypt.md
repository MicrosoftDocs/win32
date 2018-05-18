---
Description: 'Encrypts or unencrypts the contents of the Offline Files cache that are cached for the calling user.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: 'f38d1668-1403-46af-8688-3ae6402e4ee9'
ms.prod: 'windows-server-dev'
ms.technology: 'offline-files'
ms.tgt_platform: multiple
title: 'Encrypt method of the Win32\_OfflineFilesCache class'
---

# Encrypt method of the Win32\_OfflineFilesCache class

Encrypts or unencrypts the contents of the Offline Files cache that are cached for the calling user. When the cache is encrypted, all files subsequently cached are automatically encrypted. When the cache is unencrypted, all files that are subsequently cached are cached unencrypted.

## Syntax


```mof
uint32 Encrypt(
  [in] boolean Encrypt,
  [in] uint32  Flags
);
```



## Parameters

<dl> <dt>

*Encrypt* \[in\]
</dt> <dd>

**TRUE** to encrypt, **FALSE** to unencrypt.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

This parameter can be one or more of the following values.

<dt>

<span id="OfflineFilesEncryptionControlFlagLowPriority"></span><span id="offlinefilesencryptioncontrolflaglowpriority"></span><span id="OFFLINEFILESENCRYPTIONCONTROLFLAGLOWPRIORITY"></span>

<span id="OfflineFilesEncryptionControlFlagLowPriority"></span><span id="offlinefilesencryptioncontrolflaglowpriority"></span><span id="OFFLINEFILESENCRYPTIONCONTROLFLAGLOWPRIORITY"></span>**OfflineFilesEncryptionControlFlagLowPriority** (0x00000200)


</dt> <dd>

Reserved for future use.

</dd> <dt>

<span id="OfflineFilesEncryptionControlFlagAsyncProgress"></span><span id="offlinefilesencryptioncontrolflagasyncprogress"></span><span id="OFFLINEFILESENCRYPTIONCONTROLFLAGASYNCPROGRESS"></span>

<span id="OfflineFilesEncryptionControlFlagAsyncProgress"></span><span id="offlinefilesencryptioncontrolflagasyncprogress"></span><span id="OFFLINEFILESENCRYPTIONCONTROLFLAGASYNCPROGRESS"></span>**OfflineFilesEncryptionControlFlagAsyncProgress** (0x00000400)


</dt> <dd>

Progress is reported to the progress interface asynchronously with the actual operations. If this flag is not set, progress is reported synchronously with each operation.

</dd> <dt>

<span id="OfflineFilesEncryptionControlFlagInteractive"></span><span id="offlinefilesencryptioncontrolflaginteractive"></span><span id="OFFLINEFILESENCRYPTIONCONTROLFLAGINTERACTIVE"></span>

<span id="OfflineFilesEncryptionControlFlagInteractive"></span><span id="offlinefilesencryptioncontrolflaginteractive"></span><span id="OFFLINEFILESENCRYPTIONCONTROLFLAGINTERACTIVE"></span>**OfflineFilesEncryptionControlFlagInteractive** (0x00000800)


</dt> <dd>

Set this flag if the operation is allowed to display user interface elements as necessary. An example is the system's credential-request dialog.

</dd> <dt>

<span id="OfflineFilesEncryptionControlFlagConsole"></span><span id="offlinefilesencryptioncontrolflagconsole"></span><span id="OFFLINEFILESENCRYPTIONCONTROLFLAGCONSOLE"></span>

<span id="OfflineFilesEncryptionControlFlagConsole"></span><span id="offlinefilesencryptioncontrolflagconsole"></span><span id="OFFLINEFILESENCRYPTIONCONTROLFLAGCONSOLE"></span>**OfflineFilesEncryptionControlFlagConsole** (0x00001000)


</dt> <dd>

This flag is ignored if the **OfflineFilesEncryptionControlFlagInteractive** flag is not set. If the **OfflineFilesEncryptionControlFlagInteractive** flag is set, this flag indicates that any UI produced should be directed to the console window associated with the process invoking the operation.

</dd> <dt>

<span id="OfflineFilesEncryptionControlFlagBackground"></span><span id="offlinefilesencryptioncontrolflagbackground"></span><span id="OFFLINEFILESENCRYPTIONCONTROLFLAGBACKGROUND"></span>

<span id="OfflineFilesEncryptionControlFlagBackground"></span><span id="offlinefilesencryptioncontrolflagbackground"></span><span id="OFFLINEFILESENCRYPTIONCONTROLFLAGBACKGROUND"></span>**OfflineFilesEncryptionControlFlagBackground** (0x00010000)


</dt> <dd>

Set this flag if you want the encryption operation to avoid sharing violations in the event that an application opens a file that is currently open for the encryption operation. When that scenario occurs and this flag is set, the encryption operation immediately stops processing that particular file at that time. This flag is primarily used by the Offline Files service when ensuring cache encryption at user logon. Normally, a client calling this method would not set this flag.

</dd> </dl> </dd> </dl>

## Return value

This method returns either a [WMI return code](https://msdn.microsoft.com/library/aa394574) or a [system error code](https://msdn.microsoft.com/library/windows/desktop/ms681381).

## Remarks

The cancellation of this operation does not restore the cached files to their prior encryption state. This may leave the cache in a partially encrypted or unencrypted state. The same condition can occur if the operation is aborted due to an error. To resolve the partial state, repeat the operation until successful completion.

Also note that the Offline Files service automatically performs the encryption operation in the background following user logon. This ensures that all files cached by that user are in the correct state—encrypted or unencrypted—to match the state of the cache.



| If canceled while... | Cache state is...     | New cached files will be... |
|----------------------|-----------------------|-----------------------------|
| Encrypting           | Partially encrypted   | Encrypted                   |
| Unencrypting         | Partially unencrypted | Unencrypted                 |



 

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Namespace<br/>                | Root\\CIMv2<br/>                                                                                 |
| MOF<br/>                      | <dl> <dt>OfflineFilesWmiProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CscObj.dll</dt> </dl>                  |



## See also

<dl> <dt>

[**Win32\_OfflineFilesCache**](win32-offlinefilescache.md)
</dt> </dl>

 

 




