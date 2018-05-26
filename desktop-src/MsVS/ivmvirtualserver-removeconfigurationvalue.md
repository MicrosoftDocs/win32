---
title: IVMVirtualServer RemoveConfigurationValue method
description: The RemoveConfigurationValue method removes preference data for the current user for the requested key.
ms.assetid: 9a116673-d0ce-478b-924d-c63d3f2b85d6
keywords:
- RemoveConfigurationValue method Virtual Server
- RemoveConfigurationValue method Virtual Server , IVMVirtualServer interface
- IVMVirtualServer interface Virtual Server , RemoveConfigurationValue method
topic_type:
- apiref
api_name:
- IVMVirtualServer.RemoveConfigurationValue
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IVMVirtualServer::RemoveConfigurationValue method

The **RemoveConfigurationValue** method removes preference data for the current user for the requested key.

## Syntax


```C++
HRESULT RemoveConfigurationValue(
  [in] BSTR preferenceKey
);
```



## Parameters

<dl> <dt>

*preferenceKey* \[in\]
</dt> <dd>

Key used to identify the preference, as stored in the configuration file.

</dd> </dl>

## Return value

This method can return one of these values.

This method supports standard return values, as well as the following. For information on Virtual Server specific return values not listed below, see [**HRESULT Codes Specific to the Virtual Server**](hresult-codes-specific-to-the-virtual-server.md).



| Return code                                                                                             | Description                                                                  |
|---------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| <dl> <dt> **S\_OK**</dt> </dl>                   | The operation was successful.<br/>                                     |
| <dl> <dt> **E\_POINTER**</dt> </dl>              | The *preferenceKey* parameter is **NULL**.<br/>                        |
| <dl> <dt> **E\_INVALIDARG**</dt> </dl>           | The *preferenceKey* parameter is not valid or is an empty string.<br/> |
| <dl> <dt> **VM\_E\_PREF\_NOT\_FOUND**</dt> </dl> | The preference was not found.<br/>                                     |
| <dl> <dt> **DISP\_E\_EXCEPTION**</dt> </dl>      | An unexpected error occurred.<br/>                                     |



 

## Remarks

This method provides low-level access to any preference value for the current user. It can be used to remove preference values for customer-defined keys.

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

 

 





