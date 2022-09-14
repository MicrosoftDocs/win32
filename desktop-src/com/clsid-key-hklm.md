---
title: CLSID Key
description: A CLSID is a globally unique identifier that identifies a COM class object. If your server or container allows linking to its embedded objects, you need to register a CLSID for each supported class of objects.
ms.assetid: b5777d87-abf2-45b9-9d95-61db878a5810
keywords:
- CLSID registry key COM
ms.topic: article
ms.date: 05/31/2018
---

# CLSID Key

A CLSID is a globally unique identifier that identifies a COM class object. If your server or container allows linking to its embedded objects, you need to register a CLSID for each supported class of objects.

## Registry Key

**HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Classes\\CLSID**\\*{*CLSID*}*



| Registry key                                                 | Description                                                                                                                              |
|--------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| [**AppID**](appid.md)                                       | Associates an AppID with a CLSID.                                                                                                        |
| [**AutoConvertTo**](autoconvertto.md)                       | Specifies the automatic conversion of a given class of objects to a new class of objects.                                                |
| [**AutoTreatAs**](autotreatas.md)                           | Automatically sets the CLSID for the [**TreatAs**](treatas.md) key to the specified value.                                              |
| [**AuxUserType**](auxusertype.md)                           | Specifies an application's short display name and application names.                                                                     |
| [**Control**](control.md)                                   | Identifies an object as an ActiveX Control.                                                                                              |
| [**Conversion**](conversion.md)                             | Used by the **Convert** dialog box to determine the formats an application can read and write.                                           |
| [**DataFormats**](dataformats.md)                           | Specifies the default and main data formats supported by an application.                                                                 |
| [**DefaultIcon**](defaulticon.md)                           | Provides default icon information for iconic presentations of objects.                                                                   |
| [**InprocHandler**](inprochandler.md)                       | Specifies whether an application uses a custom handler.                                                                                  |
| [**InprocHandler32**](inprochandler32.md)                   | Specifies whether an application uses a custom handler.                                                                                  |
| [**InprocServer**](inprocserver.md)                         | Specifies the path to the in-process server DLL.                                                                                         |
| [**InprocServer32**](inprocserver32.md)                     | Registers a 32-bit in-process server and specifies the threading model of the apartment the server can run in.                           |
| [**Insertable**](insertable.md)                             | Indicates that objects of this class should appear in the **Insert Object** dialog box list box when used by COM container applications. |
| [**Interface**](interface.md)                               | An optional entry that specifies all interface IDs (IIDs) supported by the associated class.                                             |
| [**LocalServer**](localserver.md)                           | Specifies the full path to a 16-bit local server application.                                                                            |
| [**LocalServer32**](localserver32.md)                       | Specifies the full path to a 32-bit local server application.                                                                            |
| [**MiscStatus**](miscstatus.md)                             | Specifies how to create and display an object.                                                                                           |
| [**ProgID**](progid.md)                                     | Associates a ProgID with a CLSID.                                                                                                        |
| [**ToolBoxBitmap32**](toolboxbitmap32.md)                   | Identifies the module name and resource ID for a 16 x 16 bitmap to use for the face of a toolbar or toolbox button.                      |
| [**TreatAs**](treatas.md)                                   | Specifies the CLSID of a class that can emulate the current class.                                                                       |
| [**Verb**](verb.md)                                         | Specifies the verbs to be registered for an application.                                                                                 |
| [**Version**](version.md)                                   | Specifies the version number of the control.                                                                                             |
| [**VersionIndependentProgID**](versionindependentprogid.md) | Associates a ProgID with a CLSID. This value is used to determine the latest version of an object application.                           |



 

## Remarks

The **HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Classes** key corresponds to the **HKEY\_CLASSES\_ROOT** key, which was retained for compatibility with earlier versions of COM.

The CLSID key contains information used by the default COM handler to return information about a class when it is in the running state.

To obtain a CLSID for your application, you can use the Uuidgen.exe, or use the [**CoCreateGuid**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateguid) function.

The CLSID is a 128-bit number, in hex, within a pair of curly braces.

## Related topics

<dl> <dt>

[**CoCreateGuid**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateguid)
</dt> </dl>

 

 




