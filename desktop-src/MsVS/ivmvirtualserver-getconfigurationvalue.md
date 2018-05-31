---
title: IVMVirtualServer GetConfigurationValue method
description: The GetConfigurationValue method returns preference data for the current user for the requested key.
ms.assetid: 4ff10c47-d0b3-412b-8a7a-516f246e3049
keywords:
- GetConfigurationValue method Virtual Server
- GetConfigurationValue method Virtual Server , IVMVirtualServer interface
- IVMVirtualServer interface Virtual Server , GetConfigurationValue method
topic_type:
- apiref
api_name:
- IVMVirtualServer.GetConfigurationValue
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IVMVirtualServer::GetConfigurationValue method

The **GetConfigurationValue** method returns preference data for the current user for the requested key.

## Syntax


```C++
HRESULT GetConfigurationValue(
  [in]  BSTR    preferenceKey,
  [out] VARIANT *preferenceValue
);
```



## Parameters

<dl> <dt>

*preferenceKey* \[in\]
</dt> <dd>

Key used to identify the preference, as stored in the configuration file.

</dd> <dt>

*preferenceValue* \[out\]
</dt> <dd>

Variant used to return the preference value. Variant type may be one of: VT\_ARRAY\|VT\_UI1 (raw bytes), VT\_BSTR (string), VT\_UI4 (integer), or VT\_BOOL (Boolean).

</dd> </dl>

## Return value

This method supports standard return values, as well as the following. For information on Virtual Server specific return values not listed below, see [**HRESULT Codes Specific to the Virtual Server**](hresult-codes-specific-to-the-virtual-server.md).



| Return code                                                                                             | Description                                                  |
|---------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| <dl> <dt> **S\_OK**</dt> </dl>                   | The operation was successful.<br/>                     |
| <dl> <dt> **E\_POINTER**</dt> </dl>              | *preferenceKey* or *preferenceValue* is **NULL**.<br/> |
| <dl> <dt> **VM\_E\_PREF\_NOT\_FOUND**</dt> </dl> | The preference was not found.<br/>                     |
| <dl> <dt> **DISP\_E\_EXCEPTION**</dt> </dl>      | An unexpected error occurred.<br/>                     |



 

## Remarks

This method provides low-level access to any preference value for the current user. It can be used to retrieve preference values for customer-defined keys.

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

 

 





