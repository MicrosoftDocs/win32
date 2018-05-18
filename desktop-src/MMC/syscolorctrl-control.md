---
title: SysColorCtrl Control object
description: The SysColorCtrl control is used on a taskpad DHTML page to get system color settings that can be applied to the taskpad. The control also has methods to derive colors based on one or more specified colors.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '60532d06-0b32-4f42-a7b7-b4b05518c6e6'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["SysColorCtrl Control object MMC", "SysColorCtrl Control object MMC , described"]
topic_type:
- apiref
api_name:
- SysColorCtrl Control
- HEXactiveborder
- RGBactiveborder
- HEXactivecaption
- RGBactivecaption
- HEXappworkspace
- RGBappworkspace
- HEXbackground
- RGBbackground
- HEXbuttonface
- RGBbuttonface
- HEXbuttonhighlight
- RGBbuttonhighlight
- HEXbuttonshadow
- RGBbuttonshadow
- HEXbuttontext
- RGBbuttontext
- HEXcaptiontext
- RGBcaptiontext
- HEXgraytext
- RGBgraytext
- HEXhighlight
- RGBhighlight
- HEXhighlighttext
- RGBhighlighttext
- HEXinactiveborder
- RGBinactiveborder
- HEXinactivecaption
- RGBinactivecaption
- HEXinactivecaptiontext
- RGBinactivecaptiontext
- HEXinfobackground
- RGBinfobackground
- HEXinfotext
- RGBinfotext
- HEXmenu
- RGBmenu
- HEXmenutext
- RGBmenutext
- HEXscrollbar
- RGBscrollbar
- HEXthreeddarkshadow
- RGBthreeddarkshadow
- HEXthreedface
- RGBthreedface
- HEXthreedhighlight
- RGBthreedhighlight
- HEXthreedlightshadow
- RGBthreedlightshadow
- HEXthreedshadow
- RGBthreedshadow
- HEXwindow
- RGBwindow
- HEXwindowframe
- RGBwindowframe
- HEXwindowtext
- RGBwindowtext
api_location:
- MmcNdMgr.dll
api_type:
- COM
---

# SysColorCtrl Control object

The **SysColorCtrl** control is used on a taskpad DHTML page to get system color settings that can be applied to the taskpad. The control also has methods to derive colors based on one or more specified colors.

The MMC taskpad templates use the **SysColorCtrl** control. To create a custom taskpad that uses the system colors, the **SysColorCtrl** control should be placed as an object on the taskpad HTML page and its methods should be used to get system color values for use on the taskpad DHTML page. Optionally, your taskpad HTML page can use the methods to derive other colors (blend two colors, or lighten or darken a color) from a specified color.

The CLSID for **SysColorCtrl** is C47195EC-CD7A-11D1-8EA3-00C04F9900D7.

## Members

The **SysColorCtrl Control** object has these types of members:

