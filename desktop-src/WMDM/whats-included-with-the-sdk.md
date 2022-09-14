---
title: What's Included with the SDK
description: What's Included with the SDK
ms.assetid: c17de30b-d4b4-4698-accf-721b6c267769
keywords:
- Windows Media Device Manager,software development kit (SDK)
- Device Manager,software development kit (SDK)
- Windows Media Device Manager SDK
- Device Manager SDK
ms.topic: article
ms.date: 05/31/2018
---

# What's Included with the SDK

The following table describes the contents of the Windows Media Device Manager SDK. All files or folders are described in relation to the root SDK installation path.



| File                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WMDM\\                     | Top-level folder for the Windows Media Device Manager SDK. This folder includes the makefile for building all the sample applications.                                                                                                                                                                                                                                                                                                              |
| idl\\                      | Folder that contains all the IDL files required to build headers needed for Windows Media Device Manager methods. However, instead of using these files, you can use the header files supplied in the inc\\ folder.<br/> To see a list of these IDL files, and to learn which header files are built from which IDL files, see [Compiling the IDL Files Supplied with the SDK](compiling-the-idl-files-supplied-with-the-sdk.md).<br/> |
| inc\\....<br/>       | Folder that includes all the headers that define the interfaces and data types in this SDK.                                                                                                                                                                                                                                                                                                                                                         |
| mswmdm.h                   | Defines all the application interfaces, service provider interfaces, secure content provider interfaces, error codes, constants, structures, and the [**IComponentAuthenticate**](/windows/desktop/api/mswmdm/nn-mswmdm-icomponentauthenticate) interface.                                                                                                                                                                                                                            |
| mswmdm\_i.c                | Defines the [**IWMDMNotification**](/windows/desktop/api/mswmdm/nn-mswmdm-iwmdmnotification) interface.                                                                                                                                                                                                                                                                                                                                                                               |
| MtpExt.h                   | Defines MTP-specific structures required for applications calling [**IWMDMDevice3::DeviceIoControl**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmdevice3-deviceiocontrol).                                                                                                                                                                                                                                                                                                            |
| resource.h                 | Defines various resource constants used by the SDK samples.                                                                                                                                                                                                                                                                                                                                                                                         |
| sac.h                      | Defines secure authenticated channel data required by all applications and service providers.                                                                                                                                                                                                                                                                                                                                                       |
| scclient.h                 | Defines the [CSecureChannelClient](csecurechannelclient-class.md) class required by all applications.                                                                                                                                                                                                                                                                                                                                              |
| scserver.h                 | Defines the [CSecureChannelServer](csecurechannelserver-class.md) class required by all service providers.                                                                                                                                                                                                                                                                                                                                         |
| wmdm\_ver.h                | Optional version information about Windows Media Device Manager.                                                                                                                                                                                                                                                                                                                                                                                    |
| wmdmlog.h, wmdmlog\_i.c    | Required for applications or service providers that use the [**IWMDMLogger**](/windows/desktop/api/wmdmlog/nn-wmdmlog-iwmdmlogger) interface.                                                                                                                                                                                                                                                                                                                                           |
| wmdrmdeviceapp.h           | Required for applications that handle content metering (see [Metering Content Usage](metering-content-usage.md)).                                                                                                                                                                                                                                                                                                                                  |
| wmsstd.h                   | Defines helper macros used by the SDK samples.                                                                                                                                                                                                                                                                                                                                                                                                      |
| lib\\                      | Folder that holds the Windows Media Device Manager libraries.                                                                                                                                                                                                                                                                                                                                                                                       |
| mssachlp.lib               | The static library required by all Windows Media Device Manager applications and service providers.                                                                                                                                                                                                                                                                                                                                                 |
| drmcrypto.lib              | The static library required by all Windows Media Device Manager applications and service providers that use DRM.                                                                                                                                                                                                                                                                                                                                    |
| mdsp\\....<br/>      | Folder that contains the code for a sample service provider. For information about this sample, including how to compile and run it, see [Sample Service Provider](sample-service-provider.md).                                                                                                                                                                                                                                                    |
| apps\\....<br/>      | Folder that contains two subfolders that hold two halves of the code for a sample desktop application provided with the SDK. For information about this sample, including how to compile it, see [Sample Desktop Application](sample-desktop-application.md).                                                                                                                                                                                      |
| devicekit\\....<br/> | Folder that contains a suite of tools for testing your portable device using Windows Media Device Manager 11. Testing includes device and file enumeration and transfer, DRM capabilities, and MTP compliance. These tools have their own documentation file.                                                                                                                                                                                       |



 

## Related topics

<dl> <dt>

[**Getting Started**](getting-started.md)
</dt> </dl>

 

 





