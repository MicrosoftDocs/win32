---
title: IGPMRSOP Property Methods
description: The property methods of the interface get and set the properties described in the following table.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8a1b6a38-e2a6-455d-8d50-2545b7d6c5d2
ms.prod: windows-server-dev
ms.technology: group-policy
ms.tgt_platform: multiple
keywords:
- IGPMRSOP Property Methods GPMC
topic_type:
- apiref
api_name:
- IGPMRSOP Property Methods
- IGPMRSOP.Mode
- IGPMRSOP.get_Mode
- IGPMRSOP.Namespace
- IGPMRSOP.get_Namespace
- IGPMRSOP.LoggingComputer
- IGPMRSOP.put_LoggingComputer
- IGPMRSOP.get_LoggingComputer
- IGPMRSOP.LoggingUser
- IGPMRSOP.put_LoggingUser
- IGPMRSOP.get_LoggingUser
- IGPMRSOP.LoggingFlags
- IGPMRSOP.put_LoggingFlags
- IGPMRSOP.get_LoggingFlags
- IGPMRSOP.PlanningFlags
- IGPMRSOP.put_PlanningFlags
- IGPMRSOP.get_PlanningFlags
- IGPMRSOP.PlanningDomainController
- IGPMRSOP.put_PlanningDomainController
- IGPMRSOP.get_PlanningDomainController
- IGPMRSOP.PlanningSiteName
- IGPMRSOP.put_PlanningSiteName
- IGPMRSOP.get_PlanningSiteName
- IGPMRSOP.PlanningUser
- IGPMRSOP.put_PlanningUser
- IGPMRSOP.get_PlanningUser
- IGPMRSOP.PlanningUserSOM
- IGPMRSOP.put_PlanningUserSOM
- IGPMRSOP.get_PlanningUserSOM
- IGPMRSOP.PlanningUserWMIFilters
- IGPMRSOP.put_PlanningUserWMIFilters
- IGPMRSOP.get_PlanningUserWMIFilters
- IGPMRSOP.PlanningUserSecurityGroups
- IGPMRSOP.put_PlanningUserSecurityGroups
- IGPMRSOP.get_PlanningUserSecurityGroups
- IGPMRSOP.PlanningComputer
- IGPMRSOP.put_PlanningComputer
- IGPMRSOP.get_PlanningComputer
- IGPMRSOP.PlanningComputerSOM
- IGPMRSOP.put_PlanningComputerSOM
- IGPMRSOP.get_PlanningComputerSOM
- IGPMRSOP.PlanningComputerWMIFilters
- IGPMRSOP.put_PlanningComputerWMIFilters
- IGPMRSOP.get_PlanningComputerWMIFilters
- IGPMRSOP.PlanningComputerSecurityGroups
- IGPMRSOP.put_PlanningComputerSecurityGroups
- IGPMRSOP.get_PlanningComputerSecurityGroups
api_location:
- Gpmgmt.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IGPMRSOP Property Methods

