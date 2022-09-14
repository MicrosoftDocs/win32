---
description: An enum used to indicate the type of an event.
MS-HAID: vspixengine.EVENTTYPE
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: EVENTTYPE enumeration
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: F7A6F396-5BC0-4963-ABFD-ACB7AAE475F5
api_name: 
 - EVENTTYPE
api_type: 
 - HeaderDef
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax
---

# <span id="vspixengine.eventtype"></span>EVENTTYPE enumeration

An enum used to indicate the type of an event.

## Syntax

```cpp
C++ 
enum EVENTTYPE {
  ET_NONE = 0, 
  ET_SESSIONSTART, 
  ET_SESSIONEND, 
  ET_PROCESSSTART, 
  ET_PROCESSEND, 
  ET_FRAMEBEGIN, 
  ET_FRAMEEND, 
  ET_USEREVENTBEGIN, 
  ET_USEREVENTEND, 
  ET_USERMARKER, 
  ET_CALL, 
  ET_OBJECTCREATION, 
  ET_OBJECTPOPULATION, 
  ET_CALLSYNC, 
  ET_DRAW, 
  ET_DISPATCH 
};
```

## Constants

<span id="ET_NONE"></span><span id="et_none"></span>**ET\_NONE**  
A value that corresponds to no event.

<span id="ET_SESSIONSTART"></span><span id="et_sessionstart"></span>**ET\_SESSIONSTART**  
A value that corresponds to a session start event.

<span id="ET_SESSIONEND"></span><span id="et_sessionend"></span>**ET\_SESSIONEND**  
A value that corresponds to a session end event.

<span id="ET_PROCESSSTART"></span><span id="et_processstart"></span>**ET\_PROCESSSTART**  
A value that corresponds to a process start event.

<span id="ET_PROCESSEND"></span><span id="et_processend"></span>**ET\_PROCESSEND**  
A value that corresponds to a process end event.

<span id="ET_FRAMEBEGIN"></span><span id="et_framebegin"></span>**ET\_FRAMEBEGIN**  
A value that corresponds to a frame begin event.

<span id="ET_FRAMEEND"></span><span id="et_frameend"></span>**ET\_FRAMEEND**  
A value that corresponds to a frame end event. Not used.

<span id="ET_USEREVENTBEGIN"></span><span id="et_usereventbegin"></span>**ET\_USEREVENTBEGIN**  
A value that corresponds to a user-event begin event.

<span id="ET_USEREVENTEND"></span><span id="et_usereventend"></span>**ET\_USEREVENTEND**  
A value that corresponds to a user-event end event. Not used.

<span id="ET_USERMARKER"></span><span id="et_usermarker"></span>**ET\_USERMARKER**  
A value that corresponds to a user-marker event.

<span id="ET_CALL"></span><span id="et_call"></span>**ET\_CALL**  
A value that corresponds to a call event.

<span id="ET_OBJECTCREATION"></span><span id="et_objectcreation"></span>**ET\_OBJECTCREATION**  
A value that corresponds to an object creation event.

<span id="ET_OBJECTPOPULATION"></span><span id="et_objectpopulation"></span>**ET\_OBJECTPOPULATION**  
A value that corresponds to an object population event.

<span id="ET_CALLSYNC"></span><span id="et_callsync"></span>**ET\_CALLSYNC**  

<span id="ET_DRAW"></span><span id="et_draw"></span>**ET\_DRAW**  
A value that corresponds to a draw call event.

<span id="ET_DISPATCH"></span><span id="et_dispatch"></span>**ET\_DISPATCH**  
A value that corresponds to a dispatch event.

## Requirements

<table><colgroup><col  /><col  /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>
