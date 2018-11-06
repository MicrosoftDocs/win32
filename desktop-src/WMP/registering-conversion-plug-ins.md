---
title: Registering Conversion Plug-ins
description: Registering Conversion Plug-ins
ms.assetid: d7d6e733-7288-4707-a54a-dcaa71601646
keywords:
- Windows Media Player,conversion plug-ins
- Windows Media Player plug-ins,conversion
- plug-ins,conversion
- conversion plug-ins,registering
- registry,conversion plug-ins
ms.topic: article
ms.date: 05/31/2018
---

# Registering Conversion Plug-ins

Third-party formats must be registered before Windows Media Player can instantiate and use the conversion plug-in. To register your file for conversion, you must register the file name extension associated with your format.

The list of registered file name extensions is maintained as a set of registry keys. For details about registering third-party formats, see [File Name Extension Registry Settings](file-name-extension-registry-settings.md). The following table lists the registry value settings to register a third-party format for conversion by using a conversion plug-in.



| Value                  | Setting                                                     |
|------------------------|-------------------------------------------------------------|
| **Runtime**            | 13                                                          |
| **Permissions**        | 8 (Permission for the library).                             |
| **ConvertPluginCLSID** | The class ID of the conversion plug-in, in registry format. |



 

## Related topics

<dl> <dt>

[**Conversion Plug-ins Programming Reference**](conversion-plug-ins-programming-reference.md)
</dt> </dl>

 

 




