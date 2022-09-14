---
description: IWiaDevMgr2::SelectDeviceDlg method - Displays a dialog box that enables the user to select a hardware device for image acquisition.
ms.assetid: cd020dc6-fddf-4d7f-aa57-eae94953ef4e
title: IWiaDevMgr2::SelectDeviceDlg method (Wia.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWiaDevMgr2.SelectDeviceDlg
api_type: 
- COM
api_location: 
- Wia.h
---

# IWiaDevMgr2::SelectDeviceDlg method

Displays a dialog box that enables the user to select a hardware device for image acquisition.

## Syntax


```C++
HRESULT SelectDeviceDlg(
  [in]          HWND      hwndParent,
  [in]          LONG      lDeviceType,
  [in]          LONG      lFlags,
  [in, out]     BSTR      *pbstrDeviceID,
  [out, retval] IWiaItem2 **ppItemRoot
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

*pbstrDeviceID* \[in, out\]
</dt> <dd>

Type: **BSTR\***

On output, receives a string which contains the device's identifier string. On input, pass the address of a pointer if this information is needed, or **NULL** if it is not needed.

</dd> <dt>

*ppItemRoot* \[out, retval\]
</dt> <dd>

Type: **[**IWiaItem2**](-wia-iwiaitem2.md)\*\***

Receives the address of a pointer to the [**IWiaItem2**](-wia-iwiaitem2.md) interface of the root item of the hierarchical tree that represents the selected WIA 2.0 device. If no device is found, it receives **NULL**.

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

This method creates and displays the **Select Device** dialog box so the user can select a WIA 2.0 device for image acquisition. If a device is successfully selected, the **IWiaDevMgr2::SelectDeviceDlg** method creates a hierarchical tree of [**IWiaItem2**](-wia-iwiaitem2.md) objects for the device. It stores a pointer to the **IWiaItem2** interface of the root item in the parameter *ppItemRoot*.

The application can restrict the devices displayed to the user to particular types by specifying the device types through the *lDeviceType* parameter. If only one device meets the specification, **IWiaDevMgr2::SelectDeviceDlg** does not display the **Select Device** dialog box. Instead it creates the [**IWiaItem2**](-wia-iwiaitem2.md) tree for the device and store a pointer to the **IWiaItem2** interface of the root item in the parameter *ppItemRoot*. You can override this behavior and force **IWiaDevMgr2::SelectDeviceDlg** to display the dialog box by specifying WIA\_SELECT\_DEVICE\_NODEFAULT as the value for the *lFlags* parameter. If more than one WIA 2.0 device matches the specification, all matching devices are displayed in the **Select Device** dialog box so the user may choose one.

Applications must call the [IUnknown::Release](/windows/win32/api/unknwn/nf-unknwn-iunknown-release) method on the interface pointers they receive through the *ppItemRoot* parameter.

> [!Note]  
> It is recommended that applications make device and image selection available through a menu item named **From scanner** on the **File** menu.

 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wia.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wia.idl</dt> </dl> |



 

 
