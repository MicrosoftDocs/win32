---
title: Client Application Callback Functions
description: Two types of callback signatures.
ms.assetid: 5569BFF3-9EEC-42E6-8F63-0C569C68FA74
ms.topic: article
ms.date: 05/31/2018
---

# Client Application Callback Functions

The Windows Biometric Framework supports two types of callback signatures. Beginning with Windows 8, the following callback is supported. We recommend that you implement this callback for all new applications. This callback cannot, however, be used in Windows 7.



| Callback                                                                                     | Description                                                                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**PWINBIO\_ASYNC\_COMPLETION\_CALLBACK**](/windows/desktop/api/Winbio/nc-winbio-pwinbio_async_completion_callback)<br/> | Notifies the client application that an asynchronous operation started by using [**WinBioAsyncOpenSession**](/windows/desktop/api/Winbio/nf-winbio-winbioasyncopensession) or [**WinBioAsyncOpenFramework**](/windows/desktop/api/Winbio/nf-winbio-winbioasyncopenframework) has completed.<br/> |



 

The following callback functions were introduced in Windows 7. We recommend that you do not implement them for new applications that target Windows 8 and later operating systems.



| Callback                                                                                 | Description                                                                                                                           |
|------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| [**PWINBIO\_CAPTURE\_CALLBACK**](/windows/desktop/api/Winbio/nc-winbio-pwinbio_capture_callback)<br/>                | Returns results from the asynchronous [**WinBioCaptureSampleWithCallback**](/windows/desktop/api/Winbio/nf-winbio-winbiocapturesamplewithcallback) function.<br/> |
| [**PWINBIO\_ENROLL\_CAPTURE\_CALLBACK**](/windows/desktop/api/Winbio/nc-winbio-pwinbio_enroll_capture_callback)<br/> | Returns results from the asynchronous [**WinBioEnrollCaptureWithCallback**](/windows/desktop/api/Winbio/nf-winbio-winbioenrollcapturewithcallback) function.<br/> |
| [**PWINBIO\_EVENT\_CALLBACK**](/windows/desktop/api/Winbio/nc-winbio-pwinbio_event_callback)<br/>                    | Returns results from the asynchronous [**WinBioRegisterEventMonitor**](/windows/desktop/api/Winbio/nf-winbio-winbioregistereventmonitor) function.<br/>           |
| [**PWINBIO\_IDENTIFY\_CALLBACK**](/windows/desktop/api/Winbio/nc-winbio-pwinbio_identify_callback)<br/>              | Returns results from the asynchronous [**WinBioIdentifyWithCallback**](/windows/desktop/api/Winbio/nf-winbio-winbioidentifywithcallback) function.<br/>           |
| [**PWINBIO\_LOCATE\_SENSOR\_CALLBACK**](/windows/desktop/api/Winbio/nc-winbio-pwinbio_locate_sensor_callback)<br/>   | Returns results from the asynchronous [**WinBioLocateSensorWithCallback**](/windows/desktop/api/Winbio/nf-winbio-winbiolocatesensorwithcallback) function.<br/>   |
| [**PWINBIO\_VERIFY\_CALLBACK**](/windows/desktop/api/Winbio/nc-winbio-pwinbio_verify_callback)<br/>                  | Returns results from the asynchronous [**WinBioVerifyWithCallback**](/windows/desktop/api/Winbio/nf-winbio-winbioverifywithcallback) function.<br/>               |



 

## Related topics

<dl> <dt>

[Client Application Reference](client-application-reference.md)
</dt> </dl>

 

 





