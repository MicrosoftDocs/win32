---
Description: This TSPI\_lineSetCurrentLocation function is obsolete. TAPI called this function when the user (using the Dialing Properties dialog box) or an application (using the lineSetCurrentLocation function) changed the address translation location.
ms.assetid: acd9f05b-88ae-439a-95c0-d1e8779a32fe
title: TSPI_lineSetCurrentLocation
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# TSPI\_lineSetCurrentLocation

This TSPI\_lineSetCurrentLocation function is obsolete. TAPI called this function when the user (using the **Dialing Properties** dialog box) or an application (using the [**lineSetCurrentLocation**](https://msdn.microsoft.com/en-us/library/ms736094(v=VS.85).aspx) function) changed the address translation location.

Currently, a change in translation location results in a LINE\_DEVSTATE message with *dwParam1* set to LINEDEVSTATE\_TRANSLATECHANGE.

 

 



