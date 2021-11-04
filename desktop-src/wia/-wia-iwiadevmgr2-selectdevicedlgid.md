---
description: IWiaDevMgr2::SelectDeviceDlgID method - Displays a dialog box that enables the user to select a hardware device for image acquisition.
ms.assetid: 6baca959-0f97-4a39-88d0-ed34b813c80a
title: IWiaDevMgr2::SelectDeviceDlgID method (Wia.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWiaDevMgr2.SelectDeviceDlgID
api_type: 
- COM
api_location: 
- Wia.h
---

# IWiaDevMgr2::SelectDeviceDlgID method

Displays a dialog box that enables the user to select a hardware device for image acquisition.

## Syntax


```C++
HRESULT SelectDeviceDlgID(
  [in]          HWND hwndParent,
  [in]          LONG lDeviceType,
  [in]          LONG lFlags,
  [out, retval] BSTR *pbstrDeviceID
);
```



## Parameters

<dl> <dt>

*hwndParent* \[in\]
</dt> <dd>

Type: **HWND**

Specifies the parent window of the **Select Device** dialog box.

</dd> <dt>

*lDeviceType* \[in\]
</dt> <dd>

Type: **LONG**

Specifies which type of WIA 2.0 device to use. See [WIA Device Type Specifiers](-wia-wia-device-type-specifiers.md) for a list of possible values.

</dd> <dt>

*lFlags* \[in\]
</dt> <dd>

Type: **LONG**

Specifies the behavior of the dialog box. The value can be one of the following.

<dt>

<span id="0"></span>

<span id="0"></span>**0**


</dt> <dd>

Use the default behavior.

</dd> <dt>

<span id="WIA_SELECT_DEVICE_NODEFAULT"></span><span id="wia_select_device_nodefault"></span>

<span id="WIA_SELECT_DEVICE_NODEFAULT"></span><span id="wia_select_device_nodefault"></span>**WIA\_SELECT\_DEVICE\_NODEFAULT**


</dt> <dd>

Display the dialog box even though there is only one matching device.

</dd> </dl> </dd> <dt>

*pbstrDeviceID* \[out, retval\]
</dt> <dd>

Type: **BSTR\***

Pointer to a string that receives the identifier string of the device.

</dd> </dl>

## Return value

Type: **HRESULT**

This method can return one of these values.



| Return code                                                                                                  | Description                                                                                            |
|--------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                         | Device was successfully selected. <br/>                                                          |
| <dl> <dt>**S\_FALSE**</dt> </dl>                      | User canceled the dialog box. <br/>                                                              |
| <dl> <dt>**WIA\_S\_NO\_DEVICE\_AVAILABLE**</dt> </dl> | No WIA 2.0 hardware devices match the specifications given in the *lDeviceType* parameter. <br/> |



 

## Remarks

This method creates and displays the **Select Device** dialog box so the user can select a WIA 2.0 device for image acquisition. If a device is successfully selected, the **IWiaDevMgr2::SelectDeviceDlgID** method passes its identifier string to the application through its *pbstrDeviceID* parameter.

The application can restrict the devices displayed to the user to particular types by specifying the device types through the *lDeviceType* parameter. If only one device meets the specification, **IWiaDevMgr2::SelectDeviceDlgID** does not display the **Select Device** dialog box. Instead it passes the device's identifier string to the application without displaying the dialog box. You can override this behavior and force **IWiaDevMgr2::SelectDeviceDlgID** to display the dialog box by passing WIA\_SELECT\_DEVICE\_NODEFAULT as the value for the *lFlags* parameter. If more than one WIA 2.0 device matches the specification, all matching devices are displayed in the SelectDevice dialog box so the user may choose one.

> [!Note]  
> It is recommended that applications make device and image selection available through a menu item named **From scanner** on the **File** menu.

 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wia.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wia.idl</dt> </dl> |



 

 




