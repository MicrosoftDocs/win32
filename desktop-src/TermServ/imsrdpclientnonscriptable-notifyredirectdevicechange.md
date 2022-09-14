---
title: IMsRdpClientNonScriptable NotifyRedirectDeviceChange method
description: Notifies the device redirection module of the Remote Desktop ActiveX control that a device change has occurred on the system. This method passes WM\_DEVICECHANGE notifications to the control.
ms.assetid: 36323831-06e0-4e47-8a6c-06367119298f
ms.tgt_platform: multiple
keywords:
- NotifyRedirectDeviceChange method Remote Desktop Services
- NotifyRedirectDeviceChange method Remote Desktop Services , IMsRdpClientNonScriptable interface
- IMsRdpClientNonScriptable interface Remote Desktop Services , NotifyRedirectDeviceChange method
- NotifyRedirectDeviceChange method Remote Desktop Services , IMsRdpClientNonScriptable2 interface
- IMsRdpClientNonScriptable2 interface Remote Desktop Services , NotifyRedirectDeviceChange method
- NotifyRedirectDeviceChange method Remote Desktop Services , IMsRdpClientNonScriptable3 interface
- IMsRdpClientNonScriptable3 interface Remote Desktop Services , NotifyRedirectDeviceChange method
- NotifyRedirectDeviceChange method Remote Desktop Services , IMsRdpClientNonScriptable4 interface
- IMsRdpClientNonScriptable4 interface Remote Desktop Services , NotifyRedirectDeviceChange method
- NotifyRedirectDeviceChange method Remote Desktop Services , IMsRdpClientNonScriptable5 interface
- IMsRdpClientNonScriptable5 interface Remote Desktop Services , NotifyRedirectDeviceChange method
topic_type:
- apiref
api_name:
- IMsRdpClientNonScriptable.NotifyRedirectDeviceChange
- IMsRdpClientNonScriptable2.NotifyRedirectDeviceChange
- IMsRdpClientNonScriptable3.NotifyRedirectDeviceChange
- IMsRdpClientNonScriptable4.NotifyRedirectDeviceChange
- IMsRdpClientNonScriptable5.NotifyRedirectDeviceChange
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientNonScriptable::NotifyRedirectDeviceChange method

Notifies the device redirection module of the Remote Desktop ActiveX control that a device change has occurred on the system. This method passes [**WM\_DEVICECHANGE**](/windows/desktop/DevIO/wm-devicechange) notifications to the control.

## Syntax


```C++
HRESULT NotifyRedirectDeviceChange(
  [in] WPARAM wParam,
  [in] LPARAM lParam
);
```



## Parameters

<dl> <dt>

*wParam* \[in\]
</dt> <dd>

Specifies the device event. This parameter can be one of the following values.

<dt>

<span id="DBT_CONFIGCHANGECANCELED"></span><span id="dbt_configchangecanceled"></span>

<span id="DBT_CONFIGCHANGECANCELED"></span><span id="dbt_configchangecanceled"></span>**DBT\_CONFIGCHANGECANCELED**


</dt> <dd>

A request to change the current configuration (dock or undock) has been canceled.

</dd> <dt>

<span id="DBT_CONFIGCHANGED"></span><span id="dbt_configchanged"></span>

<span id="DBT_CONFIGCHANGED"></span><span id="dbt_configchanged"></span>**DBT\_CONFIGCHANGED**


</dt> <dd>

The current configuration has changed due to a dock or undock.

</dd> <dt>

<span id="DBT_CUSTOMEVENT"></span><span id="dbt_customevent"></span>

<span id="DBT_CUSTOMEVENT"></span><span id="dbt_customevent"></span>**DBT\_CUSTOMEVENT**


</dt> <dd>

A custom event has occurred.

</dd> <dt>

<span id="DBT_DEVICEARRIVAL"></span><span id="dbt_devicearrival"></span>

<span id="DBT_DEVICEARRIVAL"></span><span id="dbt_devicearrival"></span>**DBT\_DEVICEARRIVAL**


</dt> <dd>

A device has been inserted and is now available.

</dd> <dt>

<span id="DBT_DEVICEQUERYREMOVE"></span><span id="dbt_devicequeryremove"></span>

<span id="DBT_DEVICEQUERYREMOVE"></span><span id="dbt_devicequeryremove"></span>**DBT\_DEVICEQUERYREMOVE**


