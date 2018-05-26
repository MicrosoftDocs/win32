---
title: ISystemMediaTransportControls remove\_PropertyChanged method
description: Removes the specified event handler for the PropertyChanged event.
ms.assetid: B13B648D-BC58-40BE-B3A9-5125C4A5CFA6
keywords:
- remove_PropertyChanged method
- remove_PropertyChanged method, ISystemMediaTransportControls interface
- ISystemMediaTransportControls interface, remove_PropertyChanged method
topic_type:
- apiref
api_name:
- ISystemMediaTransportControls.remove_PropertyChanged
api_location:
- Windows.Media.SystemMediaTransportControls.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ISystemMediaTransportControls::remove\_PropertyChanged method

Removes the specified event handler for the [**PropertyChanged**](https://msdn.microsoft.com/library/windows/apps/dn278720) event.

## Syntax


```C++
HRESULT remove_PropertyChanged(
   EventRegistrationToken token
);
```



## Parameters

<dl> <dt>

*token* 
</dt> <dd>

Type: **[**EventRegistrationToken**](https://msdn.microsoft.com/library/windows/desktop/br205773)**

The registration token for the event handler. The token is obtained from the [**add\_PropertyChanged**](winrt-isystemmediatransportcontrols_add_propertychanged) method.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                                                           |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                                                      |
| Header<br/>                   | <dl> <dt>Windows.Media.SystemMediaTransportControls.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Windows.Media.SystemMediaTransportControls.idl</dt> </dl> |



## See also

<dl> <dt>

[**ISystemMediaTransportControls**](isystemmediatransportcontrols.md)
</dt> </dl>

 

 





