---
title: IMessenger MyProperty property
description: Reserved. Do not use.
ms.assetid: 2be38b7a-2cf7-442e-af48-67e5d50dc0c7
keywords:
- MyProperty property Windows Messenger
- MyProperty property Windows Messenger , IMessenger interface
- IMessenger interface Windows Messenger , MyProperty property
topic_type:
- apiref
api_name:
- IMessenger.MyProperty
- IMessenger.get_MyProperty
- IMessenger.put_MyProperty
api_location:
- Msgsc.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IMessenger::MyProperty property

\[**MyProperty** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Reserved. Do not use.

This property is read/write.

## Syntax


```C++
HRESULT put_MyProperty(
  [in]          MCONTACTPROPERTY ePropType,
  [in]          VARIANT          vPropVal
);

HRESULT get_MyProperty(
  [in]          MCONTACTPROPERTY ePropType,
  [out, retval] VARIANT          *pvPropVal
);
```



## Property value

A pointer to a **VARIANT** that contains the property value. (Variant type differs depending on the property being set or retrieved.)

## Error codes



| Name                                                                                     | Meaning                                                    |
|------------------------------------------------------------------------------------------|------------------------------------------------------------|
| <dl> <dt>E\_INVALIDARG</dt> </dl> | Returned in all cases. This method is reserved.<br/> |



## Requirements



|                                  |                                                                                       |
|----------------------------------|---------------------------------------------------------------------------------------|
| End of client support<br/> | Windows XP<br/>                                                                 |
| End of server support<br/> | Windows Server 2003<br/>                                                        |
| Header<br/>                | <dl> <dt>Msgrua.h</dt> </dl>   |
| IDL<br/>                   | <dl> <dt>Msgrua.idl</dt> </dl> |
| DLL<br/>                   | <dl> <dt>Msgsc.dll</dt> </dl>  |



## See also

<dl> <dt>

[**IMessenger**](im-imessenger.md)
</dt> <dt>

[**OnMyPropertyChange**](im-dmessengerevents-onmypropertychange.md)
</dt> </dl>

 

 





