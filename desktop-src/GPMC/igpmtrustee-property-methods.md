---
title: IGPMTrustee Property Methods
description: The property methods of the IGPMTrustee interface get the properties described in the following table. For a general discussion of property methods, see Interface Property Methods in the ADSI documentation .
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 25e0e1df-cd22-4e37-9c39-554f236f8496
ms.prod: windows-server-dev
ms.technology: group-policy
ms.tgt_platform: multiple
keywords:
- IGPMTrustee Property Methods GPMC
topic_type:
- apiref
api_name:
- IGPMTrustee Property Methods
- IGPMTrustee.TrusteeDomain
- IGPMTrustee.get_TrusteeDomain
- IGPMTrustee.TrusteeDSPath
- IGPMTrustee.get_TrusteeDSPath
- IGPMTrustee.TrusteeName
- IGPMTrustee.get_TrusteeName
- IGPMTrustee.TrusteeSid
- IGPMTrustee.get_TrusteeSid
- IGPMTrustee.TrusteeType
- IGPMTrustee.get_TrusteeType
api_location:
- Gpmgmt.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IGPMTrustee Property Methods

The property methods of the [**IGPMTrustee**](/previous-versions/windows/desktop/api/Gpmgmt/nn-gpmgmt-igpmtrustee) interface get the properties described in the following table. For a general discussion of property methods, see [**Interface Property Methods**](https://msdn.microsoft.com/library/aa746378) in the ADSI documentation .

## Properties

<dl> <dt>

**TrusteeDomain**
</dt> <dd> <dl>

The trustee domain in NetBIOS format, resolved from the SID.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **String**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_TrusteeDomain(
  [out] BSTR* bstrVal
);
```


</dt> </dl> </dd> <dt>

**TrusteeDSPath**
</dt> <dd> <dl>

Fully qualified distinguished name of the security principal in the directory service. For example, "cn=administrators,cn=builtin,dc=domainname,dc=coname,dc=com". This is the path to the directory service (DS) object that corresponds to the security principal.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **String**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_TrusteeDSPath(
  [out] BSTR* pVal
);
```


</dt> </dl> </dd> <dt>

**TrusteeName**
</dt> <dd> <dl>

Relative distinguished name (RDN) of the trustee, resolved from the SID.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **String**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_TrusteeName(
  [out] BSTR* bstrVal
);
```


</dt> </dl> </dd> <dt>

**TrusteeSid**
</dt> <dd> <dl>

The SID of the trustee.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **String**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_TrusteeSid(
  [out] BSTR* bstrVal
);
```


</dt> </dl> </dd> <dt>

**TrusteeType**
</dt> <dd> <dl>

The type of the trustee. Values include the following:

-   **SidTypeUser**
-   **SidTypeGroup**
-   **SidTypeDomain**
-   **SidTypeAlias**
-   **SidTypeWellKnownGroup**
-   **SidTypeDeletedAccount**
-   **SidTypeInvalid**
-   **SidTypeUnknown**
-   **SidTypeComputer**

The values are declared in Winnt.h.

For more information, see [**SID\_NAME\_USE**](https://msdn.microsoft.com/library/windows/desktop/aa379601) in the Security documentation .

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **String**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_TrusteeType(
  [out] LONG* lVal
);
```


</dt> </dl> </dd> </dl>

 

## Remarks

For more information about security groups, see [How Security Groups are Used in Access Control](https://msdn.microsoft.com/library/ms676928) in the Active Directory Programmer's Guide.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Header<br/>                   | <dl> <dt>Gpmgmt.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Gpmgmt.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Gpmgmt.dll</dt> </dl> |
| IID<br/>                      | IID\_IGPMTrustee is defined as 3B466DA8-C1A4-4B2A-999A-BEFCDD56CEFB<br/>        |



## See also

<dl> <dt>

[**IGPMTrustee**](/previous-versions/windows/desktop/api/Gpmgmt/nn-gpmgmt-igpmtrustee)
</dt> <dt>

[**IGPM**](/previous-versions/windows/desktop/api/Gpmgmt/nn-gpmgmt-igpm)
</dt> <dt>

[**IGPMPermission**](/previous-versions/windows/desktop/api/Gpmgmt/nn-gpmgmt-igpmpermission)
</dt> <dt>

[**IGPMSecurityInfo**](/previous-versions/windows/desktop/api/Gpmgmt/nn-gpmgmt-igpmsecurityinfo)
</dt> </dl>

 

 





