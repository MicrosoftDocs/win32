---
title: INetFwV6Mgr GetConnection method
description: The GetConnection method returns the INetFwV6Connection interface identified by a passed in connection ID.
ms.assetid: be349c94-566a-4bae-9c0d-97b105fdeb9a
keywords:
- GetConnection method ICS/ICF
- GetConnection method ICS/ICF , INetFwV6Mgr interface
- INetFwV6Mgr interface ICS/ICF , GetConnection method
topic_type:
- apiref
api_name:
- INetFwV6Mgr.GetConnection
api_location:
- Netfwv6.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# INetFwV6Mgr::GetConnection method

\[The IPv6 Internet Connection Firewall is available for use in the operating systems specified in the Requirements section. Instead, use the [Windows Firewall API](windows-firewall-start-page.md).\]

The **GetConnection** method returns the [**INetFwV6Connection**](inetfwv6connection.md) interface identified by a passed in connection ID. The connection ID is the string form of the GUID for the connection, for example, the **AdapterName** member of the [IP\_ADAPTER\_ADDRESSES](https://msdn.microsoft.com/library/windows/desktop/aa366058) structure for that connection.

## Syntax


```C++
HRESULT GetConnection(
  [in]  BSTR               bstrConnectionId,
  [out] INetFwV6Connection **ppConnection
);
```



## Parameters

<dl> <dt>

*bstrConnectionId* \[in\]
</dt> <dd>

String that contains the connection ID.

</dd> <dt>

*ppConnection* \[out\]
</dt> <dd>

Pointer to a connection interface.

</dd> </dl>

## Return value

If the method succeeds the return value is S\_OK.

If the method fails, the return value is one of the following error codes.



| Return code                                                                                   | Description                                                   |
|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| <dl> <dt>**E\_ABORT**</dt> </dl>       | The operation was aborted.<br/>                         |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | An unspecified error occurred.<br/>                     |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | One of the parameters is invalid.<br/>                  |
| <dl> <dt>**E\_NOINTERFACE**</dt> </dl> | A specified interface is not supported.<br/>            |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>     | A specified method is not implemented.<br/>             |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | The method was unable to allocate required memory.<br/> |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | A pointer passed as a parameter is not valid.<br/>      |
| <dl> <dt>**E\_UNEXPECTED**</dt> </dl>  | The method failed for unknown reasons.<br/>             |



 

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP1 \[desktop apps only\]<br/>                                   |
| Minimum supported server<br/> | None supported<br/>                                                              |
| End of client support<br/>    | Windows XP with SP1<br/>                                                         |
| Redistributable<br/>          | Advanced Networking Pack for Windows XP<br/>                                     |
| Header<br/>                   | <dl> <dt>Netfwv6.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Netfwv6.dll</dt> </dl> |



## See also

<dl> <dt>

[**INetFwV6Connection**](inetfwv6connection.md)
</dt> <dt>

[**INetFwV6Mgr**](inetfwv6mgr.md)
</dt> </dl>

 

 





