---
description: The IUpdateSession3 interface defines the following methods.
ms.assetid: 8015443a-e232-44ab-b53a-e8cc4acd4dd3
title: IUpdateSession3 Methods
ms.topic: reference
ms.date: 05/31/2018
---

# IUpdateSession3 Methods

The [**IUpdateSession3**](/windows/desktop/api/Wuapi/nn-wuapi-iupdatesession3) interface defines the following methods.



| Method                                                                           | Description                                                                                                                                                                                                                                                                                                                |
|----------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateUpdateServiceManager**](/windows/desktop/api/Wuapi/nf-wuapi-iupdatesession3-createupdateservicemanager) | Returns a pointer to an [**IUpdateServiceManager2**](/windows/desktop/api/Wuapi/nn-wuapi-iupdateservicemanager2) interface for the session.                                                                                                                                                                                                                |
| [**QueryHistory**](/windows/desktop/api/Wuapi/nf-wuapi-iupdatesession3-queryhistory)                             | Returns a pointer to an [**IUpdateHistoryEntryCollection**](/windows/desktop/api/Wuapi/nn-wuapi-iupdatehistoryentrycollection) interface. The interface contains matching event records on the computer. This causes the [**QueryHistory**](/windows/desktop/api/Wuapi/nf-wuapi-iupdatesession3-queryhistory) method to synchronously query the computer for the history of update events. |



 

For information about the members inherited by this interface, see the following interfaces:

-   [**IUpdateSession2**](/windows/desktop/api/Wuapi/nn-wuapi-iupdatesession2)
-   [**IUpdateSession**](/windows/desktop/api/Wuapi/nn-wuapi-iupdatesession)

 

 



