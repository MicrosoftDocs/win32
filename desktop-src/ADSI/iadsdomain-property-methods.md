---
title: IADsDomain Property Methods (Iads.h)
description: The IADsDomain interface methods read and write the properties described in this topic. For more information, see Interface Property Methods.
ms.assetid: ff2c4cbc-a8d5-4db5-85d4-da3367f27fa0
ms.tgt_platform: multiple
keywords:
- IADsDomain Property Methods ADSI
topic_type:
- apiref
api_name:
- IADsDomain Property Methods
- IADsDomain.AutoUnlockInterval
- IADsDomain.get_AutoUnlockInterval
- IADsDomain.put_AutoUnlockInterval
- IADsDomain.IsWorkgroup
- IADsDomain.get_IsWorkgroup
- IADsDomain.LockoutObservationInterval
- IADsDomain.get_LockoutObservationInterval
- IADsDomain.put_LockoutObservationInterval
- IADsDomain.MinPasswordAge
- IADsDomain.get_MinPasswordAge
- IADsDomain.put_MinPasswordAge
- IADsDomain.MinPasswordLength
- IADsDomain.get_MinPasswordLength
- IADsDomain.put_MinPasswordLength
- IADsDomain.MaxBadPasswordsAllowed
- IADsDomain.get_MaxBadPasswordsAllowed
- IADsDomain.put_MaxBadPasswordsAllowed
- IADsDomain.MaxPasswordAge
- IADsDomain.get_MaxPasswordAge
- IADsDomain.put_MaxPasswordAge
- IADsDomain.PasswordAttributes
- IADsDomain.get_PasswordAttributes
- IADsDomain.put_PasswordAttributes
- IADsDomain.PasswordHistoryLength
- IADsDomain.get_PasswordHistoryLength
- IADsDomain.put_PasswordHistoryLength
api_location:
- Activeds.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IADsDomain Property Methods

The [**IADsDomain**](/windows/desktop/api/Iads/nn-iads-iadsdomain) interface methods read and write the properties described in this topic. For more information, see [Interface Property Methods](interface-property-methods.md).

## Properties

<dl> <dt>

**AutoUnlockInterval**
</dt> <dd> <dl>

Indicates the minimum time that must elapse before the account is automatically reenabled.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **LONG**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_AutoUnlockInterval(
  [out] LONG* plAutoUnlockInterval
);
HRESULT put_AutoUnlockInterval(
  [in] LONG lAutoUnlockInterval
);
```


</dt> </dl> </dd> <dt>

**IsWorkgroup**
</dt> <dd> <dl>

This property is no longer implemented.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **VARIANT\_BOOL**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_IsWorkgroup(
  [out] VARIANT_BOOL* retval
);
```


</dt> </dl> </dd> <dt>

**LockoutObservationInterval**
</dt> <dd> <dl>

Indicates the time window during which the bad password count is monitored and accumulated before determining whether the account needs to be locked out. For example, if the number of bad password attempts on an account exceed the threshold (Maximum Bad Passwords Allowed) during the specified time period (Lockout Observation Interval) the account will be locked out by setting the appropriate property in the Login Parameter property set.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **LONG**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_LockoutObservationInterval(
  [out] LONG* plLockoutObservationInterval
);
HRESULT put_LockoutObservationInterval(
  [in] LONG lLockoutObservationInterval
);
```


</dt> </dl> </dd> <dt>

**MaxBadPasswordsAllowed**
</dt> <dd> <dl>

Indicates the maximum number of bad password logins allowed before an account lockout.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **LONG**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_MaxBadPasswordsAllowed(
  [out] LONG* plMaxBadPasswordsAllowed
);
HRESULT put_MaxBadPasswordsAllowed(
  [in] LONG lMaxBadPasswordsAllowed
);
```


</dt> </dl> </dd> <dt>

**MaxPasswordAge**
</dt> <dd> <dl>

