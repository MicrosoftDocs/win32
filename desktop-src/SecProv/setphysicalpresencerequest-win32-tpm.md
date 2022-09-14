---
description: Requests a TPM operation that requires physical presence.
ms.assetid: e71eb6ab-b6ab-4586-8999-0a464f11047a
title: SetPhysicalPresenceRequest method of the Win32_Tpm class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_Tpm.SetPhysicalPresenceRequest
api_type: 
- COM
api_location: 
- Win32_tpm.dll
---

# SetPhysicalPresenceRequest method of the Win32\_Tpm class

The **SetPhysicalPresenceRequest** method of the [**Win32\_Tpm**](win32-tpm.md) class requests a TPM operation that requires physical presence. After you have used this method to submit a request, apply the next step indicated in the [**GetPhysicalPresenceTransition**](getphysicalpresencetransition-win32-tpm.md) method. Finally, use the [**GetPhysicalPresenceResponse**](getphysicalpresenceresponse-win32-tpm.md) method to check whether the operation ran successfully. This method suspends BitLocker if calling could cause BitLocker recovery to be required. BitLocker would automatically resume once TPM has been provisioned.

These steps are necessary because physical presence operations can run only after the computer has detected the physically present user.

## Syntax


```mof
uint32 SetPhysicalPresenceRequest(
  [in] uint32 Request
);
```



## Parameters

<dl> <dt>

*Request* \[in\]
</dt> <dd>

Type: **uint32**

An integer value that specifies the requested TPM operation that requires physical presence.



| Value                                                                                                                               | Meaning                                                                                                                                                                                                                                                                                                     |
|-------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>0</dt> </dl>                                                        | No request.<br/> Use this value to clear a pending request.<br/>                                                                                                                                                                                                                                |
| <dl> <dt>1</dt> </dl>                                                        | Enable the TPM.<br/> This operation is reversed by operation 2.<br/> For more information, see the following related methods that do not involve physical presence: [**Enable**](enable-win32-tpm.md) and [**IsEnabled**](isenabled-win32-tpm.md).<br/>                                 |
| <dl> <dt>2</dt> </dl>                                                        | Disable the TPM.<br/> This operation is reversed by operation 1.<br/> For more information, see the following related method that does not involve physical presence: [**Disable**](disable-win32-tpm.md).<br/>                                                                          |
| <dl> <dt>3</dt> </dl>                                                        | Activate the TPM.<br/> This operation is reversed by operation 4.<br/>                                                                                                                                                                                                                          |
| <dl> <dt>4</dt> </dl>                                                        | Deactivate the TPM.<br/> This operation is reversed by operation 3.<br/>                                                                                                                                                                                                                        |
| <dl> <dt>5</dt> </dl>                                                        | Clear the TPM.<br/> This operation cannot be reversed.<br/> For more information, see the following related method that does not involve physical presence: [**Clear**](clear-win32-tpm.md).<br/>                                                                                        |
| <dl> <dt>6</dt> </dl>                                                        | Enable and activate the TPM.<br/> This operation is reversed by operation 7.<br/>                                                                                                                                                                                                               |
| <dl> <dt>7</dt> </dl>                                                        | Deactivate and disable the TPM.<br/> This operation is reversed by operation 6.<br/>                                                                                                                                                                                                            |
| <dl> <dt>8</dt> </dl>                                                        | Allow the installation of a TPM owner.<br/> This operation is reversed by operation 9.<br/>                                                                                                                                                                                                     |
| <dl> <dt>9</dt> </dl>                                                        | Prevent the installation of a TPM owner.<br/> This operation is reversed by operation 8. <br/>                                                                                                                                                                                                  |
| <dl> <dt>10</dt> </dl>                                                       | Enable, activate, and allow the installation of a TPM owner.<br/> This operation is reversed by operation 11.<br/>                                                                                                                                                                              |
| <dl> <dt>11</dt> </dl>                                                       | Deactivate, disable, and prevent the installation of a TPM owner.<br/> This operation is reversed by operation 10.<br/>                                                                                                                                                                         |
| <dl> <dt></dt> <dt>12</dt> </dl> | Deferred Physical PresenceunownedFieldUpgrade<br/> Physical presence setting has been updated.<br/> **Windows 7, Windows Server 2008 R2, Windows Vista and Windows Server 2008:** This value is not supported.<br/>                                                                       |
| <dl> <dt>14</dt> </dl>                                                       | Clear, enable, and activate the TPM.<br/> This operation cannot be reversed.<br/>                                                                                                                                                                                                               |
| <dl> <dt>15</dt> </dl>                                                       | SetNoPPIProvision\_False<br/> Sets the provision that you must be physically presence to set the TPM.<br/> This operation is reversed by operation 16.<br/> **Windows 7, Windows Server 2008 R2, Windows Vista and Windows Server 2008:** This value is not supported.<br/>         |
| <dl> <dt>16</dt> </dl>                                                       | SetNoPPIProvision\_True<br/> Sets the provision that you don't need to be physically presence to set the TPM.<br/> This operation is reversed by operation 15.<br/> **Windows 7, Windows Server 2008 R2, Windows Vista and Windows Server 2008:** This value is not supported.<br/> |
| <dl> <dt>17</dt> </dl>                                                       | SetNoPPIClear\_False<br/> Sets the provision that you must be physically presence to clear the TPM.<br/> This operation is reversed by operation 18.<br/> **Windows 7, Windows Server 2008 R2, Windows Vista and Windows Server 2008:** This value is not supported.<br/>           |
| <dl> <dt>18</dt> </dl>                                                       | SetNoPPIClear\_True<br/> Sets the provision that you don't need to be physically presence to clear the TPM.<br/> This operation is reversed by operation 17.<br/> **Windows 7, Windows Server 2008 R2, Windows Vista and Windows Server 2008:** This value is not supported.<br/>   |
| <dl> <dt>19</dt> </dl>                                                       | SetNoPPIMaintenance\_False<br/> Sets the provision that you must be physically presence to maintain the TPM.<br/> This operation is reversed by operation 20.<br/> **Windows 7, Windows Server 2008 R2, Windows Vista and Windows Server 2008:** This value is not supported.<br/>  |
| <dl> <dt>20</dt> </dl>                                                       | SetNoPPIMaintenance\_True<br/> Sets the provision that you don't need to be physically presence to maintain the TPM.<br/> This operation is reversed by operation 19.<br/> **Windows 7, Windows Server 2008 R2, Windows Vista and Windows Server 2008:** This value is not supported.<br/>   |
| <dl> <dt>21</dt> </dl>                                                       | Enable + Activate + Clear<br/> Enable, activate, and clear the TPM.<br/> **Windows 7, Windows Server 2008 R2, Windows Vista and Windows Server 2008:** This value is not supported.<br/>                                                                                                  |
| <dl> <dt>22</dt> </dl>                                                       | Enable + Activate + Clear + Enable + Activate<br/> Enable, activate, and clear the TPM, and then enable and reactivate the TPM.<br/> **Windows 7, Windows Server 2008 R2, Windows Vista and Windows Server 2008:** This value is not supported.<br/>                                      |



 

