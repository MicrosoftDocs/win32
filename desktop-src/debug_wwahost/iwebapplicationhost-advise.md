---
Description: 'Establishes a connection to allow a client to receive events.'
ms.assetid: '94c016cb-f043-4ea6-a5d1-f3486b55c97f'
title: 'IWebApplicationHost::Advise method'
---

# IWebApplicationHost::Advise method

Establishes a connection to allow a client to receive events.

## Syntax


```C++
HRESULT Advise(
  [in]  REFIID   interfaceId,
  [in]  IUnknown *callback,
  [out] DWORD    *cookie
);
```



## Parameters

<dl> <dt>

*interfaceId* \[in\]
</dt> <dd>

Type: **REFIID**

The identifier of the event interface.

</dd> <dt>

*callback* \[in\]
</dt> <dd>

Type: **[**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509)\***

The caller's event interface.

</dd> <dt>

*cookie* \[out\]
</dt> <dd>

Type: **DWORD\***

A token that uniquely identifies this connection.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                          |
| IDL<br/>                      | <dl> <dt>Webapplication.idl</dt> </dl> |



## See also

<dl> <dt>

[**IWebApplicationHost**](iwebapplicationhost.md)
</dt> <dt>

[**IWebApplicationHost::Unadvise**](iwebapplicationhost-unadvise.md)
</dt> </dl>

 

 




