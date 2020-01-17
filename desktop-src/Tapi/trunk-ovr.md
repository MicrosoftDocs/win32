---
Description: The number of the trunk over which the call is routed. This member is used for both incoming and outgoing calls.
ms.assetid: e57e1aac-a2f1-42b7-9a0c-c74009a75305
title: Trunk
ms.topic: article
ms.date: 05/31/2018
---

# Trunk

The number of the trunk over which the call is routed. This member is used for both incoming and outgoing calls.

Not all service providers support use of this information.

**TAPI 2.x:  **[**lineGetCallInfo**](https://msdn.microsoft.com/library/ms735720(v=VS.85).aspx), **dwTrunk** of [**LINECALLINFO**](https://msdn.microsoft.com/library/ms735527(v=VS.85).aspx)

**TAPI 3.x:  **[**ITCallInfo::get\_CallInfoLong**](/windows/desktop/api/tapi3if/nf-tapi3if-itcallinfo-get_callinfolong), called with **CIL\_TRUNK** member of [**CALLINFO\_LONG**](/windows/desktop/api/Tapi3if/ne-tapi3if-callinfo_long)

 

 



