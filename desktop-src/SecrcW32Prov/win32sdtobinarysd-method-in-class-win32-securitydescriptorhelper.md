---
Description: 'Converts a Win32\_SecurityDescriptor instance to a security descriptor in binary byte array format.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '6a9442f3-b6e5-4144-b0b1-4daa8a58507d'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'Win32SDToBinarySD method of the Win32\_SecurityDescriptorHelper class'
---

# Win32SDToBinarySD method of the Win32\_SecurityDescriptorHelper class

The **Win32SDToBinarySD** WMI class method converts a [**Win32\_SecurityDescriptor**](win32-securitydescriptor.md) instance to a [*security descriptor*](https://msdn.microsoft.com/library/aa390836#wmi-gloss-security-descriptor) in binary byte array format.

## Syntax


```mof
uint32 Win32SDToBinarySD(
  [in]  __SecurityDescriptor Descriptor,
  [out] uint8                BinarySD[]
);
```



## Parameters

<dl> <dt>

*Descriptor* \[in\]
</dt> <dd>

Security descriptor in [**\_\_SecurityDescriptor**](https://msdn.microsoft.com/library/aa394673) format.

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
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
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

 

 




