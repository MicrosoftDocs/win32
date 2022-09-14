---
description: Retrieves the number of times BitLocker has been suspended.
ms.assetid: B8C87352-62BA-4E5D-A273-CE74F3E1A7A8
title: GetSuspendCount method of the Win32_EncryptableVolume class (Activdbg.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_EncryptableVolume.GetSuspendCount
api_type: 
- COM
api_location: 
- Root\CIMV2\Security\MicrosoftVolumeEncryption
---

# GetSuspendCount method of the Win32\_EncryptableVolume class

The **GetSuspendCount** method of the [**Win32\_EncryptableVolume**](win32-encryptablevolume.md) class retrieves the number of reboots before protection will automatically be resumed.

## Syntax


```mof
uint32 GetSuspendCount(
   uint32 SuspendCount
);
```



## Parameters

<dl> <dt>

*SuspendCount* 
</dt> <dd>

An integer value from 0 to 15.

</dd> </dl>

## Return value

This method returns one of the following codes or another error code if it fails.



| Return code                                                                                          | Description                                                                |
|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                 | The method was successful.<br/>                                      |
| <dl> <dt>**ERROR\_NOT\_SUPPORTED**</dt> </dl> | Returned if the volume is not suspended or is not an OS volume.<br/> |



 

## Remarks

This method only applies to the OS volume, and only if it is actually suspended at the time. If the volume is not suspended or is not an OS volume, **ERROR\_NOT\_SUPPORTED** will be returned.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 Enterprise, Windows 8 Pro \[desktop apps only\]<br/>                                    |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\CIMV2\\Security\\MicrosoftVolumeEncryption<br/>                                             |
| Header<br/>                   | <dl> <dt>Activdbg.h</dt> </dl>                   |
| MOF<br/>                      | <dl> <dt>Win32\_encryptablevolume.mof</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_EncryptableVolume**](win32-encryptablevolume.md)
</dt> </dl>

 

 




