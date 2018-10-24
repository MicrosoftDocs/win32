---
Description: Opens a system dialog box to request user permission for location-enabled devices.
ms.assetid: 25b4368d-ff9d-4806-a22e-4ae0760d6f0f
title: LocationDisp.LatLongReportFactory.RequestPermissions method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- LocationDisp.LatLongReportFactory.RequestPermissions
api_type: 
- COM
api_location: 
---

# LocationDisp.LatLongReportFactory.RequestPermissions method

\[The Location API object model is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, to access location from a website, use the [W3C Geolocation API](https://msdn.microsoft.com/library/gg589513). To access location from a desktop application, use the [**Windows.Devices.Geolocation**](https://msdn.microsoft.com/library/windows/apps/br225603) API.\]

Opens a system dialog box to request user permission for location-enabled devices.

## Syntax


```JScript
LocationDisp.LatLongReportFactory.RequestPermissions(
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
> If an application running in protected mode, such as a Browser Helper Object (BHO) for Internet Explorer, calls **RequestPermissions**, and the user chooses the **Don't enable this location sensor** option in the dialog box, the location provider will not be enabled, but Windows will display the dialog box again if **RequestPermissions** is called again by the same user. Applications that run in protected mode may choose to not call **RequestPermissions** on startup so that the user does not see a possibly unwanted dialog box each time the application starts.

 

## Examples

For an example of how to use this method, see [Listening for LatLong Report Events](https://msdn.microsoft.com/library/windows/apps/br225603).

## Requirements



|                                     |                                            |
|-------------------------------------|--------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/> |
| Minimum supported server<br/> | None supported<br/>                  |



 

 




