---
title: Items.Add method
description: Adds a new Item.
ms.assetid: 09599b31-7e7b-495e-bd86-804104908324
keywords:
- Add method WIA Automation
- Add method WIA Automation , Items object
- Items object WIA Automation , Add method
topic_type:
- apiref
api_name:
- Items.Add
api_location:
- Wiaaut.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Items.Add method

Adds a new [**Item**](-wiaaut-item.md).

## Syntax


```VB
Items.Add( _
  ByVal Name As BSTR, _
  ByVal Flags As LONG _
) As HRESULT
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

Type: **BSTR**

Required. **String** value.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

Type: **LONG**

Created by using the OR operation with members of the [**WiaItemFlag**](-wiaaut-wiaitemflag.md) enumeration.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

As of the release of the Windows Image Acquisition (WIA) Automation Library, there are no imaging devices whose driver supports adding an item to a device.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wiaaut.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wiaaut.idl</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**Name (DeviceCommand)**](-wiaaut-idevicecommand-name.md)
</dt> <dt>

[**Name (DeviceEvent)**](-wiaaut-ideviceevent-name.md)
</dt> <dt>

[**RegisterPersistentEvent**](-wiaaut-idevicemanager-registerpersistentevent.md)
</dt> <dt>

[**UnregisterPersistentEvent**](-wiaaut-idevicemanager-unregisterpersistentevent.md)
</dt> <dt>

[**Name (Filter)**](-wiaaut-ifilter-name.md)
</dt> <dt>

[**Name (FilterInfo)**](-wiaaut-ifilterinfo-name.md)
</dt> <dt>

[**Items**](-wiaaut-items.md)
</dt> <dt>

[**Name (Property)**](-wiaaut-iproperty-name.md)
</dt> </dl>

 

 





