---
description: The UpdateEndpointProxySettings structure defines the proxy settings used when requesting a token.
ms.assetid: 24AA8843-D4EE-4F17-8B96-63ED25B365D2
title: UpdateEndpointProxySettings structure (UpdateEndpointAuth.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- UpdateEndpointProxySettings
api_type: 
- HeaderDef
api_location: 
- UpdateEndpointAuth.h
---

# UpdateEndpointProxySettings structure

The **UpdateEndpointProxySettings** structure defines the proxy settings used when requesting a token.

## Syntax


```C++
typedef struct tagUpdateEndpointProxySettings {
  BSTR szProxyAddr;
  BSTR szBypassList;
  BSTR szUserName;
  BSTR szPassword;
} UpdateEndpointProxySettings;
```



## Members

<dl> <dt>

**szProxyAddr**
</dt> <dd>

The DNS name or IP address of the proxy server to use (for example, "proxy.somecorp.com" or "192.168.0.4"), or an empty string if no proxy should be used.

</dd> <dt>

**szBypassList**
</dt> <dd>

A list of host addresses that should bypass the proxy server, or an empty string if all host addresses should use the proxy server

WUA does not use this data if **szProxyAddr** is empty.

</dd> <dt>

**szUserName**
</dt> <dd>

The username that is used to authenticate with the proxy server, or the empty string if no authentication is needed.

WUA does not use this data if **szProxyAddr** is empty.

</dd> <dt>

**szPassword**
</dt> <dd>

The password that is used to authenticate with the proxy server, or the empty string if no authentication is needed.

WUA does not use this data if **szProxyAddr** is empty.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                        |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                              |
| Header<br/>                   | <dl> <dt>UpdateEndpointAuth.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>UpdateEndpointAuth.idl</dt> </dl> |



## See also

<dl> <dt>

[**GetEndpointToken**](iupdateendpointauthprovider-getendpointtoken.md)
</dt> </dl>

 

 




