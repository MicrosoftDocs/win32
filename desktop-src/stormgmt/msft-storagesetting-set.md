---
title: Set method of the MSFT\_StorageSetting class
description: Sets the state of various storage settings on this computer.
ms.assetid: '94F98CA7-795B-481C-BE97-B65FF015B761'
keywords: ["Set method Windows Storage Management API", "Set method Windows Storage Management API , MSFT_StorageSetting class", "MSFT_StorageSetting class Windows Storage Management API , Set method"]
topic_type:
- apiref
api_name:
- MSFT_StorageSetting.Set
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
---

# Set method of the MSFT\_StorageSetting class

Sets the state of various storage settings on this computer.

Only the parameters specified will be set on the system.

## Syntax


```mof
UInt32 Set(
  [in] UInt16 NewDiskPolicy,
  [in] UInt32 ScrubPolicy
);
```



## Parameters

<dl> <dt>

*NewDiskPolicy* \[in\]
</dt> <dd>

The new disk policy.



| Value                                                                                                                                                                                                                                                           | Meaning                                                                                                          |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span><dl> <dt>**Unknown**</dt> <dt>0</dt> </dl>                                     | The disk policy is not specified.<br/>                                                                     |
| <span id="Online_All"></span><span id="online_all"></span><span id="ONLINE_ALL"></span><dl> <dt>**Online All**</dt> <dt>1</dt> </dl>                         | All newly discovered disks are brought online and made read/write.<br/>                                    |
| <span id="Offline_Shared"></span><span id="offline_shared"></span><span id="OFFLINE_SHARED"></span><dl> <dt>**Offline Shared**</dt> <dt>2</dt> </dl>         | All newly discovered disks that do not reside on a shared bus are brought online and made read/write.<br/> |
| <span id="Offline_All"></span><span id="offline_all"></span><span id="OFFLINE_ALL"></span><dl> <dt>**Offline All**</dt> <dt>3</dt> </dl>                     | All newly discovered disks remain offline and read-only.<br/>                                              |
| <span id="Offline_Internal"></span><span id="offline_internal"></span><span id="OFFLINE_INTERNAL"></span><dl> <dt>**Offline Internal**</dt> <dt>4</dt> </dl> | All newly discovered disks that do not reside on a shared bus remain offline and read-only.<br/>           |



 

</dd> <dt>

*ScrubPolicy* \[in\]
</dt> <dd>

The file scrub policy of the automatic data integrity scanner.



| Value                                                                        | Meaning                      |
|------------------------------------------------------------------------------|------------------------------|
| <dl> <dt>0</dt> </dl> | Off<br/>               |
| <dl> <dt>1</dt> </dl> | Integrity Streams<br/> |
| <dl> <dt>2</dt> </dl> | All<br/>               |



 

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                   |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_StorageSetting**](msft-storagesetting.md)
</dt> </dl>

 

 





