---
title: IHTTPMailTransport GetProperty method
description: Retrieves the specified LPSTR account property synchronously or asynchronously.
ms.assetid: bca6e6cb-3384-4e13-97a2-ef9c4e10c833
keywords:
- GetProperty method Windows Mail (formerly Outlook Express)
- GetProperty method Windows Mail (formerly Outlook Express) , IHTTPMailTransport interface
- IHTTPMailTransport interface Windows Mail (formerly Outlook Express) , GetProperty method
topic_type:
- apiref
api_name:
- IHTTPMailTransport.GetProperty
api_location:
- Inetcomm.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IHTTPMailTransport::GetProperty method

\[**IHTTPMailTransport::GetProperty** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Retrieves the specified **LPSTR** account property synchronously or asynchronously.

## Syntax


```C++
HRESULT GetProperty(
  [in]  HTTPMAILPROPTYPE proptype,
  [out] LPSTR            *ppszProp
);
```



## Parameters

<dl> <dt>

*proptype* \[in\]
</dt> <dd>

Type: **[**HTTPMAILPROPTYPE**](oe-httpmailproptype.md)**

Specifies a property from the [**HTTPMAILPROPTYPE**](oe-httpmailproptype.md) enumeration whose data type is **LPSTR**.

</dd> <dt>

*ppszProp* \[out\]
</dt> <dd>

Type: **LPSTR\***

Receives a pointer to an **LPSTR** that contains the value of the property specified by *proptype*.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                                         | Description                                                                                                                                                                                 |
|---------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                                | Indicates success. <br/>                                                                                                                                                              |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                        | Indicates that *proptype* is invalid, for example, [**HTTPMAIL\_PROP\_INVALID**](oe-httpmailproptype.md), **HTTPMAIL\_PROP\_MAXPOLLINGINTERVAL**, or **HTTPMAIL\_PROP\_LAST**. <br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl>                              | Indicates that the server is not available. <br/>                                                                                                                                     |
| <dl> <dt>**E\_PENDING**</dt> </dl>                           | Indicates that there are no root properties or *ppszProp* is **NULL**. The property value is being returned asynchronously. <br/>                                                     |
| <dl> <dt>**IXP\_E\_HTTP\_ROOT\_PROP\_NOT\_FOUND**</dt> </dl> | Indicates that the root properties request succeeded. The server returned XML that did not contain the specific root property requested by the client. <br/>                          |



 

## Remarks

If the property is immediately available, the function returns it synchronously, and the result of the function is S\_OK. In the sync case, it is the client's responsibility to free the property string by calling [CoTaskMemFree](http://msdn.microsoft.com/library/com/htm/cmf_a2c_63l1.asp). If the property is not immediately available, the function result is E\_PENDING, and the result is returned through the callback's OnResponse method.

The caller can force the call to return asynchronously by passing a **null***ppszProp*. The call cannot force the call to return synchronously.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





