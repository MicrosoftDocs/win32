---
description: The PdhVbGetOneCounterPath function displays a dialog box that lets the user browse the available performance counters and select one counter.
ms.assetid: a42406ef-70e0-464d-90f8-fef9e1c3471d
title: PdhVbGetOneCounterPath function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PdhVbGetOneCounterPath
api_type: 
- DllExport
api_location: 
- Pdh.dll
---

# PdhVbGetOneCounterPath function

The **PdhVbGetOneCounterPath** function displays a dialog box that lets the user browse the available performance counters and select one counter. The counter selected is returned in the *PathString* variable. The *PathString* variable must be dimensioned and initialized before this function is called, and the dimensioned size must be indicated by the *PathLength* variable.

> [!IMPORTANT]
> The function that this topic describes may be altered or unavailable in the future. Instead, Microsoft recommends that you use the functions described in [Performance Counters Functions](performance-counters-functions.md).

Function PdhVbGetOneCounterPath( \_ ByVal PathString As String, \_ ByVal PathLength As Long, \_ ByVal DetailLevel As Long, \_ ByVal CaptionString As String \_ ) As Long

## Parameters

<dl> <dt>

*PathString* 
</dt> <dd>

Initialized string variable used to receive the counter path selected by the user.

</dd> <dt>

*PathLength* 
</dt> <dd>

Length of the initialized PathString.

</dd> <dt>

*DetailLevel* 
</dt> <dd>

Types of counters to be displayed in the dialog box. This parameter can be one of the following values.



| Value                                                                                                                                                                               | Meaning                                                                                                                                                 |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="PERF_DETAIL_ADVANCED"></span><span id="perf_detail_advanced"></span><dl> <dt>**PERF\_DETAIL\_ADVANCED**</dt> </dl> | Counters that the advanced user is likely to understand, in addition to the novice-user counters.<br/>                                            |
| <span id="PERF_DETAIL_EXPERT"></span><span id="perf_detail_expert"></span><dl> <dt>**PERF\_DETAIL\_EXPERT**</dt> </dl>       | Counters that the expert user and software developer is likely to understand, in addition to the counters for the novice and advanced users.<br/> |
| <span id="PERF_DETAIL_NOVICE"></span><span id="perf_detail_novice"></span><dl> <dt>**PERF\_DETAIL\_NOVICE**</dt> </dl>       | Only counters that the novice user is likely to understand.<br/>                                                                                  |
| <span id="PERF_DETAIL_WIZARD"></span><span id="perf_detail_wizard"></span><dl> <dt>**PERF\_DETAIL\_WIZARD**</dt> </dl>       | All counters in the system.<br/>                                                                                                                  |



 

</dd> <dt>

*CaptionString* 
</dt> <dd>

String variable that contains the text that will be displayed in the caption bar of the dialog box.

</dd> </dl>

## Return value

The function returns the number of characters written to the *PathString* buffer.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                               |
| Library<br/>                  | <dl> <dt>Pdh.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Pdh.dll</dt> </dl> |



## See also

<dl> <dt>

[**PdhVbCreateCounterPathList**](pdhvbcreatecounterpathlist.md)
</dt> <dt>

[**PdhVbGetCounterPathElements**](pdhvbgetcounterpathelements.md)
</dt> <dt>

[**PdhVbGetCounterPathFromList**](pdhvbgetcounterpathfromlist.md)
</dt> </dl>

 

 




