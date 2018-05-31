---
title: IVMVirtualServer SetConfigurationValue method
description: The SetConfigurationValue method sets preference data for the current user for the requested key.
ms.assetid: 648d5c0e-3c06-40c1-8f25-76e71a102a20
keywords:
- SetConfigurationValue method Virtual Server
- SetConfigurationValue method Virtual Server , IVMVirtualServer interface
- IVMVirtualServer interface Virtual Server , SetConfigurationValue method
topic_type:
- apiref
api_name:
- IVMVirtualServer.SetConfigurationValue
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

# IVMVirtualServer::SetConfigurationValue method

The **SetConfigurationValue** method sets preference data for the current user for the requested key.

## Syntax


```C++
HRESULT SetConfigurationValue(
  [in] BSTR    preferenceKey,
  [in] VARIANT preferenceValue
);
```



## Parameters

<dl> <dt>

*preferenceKey* \[in\]
</dt> <dd>

Key used to identify the preference, as stored in the configuration file.

</dd> <dt>

*preferenceValue* \[in\]
</dt> <dd>

Variant specifying the preference value. Variant type may be one of: VT\_ARRAY\|VT\_UI1 (raw bytes), VT\_BSTR (string), VT\_UI4 (integer), or VT\_BOOL (Boolean).

</dd> </dl>

## Return value

This method can return one of these values.

This method supports standard return values, as well as the following. For information on Virtual Server specific return values not listed below, see [**HRESULT Codes Specific to the Virtual Server**](hresult-codes-specific-to-the-virtual-server.md).



| Return code                                                                                        | Description                                                                  |
|----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| <dl> <dt> **S\_OK**</dt> </dl>              | The operation was successful.<br/>                                     |
| <dl> <dt> **E\_POINTER**</dt> </dl>         | The *preferenceKey* or *preferenceValue* parameter is **NULL**.<br/>   |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>       | The *preferenceKey* parameter is not valid or is an empty string.<br/> |
| <dl> <dt> **DISP\_E\_EXCEPTION**</dt> </dl> | An unexpected error occurred.<br/>                                     |



 

## Remarks

This method provides low-level access to any preference value for the current user. It can be used to set preference values for customer-defined keys.

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMVirtualServer**](ivmvirtualserver.md)
</dt> </dl>

 

 





