---
title: Registering DSP Plug-ins
description: Registering DSP Plug-ins
ms.assetid: af264ff7-702b-4a49-a14d-ab8563a40c4e
keywords:
- Windows Media Player plug-ins,registry entries
- plug-ins,registry entries
- digital signal processing plug-ins,registry entries
- DSP plug-ins,registry entries
- registry,DSP plug-ins
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Registering DSP Plug-ins

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

To make your DSP plug-in available in Windows Media Player you must create the following registry subkeys and entries on the user's computer.


```C++
[HKEY_CLASSES_ROOT\CLSID\PluginClsid]
@=PluginClassFriendlyName

[HKEY_CLASSES_ROOT\CLSID\PluginClsid\InprocServer32]
@=PluginModuleName
"ThreadingModel"="Threading"
```



In the preceding registry syntax, the symbols in italic are placeholders for names and globally unique identifiers (GUIDs) that are specific to the DSP plug-in. The following table describes those placeholders.



| Placeholder               | Description                                                                                                                                                                                                                                                                                                                                                                                                                  |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *PluginClsid*             | A GUID that is the class identifier for the DSP plug-in's primary class. This is the class that implements **IMediaObject**, **IPluginEnable**, and possibly **ISpecifyPropertyPages**. In a dual-mode plug-in, this class also implements **IMFTransform** and **IMFGetService**.This GUID must be in registry format, complete with the curly braces.<br/> Format: {xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}<br/> |
| *PluginClassFriendlyName* | A friendly name for the DSP plug-in's primary class.Example: "ProsewareDSP Class"<br/>                                                                                                                                                                                                                                                                                                                                 |
| *PluginModuleName*        | The fully qualified path to the DLL that implements the DSP plug-in.Example: "C:\\Program Files\\Proseware\\ProsewareDsp.dll"<br/>                                                                                                                                                                                                                                                                                     |
| *Threading*               | A string that specifies the threading model for the plug-in. If the plug-in is going to run with Windows Media Player 11 on Windows Vista, this registry entry must be equal to "Both". If the plug-in is going to run on Windows XP or older operating systems, this registry entry can be equal to either "Apartment" or "Both".                                                                                           |



 

If your DSP plug-in implements a custom interface and if your plug-in is going to run in Windows Media Player 11 on Windows Vista, you must create the following registry subkeys and entries on the user's computer.


```C++
[HKEY_CLASSES_ROOT\CLSID\ProxyStubClsid]
@=PSFactoryBuffer

[HKEY_CLASSES_ROOT\CLSID\ProxyStubClsid\InprocServer32]
@=ProxyStubModuleName
"ThreadingModel"="Apartment"

[HKEY_CLASSES_ROOT\Interfaces\CustomInterfaceId]
@=CustomInterfaceName

[HKEY_CLASSES_ROOT\Interfaces\CustomInterfaceId\NumMethods]
@=NumberOfMethods

[HKEY_CLASSES_ROOT\Interfaces\CustomInterfaceId\ProxyStubClsid32]
@=ProxyStubClsid
```



In the preceding registry syntax, the symbols in italic are placeholders for names, numeric values, and globally unique identifiers (GUIDs) that are specific to the DSP plug-in. The following table describes those placeholders.



| Placeholder           | Description                                                                                                                                                                                                                                                                |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *ProxyStubClsid*      | A GUID that is the class identifier for the class that implements the proxies and stubs for the DSP plug-in's custom interfaces.This GUID must be in registry format, complete with the curly braces.<br/> Format: {xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}<br/> |
| *ProxyStubModuleName* | The fully qualified path to the DLL that implements the proxy and stub interfaces for the DSP plug-in.Example: "C:\\Program Files\\Proseware\\ProsewareDspPS.dll"<br/>                                                                                               |
| *CustomInterfaceId*   | A GUID that is the interface identifier for a custom interface that is implemented by the DSP plug-in.This GUID must be in registry format, complete with the curly braces.<br/> Format: {xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}<br/>                           |
| *CustomInterfaceName* | The name of a custom interface that is implemented by the DSP plug-in.Example: "IProsewareDsp"<br/>                                                                                                                                                                  |
| *NumberOfMethods*     | The number of methods, including inherited methods, defined by a custom interface.Example: "5"<br/>                                                                                                                                                                  |



 

