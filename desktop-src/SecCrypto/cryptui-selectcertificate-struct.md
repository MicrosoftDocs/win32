---
description: Contains information about the dialog box displayed by the CryptUIDlgSelectCertificate function.
ms.assetid: 073a67a0-427b-4b81-82a0-1bb0a216a335
title: CRYPTUI_SELECTCERTIFICATE_STRUCT structure
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CRYPTUI_SELECTCERTIFICATE_STRUCT
- CRYPTUI_SELECTCERTIFICATE_STRUCTA
- CRYPTUI_SELECTCERTIFICATE_STRUCTW
api_type: 
- NA
api_location: 
---

# CRYPTUI\_SELECTCERTIFICATE\_STRUCT structure

The **CRYPTUI\_SELECTCERTIFICATE\_STRUCT** structure contains information about the dialog box displayed by the [**CryptUIDlgSelectCertificate**](cryptuidlgselectcertificate.md) function.

## Syntax


```C++
typedef struct _CRYPTUI_SELECTCERTIFICATE_STRUCT {
  DWORD               dwSize;
  HWND                hwndParent;
  DWORD               dwFlags;
  LPCTSTR             szTitle;
  DWORD               dwDontUseColumn;
  LPCTSTR             szDisplayString;
  PFNCFILTERPROC      pFilterCallback;
  PFNCCERTDISPLAYPROC pDisplayCallback;
  void                *pvCallbackData;
  DWORD               cDisplayStores;
  HCERTSTORE          *rghDisplayStores;
  DWORD               cStores;
  HCERTSTORE          *rghStores;
  DWORD               cPropSheetPages;
  LPCPROPSHEETPAGE    rgPropSheetPages;
  HCERTSTORE          hSelectedCertStore;
} CRYPTUI_SELECTCERTIFICATE_STRUCT, *PCRYPTUI_SELECTCERTIFICATE_STRUCT;
```



## Members

<dl> <dt>

**dwSize**
</dt> <dd>

The size, in bytes, of this structure.

</dd> <dt>

**hwndParent**
</dt> <dd>

The handle of the parent window of the dialog box. If this value is **NULL**, the parent window is the default desktop window.

</dd> <dt>

**dwFlags**
</dt> <dd>

Specifies additional options for the [**CryptUIDlgSelectCertificate**](cryptuidlgselectcertificate.md) function. This can be zero or a bitwise **OR** of the following values.



| Value                                                                                                                                                                                                                                    | Meaning                                                                                                                                                                                                                                                                                                                                                                              |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="CRYPTUI_SELECTCERT_ADDFROMDS"></span><span id="cryptui_selectcert_addfromds"></span><dl> <dt>**CRYPTUI\_SELECTCERT\_ADDFROMDS**</dt> </dl>                              | Reserved.<br/>                                                                                                                                                                                                                                                                                                                                                                 |
| <span id="CRYPTUI_SELECTCERT_LEGACY"></span><span id="cryptui_selectcert_legacy"></span><dl> <dt>**CRYPTUI\_SELECTCERT\_LEGACY**</dt> </dl>                                       | Specifies that the legacy dialog is to be displayed.<br/>                                                                                                                                                                                                                                                                                                                      |
| <span id="CRYPTUI_SELECTCERT_MULTISELECT"></span><span id="cryptui_selectcert_multiselect"></span><dl> <dt>**CRYPTUI\_SELECTCERT\_MULTISELECT**</dt> </dl>                        | Allows the user to select more than one certificate in the dialog box. If this flag is set, the [**CryptUIDlgSelectCertificate**](cryptuidlgselectcertificate.md) function always returns **NULL**. The **hSelectedCertStore** member of this structure must contain a handle to a certificate store. The certificates selected by the user will be added to this store.<br/> |
| <span id="CRYPTUI_SELECTCERT_PUT_WINDOW_TOPMOST"></span><span id="cryptui_selectcert_put_window_topmost"></span><dl> <dt>**CRYPTUI\_SELECTCERT\_PUT\_WINDOW\_TOPMOST**</dt> </dl> | Forces the cryptography UI to be the top window on the screen.<br/>                                                                                                                                                                                                                                                                                                            |



 

</dd> <dt>

**szTitle**
</dt> <dd>

The display title for the dialog box. If the value of this member is **NULL**, the default title of "Select Certificate" is used.

</dd> <dt>

**dwDontUseColumn**
</dt> <dd>

Flags that can be combined to exclude columns of the display.



