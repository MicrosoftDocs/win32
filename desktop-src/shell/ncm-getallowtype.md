---
Description: Retrieves the network address types that a specified network address control accepts.
title: NCM\_GETALLOWTYPE message
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# NCM\_GETALLOWTYPE message

Retrieves the network address types that a specified network address control accepts.


```C++
NCM_GETALLOWTYPE

    wParam = 0;

    lParam = 0;            

            
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the allowed network address types as one or more of the [**NET\_STRING**](net-string.md) constants.

## Remarks

The returned mask is the criterion used to validate a network address in the [**NCM\_GETADDRESS**](ncm-getaddress.md) message.

Use this message for a network address control only. To instantiate, use the class **msctls\_netaddress** defined in Shellapi.h. Call [**InitNetworkAddressControl**](/windows/win32/Shellapi/nf-shellapi-initnetworkaddresscontrol?branch=master) at run time before sending this message. This initializes the common controls library that contains the network address control.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Shellapi.h</dt> </dl> |



## See also

<dl> <dt>

[**NCM\_SETALLOWTYPE**](ncm-setallowtype.md)
</dt> <dt>

[**NetAddr\_GetAllowType**](/windows/win32/Shellapi/nf-shellapi-netaddr_getallowtype?branch=master)
</dt> </dl>

 

 




