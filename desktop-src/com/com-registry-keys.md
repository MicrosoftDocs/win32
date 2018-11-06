---
title: COM Registry Keys
description: COM Registry Keys
ms.assetid: 08406092-eb77-4001-a4fa-659ce945e4d1
ms.topic: article
ms.date: 05/31/2018
---

# COM Registry Keys

The registry contains a wealth of information used by COM. The most important information is stored in the following keys.



| Key                                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|---------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [AppID](appid-key.md)<br/>                                   | Groups the configuration options (a set of named values) for one or more distributed COM objects into one location in the registry. Subkeys under this key are used to map an application identifier (AppID) to a remote server name. To simplify the management of common security and configuration settings, distributed COM objects hosted by the same executable are grouped into one AppID.<br/>                                                                                                                                                                                                                                                                                                                      |
| [CLSID](clsid-key-hklm.md)<br/>                              | A class identifier (CLSID) is a globally unique identifier that identifies a COM class object. If the server or container allows linking to embedded objects, register a CLSID for each supported class of objects. The CLSID key contains information used by the default COM handler to return information about a class when it is in the running state.<br/> To obtain a CLSID for your application, use uuidgen.exe, found in the \\TOOLs directory of the COM Toolkit, or use [**CoCreateGuid**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateguid). <br/>                                                                                                                                                                                       |
| [ProgID](-progid--key.md)<br/>                               | A programmatic identifier (ProgID) is a registry entry that can be associated with a CLSID. The ProgID key maps a user-friendly string to a CLSID. Like the CLSID, the ProgID identifies a class, but with less precision. Use a ProgID in programming situations where it is not possible to use a CLSID. ProgIDs should not appear in the user interface. ProgIDs are not guaranteed to be unique, so they can be used only where name collisions do not occur.<br/>                                                                                                                                                                                                                                                      |
| [VersionIndependentProgID](versionindependentprogid.md)<br/> | Associates a ProgID with a CLSID. It is used to determine the latest version of an object application. Like the ProgID, the version-independent ProgID can be registered with a human-readable name. <br/> Applications must register a version-independent programmatic identifier under the VersionIndependentProgID key. The version-independent ProgID refers to the application's class and does not change from version to version, instead remaining constant across all versions. It is used with macro languages and refers to the currently installed version of the application's class. The version-independent ProgID must correspond to the name of the latest version of the object application. <br/> |
| [file\_extension](-file-extension--key.md)<br/>              | Associates a file name extension with a ProgID.<br/> Information contained in the file name extension key is used by both the system and [file monikers](file-monikers.md). [**GetClassFile**](/windows/desktop/api/Objbase/nf-objbase-getclassfile) uses the file name extension key to supply the associated CLSID. <br/>                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [Interface](interface-key.md)<br/>                           | Registers new interfaces by associating an interface name with an interface identifier (IID). It maps IIDs to information specific to an interface. The information is required mainly for using interfaces across process boundaries. <br/> When adding a new interface, the Interface key must be completed for COM to register the new interface. There must be one IID subkey for each new interface. <br/>                                                                                                                                                                                                                                                                                                       |
| [Ole](hkey-local-machine-software-microsoft-ole.md)<br/>     | Controls default launch and access permissions for distributed COM objects as well as call-level security capabilities for applications that do not call [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity). Only administrators have full access to this portion of the registry. All other users have read-only access. <br/>                                                                                                                                                                                                                                                                                                                                                                                           |



 

## Related topics

<dl> <dt>

[Registering COM Applications](registering-com-applications.md)
</dt> </dl>

 

 