| Value                                                                                                                                                                                                                                                                                       | Meaning                                                |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| <span id="CRYPTUI_SELECT_ISSUEDTO_COLUMN"></span><span id="cryptui_select_issuedto_column"></span><dl> <dt>**CRYPTUI\_SELECT\_ISSUEDTO\_COLUMN**</dt> <dt>1 (0x1)</dt> </dl>             | Do not display **ISSUEDTO** information.<br/>    |
| <span id="CRYPTUI_SELECT_ISSUEDBY_COLUMN"></span><span id="cryptui_select_issuedby_column"></span><dl> <dt>**CRYPTUI\_SELECT\_ISSUEDBY\_COLUMN**</dt> <dt>2 (0x2)</dt> </dl>             | Do not display **ISSUEDBY** information.<br/>    |
| <span id="CRYPTUI_SELECT_INTENDEDUSE_COLUMN"></span><span id="cryptui_select_intendeduse_column"></span><dl> <dt>**CRYPTUI\_SELECT\_INTENDEDUSE\_COLUMN**</dt> <dt>4 (0x4)</dt> </dl>    | Do not display **IntendedUse** information.<br/> |
| <span id="CRYPTUI_SELECT_FRIENDLYNAME_COLUMN"></span><span id="cryptui_select_friendlyname_column"></span><dl> <dt>**CRYPTUI\_SELECT\_FRIENDLYNAME\_COLUMN**</dt> <dt>8 (0x8)</dt> </dl> | Do not display name information.<br/>            |
| <span id="CRYPTUI_SELECT_LOCATION_COLUMN"></span><span id="cryptui_select_location_column"></span><dl> <dt>**CRYPTUI\_SELECT\_LOCATION\_COLUMN**</dt> <dt>16 (0x10)</dt> </dl>           | Do not display location information.<br/>        |
| <span id="CRYPTUI_SELECT_EXPIRATION_COLUMN"></span><span id="cryptui_select_expiration_column"></span><dl> <dt>**CRYPTUI\_SELECT\_EXPIRATION\_COLUMN**</dt> <dt>32 (0x20)</dt> </dl>     | Do not display expiration information.<br/>      |



 

</dd> <dt>

**szDisplayString**
</dt> <dd>

Text that is displayed in the dialog box to instruct the user. If the value of this member is **NULL**, the default string "Select a certificate you want to use" is used.

</dd> <dt>

**pFilterCallback**
</dt> <dd>

A pointer to a [**PFNCFILTERPROC**](/windows/desktop/api/Cryptuiapi/nc-cryptuiapi-pfncfilterproc) callback function that filters the certificates that are displayed in the dialog box.

</dd> <dt>

**pDisplayCallback**
</dt> <dd>

A pointer to a [**PFNCCERTDISPLAYPROC**](pfnccertdisplayproc.md) callback function that displays certificates that the user selects to view.

</dd> <dt>

**pvCallbackData**
</dt> <dd>

Additional data that is passed to the callback functions specified by the **pFilterCallback** and **pDisplayCallback** members.

</dd> <dt>

**cDisplayStores**
</dt> <dd>

The number of certificate stores in the **rghDisplayStores** array.

</dd> <dt>

**rghDisplayStores**
</dt> <dd>

A pointer to an array of stores that contain certificates available for selection in the dialog box.

</dd> <dt>

**cStores**
</dt> <dd>

The number of certificate stores in the **rghStores** array.

</dd> <dt>

**rghStores**
</dt> <dd>

A pointer to an array of certificate stores to search when building a certificate chain and verifying trust for the certificates displayed in the dialog box.

</dd> <dt>

**cPropSheetPages**
</dt> <dd>

The number of property pages in the **rgPropSheetPages** array.

</dd> <dt>

**rgPropSheetPages**
</dt> <dd>

A pointer to an array of **PROPSHEETPAGE** structures that represent property pages that are passed to the certificate viewing dialog box when a certificate is selected for viewing.

</dd> <dt>

**hSelectedCertStore**
</dt> <dd>

A handle to a certificate store created by the caller. The certificates selected by the user are added to this store. If the number of certificates in this store is the same before and after calling [**CryptUIDlgSelectCertificate**](cryptuidlgselectcertificate.md), the user closed the dialog box without selecting any certificates.

This member is not used if the **dwFlags** member of this structure does not contain the **CRYPTUI\_SELECTCERT\_MULTISELECT** flag.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                            |
| Unicode and ANSI names<br/>   | **CRYPTUI\_SELECTCERTIFICATE\_STRUCTW** (Unicode) and **CRYPTUI\_SELECTCERTIFICATE\_STRUCTA** (ANSI)<br/> |



## See also

<dl> <dt>

[**CryptUIDlgSelectCertificate**](cryptuidlgselectcertificate.md)
</dt> </dl>

 

 




