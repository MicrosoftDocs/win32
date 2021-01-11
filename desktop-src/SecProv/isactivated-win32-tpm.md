---
description: The IsActivated method of the Win32\_Tpm class indicates whether the device is activated.
ms.assetid: 862c386c-c5b5-44d2-89a5-3735b99bf8bc
title: IsActivated method of the Win32_Tpm class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_Tpm.IsActivated
api_type: 
- COM
api_location: 
- Win32_tpm.dll
---

# IsActivated method of the Win32\_Tpm class

The **IsActivated** method of the [**Win32\_Tpm**](win32-tpm.md) class indicates whether the device is activated.

## Syntax


```mof
uint32 IsActivated(
  [out] boolean IsActivated
);
```



## Parameters

<dl> <dt>

*IsActivated* \[out\]
</dt> <dd>

Type: **boolean**

If **true**, the device is activated.

</dd> </dl>

## Return value

Type: **uint32**

All TPM errors as well as errors specific to TPM Base Services can be returned.

Common return codes are listed below.



| Return code/value                                                                                                                                 | Description                           |
|---------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0 (0x0)</dt> </dl> | The method was successful.<br/> |



 

## Remarks

Deactivation is similar to disabled, but operational state changes are possible. According to the Trusted Computing Group (TCG) v1.2 specification only the following commands are available when the device is in a deactivated state.

-   TPM\_ContinueSelfTest
-   TPM\_DSAP
-   TPM\_FlushSpecific
-   TPM\_GetCapability
-   TPM\_GetTestResult
-   TPM\_Init
-   TPM\_OIAP
-   TPM\_OSAP
-   TPM\_OwnerSetDisable
-   TPM\_PCR\_Reset
-   TPM\_PhysicalDisable
-   TPM\_PhysicalEnable
-   TPM\_PhysicalSetDeactivated
-   TPM\_Reset
-   TPM\_SaveState
-   TPM\_SelfTestFull
-   TPM\_SetCapability
-   TPM\_SHA1Complete
-   TPM\_SHA1Start
-   TPM\_SHA1Update
-   TPM\_Startup
-   TPM\_TakeOwnership
-   TPM\_Terminate\_Handle

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
</dt> </dl>

 

 
