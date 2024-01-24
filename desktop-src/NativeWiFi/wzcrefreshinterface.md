---
description: Refreshes interface information for a specific wireless LAN interface.
ms.assetid: 584b95b7-3218-4e3e-b5d9-9542488af16b
title: WZCRefreshInterface function (Wzcsapi.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WZCRefreshInterface
api_type: 
- DllExport
api_location: 
- Wzcsapi.dll
---

# WZCRefreshInterface function

\[**WZCRefreshInterface** is not supported as of Windows Vista and Windows Server 2008. Instead, use the [Native Wifi API](native-wifi-reference.md), which provides similar functionality. For more information, see [About the Native Wifi API](about-the-native-wifi-api.md).\]

The **WZCRefreshInterface** function refreshes interface information for a specific wireless LAN interface.

## Syntax


```C++
DWORD WZCRefreshInterface(
  _In_  LPWSTR      pSrvAddr,
  _In_  DWORD       dwInFlags,
  _In_  PINTF_ENTRY pIntf,
  _Out_ LPDWORD     pdwOutFlags
);
```



## Parameters

<dl> <dt>

*pSrvAddr* \[in\]
</dt> <dd>

A pointer to a string containing the name of the computer on which to execute this function. If this parameter is **NULL**, then the Wireless Zero Configuration service is called on the local computer.

If the *pSrvAddr* parameter specified is a remote computer, then the remote computer must support remote RPC calls.

</dd> <dt>

*dwInFlags* \[in\]
</dt> <dd>

A set of fields to be refreshed along with specific refresh actions to be taken. This is a bitmask that can contain any combination of the following flags.



| Value                                                                                                                                                                                                                            | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="INTF_DESCR"></span><span id="intf_descr"></span><dl> <dt>**INTF\_DESCR**</dt> <dt>0x00010000</dt> </dl>             | Refresh the interface description for a wireless LAN interface.<br/> The refreshed interface description can be retrieved by calling the [**WZCQueryInterface**](wzcqueryinterface.md) function with the **INTF\_DESCR** bit set in the *dwInFlags* parameter. The interface description is returned in the **wszDescr** member of the [**INTF\_ENTRY**](intf-entry.md) structure pointed to by the *pIntf* parameter that is returned by the **WZCQueryInterface** function.<br/>                                                           |
| <span id="INTF_NDISMEDIA"></span><span id="intf_ndismedia"></span><dl> <dt>**INTF\_NDISMEDIA**</dt> <dt>0x00020000</dt> </dl> | Refresh the NDIS media information for a wireless LAN interface.<br/> The refreshed NDIS media information can be retrieved by calling the [**WZCQueryInterface**](wzcqueryinterface.md) function with the **INTF\_NDISMEDIA** bit set in the *dwInFlags* parameter. The NDIS media information is returned in the **ulMediaState**, **ulMediaType**, and **ulPhysicalMediaType** members of the [**INTF\_ENTRY**](intf-entry.md) structure pointed to by the *pIntf* parameter that is returned by the **WZCQueryInterface** function.<br/> |
| <span id="INTF_ALL_OIDS"></span><span id="intf_all_oids"></span><dl> <dt>**INTF\_ALL\_OIDS**</dt> <dt>0xFFF00000</dt> </dl>   | Refresh all of the NDIS OIDs for a wireless LAN interface. This option refreshes most of the data for a wireless LAN interface.<br/> The refreshed information can be retrieved by calling the [**WZCQueryInterface**](wzcqueryinterface.md) function.<br/>                                                                                                                                                                                                                                                                                   |



 

</dd> <dt>

*pIntf* \[in\]
</dt> <dd>

A pointer to an [**INTF\_ENTRY**](intf-entry.md) structure that contains the key of the interface to be refreshed.

</dd> <dt>

*pdwOutFlags* \[out\]
</dt> <dd>

A set of fields that were successfully refreshed.

</dd> </dl>

## Return value

If the function succeeds, the return value is ERROR\_SUCCESS.

If the function fails, the return value may be one of the following return codes.



| Return code                                                                                              | Description                                                                                                                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**ERROR\_ARENA\_TRASHED**</dt> </dl>     | The storage control blocks were destroyed. This error is returned if the Wireless Zero Configuration service has not initialized internal objects.<br/>                                                                                                                      |
| <dl> <dt>**ERROR\_FILE\_NOT\_FOUND**</dt> </dl>   | The system cannot find the file specified. This error is returned if the GUID in the **wszGuid** member of the [**INTF\_ENTRY**](intf-entry.md) structure pointed to by the *pIntf* parameter did not match any of the wireless LAN interfaces on the local computer. <br/> |
| <dl> <dt>**ERROR\_INVALID\_PARAMETER**</dt> </dl> | A parameter is incorrect. This error is returned if the *pIntf* parameter is **NULL**. This error is returned if the **wszGuid** member of the [**INTF\_ENTRY**](intf-entry.md) structure pointed to by the *pIntf* parameter is **NULL**. <br/>                            |
| <dl> <dt>**RPC\_STATUS**</dt> </dl>               | Various error codes.<br/>                                                                                                                                                                                                                                                    |



 

## Remarks

The **wszGuid** member of the [**INTF\_ENTRY**](intf-entry.md) structure pointed to by the *pIntf* parameter must contain an interface GUID for a wireless LAN interface. A list of wireless LAN interfaces can be retrieved by calling the [**WZCEnumInterfaces**](wzcenuminterfaces.md) function.

> [!Note]  
> The *Wzcsapi.h* header file and *Wzcsapi.lib* import library file are not available in the Windows SDK.

 

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2 \[desktop apps only\]<br/>                                   |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| End of client support<br/>    | Windows XP with SP3<br/>                                                         |
| End of server support<br/>    | Windows Server 2003<br/>                                                         |
| Header<br/>                   | <dl> <dt>Wzcsapi.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Wzcsapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wzcsapi.dll</dt> </dl> |



## See also

<dl> <dt>

[**WZCEapolGetInterfaceParams**](wzceapolgetinterfaceparams.md)
</dt> <dt>

[**WZCEnumInterfaces**](wzcenuminterfaces.md)
</dt> <dt>

[**WZCQueryInterface**](wzcqueryinterface.md)
</dt> <dt>

[**INTF\_ENTRY**](intf-entry.md)
</dt> </dl>

 

 




