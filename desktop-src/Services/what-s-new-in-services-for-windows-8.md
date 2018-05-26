---
Description: Windows 8 and Windows Server 2012 include the following new capabilities for services.
ms.assetid: 42BC7325-4FAC-493E-95AC-AEF660F499C0
title: Whats New in Services for Windows 8
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# What's New in Services for Windows 8

Windows 8 and Windows Server 2012 include the following new capabilities for services.

## New Service Functions



| Function                                                                            | Description                                                                    |
|-------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| [**QueryServiceDynamicInformation**](/windows/win32/Winsvc/nf-winsvc-queryservicedynamicinformation?branch=master)<br/> | Retrieves dynamic information related to the current service start.<br/> |



 

## Updated API Elements



| API Element                                                                                     | Description                                                                                                                                                   |
|-------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**HandlerEx**](/windows/win32/WinSvc/nc-winsvc-lphandler_function_ex?branch=master)<br/>                                                       | Added **SERVICE\_CONTROL\_USERMODEREBOOT**.<br/>                                                                                                        |
| [**SERVICE\_STATUS**](/windows/win32/Winsvc/ns-winsvc-_service_status?branch=master)<br/>                                        | Added **SERVICE\_ACCEPT\_USERMODEREBOOT**.<br/>                                                                                                         |
| [**SERVICE\_TRIGGER\_SPECIFIC\_DATA\_ITEM**](/windows/win32/winsvc/ns-winsvc-_service_trigger_specific_data_item?branch=master)<br/> | Added **SERVICE\_TRIGGER\_DATA\_TYPE\_LEVEL**, **SERVICE\_TRIGGER\_DATA\_TYPE\_KEYWORD\_ANY**, and **SERVICE\_TRIGGER\_DATA\_TYPE\_KEYWORD\_ALL**.<br/> |



 

 

 




