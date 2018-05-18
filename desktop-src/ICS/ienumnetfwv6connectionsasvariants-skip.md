---
title: IEnumNetFwV6ConnectionsAsVariants Skip method
description: The Skip method skips the specified number of connections for this enumeration.
ms.assetid: '3eca33f0-d7e5-4cc1-b6c1-e792599dc93c'
keywords: ["Skip method ICS/ICF", "Skip method ICS/ICF , IEnumNetFwV6ConnectionsAsVariants interface", "IEnumNetFwV6ConnectionsAsVariants interface ICS/ICF , Skip method"]
topic_type:
- apiref
api_name:
- IEnumNetFwV6ConnectionsAsVariants.Skip
api_location:
- Netfwv6.dll
api_type:
- COM
---

# IEnumNetFwV6ConnectionsAsVariants::Skip method

\[The IPv6 Internet Connection Firewall is available for use in the operating systems specified in the Requirements section. Instead, use the [Windows Firewall API](windows-firewall-start-page.md).\]

The **Skip** method skips the specified number of connections for this enumeration.

## Syntax


```C++
HRESULT Skip(
  [in] ULONG cElt
);
```



## Parameters

<dl> <dt>

*cElt* \[in\]
</dt> <dd>

Specifies the number of connections to skip.

</dd> </dl>

## Return value

If the method succeeds the return value is S\_OK.

If the method fails, the return value is one of the following error codes.



| Return code                                                                                   | Description                                                   |
|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| <dl> <dt>**E\_ABORT**</dt> </dl>       | The operation was aborted.<br/>                         |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | An unspecified error occurred.<br/>                     |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | The parameter is invalid.<br/>                          |
| <dl> <dt>**E\_NOINTERFACE**</dt> </dl> | A specified interface is not supported.<br/>            |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>     | A specified method is not implemented.<br/>             |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | The method was unable to allocate required memory.<br/> |
| <dl> <dt>**E\_UNEXPECTED**</dt> </dl>  | The method failed for unknown reasons.<br/>             |



 

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP1 \[desktop apps only\]<br/>                                   |
| Minimum supported server<br/> | None supported<br/>                                                              |
| End of client support<br/>    | Windows XP with SP1<br/>                                                         |
| Redistributable<br/>          | Advanced Networking Pack for Windows XP<br/>                                     |
| Header<br/>                   | <dl> <dt>Netfwv6.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Netfwv6.dll</dt> </dl> |



## See also

<dl> <dt>

[**IEnumNetFwV6ConnectionsAsVariants**](ienumnetfwv6connectionsasvariants.md)
</dt> </dl>

 

 





