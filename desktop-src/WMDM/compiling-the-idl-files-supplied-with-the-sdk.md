---
title: Compiling the IDL Files Supplied with the SDK
description: Compiling the IDL Files Supplied with the SDK
ms.assetid: 718528eb-6ac4-466d-8dfd-d6f2b6c30303
keywords:
- Windows Media Device Manager,IDL files
- Device Manager,IDL files
- desktop applications,IDL files
- service providers,IDL files
- programming guide,IDL files
- IDL files
ms.topic: article
ms.date: 05/31/2018
---

# Compiling the IDL Files Supplied with the SDK

The Windows Media Device Manager SDK includes both header files and the source IDL files for most of these header files. The header files are located in the \\inc\\ folder in the SDK installation path. The IDL files are located in the \\idl\\ folder.

The precompiled headers are much simpler to use, and several of the IDL files are combined into a single provided header. However, if you decide to process your own header files from the provided IDL files, this topic describes which IDL files create which header files, and also describes the dependencies of each IDL file.

**Equivalent IDL and Provided Header Files**



| **IDL**                                                                                            | **Equivalent supplied header**               | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|----------------------------------------------------------------------------------------------------|----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WMDM.idl<br/> WMSP.idl<br/> WMSCP.idl<br/> icomponentauthenticate.idl<br/> | Mswmdm.h                                     | All four IDL files are included in this single provided header.<br/> **WMDM.idl** Defines all the application interfaces and required structures, constants, and error codes.<br/> **WMSP.idl** Defines all the service provider interfaces.<br/> **WMSCP.idl** Defines all the interfaces, GUID values, and constants required by secure content providers.<br/> **icomponentauthenticate.idl** Defines the [**IComponentAuthenticate**](/windows/desktop/api/mswmdm/nn-mswmdm-icomponentauthenticate) interface.<br/> |
| Wmdmlog.idl                                                                                        | Wmdmlog.h<br/> wmdmlog\_i.c<br/> | Defines the logging interfaces.<br/> Both supplied header files must be used, rather than just the .h file, because of a problem with the IDL file.<br/>                                                                                                                                                                                                                                                                                                                                                |
| WMDRMDeviceApp.idl                                                                                 | Wmdrmdeviceapp.h                             | Defines the [**IWMDRMDeviceApp**](iwmdrmdeviceapp.md) and [**IWMDRMDeviceApp2**](iwmdrmdeviceapp2.md) interfaces used by applications that update DRM on devices or meter play counts on devices.                                                                                                                                                                                                                                                                                                                 |



 

**IDL Dependencies**

Several of the provided IDL files have build dependencies. If you plan to compile the IDL files yourself, you must process these external dependencies in the order shown in the following table.



|   IDL                      |   Dependencies                                                                   |
|----------------------------|----------------------------------------------------------------------------------|
| icomponentauthenticate.idl | import "oaidl.idl";<br/> \#include "icomponentauthenticate.idl"<br/> |
| WMDM.idl                   | No external dependencies                                                         |
| WmdmLog.idl                | No external dependencies                                                         |
| WMDRMDeviceApp.idl         | No external dependencies                                                         |
| WMSCP.idl                  | \#include "WMDRMDeviceApp.idl"<br/> \#include "WMSP.idl"<br/>        |
| WMSP.idl                   | \#include "WMDM.idl"                                                             |



 

## Related topics

<dl> <dt>

[**Tasks Common to Applications and Service Providers**](tasks-common-to-applications-and-service-providers.md)
</dt> </dl>

 

 





