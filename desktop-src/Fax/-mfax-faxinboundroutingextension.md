---
Description: 'The FaxInboundRoutingExtension configuration object is used by a fax client application to retrieve information about a fax routing extension registered with the fax service.'
ms.assetid: 'cb875610-d6c9-473d-b9c2-0035e67a8949'
title: FaxInboundRoutingExtension object
---

# FaxInboundRoutingExtension object

The **FaxInboundRoutingExtension** configuration object is used by a fax client application to retrieve information about a fax routing extension registered with the fax service.

## Members

The **FaxInboundRoutingExtension** object has these types of members:

-   [Properties](#properties)

### Properties

The **FaxInboundRoutingExtension** object has these properties.



| Property                                                                              | Access type          | Description                                                                                                                                                                                                                                                                  |
|:--------------------------------------------------------------------------------------|:---------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Debug**](-mfax-faxinboundroutingextension-debug-vb.md)<br/>                 | Read-only<br/> | The [**Debug**](-mfax-faxinboundroutingextension-debug-vb.md) property is a Boolean value that indicates whether the fax routing extension DLL was created in a debug environment.<br/>                                                                               |
| [**FriendlyName**](-mfax-faxinboundroutingextension-friendlyname-vb.md)<br/>   | Read-only<br/> | The [**FriendlyName**](-mfax-faxinboundroutingextension-friendlyname-vb.md) property is a null-terminated string that contains the user-friendly name for the fax routing extension. The string is suitable for display to users.<br/>                                |
| [**ImageName**](-mfax-faxinboundroutingextension-imagename-vb.md)<br/>         | Read-only<br/> | The [**ImageName**](-mfax-faxinboundroutingextension-imagename-vb.md) property is a null-terminated string that contains the executable image name (DLL path and file name) of the fax routing extension.<br/>                                                        |
| [**InitErrorCode**](-mfax-faxinboundroutingextension-initerrorcode-vb.md)<br/> | Read-only<br/> | The [**InitErrorCode**](-mfax-faxinboundroutingextension-initerrorcode-vb.md) property is a value that specifies the last error code that the fax routing extension returned while the fax service was loading and initializing the fax routing extension's DLL.<br/> |
| [**MajorBuild**](-mfax-faxinboundroutingextension-majorbuild-vb.md)<br/>       | Read-only<br/> | The [**MajorBuild**](-mfax-faxinboundroutingextension-majorbuild-vb.md) property is a value that specifies the major part of the build number for the fax routing extension's DLL.<br/>                                                                               |
| [**MajorVersion**](-mfax-faxinboundroutingextension-majorversion-vb.md)<br/>   | Read-only<br/> | The [**MajorVersion**](-mfax-faxinboundroutingextension-majorversion-vb.md) property is a value that specifies the major part of the version number for the fax routing extension's DLL.<br/>                                                                         |
| [**Methods**](-mfax-faxinboundroutingextension-methods-vb.md)<br/>             | Read-only<br/> | The [**Methods**](-mfax-faxinboundroutingextension-methods-vb.md) property is an array of GUIDs that uniquely identify the inbound routing methods exposed by the fax routing extension.<br/>                                                                         |
| [**MinorBuild**](-mfax-faxinboundroutingextension-minorbuild-vb.md)<br/>       | Read-only<br/> | The [**MinorBuild**](-mfax-faxinboundroutingextension-minorbuild-vb.md) property is a value that specifies the minor part of the build number for the fax routing extension's DLL.<br/>                                                                               |
| [**MinorVersion**](-mfax-faxinboundroutingextension-minorversion-vb.md)<br/>   | Read-only<br/> | The [**MinorVersion**](-mfax-faxinboundroutingextension-minorversion-vb.md) property is a value that specifies the minor part of the version number for the fax routing extension's DLL.<br/>                                                                         |
| [**Status**](-mfax-faxinboundroutingextension-status-vb.md)<br/>               | Read-only<br/> | The [**Status**](-mfax-faxinboundroutingextension-status-vb.md) property is a value that indicates whether the fax routing extension loaded and initialized successfully. <br/>                                                                                       |
| [**UniqueName**](-mfax-faxinboundroutingextension-uniquename-vb.md)<br/>       | Read-only<br/> | The [**UniqueName**](-mfax-faxinboundroutingextension-uniquename-vb.md) property is a null-terminated string that contains a unique name for the fax routing extension. The fax service uses this name internally to identify fax routing extensions.<br/>            |



 

## Remarks

A **FaxInboundRoutingExtension** object is accessed through a [**FaxInboundRoutingExtensions**](-mfax-faxinboundroutingextensions.md) object.

![faxinboundrouting, faxroutingextensions, and faxroutingextension objects](images/faxinboundroutingextension.png)

To create a **FaxInboundRoutingExtension** object in Microsoft Visual Basic, call the [**Item**](-mfax-faxinboundroutingextensions-item.md) property of the [**FaxInboundRoutingExtensions**](-mfax-faxinboundroutingextensions.md) object.

To create a **FaxInboundRoutingExtension** object in C++, call the [**Item**](-mfax-faxinboundroutingextensions-item-cpp.md) method.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Faxcomex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |
| IID<br/>                      | CLSID\_FaxInboundRoutingExtension<br/>                                            |



## See also

<dl> <dt>

[Fax Service object hierarchy](-mfax-fax-service-extended-com-object-model.md)
</dt> <dt>

[**IFaxInboundRoutingExtension**](-mfax-faxinboundroutingextension-cpp.md)
</dt> </dl>

 

 




