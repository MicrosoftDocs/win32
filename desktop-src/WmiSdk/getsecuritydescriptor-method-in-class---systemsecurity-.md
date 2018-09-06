---
Description: Gets the security descriptor that controls access to the WMI namespace to which you are connected. The security descriptor is returned as an instance of\_\_SecurityDescriptor.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b031af45-9237-434d-91db-69222306c615
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: GetSecurityDescriptor method of the __SystemSecurity class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- __SystemSecurity.GetSecurityDescriptor
api_type: 
- COM
api_location: 
- All
---

# GetSecurityDescriptor method of the \_\_SystemSecurity class

The **GetSecurityDescriptor** method gets the security descriptor that controls access to the WMI namespace to which you are connected. The security descriptor is returned as an instance of[**\_\_SecurityDescriptor**](--securitydescriptor.md). For more information, see [Changing Access Security on Securable Objects](changing-access-security-on-securable-objects.md).

## Syntax


```mof
uint32 GetSecurityDescriptor(
  [out] __SystemSecurity Descriptor
);
```



## Parameters

<dl> <dt>

*Descriptor* \[out\]
</dt> <dd>

The security descriptor associated with the WMI namespace.

</dd> </dl>

## Return value

Returns one of the values listed in the following list, or a different value to indicate an error. For more information, see [WMI Return Codes](wmi-return-codes.md) or [**WbemErrorEnum**](/windows/desktop/api/Wbemdisp/ne-wbemdisp-wbemerrorenum).

<dl> <dt>

**0**
</dt> <dd>

Successful completion.

</dd> <dt>

**2**
</dt> <dd>

The user does not have access to the requested information.

</dd> <dt>

**8**
</dt> <dd>

Unknown failure.

</dd> <dt>

**9**
</dt> <dd>

The user does not have adequate privileges to execute the method.

</dd> <dt>

**21**
</dt> <dd>

A parameter specified in the method call is not valid.

</dd> </dl>

## Remarks

The [**Win32\_SecurityDescriptor**](https://msdn.microsoft.com/library/aa394402) instance represents a [**SECURITY\_DESCRIPTOR\_CONTROL**](https://msdn.microsoft.com/library/windows/desktop/aa379566) data type and contains a [*discretionary access control list*](https://msdn.microsoft.com/library/windows/desktop/ms721573#-security-discretionary-access-control-list-gly) (DACL) and a [*system access control list*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-system-access-control-list-gly) (SACL). For more information, see [Access Control Lists](https://msdn.microsoft.com/library/windows/desktop/aa374872).

If the **SeSecurityPrivilege** is not granted or enabled when getting a security descriptor, then only the DACL is returned in the returned security descriptor. For more information, see [**Privilege Constants**](privilege-constants.md) and [Executing Privileged Operations](executing-privileged-operations.md).

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |
| Namespace<br/>                | All WMI namespaces<br/>  |



## See also

<dl> <dt>

[**\_\_SystemSecurity**](--systemsecurity.md)
</dt> <dt>

[Setting Namepace Security Descriptors](setting-namespace-security-descriptors.md)
</dt> </dl>

 

 