</dd> </dl>

## Return value

Type: **uint32**

All TPM errors as well as errors specific to TPM Base Services can be returned.



| Return code/value                                                                                                                                                                       | Description                                                                                                                                                                                                                                  |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0 (0x0)</dt> </dl>                                       | The method was successful.<br/> Use the [**GetPhysicalPresenceTransition**](getphysicalpresencetransition-win32-tpm.md) method to determine the next step that is needed.<br/>                                                  |
| <dl> <dt>**TPM\_E\_PPI\_NOT\_SUPPORTED**</dt> <dt>2150171395 (0x80290303)</dt> </dl> | The computer does not support TPM physical presence operations by using this method.<br/> Consult your computer manufacturer for more information. Your computer's BIOS may have alternate support for configuring the TPM.<br/> |
| <dl> <dt>**TPM\_E\_PPI\_ACPI\_FAILURE**</dt> <dt>2150171392 (0x80290300)</dt> </dl>  | A hardware failure occurred.<br/> Consult your computer manufacturer for more information.<br/>                                                                                                                                  |



 

## Remarks

TPM physical presence operations do not require TPM owner authorization. However, they do require additional steps to help protect against unauthorized changes to the TPM.

Computers that support TPM physical presence operations will attempt to detect the physically present user before running the operation. While computers may differ in how this detection is performed, the idea is to have a physically present user or administrator authorize the operation.

For example, the computer may require the user to restart the computer. After the computer is restarted, the computer can display a BIOS confirmation dialog box that allows the user to confirm the operation by using the keyboard.

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

[**Enable**](enable-win32-tpm.md)
</dt> <dt>

[**IsEnabled**](isenabled-win32-tpm.md)
</dt> <dt>

[**Disable**](disable-win32-tpm.md)
</dt> <dt>

[**Clear**](clear-win32-tpm.md)
</dt> </dl>

 

 
