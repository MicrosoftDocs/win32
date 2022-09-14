---
title: Updating Existing DSP Plug-ins
description: Updating Existing DSP Plug-ins
ms.assetid: 0525030e-eb30-41a0-8191-4a5727736857
keywords:
- Windows Media Player plug-ins,digital signal processing (DSP)
- plug-ins,digital signal processing (DSP)
- digital signal processing plug-ins,updating
- DSP plug-ins,updating
- versions of Windows Media Player,DSP plug-ins
ms.topic: article
ms.date: 05/31/2018
---

# Updating Existing DSP Plug-ins

DSP plug-ins created before the release of the Windows Media Player 11 SDK might not work as expected with Windows Media Player 11 running on Windows Vista. To ensure that customers who run Windows Media Player 11 on Windows Vista can use your plug-ins, you must make some changes to your DSP plug-in code, recompile your project, and distribute the updated plug-in to your customers.

Projects created using the latest version of the Windows Media Player plug-in wizard will contain the required updates. See [Updates to the DSP Plug-in Wizard for Windows Media Player 11](updates-to-the-dsp-plug-in-wizard-for-windows-media-player-11.md). (It is a good idea to run the wizard to create a new sample project and then use a tool like Windiff.exe, which comes with Visual Studio, to inspect the differences between the sample code and your production code.)

There are three main changes you will need to make to any existing DSP plug-ins:

-   Change the way the plug-in registers. Your existing plug-in probably registers the threading model as "Apartment". Windows Media Player 11 running on Windows Vista requires that DSP plug-ins register the threading model as "Both". You can fix this by changing the threading model value in your *projectname*.rgs file, as follows:

    ```C++
    val ThreadingModel = s 'Both'
    
    ```

    

    > [!Note]  
    > Specifying the threading model as "Both" removes any serialization that COM provides for calls to custom interfaces. If you make calls to your custom interfaces from multiple threads, you must provide this serialization yourself.

     

    Windows Media Player 11 ensures that calls to DMO interfaces are properly serialized.

    1.  Add calls to [IWMPMediaPluginRegistrar::WMPRegisterPlayerPlugin](/previous-versions/windows/desktop/api/wmpservices/nf-wmpservices-iwmpmediapluginregistrar-wmpregisterplayerplugin) and [IWMPMediaPluginRegistrar::WMPUnRegisterPlayerPlugin](/previous-versions/windows/desktop/api/wmpservices/nf-wmpservices-iwmpmediapluginregistrar-wmpunregisterplayerplugin) with a new plug-in type: WMP\_PLUGINTYPE\_DSP\_OUTOFPROC in DllRegisterServer and DllUnregisterServer in your *projectnamedll*.cpp file. See the reference pages for these methods for details.
    2.  Create and distribute a proxy/stub DLL to enable COM marshaling of any custom interface implemented on or created by the plug-in class. A custom interface is any proprietary interface that you define and implement for use by the plug-in object. This includes the custom interface used by your property page, if you provided one, but might also include interfaces that connect to UI plug-ins, for example. An example of a custom interface created by the plug-in wizard is *Iprojectname*. Examples of interfaces that are not custom interfaces include **IMediaObject** and **IWMPPluginEnable**.

If your DSP plug-in processes audio, you must also add support for the following new audio formats:

-   WAVE\_FORMAT\_IEEE\_FLOAT
-   WAVE\_FORMAT\_EXTENSIBLE with subformat KSDATAFORMAT\_SUBTYPE\_IEEE\_FLOAT.

If your DSP plug-in processes video, you must add support for the NV12 video format.

See the sample audio or video DSP plug-in that the wizard creates for an example of how to process these format types.

## About the Proxy/Stub Project

Perhaps the simplest way to create a proxy/stub DLL project for your DSP plug-in is to run the DSP plug-in wizard. This will create a sample proxy/stub project that you can modify to work with your existing code. You will need to make the following changes:

1.  Remove any existing definitions for your custom interfaces from your code. For example, the DSP plug-in wizard from the Windows Media Player 10 SDK created the *Iprojectname* interface definition in the *projectname*.h file by using the **interface** keyword.
2.  Define your custom interfaces in the proxy/stub project's IDL file.
3.  Build the proxy/stub project before your main project. You can configure Visual Studio to do this automatically if both projects are part of the same solution.
4.  The MIDL compiler will create a new header file having a name in the format *projectname*\_h.h. You must include this header in your main project (in *projectname*.h). It contains the definitions for your custom interfaces.

## Distributing the Updated Plug-in

You can install the updated plug-in on your users' computers exactly as you have in the past. However, you must now also distribute and register the proxy/stub DLL.

## Related topics

<dl> <dt>

[**DSP Plug-in Developer Overview**](dsp-plug-in-developer-overview.md)
</dt> </dl>

 

 




