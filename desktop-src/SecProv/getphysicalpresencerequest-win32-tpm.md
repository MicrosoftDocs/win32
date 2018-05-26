---
Description: Returns the pending TPM physical presence operation. Use the SetPhysicalPresenceRequest method to request an operation.
ms.assetid: c50378ae-b465-4c82-beb9-8ecb7939dae2
title: GetPhysicalPresenceRequest method of the Win32\_Tpm class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# GetPhysicalPresenceRequest method of the Win32\_Tpm class

The **GetPhysicalPresenceRequest** method of the [**Win32\_Tpm**](win32-tpm.md) class returns the pending TPM physical presence operation. Use the [**SetPhysicalPresenceRequest**](setphysicalpresencerequest-win32-tpm.md) method to request an operation.

## Syntax


```mof
uint32 GetPhysicalPresenceRequest(
  [out] uint32 Request
);
```



## Parameters

<dl> <dt>

*Request* \[out\]
</dt> <dd>

Type: **uint32**

A value that specifies the pending TPM physical presence operation.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><dl> <dt>0</dt> </dl></td>
<td>No request.<br/></td>
</tr>
<tr class="even">
<td><dl> <dt>1</dt> </dl></td>
<td>Enable the TPM.<br/> This operation is reversed by operation 2. <br/> For more information, see these related methods that do not involve physical presence:
<ul>
<li>[<strong>Enable</strong>](enable-win32-tpm.md)</li>
<li>[<strong>IsEnabled</strong>](isenabled-win32-tpm.md)</li>
</ul>
<br/></td>
</tr>
<tr class="odd">
<td><dl> <dt>2</dt> </dl></td>
<td>Disable the TPM.<br/> This operation is reversed by operation 1. <br/> For more information, see this related method that does not involve physical presence: [<strong>Disable</strong>](disable-win32-tpm.md).<br/></td>
</tr>
<tr class="even">
<td><dl> <dt>3</dt> </dl></td>
<td>Activate the TPM.<br/> This operation is reversed by operation 4.<br/></td>
</tr>
<tr class="odd">
<td><dl> <dt>4</dt> </dl></td>
<td>Deactivate the TPM.<br/> This operation is reversed by operation 3.<br/></td>
</tr>
<tr class="even">
<td><dl> <dt>5</dt> </dl></td>
<td>Clear the TPM.<br/> This operation cannot be reversed.<br/> For more information, see this related method that does not involve physical presence: [<strong>Clear</strong>](clear-win32-tpm.md).<br/></td>
</tr>
<tr class="odd">
<td><dl> <dt>6</dt> </dl></td>
<td>Enable and activate the TPM. <br/> This operation is reversed by operation 7.<br/></td>
</tr>
<tr class="even">
<td><dl> <dt>7</dt> </dl></td>
<td>Deactivate and disable the TPM.<br/> This operation is reversed by operation 6. <br/></td>
</tr>
<tr class="odd">
<td><dl> <dt>8</dt> </dl></td>
<td>Allow the installation of a TPM owner. <br/> This operation is reversed by operation 9.<br/></td>
</tr>
<tr class="even">
<td><dl> <dt>9</dt> </dl></td>
<td>Prevent the installation of a TPM owner.<br/> This operation is reversed by operation 8. <br/></td>
</tr>
<tr class="odd">
<td><dl> <dt>10</dt> </dl></td>
<td>Enable, activate, and allow the installation of a TPM owner.<br/> This operation is reversed by operation 11.<br/></td>
</tr>
<tr class="even">
<td><dl> <dt>11</dt> </dl></td>
<td>Deactivate, disable, and prevent the installation of a TPM owner.<br/> This operation is reversed by operation 10.<br/></td>
</tr>
<tr class="odd">
<td><span></span><dl> <dt><strong></strong></dt> <dt>12</dt> </dl></td>
<td>Deferred Physical PresenceunownedFieldUpgrade<br/> Physical presence setting has been updated.<br/> <strong>Windows 7, Windows Server 2008 R2, Windows Vista and Windows Server 2008:</strong> This value is not supported.<br/></td>
</tr>
<tr class="even">
<td><dl> <dt>14</dt> </dl></td>
<td>Clear, enable, and activate the TPM.<br/> This operation cannot be reversed.<br/></td>
</tr>
<tr class="odd">
<td><dl> <dt>15</dt> </dl></td>
<td>SetNoPPIProvision_False<br/> Sets the provision that you must be physically presence to set the TPM.<br/> This operation is reversed by operation 16.<br/> <strong>Windows 7, Windows Server 2008 R2, Windows Vista and Windows Server 2008:</strong> This value is not supported.<br/></td>
</tr>
<tr class="even">
<td><dl> <dt>16</dt> </dl></td>
<td>SetNoPPIProvision_True<br/> Sets the provision that you don't need to be physically presence to set the TPM.<br/> This operation is reversed by operation 15.<br/> <strong>Windows 7, Windows Server 2008 R2, Windows Vista and Windows Server 2008:</strong> This value is not supported.<br/></td>
</tr>
<tr class="odd">
<td><dl> <dt>17</dt> </dl></td>
<td>SetNoPPIClear_False<br/> Sets the provision that you must be physically presence to clear the TPM.<br/> This operation is reversed by operation 18.<br/> <strong>Windows 7, Windows Server 2008 R2, Windows Vista and Windows Server 2008:</strong> This value is not supported.<br/></td>
</tr>
<tr class="even">
<td><dl> <dt>18</dt> </dl></td>
<td>SetNoPPIClear_True<br/> Sets the provision that you don't need to be physically presence to clear the TPM.<br/> This operation is reversed by operation 17.<br/> <strong>Windows 7, Windows Server 2008 R2, Windows Vista and Windows Server 2008:</strong> This value is not supported.<br/></td>
</tr>
<tr class="odd">
<td><dl> <dt>19</dt> </dl></td>
<td>SetNoPPIMaintenance_False<br/> Sets the provision that you must be physically presence to maintain the TPM.<br/> This operation is reversed by operation 20.<br/> <strong>Windows 7, Windows Server 2008 R2, Windows Vista and Windows Server 2008:</strong> This value is not supported.<br/></td>
</tr>
<tr class="even">
<td><dl> <dt>20</dt> </dl></td>
<td>SetNoPPIMaintenance_True<br/> Sets the provision that you must be physically presence to maintain the TPM.<br/> This operation is reversed by operation 19.<br/> <strong>Windows 7, Windows Server 2008 R2, Windows Vista and Windows Server 2008:</strong> This value is not supported.<br/></td>
</tr>
<tr class="odd">
<td><dl> <dt>21</dt> </dl></td>
<td>Enable + Activate + Clear<br/> Enable, activate, and clear the TPM.<br/> <strong>Windows 7, Windows Server 2008 R2, Windows Vista and Windows Server 2008:</strong> This value is not supported.<br/></td>
</tr>
<tr class="even">
<td><dl> <dt>22</dt> </dl></td>
<td>Enable + Activate + Clear + Enable + Activate<br/> Enable, activate, and clear the TPM, and then enable and reactivate the TPM.<br/> <strong>Windows 7, Windows Server 2008 R2, Windows Vista and Windows Server 2008:</strong> This value is not supported.<br/></td>
</tr>
</tbody>
</table>



 

</dd> </dl>

## Return value

Type: **uint32**

All TPM errors as well as errors specific to TPM Base Services can be returned.

The following table lists the common return codes.



| Return code/value                                                                                                                                                                      | Description                                                                                      |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0 (0x0)</dt> </dl>                                      | The method was successful.<br/>                                                            |
| <dl> <dt>**TPM\_E\_PPI\_ACPI\_FAILURE**</dt> <dt>2150171392 (0x80290300)</dt> </dl> | A hardware failure occurred. Consult your computer manufacturer for more information.<br/> |



 

## Remarks

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Windows SDK. They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](wmi.managed_object_format__mof_).

## Requirements



|                                     |                                                                                           |
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

[**Clear**](clear-win32-tpm.md)
</dt> <dt>

[**Disable**](disable-win32-tpm.md)
</dt> <dt>

[**Enable**](enable-win32-tpm.md)
</dt> <dt>

[**IsEnabled**](isenabled-win32-tpm.md)
</dt> <dt>

[**SetPhysicalPresenceRequest**](setphysicalpresencerequest-win32-tpm.md)
</dt> </dl>

 

 




