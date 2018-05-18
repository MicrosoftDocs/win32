---
Description: 'Wrapper method used to change the BMC user password.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '2bb884fc-1448-4468-b9ab-ddd65f8bd5e9'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'ChangeUserPassword method of the MSFT\_PCSVDevice class'
---

# ChangeUserPassword method of the MSFT\_PCSVDevice class

Wrapper method used to change the BMC user password.

## Syntax


```mof
uint32 ChangeUserPassword(
  [in]      string              CurrentCredential,
  [in]      string              NewPassword,
  [in, out] CIM_ConcreteJob REF Job
);
```



## Parameters

<dl> <dt>

*CurrentCredential* \[in\]
</dt> <dd>

Delimited string containing both the current username and password, separated by a colon. This is the only way to get the credential object from the Powershell cmdlet.

</dd> <dt>

*NewPassword* \[in\]
</dt> <dd>

Password that will be stored on the BMC as the new password for the user.

</dd> <dt>

*Job* \[in, out\]
</dt> <dd>

Reference to the job spawned if the operation continues after the method returns. (May be **Null** if the task is completed).

</dd> </dl>

## Return value

Indicates the result. Values between 4097 and 32767 are reserved by the DMTF. Values of 32768 and above are reserved for vendor implementations.

<dl> <dt>

**Completed with No Error** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Failed** (2)
</dt> <dt>

**Job Started** (4096)
</dt> <dt>

**DMTF Reserved** (4097–32767)
</dt> <dt>

**Vendor Reserved** (32768–65535)
</dt> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\HardwareManagement<br/>                                   |
| MOF<br/>                      | <dl> <dt>PcsvDevice.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>PCSVDevice.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_PCSVDevice**](msft-pcsvdevice.md)
</dt> </dl>

 

 




