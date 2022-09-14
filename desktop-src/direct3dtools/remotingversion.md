---
description: An enum used to indicate which version of the remoting protocul is being used.
MS-HAID: vspixengine.REMOTINGVERSION
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: REMOTINGVERSION enumeration
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: 598E9586-05FF-4889-BBAF-44814EEF203A
api_name: 
 - REMOTINGVERSION
api_type: 
 - HeaderDef
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="vspixengine.remotingversion"></span>REMOTINGVERSION enumeration

An enum used to indicate which version of the remoting protocul is being used.

## Syntax


```C++
};
```

## Constants

<span id="REMOTING_DEV12"></span><span id="remoting_dev12"></span>**REMOTING\_DEV12**  
A value which indicates that the Visual Studio 2013 RTM remoting protocol is being used.

<span id="REMOTING_DEV12_UPDATE_1"></span><span id="remoting_dev12_update_1"></span>**REMOTING\_DEV12\_UPDATE\_1**  
A value which indicates that the Visual Studio 2013 Update 1 remoting protocol is being used.

<span id="REMOTING_DEV12_UPDATE_4"></span><span id="remoting_dev12_update_4"></span>**REMOTING\_DEV12\_UPDATE\_4**  
A value which indicates that the Visual Studio 2013 Update 4 remoting protocol is being used.

<span id="REMOTING_DEV14"></span><span id="remoting_dev14"></span>**REMOTING\_DEV14**  
A value which indicates that the Visual Studio 2015 RTM remoting protocol is being used.

<span id="REMOTING_WIN10"></span><span id="remoting_win10"></span>**REMOTING\_WIN10**  
A value which indicates that the Windows 10 remoting protocol is being used (Starting with Windows 10, graphics diagnostics is an OS component)

<span id="REMOTING_WIN10_JAN_2015"></span><span id="remoting_win10_jan_2015"></span>**REMOTING\_WIN10\_JAN\_2015**  
A value which indicates that the Windows 10 (January 2015) remoting protocol is being used.

<span id="REMOTING_WIN10_JAN_2015_1"></span><span id="remoting_win10_jan_2015_1"></span>**REMOTING\_WIN10\_JAN\_2015\_1**  
A value which indicates that the Windows 10 (January 2015, v1) remoting protocol is being used.

<span id="REMOTING_WIN10_JAN_2015_2"></span><span id="remoting_win10_jan_2015_2"></span>**REMOTING\_WIN10\_JAN\_2015\_2**  
A value which indicates that the Windows 10 (January 2015, v2) remoting protocol is being used. This version of the protocol introduced requests for visualizing tiled resources.

<span id="REMOTING_WIN10_JAN_2015_3"></span><span id="remoting_win10_jan_2015_3"></span>**REMOTING\_WIN10\_JAN\_2015\_3**  
A value which indicates that the Windows 10 (January 2015, v3) remoting protocol is being used. This version of the protocol introduced IPixEngine7, now deprecated, for checking interface version support.

<span id="REMOTING_IPIXENGINE7_VERSION_CHECKING"></span><span id="remoting_ipixengine7_version_checking"></span>**REMOTING\_IPIXENGINE7\_VERSION\_CHECKING**  
A value which indicates that the Windows 10 (January 2015, v1) remoting protocol is being used. This version of the protocol moves away from relying on REMOTINGVERSION to mediate protocol capabilities. The interface GUID is now changed when non-public int

<span id="REMOTING_WIN10_FEB_2015_1"></span><span id="remoting_win10_feb_2015_1"></span>**REMOTING\_WIN10\_FEB\_2015\_1**  
A value which indicates that the Windows 10 (January 2015, v1) remoting protocol is being used. This version of the protocol introduces summary info properties with unique, fixed IDs.

<span id="REMOTING_WIN10_2015_03_00"></span><span id="remoting_win10_2015_03_00"></span>**REMOTING\_WIN10\_2015\_03\_00**  
A value which indicates that the Windows 10 (January 2015, v1) remoting protocol is being used. This version of the protocol introduced support for the DirectX11 state window.

<span id="REMOTING_LATES"></span><span id="remoting_lates"></span>**REMOTING\_LATES**  
A value which indicates that the latest remoting protocol is being used.

## Requirements

<table><colgroup><col  /><col  /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

 

 



