---
title: IEnumNetFwV6Connections Next method
description: The Next method retrieves the specified number of connections starting from the current enumeration position.
ms.assetid: 2e340398-b279-4f40-81b7-c74a6c8dbb63
keywords:
- Next method ICS/ICF
- Next method ICS/ICF , IEnumNetFwV6Connections interface
- IEnumNetFwV6Connections interface ICS/ICF , Next method
topic_type:
- apiref
api_name:
- IEnumNetFwV6Connections.Next
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

# IEnumNetFwV6Connections::Next method

\[The IPv6 Internet Connection Firewall is available for use in the operating systems specified in the Requirements section. Instead, use the [Windows Firewall API](windows-firewall-start-page.md).\]

The **Next** method retrieves the specified number of connections starting from the current enumeration position.

## Syntax


```C++
HRESULT Next(
  [in]  ULONG              cElt,
  [out] INetFwV6Connection **rgElt,
  [out] ULONG              *pcEltFetched
);
```



## Parameters

<dl> <dt>

*cElt* \[in\]
</dt> <dd>

Specifies the number of connections to retrieve.

</dd> <dt>

*rgElt* \[out\]
</dt> <dd>

Pointer to a variable that, on successful return, points to an array of pointers to [**INetFwV6Connection**](inetfwv6connection.md) interfaces.

</dd> <dt>

*pcEltFetched* \[out\]
</dt> <dd>

Pointer to a variable that, on successful return, specifies the number of connections actually returned.

</dd> </dl>

## Return value

If the method succeeds the return value is **S\_OK**.

If the method fails, the return value is one of the following error codes.



| Return code                                                                                   | Description                                                                   |
|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| <dl> <dt>**E\_ABORT**</dt> </dl>       | The operation was aborted.<br/>                                         |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | An unspecified error occurred.<br/>                                     |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | One of the parameters is invalid.<br/>                                  |
| <dl> <dt>**E\_NOINTERFACE**</dt> </dl> | A specified interface is not supported.<br/>                            |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>     | A specified method is not implemented.<br/>                             |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | The method was unable to allocate required memory.<br/>                 |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | A pointer passed as a parameter is not valid.<br/>                      |
| <dl> <dt>**E\_UNEXPECTED**</dt> </dl>  | The method failed for unknown reasons.<br/>                             |
| <dl> <dt>**S\_FALSE**</dt> </dl>       | The [**Next**](ienumnetfwv6connections-next.md) operation failed.<br/> |



 

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

[**IEnumNetFwV6Connections**](ienumnetfwv6connections.md)
</dt> <dt>

[**INetFwV6Connection**](inetfwv6connection.md)
</dt> </dl>

 

 





