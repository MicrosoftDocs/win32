---
Description: The FaxDeviceProvider configuration object is used by a fax client application to retrieve information about a fax service provider (FSP) registered with the fax service.
ms.assetid: ef32eb3d-e158-4740-82f5-661d5eded88c
title: FaxDeviceProvider object
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# FaxDeviceProvider object

The **FaxDeviceProvider** configuration object is used by a fax client application to retrieve information about a fax service provider (FSP) registered with the fax service.

## Members

The **FaxDeviceProvider** object has these types of members:

-   [Properties](#properties)

### Properties

The **FaxDeviceProvider** object has these properties.



| Property                                                                           | Access type          | Description                                                                                                                                                                                                                                                                       |
|:-----------------------------------------------------------------------------------|:---------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Debug**](-mfax-faxdeviceprovider-debug-vb.md)<br/>                       | Read-only<br/> | The [**Debug**](-mfax-faxdeviceprovider-debug-vb.md) property is a Boolean value that indicates whether the FSP DLL was created in a debug environment.<br/>                                                                                                               |
| [**DeviceIds**](-mfax-faxdeviceprovider-deviceids-vb.md)<br/>               | Read-only<br/> | The [**DeviceIds**](-mfax-faxdeviceprovider-deviceids-vb.md) property returns a variant safe array of long (VT\_I4 \| VT\_ARRAY). Each long value in the array is a device ID.<br/>                                                                                        |
| [**FriendlyName**](-mfax-faxdeviceprovider-friendlyname-vb.md)<br/>         | Read-only<br/> | The [**FriendlyName**](-mfax-faxdeviceprovider-friendlyname-vb.md) property is a null-terminated string that contains the user-friendly name for the FSP. This string is suitable for display to users.<br/>                                                               |
| [**ImageName**](-mfax-faxdeviceprovider-imagename-vb.md)<br/>               | Read-only<br/> | The [**ImageName**](-mfax-faxdeviceprovider-imagename-vb.md) property is a null-terminated string that contains the executable image name (DLL path and file name) of the FSP.<br/>                                                                                        |
| [**InitErrorCode**](-mfax-faxdeviceprovider-initerrorcode-vb.md)<br/>       | Read-only<br/> | The [**InitErrorCode**](-mfax-faxdeviceprovider-initerrorcode-vb.md) property is a value that specifies the last error code that the FSP returned while the fax service was loading and initializing the FSP DLL. This may be an HRESULT value or a Win32 error code.<br/> |
| [**MajorBuild**](-mfax-faxdeviceprovider-majorbuild-vb.md)<br/>             | Read-only<br/> | The [**MajorBuild**](-mfax-faxdeviceprovider-majorbuild-vb.md) property is a value that specifies the major part of the build number for the FSP DLL.<br/>                                                                                                                 |
| [**MajorVersion**](-mfax-faxdeviceprovider-majorversion-vb.md)<br/>         | Read-only<br/> | The [**MajorVersion**](-mfax-faxdeviceprovider-majorversion-vb.md) property is a value that specifies the major part of the version number for the FSP DLL.<br/>                                                                                                           |
| [**MinorBuild**](-mfax-faxdeviceprovider-minorbuild-vb.md)<br/>             | Read-only<br/> | The [**MinorBuild**](-mfax-faxdeviceprovider-minorbuild-vb.md) property is a value that specifies the minor part of the build number for the FSP DLL.<br/>                                                                                                                 |
| [**MinorVersion**](-mfax-faxdeviceprovider-minorversion-vb.md)<br/>         | Read-only<br/> | The [**MinorVersion**](-mfax-faxdeviceprovider-minorversion-vb.md) property is a value that specifies the minor part of the version number for the FSP DLL.<br/>                                                                                                           |
| [**Status**](-mfax-faxdeviceprovider-status-vb.md)<br/>                     | Read-only<br/> | The [**Status**](/previous-versions/windows/desktop/api/FaxComex/nf-faxcomex-ifaxdeviceprovider-get_status) property is a number that indicates whether the FSP loaded and initialized successfully.<br/>                                                                                                                          |
| [**TapiProviderName**](-mfax-faxdeviceprovider-tapiprovidername-vb.md)<br/> | Read-only<br/> | The [**TapiProviderName**](-mfax-faxdeviceprovider-tapiprovidername-vb.md) property is a null-terminated string that contains the name of the TSP associated with the FSP fax devices.<br/>                                                                                |
| [**UniqueName**](-mfax-faxdeviceprovider-uniquename-vb.md)<br/>             | Read-only<br/> | The [**UniqueName**](-mfax-faxdeviceprovider-uniquename-vb.md) property is a null-terminated string that contains the unique name that identifies the FSP.<br/>                                                                                                            |



 

## Remarks

A **FaxDeviceProvider** object is accessed through a [**FaxDeviceProviders**](-mfax-faxdeviceproviders.md) object.

![faxserver, faxdeviceproviders, and faxdeviceprovider objects](images/faxdeviceprovider.png)

To create a **FaxDeviceProvider** object in Microsoft Visual Basic, call the [**Item**](-mfax-faxdeviceproviders-item.md) property of the [**FaxDeviceProviders**](-mfax-faxdeviceproviders.md) object.

To create a **FaxDeviceProvider** object in C++, call the [**get\_Item**](/previous-versions/windows/desktop/api/FaxComex/nf-faxcomex-ifaxdeviceproviders-get_item) method.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Faxcomex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |
| IID<br/>                      | CLSID\_FaxDeviceProvider<br/>                                                     |



## See also

<dl> <dt>

[Fax Service object hierarchy](-mfax-fax-service-extended-com-object-model.md)
</dt> <dt>

[**IFaxDeviceProvider**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxdeviceprovider)
</dt> </dl>

 

 




