---
title: MicrosoftNLB\_ExtendedStatus class
description: The MicrosoftNLB\_ExtendedStatus WMI class is used by the Network Load Balancing provider to report error codes specific to Network Load Balancing.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '01d7a959-0977-4bf1-9b33-c4b046d7b777'
ms.prod: 'windows-server-dev'
ms.technology:
- 'network-load-balancing'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MicrosoftNLB_ExtendedStatus class", "MicrosoftNLB_ExtendedStatus class, described"]
topic_type:
- apiref
api_name:
- MicrosoftNLB_ExtendedStatus
- MicrosoftNLB_ExtendedStatus.Description
- MicrosoftNLB_ExtendedStatus.Operation
- MicrosoftNLB_ExtendedStatus.ParameterInfo
- MicrosoftNLB_ExtendedStatus.ProviderName
- MicrosoftNLB_ExtendedStatus.StatusCode
api_location:
- WlbsProv.dll
api_type:
- DllExport
---

# MicrosoftNLB\_ExtendedStatus class

The **MicrosoftNLB\_ExtendedStatus** [*WMI class*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-22-gly) is used by the Network Load Balancing [*provider*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-9-gly) to report error codes specific to Network Load Balancing.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("Microsoft|NLB_Provider|V1.0"), AMENDMENT]
class MicrosoftNLB_ExtendedStatus : __ExtendedStatus
{
  string Description;
  string Operation;
  string ParameterInfo;
  string ProviderName;
  uint32 StatusCode;
};
```

## Members

The **MicrosoftNLB\_ExtendedStatus** class has these types of members:

-   [Properties](#properties)

### Properties

The **MicrosoftNLB\_ExtendedStatus** class has these properties.

<dl> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Any user-defined string that describes an error or operational status.

This property is inherited from [**\_\_ExtendedStatus**](https://msdn.microsoft.com/library/aa394645).

</dd> <dt>

**Operation**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Operation that takes place at the time of a failure or anomaly. Typically, Windows Management Instrumentation (WMI) sets this property to the name of a COM API for WMI method such as the following: [**IWbemServices::CreateInstanceEnum**](https://msdn.microsoft.com/library/aa392097).

This property is inherited from [**\_\_ExtendedStatus**](https://msdn.microsoft.com/library/aa394645).

</dd> <dt>

**ParameterInfo**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Parameters involved in an error or status change. For example, if an application attempts to retrieve a class that does not exist, this property is set to the offending class name.

This property is inherited from [**\_\_ExtendedStatus**](https://msdn.microsoft.com/library/aa394645).

</dd> <dt>

**ProviderName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Identifies the provider that causes or reports an error or status change. If a provider is not involved, this string is set to "Windows Management".

This property is inherited from [**\_\_ExtendedStatus**](https://msdn.microsoft.com/library/aa394645).

</dd> <dt>

**StatusCode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("StatusCode")
</dt> </dl>

Contains Network Load Balancing and Winsock error codes. The following values map constants defined for Network Load Balancing but do not include Winsock error codes.

<dt>

<span id="WLBS_BAD_PASSW"></span><span id="wlbs_bad_passw"></span>

**WLBS\_BAD\_PASSW** (1101)


</dt> <dd></dd> <dt>

<span id="WLBS_IO_ERROR"></span><span id="wlbs_io_error"></span>

**WLBS\_IO\_ERROR** (1102)


</dt> <dd></dd> <dt>

<span id="WLBS_BAD_PARAMS"></span><span id="wlbs_bad_params"></span>

**WLBS\_BAD\_PARAMS** (1003)


</dt> <dd></dd> <dt>

<span id="WLBS_NOT_FOUND"></span><span id="wlbs_not_found"></span>

**WLBS\_NOT\_FOUND** (1004)


</dt> <dd></dd> <dt>

<span id="WLBS_TIMEOUT"></span><span id="wlbs_timeout"></span>

**WLBS\_TIMEOUT** (1103)


</dt> <dd></dd> <dt>

<span id="WLBS_PORT_OVERLAP"></span><span id="wlbs_port_overlap"></span>

**WLBS\_PORT\_OVERLAP** (1150)


</dt> <dd></dd> <dt>

<span id="WLBS_BAD_PORT_PARAMS"></span><span id="wlbs_bad_port_params"></span>

**WLBS\_BAD\_PORT\_PARAMS** (1151)


</dt> <dd></dd> <dt>

<span id="WLBS_MAX_PORT_RULES"></span><span id="wlbs_max_port_rules"></span>

**WLBS\_MAX\_PORT\_RULES** (1152)


</dt> <dd></dd> <dt>

<span id="WLBS_REG_ERROR"></span><span id="wlbs_reg_error"></span>

**WLBS\_REG\_ERROR** (1154)


</dt> <dd></dd> </dl>

For a description of the values 1101 through 1154, see the [Standard Return Values](standard-return-values.md).

</dd> </dl>

## Remarks

The **MicrosoftNLB\_ExtendedStatus** class is derived from the **\_\_ExtendedStatus** class WMI system class.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\MicrosoftNLB<br/>                                                           |
| MOF<br/>                      | <dl> <dt>WlbsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WlbsProv.dll</dt> </dl> |



 

 





