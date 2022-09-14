---
title: Code Files for the Source Provider Sample
description: Code Files for the Source Provider Sample
ms.assetid: bd6bfc98-a805-4e04-8a80-7af42ed3dbef
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

# Code Files for the Source Provider Sample

The sample source provider project includes the following source code files, with associated headers:



| File                   | Description                                                                                                                                                                                                     |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| hdsppch.cpp            | Includes standard ATL files.                                                                                                                                                                                    |
| key.c                  | Contains a dummy authentication key.                                                                                                                                                                            |
| loghelp.cpp            | Contains functions that log activity and errors by using the **WMDMLogger** class, which is implemented in the WMDMLOG.dll system file.                                                                         |
| MDServiceProvider.cpp  | Implements a class, CMDServiceProvider, that implements the [**IMDServiceProvider**](/windows/desktop/api/mswmdm/nn-mswmdm-imdserviceprovider) and IComponentAuthenticate interfaces.                                                             |
| mdsp.cpp               | DLL entry point and registration code.                                                                                                                                                                          |
| MDSPDevice.cpp         | Implements a class, CMDSPDevice, that implements the [**IMDSPDevice2**](/windows/desktop/api/mswmdm/nn-mswmdm-imdspdevice2), [**IMDSPDeviceControl**](/windows/desktop/api/mswmdm/nn-mswmdm-imdspdevicecontrol), and **ISpecifyPropertyPages** interfaces.                          |
| MDSPEnumDevice.cpp     | Implements a class, CMDSPEnumDevice, that implements the [**IMDSPEnumDevice**](/windows/desktop/api/mswmdm/nn-mswmdm-imdspenumdevice) interface.                                                                                                  |
| MDSPEnumStorage.cpp    | Implements a class, CMDSPEnumStorage, that implements the [**IMDSPEnumStorage**](/windows/desktop/api/mswmdm/nn-mswmdm-imdspenumstorage) interface.                                                                                               |
| MDSPStorage.cpp        | Implements a class, CMDSPStorage, that implements the [**IMDSPStorage2**](/windows/desktop/api/mswmdm/nn-mswmdm-imdspstorage2), [**IMDSPObjectInfo**](/windows/desktop/api/mswmdm/nn-mswmdm-imdspobjectinfo), and [**IMDSPObject**](/windows/desktop/api/mswmdm/nn-mswmdm-imdspobject) interfaces.                    |
| MDSPStorageGlobals.cpp | Implements a class, CMDSPStorageGlobals, that implements the [**IMDSPStorageGlobals**](/windows/desktop/api/mswmdm/nn-mswmdm-imdspstorageglobals) interface.                                                                                      |
| MDSPutil.cpp           | Contains various utility functions for device and file management.                                                                                                                                              |
| proppage.cpp           | Implements a class, CPropPage, that inherits the ATL classes **IPropertyPageImpl** (to implement IPropertyPage) and **CDialogImpl**, which inherits the ATL class CDialogImpl (to manage windows and messages). |



 

## Related topics

<dl> <dt>

[**Sample Service Provider**](sample-service-provider.md)
</dt> </dl>

 

 




