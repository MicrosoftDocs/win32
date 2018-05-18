---
Description: 'Register the Plug-in'
ms.assetid: '18f36e53-11f0-469c-9790-9319a28ae2f2'
title: 'Register the Plug-in'
---

# Register the Plug-in

The plug-in must be registered by creating the following registry keys. ({CLSID} represents the unique GUID for your plug-in)



|                                                                                        |                                                                                                                                                                                                                 |
|----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Key                                                                                    | Values                                                                                                                                                                                                          |
| **HKEY\_CLASSES\_ROOT\\CLSID\\{CLSID}**                                                | The (Default) value should be set to a name you choose to identify the plug-in in the registry.                                                                                                                 |
| **HKEY\_CLASSES\_ROOT\\CLSID\\{CLSID}\\InProcServer32**                                | The (Default) value should be set to the fully qualified path for the file that contains the specified module that the current process owns.The "ThreadingModel" value should be set to "Apartment".<br/> |
| **HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\PhotoAcquire\\Plugins\\{CLSID}** | The "DisplayName" value should be set to the display name of the plug-in.                                                                                                                                       |
| **HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\PhotoAcquire\\Plugins\\{CLSID}** | To enable the plug-in for the current user, the "Enabled" value must be set to 1.                                                                                                                               |



 

 

 




