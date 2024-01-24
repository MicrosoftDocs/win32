---
description: The IUpdateSearcher interface defines the following methods.
ms.assetid: 82735555-b23a-43b0-bf5b-a8cf72dc40d4
title: IUpdateSearcher Methods
ms.topic: reference
ms.date: 05/31/2018
---

# IUpdateSearcher Methods

The [**IUpdateSearcher**](/windows/desktop/api/Wuapi/nn-wuapi-iupdatesearcher) interface defines the following methods.



| Method                                                              | Description                                                                                                               |
|---------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| [**BeginSearch**](/windows/desktop/api/Wuapi/nf-wuapi-iupdatesearcher-beginsearch)                   | Begins execution of an asynchronous search for updates. The search uses the search options that are currently configured. |
| [**EndSearch**](/windows/desktop/api/Wuapi/nf-wuapi-iupdatesearcher-endsearch)                       | Completes an asynchronous search for updates.                                                                             |
| [**EscapeString**](/windows/desktop/api/Wuapi/nf-wuapi-iupdatesearcher-escapestring)                 | Converts a string into a string that can be used as a literal value in a search criteria string.                          |
| [**GetTotalHistoryCount**](/windows/desktop/api/Wuapi/nf-wuapi-iupdatesearcher-gettotalhistorycount) | Returns the number of update events on the computer.                                                                      |
| [**QueryHistory**](/windows/desktop/api/Wuapi/nf-wuapi-iupdatesearcher-queryhistory)                | Synchronously queries the computer for the history of update events.                                                      |
| [**Search**](/windows/desktop/api/Wuapi/nf-wuapi-iupdatesearcher-search)                             | Performs a synchronous search for updates. The search uses the search options that are currently configured.              |



 

 

 



