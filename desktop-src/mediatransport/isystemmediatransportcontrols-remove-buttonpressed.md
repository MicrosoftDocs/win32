---
title: ISystemMediaTransportControls remove\_ButtonPressed method
description: Removes the specified event handler for the ButtonPressed event.
ms.assetid: 8E304186-8D13-4D7C-8412-D5216FA8574A
keywords:
- remove_ButtonPressed method
- remove_ButtonPressed method, ISystemMediaTransportControls interface
- ISystemMediaTransportControls interface, remove_ButtonPressed method
topic_type:
- apiref
api_name:
- ISystemMediaTransportControls.remove_ButtonPressed
api_location:
- Windows.Media.SystemMediaTransportControls.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ISystemMediaTransportControls::remove\_ButtonPressed method

Removes the specified event handler for the [**ButtonPressed**](https://msdn.microsoft.com/library/windows/apps/dn278706) event.

## Syntax


```C++
HRESULT remove_ButtonPressed(
   EventRegistrationToken token
);
```



## Parameters

<dl> <dt>

*token* 
</dt> <dd>

Type: **[**EventRegistrationToken**](https://msdn.microsoft.com/library/windows/desktop/br205773)**

The registration token for the event handler. The token is obtained from the [**add\_ButtonPressed**](https://www.bing.com/search?q=**add\_ButtonPressed**) method.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/windows/desktop/455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

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

 

 





