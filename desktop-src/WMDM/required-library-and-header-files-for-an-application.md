---
title: Required Library and Header Files for an Application
description: Required Library and Header Files for an Application
ms.assetid: 922627d5-03a8-4b5b-be00-6f2c3500dd66
keywords:
- Windows Media Device Manager,libraries
- Device Manager,libraries
- programming guide,libraries
- desktop applications,libraries
- creating Windows Media Device Manager applications,libraries
- libraries
- Windows Media Device Manager,header files
- Device Manager,header files
- programming guide,header files
- desktop applications,header files
- creating Windows Media Device Manager applications,header files
- header files
ms.topic: article
ms.date: 05/31/2018
---

# Required Library and Header Files for an Application

This section lists the libraries, header files or IDL files you will need to include to develop a Windows Media Device Manager application or plug-in. As mentioned in [Compiling the IDL Files Supplied with the SDK](compiling-the-idl-files-supplied-with-the-sdk.md), the SDK includes both IDL files and prebuilt header files, and your application can use either. (Note that some header files do not have corresponding IDL files, and you cannot build them yourself.) If building your own IDL files, include the dependencies listed in Compiling the IDL Files Supplied with the SDK.

Not all applications will require all files; read the description to learn whether your application requires a file.



| Prebuilt header or library       | Equivalent IDL                                | Description                                                                                                                                                                                                                                               |
|----------------------------------|-----------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| mssachlp.lib                     | none                                          | Required by all applications. Contains Windows Media Device Manager objects.                                                                                                                                                                              |
| wmvcore.lib                      | none                                          | Required by applications that use Windows Media Format SDK objects or functions.                                                                                                                                                                          |
| initguid.h                       | none (Platform SDK header)                    | Required by all applications to define the **GUID** values using the prebuilt Mswmdm.h file. You must include initguid.h once and only once in your project. This header redefines the **DEFINE\_GUID** macro to avoid external **GUID** naming problems. |
| mmreg.h                          | none (Platform SDK header)                    | Required by applications that reference various standard Windows Media format definitions, such as **WAVEFORMATEX**.                                                                                                                                      |
| mswmdm.h                         | WMDM.idlicomponentauthenticate.idl<br/> | Required by all applications. Defines all the application interfaces, as well as structures, metadata, error, and other constants.                                                                                                                        |
| sac.h                            | none                                          | Required by all applications. Defines SAC protocols.                                                                                                                                                                                                      |
| scclient.h                       | none                                          | Required by all applications. Declares the [CSecureChannelClient](csecurechannelclient-class.md) class.                                                                                                                                                  |
| wmdmlog.hwmdmlog\_i.c<br/> | Wmdmlog.idl                                   | Required by applications that use the [**IWMDMLogger**](/windows/desktop/api/wmdmlog/nn-wmdmlog-iwmdmlogger) interface.                                                                                                                                                                       |
| wmdrmdeviceapp.h                 | WMDRMDeviceApp.idl                            | Required by applications or plug-ins that update DRM components or meter play counts on devices.                                                                                                                                                          |
| wmsdk.h                          | none (provided by Windows Media Format SDK)   | Required for applications that use Windows Media Format SDK methods.                                                                                                                                                                                      |
| MtpExt.h                         | none                                          | Required for applications that call [**IWMDMDevice3::DeviceIoControl**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmdevice3-deviceiocontrol) on MTP devices. Defines various standard MTP constants and structures.                                                                          |
| Key.c                            | none                                          | Defines a key and certificate from Microsoft. The version shipped with the SDK includes a test dummy key that will allow the use of non-DRM protected Windows Media files.                                                                                |



 

## Related topics

<dl> <dt>

[**Programming Guide**](programming-guide.md)
</dt> </dl>

 

 





