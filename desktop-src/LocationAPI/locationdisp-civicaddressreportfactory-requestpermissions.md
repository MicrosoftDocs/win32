---
description: LocationDisp.CivicAddressReportFactory.RequestPermissions method - Opens a system dialog box to request user permission for location-enabled devices.
ms.assetid: b213591a-2830-4979-b532-e71cdef1b994
title: LocationDisp.CivicAddressReportFactory.RequestPermissions method
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- LocationDisp.CivicAddressReportFactory.RequestPermissions
api_type:
- COM
api_location: 
---

# LocationDisp.CivicAddressReportFactory.RequestPermissions method

\[The Location API object model is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, to access location from a website, use the [W3C Geolocation API](/previous-versions/windows/internet-explorer/ie-developer/samples/gg589513(v=vs.85)). To access location from a desktop application, use the [**Windows.Devices.Geolocation**](/uwp/api/Windows.Devices.Geolocation) API.\]

Opens a system dialog box to request user permission for location-enabled devices.

## Syntax


```JScript
LocationDisp.CivicAddressReportFactory.RequestPermissions(
  hWnd
)
```



## Parameters

<dl> <dt>

*hWnd* 
</dt> <dd>

This parameter is not used and should be set to zero.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

The call is synchronous and the caller waits for the dialog box to be closed.

> [!Note]  
> If an application running in protected mode, such as a Browser Helper Object (BHO) for Internet Explorer, calls **RequestPermissions**, and the user chooses the **Don't enable this location sensor** option in the dialog box, the location provider will not be enabled, but Windows will display the dialog box again if **RequestPermissions** is called again by the same user. Applications that run in protected mode may choose to not call [**RequestPermissions**](/windows/win32/api/locationapi/nf-locationapi-ilocation-requestpermissions) on startup so that the user does not see a possibly unwanted dialog box each time the application starts.

 

## Examples

For an example of how to use this method, see [Listening for Civic Address Report Events](/uwp/api/Windows.Devices.Geolocation).

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/> |
| Minimum supported server<br/> | None supported<br/>                  |



 

