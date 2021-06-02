---
description: The NMEVENTDATA structure contains information about an event condition that is passed to Network Monitor to insert a line in the expert viewer.
ms.assetid: 35cda410-d45a-4a51-91b7-8bd4a0c9957f
title: NMEVENTDATA structure (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- NMEVENTDATA
api_type: 
- HeaderDef
api_location: 
- Netmon.h
---

# NMEVENTDATA structure

The **NMEVENTDATA** structure contains information about an event condition that is passed to Network Monitor to insert a line in the expert viewer.

## Syntax


```C++
typedef struct {
  BYTE         Version;
  DWORD        EventIdent;
  DWORD        Flags;
  DWORD        Severity;
  BYTE         NumColumns;
  LPSTR        szSourceName;
  LPSTR        szEventName;
  LPSTR        szDescription;
  LPSTR        szMachine;
  JTYPE        Justification;
  LPSTR        szUrl;
  SYSTEMTIME   SysTime;
  NMCOLUMNINFO Column[];
} NMEVENTDATA, *PNMEVENTDATA;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

Version number of the **NMEVENTDATA** structure. The version number must be zero. Future versions of Network Monitor may support a higher version number.

</dd> <dt>

**EventIdent**
</dt> <dd>

Identifier of the event. **EventIdent** is unique to each expert, and references an [event reference page](event-reference-page.md).

</dd> <dt>

**Flags**
</dt> <dd>

A set of flags that describes who sends the event data, and how the event is displayed.



| Value                                                                                                                                                                                                                                              | Meaning                                                                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="EVENT_FLAG_EXPERT"></span><span id="event_flag_expert"></span><dl> <dt>**EVENT\_FLAG\_EXPERT**</dt> </dl>                                                                         | The event came from an expert. <br/>                                                                                                                                  |
| <span id="NMEVENTFLAG_DO_NOT_DISPLAY_SEVERITY"></span><span id="nmeventflag_do_not_display_severity"></span><dl> <dt>**NMEVENTFLAG\_DO\_NOT\_DISPLAY\_SEVERITY**</dt> </dl>                 | Do not display the severity level for the event. <br/>                                                                                                                |
| <span id="NMEVENTFLAG_DO_NOT_DISPLAY_SOURCE"></span><span id="nmeventflag_do_not_display_source"></span><dl> <dt>**NMEVENTFLAG\_DO\_NOT\_DISPLAY\_SOURCE**</dt> </dl>                       | Do not display the source name for the event. <br/>                                                                                                                   |
| <span id="NMEVENTFLAG_DO_NOT_DISPLAY_EVENT_NAME"></span><span id="nmeventflag_do_not_display_event_name"></span><dl> <dt>**NMEVENTFLAG\_DO\_NOT\_DISPLAY\_EVENT\_NAME**</dt> </dl>          | Do not display the event name for the event. <br/>                                                                                                                    |
| <span id="NMEVENTFLAG_DO_NOT_DISPLAY_DESCRIPTION"></span><span id="nmeventflag_do_not_display_description"></span><dl> <dt>**NMEVENTFLAG\_DO\_NOT\_DISPLAY\_DESCRIPTION**</dt> </dl>        | Do not display the description for the event. <br/>                                                                                                                   |
| <span id="NMEVENTFLAG_DO_NOT_DISPLAY_MACHINE"></span><span id="nmeventflag_do_not_display_machine"></span><dl> <dt>**NMEVENTFLAG\_DO\_NOT\_DISPLAY\_MACHINE**</dt> </dl>                    | Do not display the machine name for the event. <br/>                                                                                                                  |
| <span id="NMEVENTFLAG_DO_NOT_DISPLAY_TIME"></span><span id="nmeventflag_do_not_display_time"></span><dl> <dt>**NMEVENTFLAG\_DO\_NOT\_DISPLAY\_TIME**</dt> </dl>                             | Do not display the time for the event <br/>                                                                                                                           |
| <span id="NMEVENTFLAG_DO_NOT_DISPLAY_FIXED_COLUMNS"></span><span id="nmeventflag_do_not_display_fixed_columns"></span><dl> <dt>**NMEVENTFLAG\_DO\_NOT\_DISPLAY\_FIXED\_COLUMNS**</dt> </dl> | Do not display the Severity, Source, Event Name, Description, Machine, or Time columns. This is not a single flag, but it is a union of the previous six flags. <br/> |



 

</dd> <dt>

**Severity**
</dt> <dd>

Severity level of the event. The severity level can have one of the following values:

NMEVENT\_SEVERITY\_INFORMATIONAL NMEVENT\_SEVERITY\_WARNING NMEVENT\_SEVERITY\_STRONG\_WARNING NMEVENT\_SEVERITY\_ERROR NMEVENT\_SEVERITY\_SEVERE\_ERROR NMEVENT\_SEVERITY\_CRITICAL\_ERROR

</dd> <dt>

**NumColumns**
</dt> <dd>

Number of columns designated in the current structure.

</dd> <dt>

**szSourceName**
</dt> <dd>

Name of the expert that is displayed.

</dd> <dt>

**szEventName**
</dt> <dd>

Name of the event that is displayed.

</dd> <dt>

**szDescription**
</dt> <dd>

Description of the event that is displayed.

</dd> <dt>

**szMachine**
</dt> <dd>

Obsolete, should be **NULL**.

</dd> <dt>

**Justification**
</dt> <dd>

Information displayed in the second window of the Event Viewer. The **Justification** member may be **NULL**. If it is **NULL**, the second window is not be visible.

</dd> <dt>

**szUrl**
</dt> <dd>

Reserved; this member must be **NULL**.

</dd> <dt>

**SysTime**
</dt> <dd>

Time at which the event condition occurs. The time is measured relative to the beginning of the capture.

</dd> <dt>

**Column**
</dt> <dd>

Table of column structures that appears in the top pane of the Event Viewer.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



 

 




