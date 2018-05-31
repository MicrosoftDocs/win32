---
Description: In most cases device configuration data is associated with a specific fax device.
ms.assetid: fd5063d5-b9ff-4899-b275-e0ed037c11d3
title: Storing Global Configuration Data
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Storing Global Configuration Data

In most cases device configuration data is associated with a specific fax device. For example, an fax service provider (FSP) that provides support for fax-over-Internet Protocol (FoIP) transmissions can associate an Internet Protocol (IP) address with each device it exposes.

There are other occasions when an extension must store data that relates to the entire extension, rather than just to a specific device. For example, a fax routing extension may use optical character recognition (OCR) technology to scan a received fax and convert it to text. The routing extension may have three different routing methods that use OCR (for example, *Fax2Doc*, *Fax2Txt*, and *Fax2Rtf*). Each method converts the Tagged Image File Format (TIFF) fax image to a different text format. Because the OCR process itself has configurable parameters that apply to all three methods (such as skew limit or resolution), the OCR configuration data is global rather than device-specific.

To store global configuration data such as the OCR parameters, you can specify a special device ID (ID = 0). This special device ID is not associated with any fax device. The ID is available for storage of global configuration data. To use this ID, specify zero in the *dwDeviceID* parameter when you call the [**FaxExtGetData**](/previous-versions/windows/desktop/api/FaxExt/nf-faxext-faxextgetdata), [**FaxExtSetData**](/previous-versions/windows/desktop/api/FaxExt/nf-faxext-faxextsetdata), or [**FaxExtRegisterForEvents**](/previous-versions/windows/desktop/api/FaxExt/nf-faxext-faxextregisterforevents) callback function.

 

 



