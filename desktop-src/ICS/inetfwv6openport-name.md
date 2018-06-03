---
title: INetFwV6OpenPort Name property
description: Returns the display name for this port and protocol pair. The name is for informational purposes only and has no bearing on the operation of the system.
ms.assetid: 4f61bf9e-62ac-42b6-9ea5-fbf9b4ee4a8e
keywords:
- Name property ICS/ICF
- Name property ICS/ICF , INetFwV6OpenPort interface
- INetFwV6OpenPort interface ICS/ICF , Name property
topic_type:
- apiref
api_name:
- INetFwV6OpenPort.Name
- INetFwV6OpenPort.get_Name
api_location:
- Netfwv6.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# INetFwV6OpenPort::Name property

\[The IPv6 Internet Connection Firewall is available for use in the operating systems specified in the Requirements section. Instead, use the [Windows Firewall API](windows-firewall-start-page.md).\]

Returns the display name for this port and protocol pair. The name is for informational purposes only and has no bearing on the operation of the system.

This property is read-only.

## Syntax


```C++
HRESULT get_Name(
  [out] PORT_PROTOCOL *pbstrName
);
```



## Property value

Returns the display name for this pair.

## Error codes

If the method succeeds, the return value is S\_OK.

If the method fails, the return value is one of the following error codes.



| Name                                                                                      | Meaning                                                       |
|-------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| <dl> <dt>E\_ABORT</dt> </dl>       | The operation was aborted.<br/>                         |
| <dl> <dt>E\_FAIL</dt> </dl>        | An unspecified error occurred.<br/>                     |
| <dl> <dt>E\_INVALIDARG</dt> </dl>  | The parameter is invalid.<br/>                          |
| <dl> <dt>E\_NOINTERFACE</dt> </dl> | A specified interface is not supported.<br/>            |
| <dl> <dt>E\_NOTIMPL</dt> </dl>     | A specified method is not implemented.<br/>             |
| <dl> <dt>E\_OUTOFMEMORY</dt> </dl> | The method was unable to allocate required memory.<br/> |
| <dl> <dt>E\_POINTER</dt> </dl>     | A pointer passed as a parameter is not valid.<br/>      |
| <dl> <dt>E\_UNEXPECTED</dt> </dl>  | The method failed for unknown reasons.<br/>             |



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

[INetFwV6OpenPort](https://msdn.microsoft.com/library/windows/desktop/aa365921)
</dt> <dt>

[**INetFwV6OpenPort**](inetfwv6openport.md)
</dt> </dl>

 

 





