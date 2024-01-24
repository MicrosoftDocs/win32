---
description: Creates an enumerator of property information for each available Windows Image Acquisition (WIA) 2.0 device.
ms.assetid: e37b73d5-5192-46e4-bb1c-bd1ef41f1d6c
title: IWiaDevMgr2::EnumDeviceInfo method (Wia.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWiaDevMgr2.EnumDeviceInfo
api_type: 
- COM
api_location: 
- Wia.h
---

# IWiaDevMgr2::EnumDeviceInfo method

Creates an enumerator of property information for each available Windows Image Acquisition (WIA) 2.0 device.

## Syntax


```C++
HRESULT EnumDeviceInfo(
  [in]          LONG              lFlags,
  [out, retval] IEnumWIA_DEV_INFO **ppIEnum
);
```



## Parameters

<dl> <dt>

*lFlags* \[in\]
</dt> <dd>

Type: **LONG**

Specifies the type of WIA 2.0 devices to enumerate.

<dt>

<span id="WIA_DEVINFO_ENUM_LOCAL"></span><span id="wia_devinfo_enum_local"></span>

<span id="WIA_DEVINFO_ENUM_LOCAL"></span><span id="wia_devinfo_enum_local"></span>**WIA\_DEVINFO\_ENUM\_LOCAL**


</dt> <dd>

Only locally connected active scanner devices are enumerated.

</dd> <dt>

<span id="WIA_DEVINFO_ENUM_ALL"></span><span id="wia_devinfo_enum_all"></span>

<span id="WIA_DEVINFO_ENUM_ALL"></span><span id="wia_devinfo_enum_all"></span>**WIA\_DEVINFO\_ENUM\_ALL**


</dt> <dd>

All devices are enumerated, both locally and remote, including inactive (disconnected) devices and legacy STI-only devices.

</dd> </dl> </dd> <dt>

*ppIEnum* \[out, retval\]
</dt> <dd>

Type: **[**IEnumWIA\_DEV\_INFO**](/windows/desktop/api/wia_xp/nn-wia_xp-ienumwia_dev_info)\*\***

Receives the address of a pointer to the [**IEnumWIA\_DEV\_INFO**](/windows/desktop/api/wia_xp/nn-wia_xp-ienumwia_dev_info) interface.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

The **IWiaDevMgr2::EnumDeviceInfo** method creates an enumerator object that supports the [**IEnumWIA\_DEV\_INFO**](/windows/desktop/api/wia_xp/nn-wia_xp-ienumwia_dev_info) interface. The method stores a pointer to the **IEnumWIA\_DEV\_INFO** interface in the parameter *ppIEnum*. Applications can use the **IEnumWIA\_DEV\_INFO** interface pointer to enumerate the properties of each WIA 2.0 device attached to the user's computer.

Applications must call the [IUnknown::Release](/windows/win32/api/unknwn/nf-unknwn-iunknown-release) method on the interface pointers they receive through the *ppIEnum* parameter.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wia.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wia.idl</dt> </dl> |



 

 
