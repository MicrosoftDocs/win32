---
title: Code Files for the Source Provider Sample
description: Code Files for the Source Provider Sample
ms.assetid: 'bd6bfc98-a805-4e04-8a80-7af42ed3dbef'
keywords: ["Windows Media Device Manager,samples", "Device Manager,samples", "Windows Media Device Manager,service provider sample", "Device Manager,service provider sample", "service providers,samples", "samples,service providers"]
---

# Code Files for the Source Provider Sample

The sample source provider project includes the following source code files, with associated headers:



| File                   | Description                                                                                                                                                                                                     |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| hdsppch.cpp            | Includes standard ATL files.                                                                                                                                                                                    |
| key.c                  | Contains a dummy authentication key.                                                                                                                                                                            |
| loghelp.cpp            | Contains functions that log activity and errors by using the **WMDMLogger** class, which is implemented in the WMDMLOG.dll system file.                                                                         |
| MDServiceProvider.cpp  | Implements a class, CMDServiceProvider, that implements the [**IMDServiceProvider**](imdserviceprovider.md) and IComponentAuthenticate interfaces.                                                             |
| mdsp.cpp               | DLL entry point and registration code.                                                                                                                                                                          |
| MDSPDevice.cpp         | Implements a class, CMDSPDevice, that implements the [**IMDSPDevice2**](imdspdevice2.md), [**IMDSPDeviceControl**](imdspdevicecontrol.md), and **ISpecifyPropertyPages** interfaces.                          |
| MDSPEnumDevice.cpp     | Implements a class, CMDSPEnumDevice, that implements the [**IMDSPEnumDevice**](imdspenumdevice.md) interface.                                                                                                  |
| MDSPEnumStorage.cpp    | Implements a class, CMDSPEnumStorage, that implements the [**IMDSPEnumStorage**](imdspenumstorage.md) interface.                                                                                               |
| MDSPStorage.cpp        | Implements a class, CMDSPStorage, that implements the [**IMDSPStorage2**](imdspstorage2.md), [**IMDSPObjectInfo**](imdspobjectinfo.md), and [**IMDSPObject**](imdspobject.md) interfaces.                    |
| MDSPStorageGlobals.cpp | Implements a class, CMDSPStorageGlobals, that implements the [**IMDSPStorageGlobals**](imdspstorageglobals.md) interface.                                                                                      |
| MDSPutil.cpp           | Contains various utility functions for device and file management.                                                                                                                                              |
| proppage.cpp           | Implements a class, CPropPage, that inherits the ATL classes **IPropertyPageImpl** (to implement IPropertyPage) and **CDialogImpl**, which inherits the ATL class CDialogImpl (to manage windows and messages). |



 

## Related topics

<dl> <dt>

[**Sample Service Provider**](sample-service-provider.md)
</dt> </dl>

 

 




