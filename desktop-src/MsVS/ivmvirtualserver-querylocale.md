---
title: IVMVirtualServer QueryLocale method
description: The QueryLocale method returns the preferred Virtual Server service locale selected from the set of languages specified by an RFC-2616 compliant language string.
ms.assetid: 344bb1e6-60ba-489d-b086-5b0fd7f92229
keywords:
- QueryLocale method Virtual Server
- QueryLocale method Virtual Server , IVMVirtualServer interface
- IVMVirtualServer interface Virtual Server , QueryLocale method
topic_type:
- apiref
api_name:
- IVMVirtualServer.QueryLocale
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMVirtualServer::QueryLocale method

The **QueryLocale** method returns the preferred Virtual Server service locale selected from the set of languages specified by an [RFC-2616](Http://go.microsoft.com/fwlink/p/?linkid=84048) compliant language string.

## Syntax


```C++
HRESULT QueryLocale(
  [in]  BSTR  inLanguage,
  [out] ULONG *outLocale
);
```



## Parameters

<dl> <dt>

*inLanguage* \[in\]
</dt> <dd>

RFC-2616 compliant language string.

</dd> <dt>

*outLocale* \[out\]
</dt> <dd>

Retrieves the value of the desired Windows Locale ID selected from the *inLanguage* parameter.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                       | Description                                       |
|---------------------------------------------------------------------------------------------------|---------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>              | The operation was successful.<br/>          |
| <dl> <dt>**E\_POINTER**</dt> </dl>         | The *outLocale* parameter is **NULL**.<br/> |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> </dl> | An unexpected error occurred.<br/>          |



 

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMVirtualServer**](ivmvirtualserver.md)
</dt> <dt>

[**DefaultLocale**](ivmvirtualserver-defaultlocale.md)
</dt> <dt>

[**Locale**](ivmvirtualserver-locale.md)
</dt> </dl>

 

 





