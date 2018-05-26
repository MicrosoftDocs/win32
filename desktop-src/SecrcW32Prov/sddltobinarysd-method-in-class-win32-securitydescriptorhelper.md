---
Description: Converts a security descriptor in Security Descriptor Definition Language (SDDL) string format to a binary byte array security descriptor format.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ea8418b3-ec3e-4fca-ab47-aa51f49f6152
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: SDDLToBinarySD method of the Win32\_SecurityDescriptorHelper class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SDDLToBinarySD method of the Win32\_SecurityDescriptorHelper class

The **SDDLToBinarySD** method converts a [*security descriptor*](https://msdn.microsoft.com/library/aa390836#wmi-gloss-security-descriptor) in [Security Descriptor Definition Language](https://msdn.microsoft.com/library/windows/desktop/aa379570) (SDDL) string format to a binary byte array security descriptor format.

## Syntax


```mof
uint32 SDDLToBinarySD(
  [in]  string SDDL,
  [out] uint8  BinarySD[]
);
```



## Parameters

<dl> <dt>

*SDDL* \[in\]
</dt> <dd>

Security descriptor in SDDL format.

</dd> <dt>

*BinarySD* \[out\]
</dt> <dd>

Security descriptor in binary byte array format.

</dd> </dl>

## Return value

Returns one of the values listed in the following list.

<dl> <dt>

**S\_OK**
</dt> <dd>

0 (0x0)

The call was successful. The scripting and Visual Basic constant is **wbemNoErr**.

</dd> <dt>

**WBEM\_E\_INVALID\_PARAMETER**
</dt> <dd>

2147749896 (0x80041008)

One of the parameters to the call is not correct. The scripting and Visual Basic constant is **wbemErrInvalidParameter**.

</dd> <dt>

**WBEM\_E\_PROVIDER\_FAILURE**
</dt> <dd>

2147749892 (0x80041004)

Provider has failed at some time other than during initialization. The scripting and Visual Basic constant is **wbemErrProviderFailure**.

</dd> <dt>

**WBEM\_E\_OUT\_OF\_MEMORY**
</dt> <dd>

2147749894 (0x80041006)

Not enough memory for the operation. The scripting and Visual Basic constant is **wbemErrOutOfMemory**.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMv2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Secrcw32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_SecurityDescriptorHelper**](win32-securitydescriptorhelper.md)
</dt> <dt>

[WMI Security Descriptor Objects](https://msdn.microsoft.com/library/aa394577)
</dt> <dt>

[Changing Access Security on Securable Objects](https://msdn.microsoft.com/library/aa384905)
</dt> </dl>

 

 




