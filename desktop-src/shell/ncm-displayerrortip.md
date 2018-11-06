---
Description: Displays an error message in the balloon tip associated with the network address control.
title: NCM_DISPLAYERRORTIP message
ms.topic: article
ms.date: 05/31/2018
---

# NCM\_DISPLAYERRORTIP message

Displays an error message in the balloon tip associated with the network address control.


```C++
NCM_DISPLAYERRORTIP

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

If this message succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

Send this message to display an error message when an address typed into the control does not validate against the allowed network address types set with the [**NCM\_SETALLOWTYPE**](ncm-setallowtype.md) message. Use the [**NCM\_GETADDRESS**](ncm-getaddress.md) message to validate the address.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Shellapi.h</dt> </dl> |



## See also

<dl> <dt>

[**NetAddr\_DisplayErrorTip**](/windows/desktop/api/Shellapi/nf-shellapi-netaddr_displayerrortip)
</dt> </dl>

 

 