Indicates the maximum time interval, in seconds, after which the password must be changed by the user.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **LONG**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_MaxPasswordAge(
  [out] LONG* plMaxPasswordAge
);
RESULT put_MaxPasswordAge(
  [in] LONG lMaxPasswordAge
);
```


</dt> </dl> </dd> <dt>

**MinPasswordAge**
</dt> <dd> <dl>

Indicates the minimum time interval, in seconds, before the password can be changed.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **LONG**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_MinPasswordAge(
  [out] LONG* plMinPasswordAge
);
HRESULT put_MinPasswordAge(
  [in] LONG lMinPasswordAge
);
```


</dt> </dl> </dd> <dt>

**MinPasswordLength**
</dt> <dd> <dl>

Indicates the minimum number of characters that must be used for a password.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **LONG**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_MinPasswordLength(
  [out] LONG* plMinPasswordLength
);
HRESULT put_MinPasswordLength(
  [in] LONG lMinPasswordLength
);
```


</dt> </dl> </dd> <dt>

**PasswordAttributes**
</dt> <dd> <dl>

Indicates restrictions on passwords, as defined by the following list of attributes and values.

> [!Note]  
> For PASSWORD\_ATTR\_COMPLEX, the password must include at least one punctuation mark or non-printable character.

 

<dt>

<span id="PASSWORD_ATTR_NONE"></span><span id="password_attr_none"></span>

**PASSWORD\_ATTR\_NONE** (0x00000000)


</dt> <dd></dd> <dt>

<span id="PASSWORD_ATTR_MIXED_CASE"></span><span id="password_attr_mixed_case"></span>

**PASSWORD\_ATTR\_MIXED\_CASE** (0x00000001)


</dt> <dd></dd> <dt>

<span id="PASSWORD_ATTR_COMPLEX"></span><span id="password_attr_complex"></span>

**PASSWORD\_ATTR\_COMPLEX** (0x00000002)


</dt> <dd></dd> </dl> <dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **LONG**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_PasswordAttributes(
  [out] LONG* plPasswordAttributes
);
HRESULT put_PasswordAttributes(
  [in] LONG lPasswordAttributes
);
```


</dt> </dl> </dd> <dt>

**PasswordHistoryLength**
</dt> <dd> <dl>

Indicates the number of previous passwords saved in the history list. The user cannot reuse a password in the history list.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **LONG**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_PasswordHistoryLength(
  [out] LONG* plPasswordHistoryLength
);
HRESULT put_PasswordHistoryLength(
  [in] LONG lPasswordHistoryLength
);
```


</dt> </dl> </dd> </dl>

 

## Examples

The following code example displays the value of the **PasswordHistoryLength** property.


```VB
Dim dom As IADsDomain
On Error Resume Next

Set dom = GetObject("WinNT://myDomain")

debug.print "PasswordHistoryLength" & dom.PasswordHistoryLength
```



The following code example displays the value of the **PasswordHistoryLength** property.


```C++
LPWSTR adsPath = L"WinNT://myDomain";
LONG nPasswordHistoryLength = 0;

// Bind to the domain object.
hr = ADsGetObject(adsPath,IID_IADsDomain,(void**)&pDomain);
if(FAILED(hr)) {goto Cleanup;}

hr = pDomain->get_PasswordHistoryLength(&nPasswordHistoryLength);
if(FAILED(hr)) {goto Cleanup;}
printf("Password history length: %d",nPasswordHistoryLength);

Cleanup:
    if(pDomain) pDomain->Release();
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Iads.h</dt> </dl>       |
| DLL<br/>                      | <dl> <dt>Activeds.dll</dt> </dl> |
| IID<br/>                      | IID\_IADsDomain is defined as 00E4C220-FD16-11CE-ABC4-02608C9E7553<br/>           |



## See also

<dl> <dt>

[**IADsDomain**](/windows/desktop/api/Iads/nn-iads-iadsdomain)
</dt> <dt>

[Interface Property Methods](interface-property-methods.md)
</dt> </dl>

 

 





