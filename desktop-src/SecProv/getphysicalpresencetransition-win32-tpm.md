---
description: Indicates the user action that is needed to perform the Trusted Platform Module (TPM) physical presence operation. Use the SetPhysicalPresenceRequest method to request an operation.
ms.assetid: abbd9702-c3a7-468a-bc83-2b7739d0b7bf
title: GetPhysicalPresenceTransition method of the Win32_Tpm class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_Tpm.GetPhysicalPresenceTransition
api_type: 
- COM
api_location: 
- Win32_tpm.dll
---

# GetPhysicalPresenceTransition method of the Win32\_Tpm class

The **GetPhysicalPresenceTransition** method of the [**Win32\_Tpm**](win32-tpm.md) class indicates the user action that is needed to perform the Trusted Platform Module (TPM) physical presence operation. Use the [**SetPhysicalPresenceRequest**](setphysicalpresencerequest-win32-tpm.md) method to request an operation. The required user action is set for your computer at the time of manufacture. Usually a computer restart is needed.

## Syntax


```mof
uint32 GetPhysicalPresenceTransition(
  [out] uint32 Transition
);
```



## Parameters

<dl> <dt>

*Transition* \[out\]
</dt> <dd>

Type: **uint32**

An integer value that specifies the transition needed to perform a TPM physical presence operation.



| Value                                                                        | Meaning                                                                                                                                                                                                                                                        |
|------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>0</dt> </dl> | No user action is needed to perform a TPM physical presence operation.<br/>                                                                                                                                                                              |
| <dl> <dt>1</dt> </dl> | To perform a TPM physical presence operation, the user must shutdown the computer and then turn it back on by using the power button. The user must be physically present at the computer to accept or reject the change when prompted by the BIOS.<br/> |
| <dl> <dt>2</dt> </dl> | To perform a TPM physical presence operation, the user must restart the computer by using a warm reboot. The user must be physically present at the computer to accept or reject the change when prompted by the BIOS.<br/>                              |
| <dl> <dt>3</dt> </dl> | The required user action is unknown.<br/>                                                                                                                                                                                                                |



 

</dd> </dl>

## Return value

Type: **uint32**

All TPM errors as well as errors specific to TPM Base Services can be returned.

The following table lists some of the common return codes.



| Return code/value                                                                                                                                                                      | Description                                                                                      |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0 (0x0)</dt> </dl>                                      | The method was successful.<br/>                                                            |
| <dl> <dt>**TPM\_E\_PPI\_ACPI\_FAILURE**</dt> <dt>2150171392 (0x80290300)</dt> </dl> | A hardware failure occurred. Consult your computer manufacturer for more information.<br/> |



 

## Remarks

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Windows SDK. They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](../wmisdk/managed-object-format--mof-.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\CIMV2\\Security\\MicrosoftTpm<br/>                                            |
| MOF<br/>                      | <dl> <dt>Win32\_tpm.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Win32\_tpm.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_Tpm**](win32-tpm.md)
</dt> <dt>

[**SetPhysicalPresenceRequest**](setphysicalpresencerequest-win32-tpm.md)
</dt> </dl>

 

 
