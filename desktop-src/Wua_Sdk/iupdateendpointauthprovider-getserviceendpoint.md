---
description: Requests an endpoint that is used to connect to a service.
ms.assetid: 4C02EA78-AD77-42CD-B94F-C8C3ED26CB4C
title: IUpdateEndpointProvider::GetServiceEndpoint method (UpdateEndpointAuth.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IUpdateEndpointProvider.GetServiceEndpoint
api_type: 
- COM
api_location: 
- UpdateEndpointAuth.dll
---

# IUpdateEndpointProvider::GetServiceEndpoint method

Requests an endpoint that is used to connect to a service.

## Syntax


```C++
HRESULT GetServiceEndpoint(
  [in]  GUID                        ServiceId,
  [in]  UpdateEndpointType          endpointType,
  [in]  UpdateEndpointProxySettings proxySettings,
  [in]  HANDLE_PTR                  hUserToken,
  [in]  BOOL                        fRefreshOnline,
  [out] BSTR                        *pbstrEndpointLoc
);
```



## Parameters

<dl> <dt>

*ServiceId* \[in\]
</dt> <dd>

Identifies the service to be updated.

</dd> <dt>

*endpointType* \[in\]
</dt> <dd>

Identifies the type of endpoint implemented by the service.

The [**UpdateEndpointType**](updateendpointtype.md) enumeration defines the following constants.

<dt>

<span id="uetClientServer"></span><span id="uetclientserver"></span><span id="UETCLIENTSERVER"></span>

<span id="uetClientServer"></span><span id="uetclientserver"></span><span id="UETCLIENTSERVER"></span>**uetClientServer**


</dt> <dd>

A client-server endpoint that is used to connect to the update service.

</dd> <dt>

<span id="uetReporting"></span><span id="uetreporting"></span><span id="UETREPORTING"></span>

<span id="uetReporting"></span><span id="uetreporting"></span><span id="UETREPORTING"></span>**uetReporting**


</dt> <dd>

A Reporting endpoint that is used used when the client reports the results of scans, downloads, and installs back to the update service

</dd> <dt>

<span id="uetWuaSelfUpdate"></span><span id="uetwuaselfupdate"></span><span id="UETWUASELFUPDATE"></span>

<span id="uetWuaSelfUpdate"></span><span id="uetwuaselfupdate"></span><span id="UETWUASELFUPDATE"></span>**uetWuaSelfUpdate**


</dt> <dd>

A Self-Update endpoint that is used when the client computer contacts an update service to see whether there is a new version of the Windows Update Agent client software.

</dd> <dt>

<span id="uetRegulation"></span><span id="uetregulation"></span><span id="UETREGULATION"></span>

<span id="uetRegulation"></span><span id="uetregulation"></span><span id="UETREGULATION"></span>**uetRegulation**


</dt> <dd>

A Regulation endpoint that is used when the client computer contacts the regulation service to act on a particular update that is applicable to the target computer.

</dd> <dt>

<span id="uetSimpleTargeting"></span><span id="uetsimpletargeting"></span><span id="UETSIMPLETARGETING"></span>

<span id="uetSimpleTargeting"></span><span id="uetsimpletargeting"></span><span id="UETSIMPLETARGETING"></span>**uetSimpleTargeting**


</dt> <dd>

A Simple-Targeting endoint that is used only with private services (WSUS servers in corporate environments).

</dd> </dl> </dd> <dt>

*proxySettings* \[in\]
</dt> <dd>

Identifies the settings that are used when connecting to a proxy server.

</dd> <dt>

*hUserToken* \[in\]
</dt> <dd>

Contains a token handle object that represents the user. The endpoint provider uses this token to determine which proxy settings and credentials to use.

</dd> <dt>

*fRefreshOnline* \[in\]
</dt> <dd>

Indicates weather WUA requests a new token. True indicates that a new token is requested. False indicates that a new or cached token is requested. See Remarks for more information.

</dd> <dt>

*pbstrEndpointLoc* \[out\]
</dt> <dd>

Specify the URL used to communicate with the service. For example, for a cleint-server endpoint this would be the URL to the client server service. See Remarks for more information.

</dd> </dl>

## Return value

Returns **S\_OK** if successful. Otherwise, returns a COM or Windows error code.

## Remarks

WUA typically sets the *fRefreshOnline* parameter to false when this method is first called, then if a connection error occures WUA sets that parameter to true when the method is called again. However, the implementation of this method can request a new token from a Security Token Service (STS) or provide a cached token at any time.

If the endpoint does not need authentication, then the caller can connect to the service using only the URL specified by the *pbstrEndpointLoc* parameter.

If the endpoint does need authentication, then the caller can use the URL specified by the *pbstrEndpointLoc* parameter and the data provided by the other parameters.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP, Windows 2000 Professional with SP3 \[desktop apps only\]<br/>                   |
| Minimum supported server<br/> | Windows Server 2003, Windows 2000 Server with SP3 \[desktop apps only\]<br/>                |
| Header<br/>                   | <dl> <dt>UpdateEndpointAuth.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>UpdateEndpointAuth.idl</dt> </dl> |
| Library<br/>                  | <dl> <dt>UpdateEndpointAuth.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>UpdateEndpointAuth.dll</dt> </dl> |



## See also

<dl> <dt>

[**IUpdateEndpointProvider**](iupdateendpointprovider.md)
</dt> </dl>

 

 




