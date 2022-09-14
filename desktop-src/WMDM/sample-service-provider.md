---
title: Sample Service Provider
description: Sample Service Provider
ms.assetid: bbdeddb5-4ddf-4a61-828c-a9ba7af307ea
keywords:
- Windows Media Device Manager,samples
- Device Manager,samples
- Windows Media Device Manager,service provider sample
- Device Manager,service provider sample
- service providers,samples
- samples,service providers
ms.topic: article
ms.date: 05/31/2018
---

# Sample Service Provider

The Windows Media Device Manager SDK includes a sample service provider for you to use. This service provider includes a class that reports each hard drive on the computer as if it were an attached device. The only application that will use this service provider is the sample application; Windows Explorer will not see the "devices" reported by this service provider. The service provider sample is a COM object built on ATL. The following steps explain how to use the sample service provider:

> [!Note]  
> The sample service provider implements very few features, and so it should not be used for testing Windows Media Device Manager applications. To test an application, use a fully-implemented service provider.

 

-   The sample was shipped with a coding error that will cause the service provider to malfunction. To correct this error, open the MDSPEnumStorage.cpp file installed in the folder < *SDK installation path* >\\WMFSDK95\\WMDM\\mdsp\\mshdsp, go to line 185, and change the following line:

`wcsncpy(pStg->m_wcsName, m_wcsPath, dwLen);`

To this:

`wcsncpy(pStg->m_wcsName, m_wcsPath, ARRAYSIZE(pStg->m_wcsName));`

1.  Compile the MsHDSP.dll file. You can do this using either NMAKE or Visual Studio. See [Compiling the Sample Service Provider Using NMAKE](compiling-the-sample-service-provider-using-nmake.md) or [Compiling the Sample Service Provider Using Visual Studio](compiling-the-sample-service-provider-using-visual-studio.md) to learn how to compile the application.
2.  Register MsHDSP.dll using regsvr32. The following line, typed into a command-prompt window in the same folder as MsHDSP.dll, will register the sample service provider:

    ```C++
    regsvr32 mshdsp.dll
    ```

    

    To stop impersonating a device, enter the following line at the command prompt:

    ```C++
    regsvr32 /u mshdsp.dll
    ```

    

3.  The removable devices impersonated by this DLL can only be seen by the sample application shipped with this SDK. Compile the sample application using one of the methods described in [Sample Desktop Application](sample-desktop-application.md).
4.  To debug the service provider with Visual Studio, open the service provider in Visual Studio and select **Start** on the **Debug** menu. In the popup dialog box, browse to the sample application you built in the preceding step, and click **OK**, and the service provider will begin running in debug mode.

    To run the service provider without debugging in Visual Studio, simply register the msdhsp.dll and run the sample desktop application that ships with the SDK. The sample desktop application runs the sample service provider automatically.

## Related topics

<dl> <dt>

[**Samples**](samples.md)
</dt> </dl>

 

 




