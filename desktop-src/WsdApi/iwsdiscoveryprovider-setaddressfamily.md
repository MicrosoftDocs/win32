---
Description: 'Specifies the IP address family (IPv4, IPv6, or both) to search when discovering WSD devices.'
ms.assetid: '33b13cd5-ea60-4928-a220-db563c00a43c'
title: 'IWSDiscoveryProvider::SetAddressFamily method'
---

# IWSDiscoveryProvider::SetAddressFamily method

Specifies the IP address family (IPv4, IPv6, or both) to search when discovering WSD devices.

## Syntax


```C++
HRESULT SetAddressFamily(
  [in] DWORD dwAddressFamily
);
```



## Parameters

<dl> <dt>

*dwAddressFamily* \[in\]
</dt> <dd>

The address family to search when discovering devices.



| Value                                                                                                                                                                                                                                                                                     | Meaning                                         |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| <span id="WSDAPI_ADDRESSFAMILY_IPV4"></span><span id="wsdapi_addressfamily_ipv4"></span><dl> <dt>**WSDAPI\_ADDRESSFAMILY\_IPV4**</dt> </dl>                                                                                        | Search over IPv4 addresses.<br/>          |
| <span id="WSDAPI_ADDRESSFAMILY_IPV6"></span><span id="wsdapi_addressfamily_ipv6"></span><dl> <dt>**WSDAPI\_ADDRESSFAMILY\_IPV6**</dt> </dl>                                                                                        | Search over IPv6 addresses.<br/>          |
| <span id="WSDAPI_ADDRESSFAMILY_IPV4___WSDAPI_ADDRESSFAMILY_IPV6"></span><span id="wsdapi_addressfamily_ipv4___wsdapi_addressfamily_ipv6"></span><dl> <dt>**WSDAPI\_ADDRESSFAMILY\_IPV4 \| WSDAPI\_ADDRESSFAMILY\_IPV6**</dt> </dl> | Search over IPv4 and IPv6 addresses.<br/> |



 

</dd> </dl>

## Return value

This method can return one of these values.

Possible return values include, but are not limited to, the following.



| Return code                                                                                                             | Description                                                                                                                                                                  |
|-------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                                    | Method completed successfully.<br/>                                                                                                                                    |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                            | *dwAddressFamily* has a value other than WSDAPI\_ADDRESSFAMILY\_IPV4, WSDAPI\_ADDRESSFAMILY\_IPV6, or WSDAPI\_ADDRESSFAMILY\_IPV4 \| WSDAPI\_ADDRESSFAMILY\_IPV6.<br/> |
| <dl> <dt>**STG\_E\_INVALIDFUNCTION**</dt> </dl>                  | The address family has already been set for this publisher.<br/>                                                                                                       |
| <dl> <dt>**HRESULT\_FROM\_WIN32(WSAESOCKTNOSUPPORT)**</dt> </dl> | The system does not support the address family specified by *dwAddressFamily*.<br/>                                                                                    |



 

## Remarks

This method can be called only once on a provider. This method must be called before a notification sink is attached to the provider. That means **SetAddressFamily** must be called before [**Attach**](iwsdiscoveryprovider-attach-method.md) is called on a provider.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| IDL<br/>                      | <dl> <dt>Wsddisco.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wsdapi.dll</dt> </dl>   |



## See also

<dl> <dt>

[**IWSDiscoveryProvider**](iwsdiscoveryprovider.md)
</dt> </dl>

 

 




