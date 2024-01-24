---
description: WMI return codes that indicate status and do not indicate an error.
ms.assetid: 36faa3fb-9496-47ca-bdba-f8eb52a06ff7
ms.tgt_platform: multiple
title: WMI Non-Error Constants (WbemCli.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WMI Non-Error Constants

WMI return codes that indicate status and do not indicate an error.

If an operation does not result in an error, WMI returns one of the following codes as an **HRESULT** that indicates the status of the operation.

> [!Note]  
> Some methods in WMI classes can return system and network error codes (64 for example). You can check the definition of these types of error codes by using the **net helpmsg** command in the command prompt window. For example, the command **net helpmsg 64** returns the message: The specified network name is no longer available.

 

In C++, you can call [**FormatMessage**](/windows/desktop/api/winbase/nf-winbase-formatmessage) and specify **C:\\Windows\\System32\\wbem\\wmiutils.dll** as the message module.

<dl> <dt>

<span id="WBEM_S_NO_ERROR"></span><span id="wbem_s_no_error"></span>**WBEM\_S\_NO\_ERROR**
</dt> <dd> <dl> <dt>

0 (0x0)
</dt> <dt>



The operation was successful.


</dt> </dl> </dd> <dt>

<span id="WBEM_S_FALSE"></span><span id="wbem_s_false"></span>**WBEM\_S\_FALSE**
</dt> <dd> <dl> <dt>

1 (0x1)
</dt> <dt>



No more objects are available, the number of objects returned is less than the number requested, or this is the end of an enumeration. This value is also returned when this method is called with a value of 0 for the *uCount* parameter.


</dt> </dl> </dd> <dt>

<span id="WBEM_S_ALREADY_EXISTS"></span><span id="wbem_s_already_exists"></span>**WBEM\_S\_ALREADY\_EXISTS**
</dt> <dd> <dl> <dt>

262145 (0x40001)
</dt> <dt>



An attempt was made to create an object or class that already exists.


</dt> </dl> </dd> <dt>

<span id="WBEM_S_RESET_TO_DEFAULT"></span><span id="wbem_s_reset_to_default"></span>**WBEM\_S\_RESET\_TO\_DEFAULT**
</dt> <dd> <dl> <dt>

262146 (0x40002)
</dt> <dt>



An overridden property was deleted. This value is returned to signal that the original non-overridden value has been restored as a result of the deletion.


</dt> </dl> </dd> <dt>

<span id="WBEM_S_DIFFERENT"></span><span id="wbem_s_different"></span>**WBEM\_S\_DIFFERENT**
</dt> <dd> <dl> <dt>

262147 (0x40003)
</dt> <dt>



The items (objects, classes, and so on) that are being compared are not identical.


</dt> </dl> </dd> <dt>

<span id="WBEM_S_TIMEDOUT"></span><span id="wbem_s_timedout"></span>**WBEM\_S\_TIMEDOUT**
</dt> <dd> <dl> <dt>

262148 (0x40004)
</dt> <dt>



A call timed out. This is not an error condition. Therefore, some results may have also been returned.


</dt> </dl> </dd> <dt>

<span id="WBEM_S_NO_MORE_DATA"></span><span id="wbem_s_no_more_data"></span>**WBEM\_S\_NO\_MORE\_DATA**
</dt> <dd> <dl> <dt>

262149 (0x40005)
</dt> <dt>



No more data is available from the enumeration, and the user must terminate the enumeration.


</dt> </dl> </dd> <dt>

<span id="WBEM_S_OPERATION_CANCELLED"></span><span id="wbem_s_operation_cancelled"></span>**WBEM\_S\_OPERATION\_CANCELLED**
</dt> <dd> <dl> <dt>

262150 (0x40006)
</dt> <dt>



The operation was intentionally or unintentionally canceled.


</dt> </dl> </dd> <dt>

<span id="WBEM_S_PENDING"></span><span id="wbem_s_pending"></span>**WBEM\_S\_PENDING**
</dt> <dd> <dl> <dt>

262151 (0x40007)
</dt> <dt>



A request is still in progress, and the results are not yet available.


</dt> </dl> </dd> <dt>

<span id="WBEM_S_DUPLICATE_OBJECTS"></span><span id="wbem_s_duplicate_objects"></span>**WBEM\_S\_DUPLICATE\_OBJECTS**
</dt> <dd> <dl> <dt>

262152 (0x40008)
</dt> <dt>



More than one copy of the same object was detected in the result set of an enumeration.


</dt> </dl> </dd> <dt>

<span id="WBEM_S_ACCESS_DENIED"></span><span id="wbem_s_access_denied"></span>**WBEM\_S\_ACCESS\_DENIED**
</dt> <dd> <dl> <dt>

262153 (0x40009)
</dt> <dt>



The user was denied access to some but not all resources.


</dt> </dl> </dd> <dt>

<span id="WBEM_S_PARTIAL_RESULTS"></span><span id="wbem_s_partial_results"></span>**WBEM\_S\_PARTIAL\_RESULTS**
</dt> <dd> <dl> <dt>

262160 (0x40010)
</dt> <dt>



The user did not receive all of the objects requested due to inaccessible resources (other than security violations).


</dt> </dl> </dd> <dt>

<span id="WBEM_S_LIMITED_SERVICE"></span><span id="wbem_s_limited_service"></span>**WBEM\_S\_LIMITED\_SERVICE**
</dt> <dd> <dl> <dt>

274433 (0x43001)
</dt> <dt>



The provider is capable of limited service.


</dt> </dl> </dd> <dt>

<span id="WBEM_S_INDIRECTLY_UPDATED"></span><span id="wbem_s_indirectly_updated"></span>**WBEM\_S\_INDIRECTLY\_UPDATED**
</dt> <dd> <dl> <dt>

274434 (0x43002)
</dt> <dt>



Reserved for future use.


</dt> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Header<br/>                   | <dl> <dt>WbemCli.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>WbemCli.idl</dt> </dl> |



## See also

<dl> <dt>

[WMI Return Codes](wmi-return-codes.md)
</dt> </dl>

 

