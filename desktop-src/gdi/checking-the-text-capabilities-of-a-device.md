---
description: You can use the EnumFonts and EnumFontFamilies functions to enumerate the fonts that are available in a printer-compatible memory device context.
ms.assetid: d68de203-2d5f-4a28-bb57-1dda9fcb078a
title: Checking the Text Capabilities of a Device
ms.topic: article
ms.date: 05/31/2018
---

# Checking the Text Capabilities of a Device

You can use the [EnumFonts](/windows/desktop/api/Wingdi/nf-wingdi-enumfontsa) and [EnumFontFamilies](/windows/desktop/api/Wingdi/nf-wingdi-enumfontfamiliesa) functions to enumerate the fonts that are available in a printer-compatible memory device context. You can also use the [GetDeviceCaps](/windows/desktop/api/Wingdi/nf-wingdi-getdevicecaps) function to retrieve information about the text capabilities of a device. By calling the [**GetDeviceCaps**](/windows/win32/api/wingdi/nf-wingdi-getdevicecaps) function with the NUMFONTS index, you can determine the minimum number of fonts supported by a printer. (An individual printer may support more fonts than specified in the return value from **GetDeviceCaps** with the NUMFONTS index.) By using the TEXTCAPS index, you can identify many of the text capabilities of the specified device.

 

 
