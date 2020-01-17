---
Description: A service provider can indicate externally generated phone numbers by setting members of the LINECALLINFO structure when processing the TSPI\_lineGetCallInfo function.
ms.assetid: 10c83199-de7d-4a9b-84c4-ef8f5ea5055a
title: Externally Generated Phone Numbers
ms.topic: article
ms.date: 05/31/2018
---

# Externally Generated Phone Numbers

A service provider can indicate externally generated phone numbers (that is, numbers for outbound calls generated externally to the computer) by setting the **DisplayableAddress**, **CalledParty**, or [Comment](https://msdn.microsoft.com/library/ms726934(v=VS.85).aspx) members in the [**LINECALLINFO**](https://msdn.microsoft.com/library/ms735527(v=VS.85).aspx) structure when processing the [**TSPI\_lineGetCallInfo**](https://msdn.microsoft.com/library/ms725566(v=VS.85).aspx) function. If TAPI has not saved its own data for these members, it leaves the data set by the service provider unchanged. If TAPI does have cached data for these members, TAPI adds its text to the end of the variable portion of the **LINECALLINFO** structure and overwrites the size and offset the service provider has put into the fixed portion.

A service provider can also copy an outbound number into the **CalledID** member. Therefore, logging applications should check the **CalledID** member on outbound calls if the **DisplayableAddress** and **CalledParty** members are empty.

 

 



