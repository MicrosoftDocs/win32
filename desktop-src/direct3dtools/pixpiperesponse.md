---
description: An enum used to send responses from the capture engine to Graphics Diagnostics.
MS-HAID: vspixengine.PixPipeResponse
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: PixPipeResponse enumeration
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: 5BFEE25D-3E03-493E-AFEF-DD8C70C53FC5
api_name: 
 - PixPipeResponse
api_type: 
 - HeaderDef
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="vspixengine.pixpiperesponse"></span>PixPipeResponse enumeration

An enum used to send responses from the capture engine to Graphics Diagnostics.

## Syntax


```C++
};
```

## Constants

<span id="NEW_DATA_AVAILABLE"></span><span id="new_data_available"></span>**NEW\_DATA\_AVAILABLE**  
A response which indicates that new data has been written to the graphics log and is ready to be read.

<span id="EXPERIMENT_DATA"></span><span id="experiment_data"></span>**EXPERIMENT\_DATA**  
A response which indicates configuration information about the capture session.

<span id="ERRORCODE"></span><span id="errorcode"></span>**ERRORCODE**  
A response which indicates that the capture engine has encountered an error.

<span id="APPLICATIONCAPTUREINPROGRESS"></span><span id="applicationcaptureinprogress"></span>**APPLICATIONCAPTUREINPROGRESS**  
A response which indicates that the capture engine has started capturing graphics information. This does not indicate that data is available to be examined yet.

<span id="PARTIAL_DATA"></span><span id="partial_data"></span>**PARTIAL\_DATA**  
A response which indicates that partial data has been written to the graphics log.

<span id="READY"></span><span id="ready"></span>**READY**  
A response which indicates that the capture engine is ready to start capturing graphics information.

<span id="DONE"></span><span id="done"></span>**DONE**  
Internal

<span id="CAPTURESTARTED"></span><span id="capturestarted"></span>**CAPTURESTARTED**  
A response which indicates that a frame capture has started.

<span id="STATUS"></span><span id="status"></span>**STATUS**  
A response which indicates status information about the app being captured; for example, framerate.

## Requirements

<table><colgroup><col  /><col  /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

 

 



