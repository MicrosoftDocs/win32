---
description: The information DC is used to retrieve default device data.
ms.assetid: 8fd05c17-e8c9-4747-9a66-ce7d958edeb9
title: Information Device Contexts
ms.topic: article
ms.date: 05/31/2018
---

# Information Device Contexts

The information DC is used to retrieve default device data. For example, an application can call the [**CreateIC**](/windows/desktop/api/Wingdi/nf-wingdi-createica) function to create an information DC for a particular model of printer and then call the [**GetCurrentObject**](/windows/desktop/api/Wingdi/nf-wingdi-getcurrentobject) and [**GetObject**](/windows/desktop/api/Wingdi/nf-wingdi-getobject) functions to retrieve the default pen or brush attributes. Because the system can retrieve device information without creating the structures normally associated with the other types of device contexts, an information DC involves far less overhead and is created significantly faster than any of the other types. After an application finishes retrieving data by using an information DC, it must call the [**DeleteDC**](/windows/desktop/api/Wingdi/nf-wingdi-deletedc) function.

 

 



