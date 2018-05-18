---
Description: 'Sets the network address types that a specified network address control accepts.'
title: 'NCM\_SETALLOWTYPE message'
---

# NCM\_SETALLOWTYPE message

Sets the network address types that a specified network address control accepts.


```C++
NCM_SETALLOWTYPE

    wParam = (WPARAM) (DWORD) addrMask;

    lParam = 0;            

            
```



## Parameters

<dl> <dt>

*addrMask* \[in\]
</dt> <dd>Specifies the network address types as one or more of the [**NET\_STRING**](net-string.md) constants.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns S\_OK if successful, or an error value otherwise.

## Remarks

The mask set is the criterion used to validate a network address in the [**NCM\_GETADDRESS**](ncm-getaddress.md) message.

Use this message for a network address control only. To instantiate, use the class **msctls\_netaddress** defined in Shellapi.h. Call [**InitNetworkAddressControl**](initnetworkaddresscontrol.md) at run time before sending this message. This initializes the common controls library that contains the network address control.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Shellapi.h</dt> </dl> |



## See also

<dl> <dt>

[**NCM\_GETALLOWTYPE**](ncm-getallowtype.md)
</dt> <dt>

[**NetAddr\_SetAllowType**](netaddr-setallowtype.md)
</dt> </dl>

 

 




