---
title: IEnumNetFwV6OpenPortsAsVariants Reset method
description: The Reset method causes subsequent enumeration calls to operate from the beginning of the enumeration.
ms.assetid: 'eecd6ab1-4839-401e-8d5b-2420915ab9c7'
keywords: ["Reset method ICS/ICF", "Reset method ICS/ICF , IEnumNetFwV6OpenPortsAsVariants interface", "IEnumNetFwV6OpenPortsAsVariants interface ICS/ICF , Reset method"]
topic_type:
- apiref
api_name:
- IEnumNetFwV6OpenPortsAsVariants.Reset
api_location:
- Netfwv6.dll
api_type:
- COM
---

# IEnumNetFwV6OpenPortsAsVariants::Reset method

\[The IPv6 Internet Connection Firewall is available for use in the operating systems specified in the Requirements section. Instead, use the [Windows Firewall API](windows-firewall-start-page.md).\]

The **Reset** method causes subsequent enumeration calls to operate from the beginning of the enumeration.

## Syntax


```C++
HRESULT Reset();
```



## Parameters

This method has no parameters.

## Return value

If the method succeeds the return value is S\_OK.

If the method fails, the return value is one of the following error codes.



| Return code                                                                                   | Description                                                   |
|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| <dl> <dt>**E\_ABORT**</dt> </dl>       | The operation was aborted.<br/>                         |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | An unspecified error occurred.<br/>                     |
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

[**IEnumNetFwV6OpenPortsAsVariants**](https://msdn.microsoft.com/library/windows/desktop/aa364746)
</dt> <dt>

[**IEnumNetFwV6OpenPortsAsVariants**](ienumnetfwv6openportsasvariants.md)
</dt> </dl>

 

 





