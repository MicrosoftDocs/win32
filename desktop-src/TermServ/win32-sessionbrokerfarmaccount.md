---
title: Win32_SessionBrokerFarmAccount class
description: The Win32\_SessionBrokerFarmAccount class is no longer available for use as of Windows Server 2012. | Win32_SessionBrokerFarmAccount class
ms.assetid: a76ade0f-cd94-438c-bc07-30dc4b4ee6c8
ms.tgt_platform: multiple
keywords:
- Win32_SessionBrokerFarmAccount class Remote Desktop Services
- Win32_SessionBrokerFarmAccount class Remote Desktop Services , described
topic_type:
- apiref
api_name:
- Win32_SessionBrokerFarmAccount
- Win32_SessionBrokerFarmAccount.FarmName
- Win32_SessionBrokerFarmAccount.Manual
- Win32_SessionBrokerFarmAccount.AccountName
- Win32_SessionBrokerFarmAccount.AccountDomain
- Win32_SessionBrokerFarmAccount.AccountPassword
- Win32_SessionBrokerFarmAccount.AccountSPN1
- Win32_SessionBrokerFarmAccount.AccountSPN2
- Win32_SessionBrokerFarmAccount.ComputerDNSName
api_location:
- TssdWmi.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Win32\_SessionBrokerFarmAccount class

\[The **Win32\_SessionBrokerFarmAccount** class is no longer available for use as of Windows Server 2012.\]

Defines a session broker farm account.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("Win32_WIN32_SESSIONBROKERFARMACCOUNT_Prov"), AMENDMENT]
class Win32_SessionBrokerFarmAccount
{
  string  FarmName;
  boolean Manual;
  string  AccountName;
  string  AccountDomain;
  string  AccountPassword;
  string  AccountSPN1;
  string  AccountSPN2;
  string  ComputerDNSName;
};
```

## Members

The **Win32\_SessionBrokerFarmAccount** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Win32\_SessionBrokerFarmAccount** class has these methods.



| Method                                                      | Description                          |
|:------------------------------------------------------------|:-------------------------------------|
| [**DeleteEx**](deleteex-win32-sessionbrokerfarmaccount.md) | Deletes the farm account.<br/> |



 

### Properties

The **Win32\_SessionBrokerFarmAccount** class has these properties.

<dl> <dt>

**AccountDomain**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The name of the domain the farm account belongs to.

</dd> <dt>

**AccountName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The name of the farm account.

</dd> <dt>

**AccountPassword**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The password of the farm account.

</dd> <dt>

**AccountSPN1**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The first service principal name (SPN) associated with the farm account.

</dd> <dt>

**AccountSPN2**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The second SPN associated with the farm account.

</dd> <dt>

**ComputerDNSName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The DNS name of the computer associated with the farm account.

</dd> <dt>

**FarmName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

The name of the session broker farm.

</dd> <dt>

**Manual**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates if the password for the account is updated manually.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                      |
| End of client support<br/>    | None supported<br/>                                                              |
| End of server support<br/>    | Windows Server 2008 R2<br/>                                                      |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                               |
| MOF<br/>                      | <dl> <dt>TssdWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>TssdWmi.dll</dt> </dl> |



 

