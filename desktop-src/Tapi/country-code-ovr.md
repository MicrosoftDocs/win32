---
Description: The country or region code is relevant only when the address type is LINEADDRESSTYPE\_PHONENUMBER. It identifies an area of the world.
ms.assetid: d838c2ac-4ee3-4314-8573-deed6c7430e3
title: Country or Region Code
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Country or Region Code

The country or region code is relevant only when the address type is LINEADDRESSTYPE\_PHONENUMBER. It identifies an area of the world.

All service providers that support use of telephone numbers must support use of this information.

**TAPI 2.x:** See [**lineGetCallInfo**](https://msdn.microsoft.com/en-us/library/ms735720(v=VS.85).aspx) (**dwCountryCode** member of *lpCallInfo*).

**TAPI 3.x:** See [**ITCallInfo::get\_CallInfoLong**](/windows/desktop/api/tapi3if/nf-tapi3if-itcallinfo-get_callinfolong) (**CIL\_COUNTRYCODE** member of [**CALLINFO\_LONG**](/windows/desktop/api/Tapi3if/ne-tapi3if-callinfo_long)).

 

 



