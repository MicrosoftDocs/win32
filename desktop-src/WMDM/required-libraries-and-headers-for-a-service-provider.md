---
title: Required Libraries and Headers for a Service Provider
description: Required Libraries and Headers for a Service Provider
ms.assetid: 13ef830d-c1cf-4e4c-8fbd-20b5c38b9208
keywords:
- Windows Media Device Manager,libraries
- Device Manager,libraries
- programming guide,libraries
- service providers,libraries
- creating service providers,libraries
- libraries
- Windows Media Device Manager,header files
- Device Manager,header files
- programming guide,header files
- service providers,header files
- creating service providers,header files
- header files
ms.topic: article
ms.date: 05/31/2018
---

# Required Libraries and Headers for a Service Provider

This section lists the libraries, header files or IDL files you will need to include to develop a Windows Media Device Manager application or plug-in. As mentioned in [Compiling the IDL Files Supplied with the SDK](compiling-the-idl-files-supplied-with-the-sdk.md), the SDK includes both IDL files and prebuilt header files, and your application can use either. (Note that some header files do not have corresponding IDL files, and you cannot build them yourself.) If building your own IDL files, include the dependencies listed in Compiling the IDL Files Supplied with the SDK.

Not all applications will require all files; read the description to learn if your application requires a file.



| Prebuilt header or library       | Equivalent IDL                                                                | Description                                                                                                                                                                                                                                                    |
|----------------------------------|-------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| mssachlp.lib                     | none                                                                          | Required by all service providers. Defines Windows Media Device Manager objects.                                                                                                                                                                               |
| initguid.h                       | none (Platform SDK header)                                                    | Required by all service providers to define the **GUID** values using the prebuilt Mswmdm.h file. You must include initguid.h once and only once in your project. This header redefines the **DEFINE\_GUID** macro to avoid external **GUID** naming problems. |
| mswmdm.h                         | WMDM.idl<br/> WMSP.idl<br/> icomponentauthenticate.idl<br/> | Required by all service providers. Defines all the service provider interfaces, structures, metadata, error codes, and other constants.                                                                                                                        |
| sac.h                            | none                                                                          | Required by all service providers. Defines SAC protocols.                                                                                                                                                                                                      |
| scserver.h                       | none                                                                          | Required by all service providers. Declares the [CSecureChannelServer](csecurechannelserver-class.md) class.                                                                                                                                                  |
| wmdmlog.hwmdmlog\_i.c<br/> | Wmdmlog.idl                                                                   | Required by service providers that use the [**IWMDMLogger**](/windows/desktop/api/wmdmlog/nn-wmdmlog-iwmdmlogger) interface.                                                                                                                                                                       |
| wmsdk.h                          | none (provided by Windows Media Format SDK)                                   | Required for service providers that use Windows Media Format SDK methods.                                                                                                                                                                                      |
| wmvcore.lib                      | none                                                                          | Required by service providers that use Windows Media Format SDK objects or functions.                                                                                                                                                                          |
| mmreg.h                          | none (Platform SDK header)                                                    | Required by service providers that reference various standard Windows Media format definitions, such as **WAVEFORMATEX**.                                                                                                                                      |
| MtpExt.h                         | none                                                                          | Required for service providers that handle [**IMDSPDevice3::DeviceIoControl**](/windows/desktop/api/mswmdm/nf-mswmdm-imdspdevice3-deviceiocontrol) on MTP devices. Defines various standard MTP constants and structures.                                                                        |
| Key.c                            | none                                                                          | Defines a key and certificate from Microsoft. The version shipped with the SDK includes a test dummy key that will allow the use of non-DRM protected Windows Media files.                                                                                     |



 

## Related topics

<dl> <dt>

[**Creating a Service Provider**](creating-a-service-provider.md)
</dt> </dl>

 

 