If your DSP plug-in provides a property page, you must create the following registry subkeys and entries on the user's computer.


```C++
[HKEY_CLASSES_ROOT\CLSID\PropPageClsid]
@=PropPageClassFriendlyName

[HKEY_CLASSES_ROOT\CLSID\PropPageClsid\InprocServer32]
@=PluginModuleName
"ThreadingModel"="Apartment"
```



In the preceding registry syntax, the symbols in italic are placeholders for names and globally unique identifiers (GUIDs) that are specific to the DSP plug-in. The following table describes those placeholders.



| Placeholder                 | Description                                                                                                                                                                                                                            |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *PropPageClsid*             | A GUID that is the class identifier for the property page class provided by the DSP plug-in.This GUID must be in registry format, complete with the curly braces.<br/> Format: {xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}<br/> |
| *PropPageClassFriendlyName* | A friendly name for the property page class.Example: "ProsewareDSP Property Page Class"<br/>                                                                                                                                     |
| *PluginModuleName*          | The fully qualified path to the DLL that implements the DSP plug-in.Example: "C:\\Program Files\\Proseware\\ProsewareDsp.dll"<br/>                                                                                               |



 

**Calling IWMPPluginRegistrar**

In addition to the registry subkeys and entries described in the preceding lists and tables, you must create some registry keys and entries by calling [IWMPMediaPluginRegistrar::WMPRegisterPlayerPlugin](/previous-versions/windows/desktop/api/wmpservices/nf-wmpservices-iwmpmediapluginregistrar-wmpregisterplayerplugin). This method performs the necessary registration to enable Windows Media Player to recognize your plug-in and present it as an option to the user.

Call **IWMPMediaPluginRegistrar::WMPRegisterPlayerPlugin** in your plug-in's **DllRegisterServer** function, and call [IWMPMediaPluginRegistrar::WMPUnRegisterPlayerPlugin](/previous-versions/windows/desktop/api/wmpservices/nf-wmpservices-iwmpmediapluginregistrar-wmpunregisterplayerplugin) in your plug-in's **DllUnregisterServer** function. To get a pointer to an **IWMPMediaPluginRegistrar** interface, call **CoCreateInstance**, passing CLSID\_WMPMediaPluginRegistrar as the Class ID. The constant CLSID\_WMPMediaPluginRegistrar is defined in wmpservices.h.

**Registration in the DSP Plug-in Wizard**

The DSP plug-in wizard, which is included in the Windows SDK, generates sample code that is based on Active Template Library (ATL). The sample plug-in's **DllRegisterServer** function calls ATL's **RegisterServer** function, which creates registry subkeys and entries according to two registry script files in the Visual Studio project. The file *ProjectName*.rgs contains the script for registering the plug-in's main class, and the file *ProjectName* PropPage.rgs contains the script for registering the plug-in's property page class. The sample plug-in's **DllRegisterServer** function also calls **IWMPPluginRegistrar::WMPRegisterPlayerPlugin**.

The DSP plug-in wizard also generates code for a proxy-stub component that is a self-registering .dll file. The registration code for that file is in dlldata.cpp. The macro **DLLDATA\_ROUTINES** expands to include an implementation of **DllRegisterServer**.

## Related topics

<dl> <dt>

[**DSP Plug-in Developer Overview**](dsp-plug-in-developer-overview.md)
</dt> <dt>

[**IWMPMediaPluginRegistrar**](/previous-versions/windows/desktop/api/wmpservices/nn-wmpservices-iwmpmediapluginregistrar)
</dt> </dl>

 

 