The property methods of the interface get and set the properties described in the following table. For a general discussion of property methods, see [Interface Property Methods](https://msdn.microsoft.com/library/aa746378) in the ADSI documentation . RSoP planning mode requires a Windows Server domain controller to perform the query.

The [**IGPMRSOP**](/previous-versions/windows/desktop/api/Gpmgmt/nn-gpmgmt-igpmrsop) interface defines the following properties.

## Properties

<dl> <dt>

**LoggingComputer**
</dt> <dd> <dl>

Name of the computer being logged. The computer must have RSoP enabled.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **String**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT put_LoggingComputer(
  [in] BSTR bstrVal
);
HRESULT get_LoggingComputer(
  [out] BSTR* bstrVal
);
```


</dt> </dl> </dd> <dt>

**LoggingFlags**
</dt> <dd> <dl>

Logging mode flags. This property can be one of the following values:

-   **RSOP\_NO\_COMPUTER**

-   **RSOP\_NO\_USER**

**RSOP\_NO\_COMPUTER** and **RSOP\_NO\_USER** must not be specified together.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **Long**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT put_LoggingFlags(
  [in] long lVal
);
HRESULT get_LoggingFlags(
  [out] long* lVal
);
```


</dt> </dl> </dd> <dt>

**LoggingUser**
</dt> <dd> <dl>

Name of the user targeted in logging mode.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **String**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT put_LoggingUser(
  [in] BSTR bstrVal
);
HRESULT get_LoggingUser(
  [out] BSTR* bstrVal
);
```


</dt> </dl> </dd> <dt>

**Mode**
</dt> <dd> <dl>

RSOP mode. This property can be one of the following: **rsopUnknown**, **rsopPlanning**, or **rsopLogging**.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Mode(
  [out] GPMRSOPMode* pVal
);
```


</dt> </dl> </dd> <dt>

**Namespace**
</dt> <dd> <dl>

RSOP WMI namespace generated as output from an RSoP simulation. The format is typically "\\\\computername\\root\\rsop\\namespace".

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **String**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Namespace(
  [out] BSTR* bstrVal
);
```


</dt> </dl> </dd> <dt>

**PlanningComputer**
</dt> <dd> <dl>

Name of the computer to use during planning mode simulation. This is the SAM account name of the Computer object; for example, example\\computer.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **String**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT put_PlanningComputer(
  [in] BSTR bstrVal
);
HRESULT get_PlanningComputer(
  [out] BSTR* bstrVal
);
```


</dt> </dl> </dd> <dt>

**PlanningComputerSecurityGroups**
</dt> <dd> <dl>

The *pvarVal* contains the security groups to associate with the computer during planning mode simulation. The **PlanningComputerSecurityGroups** property returns a **SAFEARRAY** that contains **VARIANT** members. Each **VARIANT** contains a Dispatch pointer to the [**IGPMTrustee**](/previous-versions/windows/desktop/api/Gpmgmt/nn-gpmgmt-igpmtrustee) interface.

Set the **PlanningComputerSecurityGroups** property to an empty **SAFEARRAY** to specify that the RSoP query must be run with no security groups. If you set the property to **VT\_NULL**, or never set the property, the query uses the default security groups for the user. If no security groups are specified, the property returns a **VARIANT** of type **VT\_NULL**. When specifying a list of security groups for a query, "Authenticated Users" and "Everyone" is always implicit and should not be in the list.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **Variant**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT put_PlanningComputerSecurityGroups(
  [in] VARIANT varVal
);
HRESULT get_PlanningComputerSecurityGroups(
  [out] VARIANT* pvarVal
);
```


</dt> </dl> </dd> <dt>

**PlanningComputerSOM**
</dt> <dd> <dl>

Scope of management (SOM) to use for the computer during planning mode simulation. This is the distinguished name of the Active Directory container in which the user object resides, for purposes of the RSoP simulation. It is not necessary that this property be the true location where the object currently resides.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **String**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT put_PlanningComputerSOM(
  [in] BSTR bstrVal
);
HRESULT get_PlanningComputerSOM(
  [out] BSTR* bstrVal
);
```


</dt> </dl> </dd> <dt>

**PlanningComputerWMIFilters**
</dt> <dd> <dl>

The *pvarVal* parameter contains the WMI filters to associate with the computer during planning mode simulation. The **PlanningComputerWMIFilters** property returns a **SAFEARRAY** that contains **VARIANT** members. Each **VARIANT** contains a Dispatch pointer to the [**IGPMWMIFilter**](/previous-versions/windows/desktop/api/Gpmgmt/nn-gpmgmt-igpmwmifilter) interface.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **Variant**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT put_PlanningComputerWMIFilters(
  [in] VARIANT varVal
);
HRESULT get_PlanningComputerWMIFilters(
  [out] VARIANT* pvarVal
);
```


</dt> </dl> </dd> <dt>

**PlanningDomainController**
</dt> <dd> <dl>

Name of the DC to use in planning mode. This can be a DNS name or a NetBIOS name. The DC must be running Windows Server.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **String**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT put_PlanningDomainController(
  [in] BSTR bstrVal
);
HRESULT get_PlanningDomainController(
  [out] BSTR* bstrVal
);
```


</dt> </dl> </dd> <dt>

**PlanningFlags**
</dt> <dd> <dl>

Planning mode flags. The value of this property can be one or more of the following constants combined using logical OR operators.

-   **RSOP\_NO\_COMPUTER**
-   **RSOP\_NO\_USER**
-   **RSOP\_PLANNING\_ASSUME\_SLOW\_LINK**
-   **RSOP\_PLANNING\_ASSUME\_LOOPBACK\_MERGE**
-   **RSOP\_PLANNING\_ASSUME\_LOOPBACK\_REPLACE**
-   **RSOP\_PLANNING\_ASSUME\_USER\_WQLFILTER\_TRUE**
-   **RSOP\_PLANNING\_ASSUME\_COMP\_WQLFILTER\_TRUE**

**RSOP\_NO\_COMPUTER** and **RSOP\_NO\_USER** must not be specified together.

**RSOP\_PLANNING\_ASSUME\_LOOPBACK\_MERGE** and **RSOP\_PLANNING\_ASSUME\_LOOPBACK\_REPLACE** must not be specified together.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **Long**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT put_PlanningFlags(
  [in] long lVal
);
HRESULT get_PlanningFlags(
  [out] long* lVal
);
```


</dt> </dl> </dd> <dt>

**PlanningSiteName**
</dt> <dd> <dl>

Name of the site to use during planning mode simulation; for example, Default-first-site-name.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **String**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT put_PlanningSiteName(
  [in] BSTR bstrVal
);
HRESULT get_PlanningSiteName(
  [out] BSTR* bstrVal
);
```


</dt> </dl> </dd> <dt>

**PlanningUser**
</dt> <dd> <dl>

Name of the user for planning mode simulation. This is the Security Accounts Manager (SAM) account name of the User object; for example, example\\user.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **String**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT put_PlanningUser(
  [in] BSTR bstrVal
);
HRESULT get_PlanningUser(
  [out] BSTR* bstrVal
);
```


</dt> </dl> </dd> <dt>

**PlanningUserSecurityGroups**
</dt> <dd> <dl>

The *pvarVal* parameter contains the security groups to associate with the user during planning mode simulation. The **PlanningUserSecurityGroups** property returns a **SAFEARRAY** of **VARIANT** members. Each **VARIANT** contains a Dispatch pointer to the [**IGPMTrustee**](/previous-versions/windows/desktop/api/Gpmgmt/nn-gpmgmt-igpmtrustee) interface.

Set the **PlanningUserSecurityGroups** property to an empty **SAFEARRAY** to specify that the RSoP query must be run with no security groups. If you set the property to **VT\_NULL**, or never set the property, the query uses the default security groups for the user. If no security groups are specified, the property returns a **VARIANT** of type **VT\_NULL**. When specifying a list of security groups for a query, "Authenticated Users" and "Everyone" is always implicit and should not be in the list.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **Variant**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT put_PlanningUserSecurityGroups(
  [in] VARIANT varVal
);
HRESULT get_PlanningUserSecurityGroups(
  [out] VARIANT* pvarVal
);
```


</dt> </dl> </dd> <dt>

**PlanningUserSOM**
</dt> <dd> <dl>

Name of the user scope of management (SOM) to use during planning mode simulation. This is the distinguished name of the Active Directory container in which the user object resides, for purposes of the RSoP simulation. It is not necessary that this property be the true location where the object currently resides.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **String**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT put_PlanningUserSOM(
  [in] BSTR bstrVal
);
HRESULT get_PlanningUserSOM(
  [out] BSTR* bstrVal
);
```


</dt> </dl> </dd> <dt>

**PlanningUserWMIFilters**
</dt> <dd> <dl>

The *pvarVal* parameter contains the WMI filters to associate with the user during planning mode simulation. The **PlanningUserWMIFilters** property returns a **SAFEARRAY** that contains **VARIANT** members. Each **VARIANT** contains a Dispatch pointer to the [**IGPMWMIFilter**](/previous-versions/windows/desktop/api/Gpmgmt/nn-gpmgmt-igpmwmifilter) interface.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **Variant**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT put_PlanningUserWMIFilters(
  [in] VARIANT varVal
);
HRESULT get_PlanningUserWMIFilters(
  [out] VARIANT* pvarVal
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
| IID<br/>                      | IID\_IGPMRSOP is defined as 49ED785A-3237-4FF2-B1F0-FDF5A8D5A1EE<br/>           |



## See also

<dl> <dt>

[**IGPMRSOP**](/previous-versions/windows/desktop/api/Gpmgmt/nn-gpmgmt-igpmrsop)
</dt> <dt>

[**IGPM**](/previous-versions/windows/desktop/api/Gpmgmt/nn-gpmgmt-igpm)
</dt> <dt>

[**IGPMWMIFilter**](/previous-versions/windows/desktop/api/Gpmgmt/nn-gpmgmt-igpmwmifilter)
</dt> <dt>

[**IGPMTrustee**](/previous-versions/windows/desktop/api/Gpmgmt/nn-gpmgmt-igpmtrustee)
</dt> </dl>

 

 





