---
description: Gets EAPOL configuration parameters for the specified wireless LAN interface.
ms.assetid: 3dce15be-879d-42e9-b8eb-96d52c004acb
title: WZCEapolGetInterfaceParams function (Wzcsapi.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WZCEapolGetInterfaceParams
api_type: 
- DllExport
api_location: 
- Wzcsapi.dll
---

# WZCEapolGetInterfaceParams function

\[**WZCEapolGetInterfaceParams** is no longer supported as of Windows Vista and Windows Server 2008. Instead, use the [Native Wifi API](native-wifi-reference.md), which provides similar functionality. For more information, see [About the Native Wifi API](about-the-native-wifi-api.md).\]

The **WZCEapolGetInterfaceParams** function gets EAPOL configuration parameters for the specified wireless LAN interface.

## Syntax


```C++
DWORD WZCEapolGetInterfaceParams(
  _In_    LPWSTR            pSrvAddr,
  _In_    PWCHAR            pwszGuid,
  _In_    DWORD             dwSizeOfSSID,
  _In_    BYTE              *pbSSID,
  _Inout_ EAPOL_INTF_PARAMS *pIntfParams
);
```



## Parameters

<dl> <dt>

*pSrvAddr* \[in\]
</dt> <dd>

A pointer to a string containing the name of the computer on which to execute this function. If this parameter is **NULL**, then the Wireless Zero Configuration service is called on the local computer.

If the *pSrvAddr* parameter specified is a remote computer, then the remote computer must support remote RPC calls.

</dd> <dt>

*pwszGuid* \[in\]
</dt> <dd>

The GUID of the interface for which data is to be retrieved.

</dd> <dt>

*dwSizeOfSSID* \[in\]
</dt> <dd>

The size of the network identifier for which data is to be retrieved.

</dd> <dt>

*pbSSID* \[in\]
</dt> <dd>

A pointer to the network identifier for which data is to be retrieved.

</dd> <dt>

*pIntfParams* \[in, out\]
</dt> <dd>

A pointer to a [**EAPOL\_INTF\_PARAMS**](eapol-intf-params.md) structure that contains interface parameters.

</dd> </dl>

## Return value

Returns ERROR\_SUCCESS if the operation completes successfully; otherwise, returns one of the Windows system error codes.

## Remarks

If the **WZCEapolGetInterfaceParams** returns ERROR\_SUCCESS, the caller should call [**LocalFree**](/windows/win32/api/winbase/nf-winbase-localfree) to release the internal buffers allocated for the data returned once this information is no longer needed.

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

[**WZCEnumInterfaces**](wzcenuminterfaces.md)
</dt> <dt>

[**WZCQueryInterface**](wzcqueryinterface.md)
</dt> <dt>

[**WZCRefreshInterface**](wzcrefreshinterface.md)
</dt> </dl>

 

 