-   [Events](#events)
-   [Methods](#methods)
-   [Properties](#properties)

### Events

The **SysColorCtrl Control** object has these events.



| Event                                    | Description                                    |
|:-----------------------------------------|:-----------------------------------------------|
| [**SysColorChange**](syscolorchange.md) | A system color change has occurred.<br/> |



 

### Methods

The **SysColorCtrl Control** object has these methods.



| Method                                             | Description                                                                                                                                               |
|:---------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ConvertHexToRGB**](converthextorgb.md)         | Converts a hexadecimal value to RGB.<br/>                                                                                                           |
| [**ConvertRGBToHex**](convertrgbtohex.md)         | Converts an RGB value to hexadecimal.<br/>                                                                                                          |
| [**Get3QuarterDarkHex**](get3quarterdarkhex.md)   | Derives a "darker" color by calculating a color that is blended 75% between a given color and black. Returns as a hexadecimal value.<br/>           |
| [**Get3QuarterDarkRGB**](get3quarterdarkrgb.md)   | Derives a "darker" color by calculating a color that is blended 75% between a given color and black. Returns as an RGB value.<br/>                  |
| [**Get3QuarterLightHex**](get3quarterlighthex.md) | Derives a "lighter" color by calculating a color that is blended 75% between a given color and white. Returns as a hexadecimal value.<br/>          |
| [**Get3QuarterLightRGB**](get3quarterlightrgb.md) | Derives a "lighter" color by calculating a color that is blended 75% between a given color and white. Returns as an RGB value.<br/>                 |
| [**GetBlueFromRGB**](getbluefromrgb.md)           | Gets the blue value from an RGB value.<br/>                                                                                                         |
| [**GetDerivedHex**](getderivedhex.md)             | Derives a color based on a starting color, a color to move toward, and a percentage to move toward that color. Returns as a hexadecimal value.<br/> |
| [**GetDerivedRGB**](getderivedrgb.md)             | Derives a color based on a starting color, a color to move toward, and a percentage to move toward that color. Returns as an RGB value.<br/>        |
| [**GetGreenFromRGB**](getgreenfromrgb.md)         | Gets the green value from an RGB value.<br/>                                                                                                        |
| [**GetHalfDarkHex**](gethalfdarkhex.md)           | Derives a "darker" color by calculating a color that is blended 50% between a given color and black. Returns as a hexadecimal value.<br/>           |
| [**GetHalfDarkRGB**](gethalfdarkrgb.md)           | Derives a "darker" color by calculating a color that is blended 50% between a given color and black. Returns as an RGB value.<br/>                  |
| [**GetHalfLightHex**](gethalflighthex.md)         | Derives a "lighter" color by calculating a color that is blended 50% between a given color and white. Returns as a hexadecimal value.<br/>          |
| [**GetHalfLightRGB**](gethalflightrgb.md)         | Derives a "lighter" color by calculating a color that is blended 50% between a given color and white. Returns as an RGB value.<br/>                 |
| [**GetQuarterDarkHex**](getquarterdarkhex.md)     | Derives a "darker" color by calculating a color that is blended 25% between a given color and black. Returns as a hexadecimal value.<br/>           |
| [**GetQuarterDarkRGB**](getquarterdarkrgb.md)     | Derives a "darker" color by calculating a color that is blended 25% between a given color and black. Returns as an RGB value.<br/>                  |
| [**GetQuarterLightHex**](getquarterlighthex.md)   | Derives a "lighter" color by calculating a color that is blended 25% between a given color and white. Returns as a hexadecimal value.<br/>          |
| [**GetQuarterLightRGB**](getquarterlightrgb.md)   | Derives a "lighter" color by calculating a color that is blended 25% between a given color and white. Returns as an RGB value.<br/>                 |
| [**GetRedFromRGB**](getredfromrgb.md)             | Gets the red value from an RGB value.<br/>                                                                                                          |



 

### Properties

The **SysColorCtrl Control** object has these properties.



| Property                          | Description                                      |
|:----------------------------------|:-------------------------------------------------|
| HEXactiveborder<br/>        | Active border color, in HEX.<br/>          |
| HEXactivecaption<br/>       | Active caption color, in HEX.<br/>         |
| HEXappworkspace<br/>        | Application workspace color, in HEX.<br/>  |
| HEXbackground<br/>          | Background color, in HEX.<br/>             |
| HEXbuttonface<br/>          | Button face color, in HEX.<br/>            |
| HEXbuttonhighlight<br/>     | Button highlight color, in HEX.<br/>       |
| HEXbuttonshadow<br/>        | Button shadow color, in HEX.<br/>          |
| HEXbuttontext<br/>          | Button text color, in HEX.<br/>            |
| HEXcaptiontext<br/>         | Caption text color, in HEX.<br/>           |
| HEXgraytext<br/>            | Gray text color, in HEX.<br/>              |
| HEXhighlight<br/>           | Highlight color, in HEX.<br/>              |
| HEXhighlighttext<br/>       | Highlight text color, in HEX.<br/>         |
| HEXinactiveborder<br/>      | Inactive border color, in HEX.<br/>        |
| HEXinactivecaption<br/>     | Inactive caption color, in HEX.<br/>       |
| HEXinactivecaptiontext<br/> | Inactive caption text color, in HEX.<br/>  |
| HEXinfobackground<br/>      | Information background color, in HEX.<br/> |
| HEXinfotext<br/>            | Information text color, in HEX.<br/>       |
| HEXmenu<br/>                | Menu color, in HEX.<br/>                   |
| HEXmenutext<br/>            | Menu text color, in HEX.<br/>              |
| HEXscrollbar<br/>           | Scrollbar color, in HEX.<br/>              |
| HEXthreeddarkshadow<br/>    | 3D dark shadow color, in HEX.<br/>         |
| HEXthreedface<br/>          | 3D face color, in HEX.<br/>                |
| HEXthreedhighlight<br/>     | 3D highlight color, in HEX.<br/>           |
| HEXthreedlightshadow<br/>   | 3D light shadow color, in HEX.<br/>        |
| HEXthreedshadow<br/>        | 3D shadow color, in HEX.<br/>              |
| HEXwindow<br/>              | Window color, in HEX.<br/>                 |
| HEXwindowframe<br/>         | Window frame color, in HEX.<br/>           |
| HEXwindowtext<br/>          | Window text color, in HEX.<br/>            |
| RGBactiveborder<br/>        | Active border color, in RGB.<br/>          |
| RGBactivecaption<br/>       | Active caption color, in RGB.<br/>         |
| RGBappworkspace<br/>        | Application workspace color, in RGB.<br/>  |
| RGBbackground<br/>          | Background color, in RGB.<br/>             |
| RGBbuttonface<br/>          | Button face color, in RGB.<br/>            |
| RGBbuttonhighlight<br/>     | Button highlight color, in RGB.<br/>       |
| RGBbuttonshadow<br/>        | Button shadow color, in RGB.<br/>          |
| RGBbuttontext<br/>          | Button text color, in RGB.<br/>            |
| RGBcaptiontext<br/>         | Caption text color, in RGB.<br/>           |
| RGBgraytext<br/>            | Gray text color, in RGB.<br/>              |
| RGBhighlight<br/>           | Highlight color, in RGB.<br/>              |
| RGBhighlighttext<br/>       | Highlight text color, in RGB.<br/>         |
| RGBinactiveborder<br/>      | Inactive border color, in RGB.<br/>        |
| RGBinactivecaption<br/>     | Inactive caption color, in RGB.<br/>       |
| RGBinactivecaptiontext<br/> | Inactive caption text color, in RGB.<br/>  |
| RGBinfobackground<br/>      | Information background color, in RGB.<br/> |
| RGBinfotext<br/>            | Information text color, in RGB.<br/>       |
| RGBmenu<br/>                | Menu color, in RGB.<br/>                   |
| RGBmenutext<br/>            | Menu text color, in RGB.<br/>              |
| RGBscrollbar<br/>           | Scrollbar color, in RGB.<br/>              |
| RGBthreeddarkshadow<br/>    | 3D dark shadow color, in RGB.<br/>         |
| RGBthreedface<br/>          | 3D face color, in RGB.<br/>                |
| RGBthreedhighlight<br/>     | 3D highlight color, in RGB.<br/>           |
| RGBthreedlightshadow<br/>   | 3D light shadow color, in RGB.<br/>        |
| RGBthreedshadow<br/>        | 3D shadow color, in RGB.<br/>              |
| RGBwindow<br/>              | Window color, in RGB.<br/>                 |
| RGBwindowframe<br/>         | Window frame color, in RGB.<br/>           |
| RGBwindowtext<br/>          | Window text color, in RGB.<br/>            |



 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>     |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>MmcNdMgr.dll</dt> </dl> |



 

 





