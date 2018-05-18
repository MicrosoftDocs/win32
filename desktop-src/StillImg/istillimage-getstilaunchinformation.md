---
title: GetSTILaunchInformation method
description: The IStillImage GetSTILaunchInformation method is used to determine if an application was launched by a push model device event. It is also used to retrieve the device event information.
ms.assetid: 'd4e626cf-7fdf-4816-83f8-ca9fe31d2d6f'
keywords: ["GetSTILaunchInformation method Still Image"]
topic_type:
- apiref
api_name:
- GetSTILaunchInformation
api_location:
- Sti.dll
api_type:
- COM
---

# GetSTILaunchInformation method

The **IStillImage::GetSTILaunchInformation** method is used to determine if an application was launched by a push model device event. It is also used to retrieve the device event information.

## Syntax


```C++
HRESULT GetSTILaunchInformation(
  [out] LPWSTR pwszDeviceName,
        DWORD  pdwEventCode,
  [out] LPWSTR pwszEventName
);
```



## Parameters

<dl> <dt>

*pwszDeviceName* \[out\]
</dt> <dd>

If the application was launched by a push model event by means of the Event Monitor, this is set to the friendly device name of the device which caused the event.

</dd> <dt>

*pdwEventCode* 
</dt> <dd>

Reserved.

</dd> <dt>

*pwszEventName* \[out\]
</dt> <dd>

If the application was launched by a push model event from the Event Monitor, this is set to a string representation of the event GUID. Sti.h defines the following standard event GUIDs:

 



| GUID                                                                                                                                                                                                                                      | Meaning                                             |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| <dl> <dt></dt> </dl>                                                                                                                                                               |                                                     |
| <span id="GUID_DeviceArrivedLaunch"></span><span id="guid_devicearrivedlaunch"></span><span id="GUID_DEVICEARRIVEDLAUNCH"></span><dl> <dt>**GUID\_DeviceArrivedLaunch**</dt> </dl> | Launch the Still Image application.<br/>      |
| <span id="GUID_ScanImage"></span><span id="guid_scanimage"></span><span id="GUID_SCANIMAGE"></span><dl> <dt>**GUID\_ScanImage**</dt> </dl>                                         | Use the imaging device to scan an image.<br/> |
| <span id="GUID_ScanPrintImage"></span><span id="guid_scanprintimage"></span><span id="GUID_SCANPRINTIMAGE"></span><dl> <dt>**GUID\_ScanPrintImage**</dt> </dl>                     | Scan an image and print it.<br/>              |
| <span id="GUID_ScanFaxImage"></span><span id="guid_scanfaximage"></span><span id="GUID_SCANFAXIMAGE"></span><dl> <dt>**GUID\_ScanFaxImage**</dt> </dl>                             | Scan an image and fax it.<br/>                |
| <span id="GUID_STIUserDefined1"></span><span id="guid_stiuserdefined1"></span><span id="GUID_STIUSERDEFINED1"></span><dl> <dt>**GUID\_STIUserDefined1**</dt> </dl>                 | Application-defined event.<br/>               |
| <span id="GUID_STIUserDefined2"></span><span id="guid_stiuserdefined2"></span><span id="GUID_STIUSERDEFINED2"></span><dl> <dt>**GUID\_STIUserDefined2**</dt> </dl>                 | Application-defined event.<br/>               |
| <span id="GUID_STIUserDefined3"></span><span id="guid_stiuserdefined3"></span><span id="GUID_STIUSERDEFINED3"></span><dl> <dt>**GUID\_STIUserDefined3**</dt> </dl>                 | Application-defined event.<br/>               |



 

</dd> </dl>

## Return value

If the application was launched by the Event Monitor in response to a device event, this method returns S\_OK, and the device event information is stored in the method arguments.

If the application was not launched by the STI Event Monitor in response to a device event, this method returns a COM error code.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Sti.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Sti.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Sti.dll</dt> </dl> |



## See also

<dl> <dt>

[About Still Image](about-still-image.md)
</dt> <dt>

[Making an Application Still Image-Aware](making-an-application-still-image-aware.md)
</dt> </dl>

 

 