</dt> <dd>

Permission is requested to remove a device. Any application can deny this request and cancel the removal.

</dd> <dt>

<span id="DBT_DEVICEQUERYREMOVEFAILED"></span><span id="dbt_devicequeryremovefailed"></span>

<span id="DBT_DEVICEQUERYREMOVEFAILED"></span><span id="dbt_devicequeryremovefailed"></span>**DBT\_DEVICEQUERYREMOVEFAILED**


</dt> <dd>

A request to remove a device has been canceled.

</dd> <dt>

<span id="DBT_DEVICEREMOVECOMPLETE"></span><span id="dbt_deviceremovecomplete"></span>

<span id="DBT_DEVICEREMOVECOMPLETE"></span><span id="dbt_deviceremovecomplete"></span>**DBT\_DEVICEREMOVECOMPLETE**


</dt> <dd>

A device has been removed.

</dd> <dt>

<span id="DBT_DEVICEREMOVEPENDING"></span><span id="dbt_deviceremovepending"></span>

<span id="DBT_DEVICEREMOVEPENDING"></span><span id="dbt_deviceremovepending"></span>**DBT\_DEVICEREMOVEPENDING**


</dt> <dd>

A device is about to be removed. The removal cannot be denied.

</dd> <dt>

<span id="DBT_DEVICETYPESPECIFIC"></span><span id="dbt_devicetypespecific"></span>

<span id="DBT_DEVICETYPESPECIFIC"></span><span id="dbt_devicetypespecific"></span>**DBT\_DEVICETYPESPECIFIC**


</dt> <dd>

A device-specific event has occurred.

</dd> <dt>

<span id="DBT_DEVNODES_CHANGED"></span><span id="dbt_devnodes_changed"></span>

<span id="DBT_DEVNODES_CHANGED"></span><span id="dbt_devnodes_changed"></span>**DBT\_DEVNODES\_CHANGED**


</dt> <dd>

A device has been added to or removed from the system.

</dd> <dt>

<span id="DBT_QUERYCHANGECONFIG"></span><span id="dbt_querychangeconfig"></span>

<span id="DBT_QUERYCHANGECONFIG"></span><span id="dbt_querychangeconfig"></span>**DBT\_QUERYCHANGECONFIG**


</dt> <dd>

Permission is requested to change the current configuration (dock or undock).

</dd> <dt>

<span id="DBT_USERDEFINED"></span><span id="dbt_userdefined"></span>

<span id="DBT_USERDEFINED"></span><span id="dbt_userdefined"></span>**DBT\_USERDEFINED**


</dt> <dd>

The meaning of this message is user-defined.

</dd> </dl> </dd> <dt>

*lParam* \[in\]
</dt> <dd>

Pointer to a structure that contains event-specific data. Its format depends on the value of the *wParam* parameter. For more information, refer to the documentation for each event. For more information, see [Device Event Types](/windows/desktop/DevIO/device-event-types).

</dd> </dl>

## Return value

Return **S\_OK** if successful.

## Remarks

A container application that allows dynamic addition or removal of devices should process the [**WM\_DEVICECHANGE**](/windows/desktop/DevIO/wm-devicechange) message in its top level window and forward the message to the control using the **NotifyRedirectDeviceChange** method. An example of a dynamic device change is when a redirected disk drive is added or removed while the system is running.

For more information about Remote Desktop Web Connection, see [Requirements for Remote Desktop Web Connection](requirements-for-remote-desktop-web-connection.md).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                               |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl>       |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl>       |
| IID<br/>                      | IID\_IMsRdpClientNonScriptable is defined as 2f079c4c-87b2-4afd-97ab-20cdb43038ae<br/> |



## See also

<dl> <dt>

[**IMsRdpClientNonScriptable2**](imsrdpclientnonscriptable2.md)
</dt> <dt>

[**IMsRdpClientNonScriptable3**](imsrdpclientnonscriptable3.md)
</dt> <dt>

[**IMsRdpClientNonScriptable4**](imsrdpclientnonscriptable4.md)
</dt> <dt>

[**IMsRdpClientNonScriptable5**](imsrdpclientnonscriptable5.md)
</dt> <dt>

[**IMsRdpClientNonScriptable**](imsrdpclientnonscriptable-interface.md)
</dt> </dl>

 

