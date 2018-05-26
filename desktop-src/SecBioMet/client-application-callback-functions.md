---
title: Client Application Callback Functions
description: Two types of callback signatures.
ms.assetid: 5569BFF3-9EEC-42E6-8F63-0C569C68FA74
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Client Application Callback Functions

The Windows Biometric Framework supports two types of callback signatures. Beginning with Windows 8, the following callback is supported. We recommend that you implement this callback for all new applications. This callback cannot, however, be used in Windows 7.



| Callback                                                                                     | Description                                                                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**PWINBIO\_ASYNC\_COMPLETION\_CALLBACK**](/windows/win32/Winbio/nc-winbio-pwinbio_async_completion_callback?branch=master)<br/> | Notifies the client application that an asynchronous operation started by using [**WinBioAsyncOpenSession**](/windows/win32/Winbio/nf-winbio-winbioasyncopensession?branch=master) or [**WinBioAsyncOpenFramework**](/windows/win32/Winbio/nf-winbio-winbioasyncopenframework?branch=master) has completed.<br/> |



 

The following callback functions were introduced in Windows 7. We recommend that you do not implement them for new applications that target Windows 8 and later operating systems.



| Callback                                                                                 | Description                                                                                                                           |
|------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| [**PWINBIO\_CAPTURE\_CALLBACK**](/windows/win32/Winbio/nc-winbio-pwinbio_capture_callback?branch=master)<br/>                | Returns results from the asynchronous [**WinBioCaptureSampleWithCallback**](/windows/win32/Winbio/nf-winbio-winbiocapturesamplewithcallback?branch=master) function.<br/> |
| [**PWINBIO\_ENROLL\_CAPTURE\_CALLBACK**](/windows/win32/Winbio/nc-winbio-pwinbio_enroll_capture_callback?branch=master)<br/> | Returns results from the asynchronous [**WinBioEnrollCaptureWithCallback**](/windows/win32/Winbio/nf-winbio-winbioenrollcapturewithcallback?branch=master) function.<br/> |
| [**PWINBIO\_EVENT\_CALLBACK**](/windows/win32/Winbio/nc-winbio-pwinbio_event_callback?branch=master)<br/>                    | Returns results from the asynchronous [**WinBioRegisterEventMonitor**](/windows/win32/Winbio/nf-winbio-winbioregistereventmonitor?branch=master) function.<br/>           |
| [**PWINBIO\_IDENTIFY\_CALLBACK**](/windows/win32/Winbio/nc-winbio-pwinbio_identify_callback?branch=master)<br/>              | Returns results from the asynchronous [**WinBioIdentifyWithCallback**](/windows/win32/Winbio/nf-winbio-winbioidentifywithcallback?branch=master) function.<br/>           |
| [**PWINBIO\_LOCATE\_SENSOR\_CALLBACK**](/windows/win32/Winbio/nc-winbio-pwinbio_locate_sensor_callback?branch=master)<br/>   | Returns results from the asynchronous [**WinBioLocateSensorWithCallback**](/windows/win32/Winbio/nf-winbio-winbiolocatesensorwithcallback?branch=master) function.<br/>   |
| [**PWINBIO\_VERIFY\_CALLBACK**](/windows/win32/Winbio/nc-winbio-pwinbio_verify_callback?branch=master)<br/>                  | Returns results from the asynchronous [**WinBioVerifyWithCallback**](/windows/win32/Winbio/nf-winbio-winbioverifywithcallback?branch=master) function.<br/>               |



 

## Related topics

<dl> <dt>

[Client Application Reference](client-application-reference.md)
</dt> </dl>

 

 





