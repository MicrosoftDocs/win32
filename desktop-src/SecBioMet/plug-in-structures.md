---
title: Plug-in Structures
description: Structures for client application development by the Windows Biometric Framework API.
ms.assetid: 64fb908c-72c2-4639-a2f6-77ede080512c
keywords:
- Windows Biometric Framework API Windows Biometric Framework API , plug-in structures
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Plug-in Structures

The following structures are supported for client application development by the Windows Biometric Framework API.

## In this section



| Topic                                                                                                | Description                                                                                                                           |
|------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| [**WINBIO\_ACCOUNT\_POLICY**](winbio-account-policy.md)<br/>                                  | Contains either a default or account-specific antispoofing policy.<br/>                                                         |
| [**WINBIO\_ADAPTER\_INTERFACE\_VERSION**](/windows/win32/Winbio_adapter/ns-winbio_adapter-_winbio_adapter_interface_version?branch=master)<br/>           | Contains a major and minor version number used in the engine, sensor, and storage adapter interface tables.<br/>                |
| [**WINBIO\_ENGINE\_INTERFACE**](/windows/win32/Winbio_adapter/ns-winbio_adapter-_winbio_engine_interface?branch=master)<br/>                              | Contains pointers to your custom engine adapter functions.<br/>                                                                 |
| [**WINBIO\_EXTENDED\_ENROLLMENT\_PARAMETERS**](winbio-extended-enrollment-parameters.md)<br/> | Contains additional information that an engine adapter needs to create an enrollment template. <br/>                            |
| [**WINBIO\_PIPELINE**](/windows/win32/Winbio_adapter/ns-winbio_adapter-_winbio_pipeline?branch=master)<br/>                                               | Contains shared context information used by the sensor, engine, and storage adapter components in a single biometric unit.<br/> |
| [**WINBIO\_SENSOR\_INTERFACE**](/windows/win32/Winbio_adapter/ns-winbio_adapter-_winbio_sensor_interface?branch=master)<br/>                              | Contains pointers to your custom sensor adapter functions.<br/>                                                                 |
| [**WINBIO\_STORAGE\_INTERFACE**](/windows/win32/Winbio_adapter/ns-winbio_adapter-_winbio_storage_interface?branch=master)<br/>                            | Contains pointers to your custom storage adapter functions.<br/>                                                                |
| [**WINBIO\_STORAGE\_RECORD**](/windows/win32/Winbio_adapter/ns-winbio_adapter-_winbio_storage_record?branch=master)<br/>                                  | Contains a biometric template and associated data in a standard format.<br/>                                                    |



 

## Related topics

<dl> <dt>

[Plug-in Reference](plug-in-reference.md)
</dt> <dt>

[Plug-in Functions](plug-in-functions.md)
</dt> <dt>

[**WbioQueryEngineInterface**](/windows/win32/Winbio_adapter/nf-winbio_adapter-wbioqueryengineinterface?branch=master)
</dt> <dt>

[**WbioQuerySensorInterface**](/windows/win32/Winbio_adapter/nf-winbio_adapter-wbioquerysensorinterface?branch=master)
</dt> <dt>

[**WbioQueryStorageInterface**](/windows/win32/Winbio_adapter/nf-winbio_adapter-wbioquerystorageinterface?branch=master)
</dt> </dl>

 

 





