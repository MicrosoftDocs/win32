---
description: Indicates if confirmation from a physically present user is required for a given physical presence operation.
ms.assetid: 1CE558B7-EB6F-42CB-B52B-2A0101E90BD5
title: Win32_Tpm::GetPhysicalPresenceConfirmationStatus method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_Tpm.GetPhysicalPresenceConfirmationStatus
api_type: 
- COM
api_location: 
- Win32_tpm.dll
---

# Win32\_Tpm::GetPhysicalPresenceConfirmationStatus method

Indicates if confirmation from a physically present user is required for a given physical presence operation.

This method is only accessible by local administrators.

## Syntax


```C++
uint32 GetPhysicalPresenceConfirmationStatus(
  [in]  uint32 Operation,
  [out] uint32 ConfirmationStatus
);
```



## Parameters

<dl> <dt>

*Operation* \[in\]
</dt> <dd>

An integer value that specifies the requested TPM operation that requires physical presence. Vendor specific commands are supported as well.

The *Operation* parameter may consist of the following values.



| Value                                                                                                                               | Meaning                                                  |
|-------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| <dl> <dt>1</dt> </dl>                                                        | Enable<br/>                                        |
| <dl> <dt>2</dt> </dl>                                                        | Disable<br/>                                       |
| <dl> <dt>3</dt> </dl>                                                        | Activate<br/>                                      |
| <dl> <dt>4</dt> </dl>                                                        | Deactivate<br/>                                    |
| <dl> <dt>5</dt> </dl>                                                        | Clear<br/>                                         |
| <dl> <dt>6</dt> </dl>                                                        | Enable + Activate<br/>                             |
| <dl> <dt>7</dt> </dl>                                                        | Deactivate + Disable<br/>                          |
| <dl> <dt>8</dt> </dl>                                                        | SetOwnerInstall\_True<br/>                         |
| <dl> <dt>9</dt> </dl>                                                        | SetOwnerInstall\_False<br/>                        |
| <dl> <dt>10</dt> </dl>                                                       | Enable + Activate + SetOwnerInstall\_True<br/>     |
| <dl> <dt>11</dt> </dl>                                                       | SetOwnerInstall\_False + Deactivate + Disable<br/> |
| <dl> <dt></dt> <dt>12</dt> </dl> | Deferred Physical PresenceunownedFieldUpgrade<br/> |
| <dl> <dt></dt> <dt>14</dt> </dl> | Clear + Enable + Activate<br/>                     |
| <dl> <dt>15</dt> </dl>                                                       | SetNoPPIProvision\_False<br/>                      |
| <dl> <dt>16</dt> </dl>                                                       | SetNoPPIProvision\_True<br/>                       |
| <dl> <dt>17</dt> </dl>                                                       | SetNoPPIClear\_False<br/>                          |
| <dl> <dt>18</dt> </dl>                                                       | SetNoPPIClear\_True<br/>                           |
| <dl> <dt>19</dt> </dl>                                                       | SetNoPPIMaintenance\_False<br/>                    |
| <dl> <dt>20</dt> </dl>                                                       | SetNoPPIMaintenance\_True<br/>                     |
| <dl> <dt>21</dt> </dl>                                                       | Enable + Activate + Clear<br/>                     |
| <dl> <dt>22</dt> </dl>                                                       | Enable + Activate + Clear + Enable + Activate<br/> |



 

</dd> <dt>

*ConfirmationStatus* \[out\]
</dt> <dd>

Returns the confirmation status for physical presence command.

The *ConfirmationStatus* parameter may consist of the following values.



| Value                                                                        | Meaning                                                                |
|------------------------------------------------------------------------------|------------------------------------------------------------------------|
| <dl> <dt>0</dt> </dl> | Not implemented<br/>                                             |
| <dl> <dt>1</dt> </dl> | BIOS only.<br/>                                                  |
| <dl> <dt>2</dt> </dl> | Blocked for the operating system by the BIOS configuration.<br/> |
| <dl> <dt>3</dt> </dl> | Allowed and physically present user required.<br/>               |
| <dl> <dt>4</dt> </dl> | Allowed and physically present user not required<br/>            |



 

</dd> </dl>

## Return value

All TPM errors as well as errors specific to [TPM Base Services](../tbs/tbs-return-codes.md) can be returned.

Common return codes are listed below.



| Return code/value                                                                                                                                 | Description                           |
|---------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0 (0x0)</dt> </dl> | The method was successful.<br/> |



 

## Remarks

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Windows SDK. They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](../wmisdk/managed-object-format--mof-.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | \\\\.\\root\\CIMV2\\Security\\MicrosoftTpm<br/>                                     |
| MOF<br/>                      | <dl> <dt>Win32\_tpm.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Win32\_tpm.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_Tpm**](win32-tpm.md)
</dt> </dl>

 

 
