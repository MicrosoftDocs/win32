---
description: The IUpdateHistoryEntry interface defines the following properties.
ms.assetid: ea4e698c-4a4c-4266-96e0-870dc5709a72
title: IUpdateHistoryEntry Properties
ms.topic: article
ms.date: 05/31/2018
---

# IUpdateHistoryEntry Properties

The [**IUpdateHistoryEntry**](/windows/desktop/api/Wuapi/nn-wuapi-iupdatehistoryentry) interface defines the following properties.



| Property                                                               | Description                                                                                                              |
|------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| [**ClientApplicationID**](/windows/desktop/api/Wuapi/nf-wuapi-iupdatehistoryentry-get_clientapplicationid) | Gets the identifier of the client application that processed an update.                                                  |
| [**Date**](/windows/desktop/api/Wuapi/nf-wuapi-iupdatehistoryentry-get_date)                               | Gets the date and the time an update was applied.                                                                        |
| [**Description**](/windows/desktop/api/Wuapi/nf-wuapi-iupdatehistoryentry-get_description)                 | Gets the description of an update.                                                                                       |
| [**HResult**](/windows/desktop/api/Wuapi/nf-wuapi-iupdatehistoryentry-get_hresult)                         | Gets the **HRESULT** value that is returned from the operation on an update.                                             |
| [**Operation**](/windows/desktop/api/Wuapi/nf-wuapi-iupdatehistoryentry-get_operation)                     | Gets an [**UpdateOperation**](/windows/win32/api/wuapi/ne-wuapi-updateoperation) value that specifies the operation on an update.                      |
| [**ResultCode**](/windows/desktop/api/Wuapi/nf-wuapi-iupdatehistoryentry-get_resultcode)                   | Gets an [**OperationResultCode**](/windows/win32/api/wuapi/ne-wuapi-operationresultcode) value that specifies the result of an operation on an update. |
| [**ServerSelection**](/windows/desktop/api/Wuapi/nf-wuapi-iupdatehistoryentry-get_serverselection)         | Gets the [**ServerSelection**](/openspecs/windows_protocols/ms-uamg/07e2bfa4-6795-4189-b007-cc50b476181a) value that indicates which server provided an update.                |
| [**ServiceID**](/windows/desktop/api/Wuapi/nf-wuapi-iupdatehistoryentry-get_serviceid)                     | Gets the service identifier of an update service that is not a Windows update.                                           |
| [**SupportUrl**](/windows/desktop/api/Wuapi/nf-wuapi-iupdatehistoryentry-get_supporturl)                   | Gets a hyperlink to the language-specific support information for an update.                                             |
| [**Title**](/windows/desktop/api/Wuapi/nf-wuapi-iupdatehistoryentry-get_title)                             | Gets the title of an update.                                                                                             |
| [**UninstallationNotes**](/windows/win32/api/wuapi/nf-wuapi-iupdatehistoryentry-get_uninstallationnotes) | Gets the uninstallation notes of an update.                                                                              |
| [**UninstallationSteps**](/windows/desktop/api/Wuapi/nf-wuapi-iupdatehistoryentry-get_uninstallationsteps) | Gets the [**IStringCollection**](/windows/desktop/api/Wuapi/nn-wuapi-istringcollection) interface that contains the uninstallation steps for an update.  |
| [**UnmappedResultCode**](/windows/desktop/api/Wuapi/nf-wuapi-iupdatehistoryentry-get_unmappedresultcode)   | Gets the unmapped result code that is returned from an operation on an update.                                           |
| [**UpdateIdentity**](/windows/desktop/api/Wuapi/nf-wuapi-iupdatehistoryentry-get_updateidentity)           | Gets a string. The string contains the unique identifier of an update.                                                   |



 

 

 
