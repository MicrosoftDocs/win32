---
Description: TAPI provides a number of functions for manipulating call handles, determining the relationship among lines, calls, and address, and so on.
ms.assetid: 283fe5e9-689f-4b87-97a6-b345c22ec6a2
title: Call Handle Manipulation
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Call Handle Manipulation

TAPI provides a number of functions for manipulating call handles, determining the relationship among lines, calls, and address, and so on. Most of this functionality is implemented strictly within TAPI without reference to the service provider, except for [**TSPI\_lineGetCallAddressID**](https://msdn.microsoft.com/en-us/library/ms725563(v=VS.85).aspx). This function retrieves the address identifier of an existing call within its line. Service providers that model a line as a group of address identifiers can choose an unpredictable address for a new inbound or outbound call. This function gives TAPI sufficient information to implement the [**lineGetNewCalls**](https://msdn.microsoft.com/en-us/library/ms735761(v=VS.85).aspx) operation when it is invoked with the LINECALLSELECT\_ADDRESS option.

 

 



