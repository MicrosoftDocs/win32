---
title: XTYP\_MONITOR transaction
description: A Dynamic Data Exchange (DDE) debugger's DDE callback function, DdeCallback, receives the XTYP\_MONITOR transaction whenever a DDE event occurs in the system.
ms.assetid: 'a27791b1-c1b4-4516-b050-71da164fa80a'
keywords: ["XTYP_MONITOR transaction Data Exchange"]
topic_type:
- apiref
api_name:
- XTYP_MONITOR
api_location:
- Ddeml.h
api_type:
- HeaderDef
---

# XTYP\_MONITOR transaction

A Dynamic Data Exchange (DDE) debugger's DDE callback function, [*DdeCallback*](ddecallback.md), receives the **XTYP\_MONITOR** transaction whenever a DDE event occurs in the system. To receive this transaction, an application must specify the **APPCLASS\_MONITOR** value when it calls the [**DdeInitialize**](ddeinitialize.md) function.


```C++
#define     XCLASS_NOTIFICATION      0x8000
#define     XTYPF_NOBLOCK            0x0002
#define     XTYP_MONITOR            (0x00F0 | XCLASS_NOTIFICATION | XTYPF_NOBLOCK)
```



## Parameters

<dl> <dt>

*uType* 
</dt> <dd>

The transaction type.

</dd> <dt>

*uFmt* 
</dt> <dd>

Not used.

</dd> <dt>

*hconv* 
</dt> <dd>

Not used.

</dd> <dt>

*hsz1* 
</dt> <dd>

Not used.

</dd> <dt>

*hsz2* 
</dt> <dd>

Not used.

</dd> <dt>

*hdata* 
</dt> <dd>

A handle to a DDE object that contains information about the DDE event. The application should use the [**DdeAccessData**](ddeaccessdata.md) function to obtain a pointer to the object.

</dd> <dt>

*dwData1* 
</dt> <dd>

Not used.

</dd> <dt>

*dwData2* 
</dt> <dd>

The DDE event. This parameter can be one of the following values.



| Value                                                                                                                                                                                                                      | Meaning                                                                                                                                                                                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="MF_CALLBACKS"></span><span id="mf_callbacks"></span><dl> <dt>**MF\_CALLBACKS**</dt> <dt>0x08000000</dt> </dl> | The system sent a transaction to a DDE callback function. The DDE object contains a [**MONCBSTRUCT**](moncbstruct-str.md) structure that provides information about the transaction.<br/>                                                                                                                                               |
| <span id="MF_CONV"></span><span id="mf_conv"></span><dl> <dt>**MF\_CONV**</dt> <dt>0x40000000</dt> </dl>                | A DDE conversation was established or terminated. The DDE object contains a [**MONCONVSTRUCT**](monconvstruct-str.md) structure that provides information about the conversation.<br/>                                                                                                                                                  |
| <span id="MF_ERRORS"></span><span id="mf_errors"></span><dl> <dt>**MF\_ERRORS**</dt> <dt>0x10000000</dt> </dl>          | A DDE error occurred. The DDE object contains a [**MONERRSTRUCT**](monerrstruct-str.md) structure that provides information about the error.<br/>                                                                                                                                                                                       |
| <span id="MF_HSZ_INFO"></span><span id="mf_hsz_info"></span><dl> <dt>**MF\_HSZ\_INFO**</dt> <dt>0x01000000</dt> </dl>   | A DDE application created, freed, or incremented the usage count of a string handle, or a string handle was freed as a result of a call to the [**DdeUninitialize**](ddeuninitialize.md) function. The DDE object contains a [**MONHSZSTRUCT**](monhszstruct-str.md) structure that provides information about the string handle.<br/> |
| <span id="MF_LINKS"></span><span id="mf_links"></span><dl> <dt>**MF\_LINKS**</dt> <dt>0x20000000</dt> </dl>             | A DDE application started or stopped an advise loop. The DDE object contains a [**MONLINKSTRUCT**](monlinkstruct-str.md) structure that provides information about the advise loop.<br/>                                                                                                                                                |
| <span id="MF_POSTMSGS"></span><span id="mf_postmsgs"></span><dl> <dt>**MF\_POSTMSGS**</dt> <dt>0x04000000</dt> </dl>    | The system or an application posted a DDE message. The DDE object contains a [**MONMSGSTRUCT**](monmsgstruct-str.md) structure that provides information about the message.<br/>                                                                                                                                                        |
| <span id="MF_SENDMSGS"></span><span id="mf_sendmsgs"></span><dl> <dt>**MF\_SENDMSGS**</dt> <dt>0x02000000</dt> </dl>    | The system or an application sent a DDE message. The DDE object contains a [**MONMSGSTRUCT**](monmsgstruct-str.md) structure that provides information about the message.<br/>                                                                                                                                                          |



 

</dd> </dl>

## Return value

If the callback function processes this transaction, it should return 0.

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                   |
| Header<br/>                   | <dl> <dt>Ddeml.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**DdeAccessData**](ddeaccessdata.md)
</dt> <dt>

[**DdeInitialize**](ddeinitialize.md)
</dt> <dt>

[**DdeUninitialize**](ddeuninitialize.md)
</dt> <dt>

[**MONCBSTRUCT**](moncbstruct-str.md)
</dt> <dt>

[**MONCONVSTRUCT**](monconvstruct-str.md)
</dt> <dt>

[**MONERRSTRUCT**](monerrstruct-str.md)
</dt> <dt>

[**MONHSZSTRUCT**](monhszstruct-str.md)
</dt> <dt>

[**MONLINKSTRUCT**](monlinkstruct-str.md)
</dt> <dt>

[**MONMSGSTRUCT**](monmsgstruct-str.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Dynamic Data Exchange Management Library](dynamic-data-exchange-management-library.md)
</dt> </dl>

 

 





