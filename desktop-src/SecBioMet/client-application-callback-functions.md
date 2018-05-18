---
title: Client Application Callback Functions
description: Two types of callback signatures.
ms.assetid: '5569BFF3-9EEC-42E6-8F63-0C569C68FA74'
---

# Client Application Callback Functions

The Windows Biometric Framework supports two types of callback signatures. Beginning with Windows 8, the following callback is supported. We recommend that you implement this callback for all new applications. This callback cannot, however, be used in Windows 7.



| Callback                                                                                     | Description                                                                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**PWINBIO\_ASYNC\_COMPLETION\_CALLBACK**](pwinbio-async-completion-callback.md)<br/> | Notifies the client application that an asynchronous operation started by using [**WinBioAsyncOpenSession**](winbioasyncopensession.md) or [**WinBioAsyncOpenFramework**](winbioasyncopenframework.md) has completed.<br/> |



 

The following callback functions were introduced in Windows 7. We recommend that you do not implement them for new applications that target Windows 8 and later operating systems.



| Callback                                                                                 | Description                                                                                                                           |
|------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| [**PWINBIO\_CAPTURE\_CALLBACK**](pwinbio-capture-callback.md)<br/>                | Returns results from the asynchronous [**WinBioCaptureSampleWithCallback**](winbiocapturesamplewithcallback.md) function.<br/> |
| [**PWINBIO\_ENROLL\_CAPTURE\_CALLBACK**](pwinbio-enroll-capture-callback.md)<br/> | Returns results from the asynchronous [**WinBioEnrollCaptureWithCallback**](winbioenrollcapturewithcallback.md) function.<br/> |
| [**PWINBIO\_EVENT\_CALLBACK**](pwinbio-event-callback.md)<br/>                    | Returns results from the asynchronous [**WinBioRegisterEventMonitor**](winbioregistereventmonitor.md) function.<br/>           |
| [**PWINBIO\_IDENTIFY\_CALLBACK**](pwinbio-identify-callback.md)<br/>              | Returns results from the asynchronous [**WinBioIdentifyWithCallback**](winbioidentifywithcallback.md) function.<br/>           |
| [**PWINBIO\_LOCATE\_SENSOR\_CALLBACK**](pwinbio-locate-sensor-callback.md)<br/>   | Returns results from the asynchronous [**WinBioLocateSensorWithCallback**](winbiolocatesensorwithcallback.md) function.<br/>   |
| [**PWINBIO\_VERIFY\_CALLBACK**](pwinbio-verify-callback.md)<br/>                  | Returns results from the asynchronous [**WinBioVerifyWithCallback**](winbioverifywithcallback.md) function.<br/>               |



 

## Related topics

<dl> <dt>

[Client Application Reference](client-application-reference.md)
</dt> </dl>

 

 





