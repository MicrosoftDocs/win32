---
description: Windows 8 and Windows Server 2012 include the following new capabilities for services.
ms.assetid: 42BC7325-4FAC-493E-95AC-AEF660F499C0
title: Whats New in Services for Windows 8
ms.topic: article
ms.date: 05/31/2018
---

# What's New in Services for Windows 8

Windows 8 and Windows Server 2012 include the following new capabilities for services.

## New Service Functions



| Function                                                                            | Description                                                                    |
|-------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| [**QueryServiceDynamicInformation**](/windows/desktop/api/Winsvc/nf-winsvc-queryservicedynamicinformation)<br/> | Retrieves dynamic information related to the current service start.<br/> |



 

## Updated API Elements



| API Element                                                                                     | Description                                                                                                                                                   |
|-------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**HandlerEx**](/windows/desktop/api/WinSvc/nc-winsvc-lphandler_function_ex)<br/>                                                       | Added **SERVICE\_CONTROL\_USERMODEREBOOT**.<br/>                                                                                                        |
| [**SERVICE\_STATUS**](/windows/desktop/api/Winsvc/ns-winsvc-service_status)<br/>                                        | Added **SERVICE\_ACCEPT\_USERMODEREBOOT**.<br/>                                                                                                         |
| [**SERVICE\_TRIGGER\_SPECIFIC\_DATA\_ITEM**](/windows/desktop/api/winsvc/ns-winsvc-service_trigger_specific_data_item)<br/> | Added **SERVICE\_TRIGGER\_DATA\_TYPE\_LEVEL**, **SERVICE\_TRIGGER\_DATA\_TYPE\_KEYWORD\_ANY**, and **SERVICE\_TRIGGER\_DATA\_TYPE\_KEYWORD\_ALL**.<br/> |



 

 

 




