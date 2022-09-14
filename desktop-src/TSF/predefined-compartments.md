---
title: Predefined Compartments (Ctffunc.h)
description: The following values identify compartments implemented by Text Services Framework.
ms.assetid: 65177979-ff91-4f62-8ba5-3c426b221b6c
keywords:
- Predefined Compartments Text Services Framework
topic_type:
- apiref
api_name:
- Predefined Compartments
api_location:
- Ctffunc.h
- Mstctf.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Predefined Compartments

The following values identify compartments implemented by Text Services Framework.

The following compartment identifiers are defined in Ctffunc.idl and Ctffunc.h.



| Flag                                     | Value  | Description                                                                                                                                                                                                                                                                               |
|------------------------------------------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GUID\_COMPARTMENT\_SAPI\_AUDIO           | VT\_I4 | A **DWORD** that is zero if the Speech API (SAPI) audio is off or nonzero if the SAPI audio is on. This compartment is specific to a thread manager object.                                                                                                                               |
| GUID\_COMPARTMENT\_SPEECH\_CFGMENU       | VT\_I4 | A **DWORD** that is zero if the speech configuration menu is unavailable or nonzero if the speech configuration menu is available. This compartment is specific to a thread manager object.                                                                                               |
| GUID\_COMPARTMENT\_SPEECH\_DICTATIONSTAT | VT\_I4 | A **DWORD** value that contains zero or a combination of one or more of the [**TF\_DICTATION\_ENABLED**](speech-recognition-constants.md), **TF\_COMMANDING\_ENABLED**, **TF\_DICTATION\_ON** or **TF\_COMMANDING\_ON** values. This compartment is specific to a thread manager object. |
| GUID\_COMPARTMENT\_SPEECH\_UI\_STATUS    | VT\_I4 | A **DWORD** value that contains zero or a combination of one or more of the [**TF\_SHOW\_BALLOON**](speech-recognition-constants.md) or **TF\_DISABLE\_BALLOON** values. This is a global compartment.                                                                                   |



 

The following compartment identifiers are defined in MSCTF.IDL and MSCTF.H.



| Flag                                                    | Value  | Description                                                                                                                                                                                                                                                   |
|---------------------------------------------------------|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GUID\_COMPARTMENT\_EMPTYCONTEXT                         | VT\_I4 | A **DWORD** that is nonzero if the context is empty or zero otherwise. This compartment is specific to a context object.                                                                                                                                      |
| GUID\_COMPARTMENT\_HANDWRITING\_OPENCLOSE               | VT\_I4 | A **DWORD** that is nonzero if the handwriting recognition is open or zero if the handwriting recognition is closed. This compartment is specific to a thread manager object.                                                                                 |
| GUID\_COMPARTMENT\_KEYBOARD\_DISABLED                   | VT\_I4 | A **DWORD** that is nonzero if the keyboard is disabled or zero otherwise. This compartment is specific to a context object.                                                                                                                                  |
| GUID\_COMPARTMENT\_KEYBOARD\_INPUTMODE\_CONVERSION      | VT\_I4 | A **DWORD** value of the proper combination of [**TF\_CONVERSIONMODE\_**](flags-for-conversion-mode.md) flags. This compartment is specific to a thread manager object.                                                                                      |
| GUID\_COMPARTMENT\_KEYBOARD\_INPUTMODE\_SENTENCE        | VT\_I4 | A **DWORD** value of [**TF\_SENTENCEMODE\_**](flags-for-conversion-mode.md). This compartment is specific to a thread manager object.                                                                                                                        |
| GUID\_COMPARTMENT\_KEYBOARD\_OPENCLOSE                  | VT\_I4 | A **DWORD** that is nonzero if the keyboard is open or zero if the keyboard is closed. This compartment is specific to a thread manager object.                                                                                                               |
| GUID\_COMPARTMENT\_PERSISTMENUENABLED                   | VT\_I4 | A **DWORD** that is nonzero to cause the speech text service to enable the **Save Speech Data** menu item or zero to disable it. This compartment is specific to a document manager object.                                                                   |
| GUID\_COMPARTMENT\_SPEECH\_DISABLED                     | VT\_I4 | A **DWORD** that contains zero or a combination of one or more of the [**TF\_DISABLE\_SPEECH**](speech-recognition-constants.md), **TF\_DISABLE\_DICTATION** or **TF\_DISABLE\_COMMANDING** values. This compartment is specific to a thread manager object. |
| GUID\_COMPARTMENT\_SPEECH\_OPENCLOSE                    | VT\_I4 | A **DWORD** that is nonzero if speech input is active or zero if speech input is inactive. This is a global compartment.                                                                                                                                      |
| GUID\_COMPARTMENT\_TIPUISTATUS                          | VT\_I4 | Not currently used.                                                                                                                                                                                                                                           |
| GUID\_COMPARTMENT\_TRANSITORYEXTENSION                  | VT\_I4 | A **DWORD** value of [**TF\_TRANSITORYEXTENSION\_NONE**](values-for-guid-compartment-transitoryextension.md), **TF\_TRANSITORYEXTENSION\_FLOATING** or **TF\_TRANSITORYEXTENSION\_ATSELECTION**. This compartment is specific to a document manager object.  |
| GUID\_COMPARTMENT\_TRANSITORYEXTENSION\_DOCUMENTMANAGER | VT\_I4 | An IUnknown value for the [**ITfDocumentMgr**](/windows/desktop/api/Msctf/nn-msctf-itfdocumentmgr) interface that refers the transitory document of this document manager. This compartment is specific to a document manager object.                                                         |
| GUID\_COMPARTMENT\_TRANSITORYEXTENSION\_PARENT          | VT\_I4 | An IUnknown value for the [**ITfDocumentMgr**](/windows/desktop/api/Msctf/nn-msctf-itfdocumentmgr) interface that refers the parent document manager of this transitory document. This compartment is specific to a document manager object.                                                  |



 

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                                                                     |
| Redistributable<br/>          | TSF 1.0 on Windows 2000 Professional<br/>                                                                                                          |
| Header<br/>                   | <dl> <dt>Ctffunc.h; </dt> <dt>Mstctf.h</dt> </dl>     |
| IDL<br/>                      | <dl> <dt>Ctffunc.idl; </dt> <dt>Mstctf.idl</dt> </dl> |



## See also

<dl> <dt>

[**Speech Recognition Constants**](speech-recognition-constants.md)
</dt> </dl>

 

 





