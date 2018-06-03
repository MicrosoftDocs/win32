---
title: Making an Application Still Image-Aware
description: Existing applications must be revised to make use of the Still Image (STI) push model behavior.
ms.assetid: 6fa6af12-4aea-4143-af8e-967473b571b4
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Making an Application Still Image-Aware

Existing applications must be revised to make use of the Still Image (STI) push model behavior.

An application detects whether or not it was launched by the Event Monitor. If the [**GetSTILaunchInformation**](istillimage-getstilaunchinformation.md) method return value indicates success, then the application was launched by the Event Monitor. An application, TWAIN data source, or other software can decide to reject using the device that caused the push model event. However, it must notify the user in some manner as to why the device is not acceptable. This allows the user to access the STI Control Panel and deselect this particular application for use with this device.

If the Event Monitor launched an application, the application may need additional information to locate the device by means of its imaging API. TWAIN and ISIS are the two imaging APIs for which Microsoft defines information. However, any imaging API can use the STI mechanism to obtain additional information. On installation of a Still Image device, an .inf file is used to place information into the registry that provides this supplementary information. A key/value string is used to specify this information, such as:

`TWAINDS="HP PictureScan 3.0"`

`ISIS="epson.pxw"`

The application then uses the [**GetDeviceValue**](istillimage-getdevicevalue.md) function to obtain the associated data.

Once a TWAIN data source has been loaded, it obtains the device and event by the same [**GetSTILaunchInformation**](istillimage-getstilaunchinformation.md) method because it is in the original address space. With this information, it can open the device and start communication. This provides a seamless transition from push event to application launch and image acquisition.

If the Event Monitor receives another event on the device, it launches the registered application again. Therefore, it is wise to register a small stub program for each device event. The stub program loads quickly when an event occurs. If, for example, a user presses a Scan button on a scanner that triggers a Still Image event, the Event Monitor launches the stub program. The stub determines if the appropriate application to respond to the event is running. If not, it launches the application. If the user presses the Scan button again without closing the application, the Event Monitor runs the stub program again. The stub checks to see if it is the first program instance or if the appropriate application is running. If another copy of the stub already launched the application, the current instance of the stub uses an interprocess communication (IPC) method to pass the event information to the running application. It then exits and keeps memory usage to a minimum.

When an application is uninstalled, it needs to call [**UnRegisterLaunchAppliction**](istillimage-unregisterlaunchapplication.md) to remove itself from the permanent list of applications that use the push model. You cannot add or remove an application from the Control Panel. You can only select or deselect those applications to be associated with particular devices.

The following code fragment illustrates how an application can use the Still Image API:


```C++
// call STI to find out whether we were launched by STI 
HRESULT hres; 
hres = StiCreateInstance(GetModuleHandle(NULL), STI_VERSION, &amp;g_pSti, NULL);
hres = g_pSti->RegisterLaunchApplication(L"MyApp", szModulePathW);

// Was this a STI launch? 
// Call STI-API and get the device name, event, and event code 
WCHAR   szDeviceName[65];
WCHAR   szEventName[65];
char    ActualDeviceName [256];
DWORD   dwEventCode;
hres = g_pSti->GetSTILaunchInformation(szDeviceName,
                                       &amp;dwEventCode,
                                       szEventName);
if (SUCCEEDED(hres)) 
{
    DWORD val = 256, type;
    g_pSti->GetDeviceValue(szDeviceName, 
                           STI_DEVICE_VALUE_TWAIN_NAME,
                           &amp;type,
                           (unsigned char*)&amp;ActualDeviceName[0],
                           &amp;val);
}
```



 

 




