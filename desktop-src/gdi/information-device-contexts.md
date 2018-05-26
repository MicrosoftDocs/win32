---
Description: The information DC is used to retrieve default device data.
ms.assetid: 8fd05c17-e8c9-4747-9a66-ce7d958edeb9
title: Information Device Contexts
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Information Device Contexts

The information DC is used to retrieve default device data. For example, an application can call the [**CreateIC**](/windows/win32/Wingdi/nf-wingdi-createica?branch=master) function to create an information DC for a particular model of printer and then call the [**GetCurrentObject**](/windows/win32/Wingdi/nf-wingdi-getcurrentobject?branch=master) and [**GetObject**](/windows/win32/Wingdi/nf-wingdi-getobject?branch=master) functions to retrieve the default pen or brush attributes. Because the system can retrieve device information without creating the structures normally associated with the other types of device contexts, an information DC involves far less overhead and is created significantly faster than any of the other types. After an application finishes retrieving data by using an information DC, it must call the [**DeleteDC**](/windows/win32/Wingdi/nf-wingdi-deletedc?branch=master) function.

 

 



