---
description: Contains information for the CryptUIDlgViewSignerInfo function.
ms.assetid: 2b76de4f-4b35-477e-a67e-435434e066c6
title: CRYPTUI_VIEWSIGNERINFO_STRUCT structure
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CRYPTUI_VIEWSIGNERINFO_STRUCT
- CRYPTUI_VIEWSIGNERINFO_STRUCTA
- CRYPTUI_VIEWSIGNERINFO_STRUCTW
api_type: 
- NA
api_location: 
---

# CRYPTUI\_VIEWSIGNERINFO\_STRUCT structure

\[The **CRYPTUI\_VIEWSIGNERINFO\_STRUCT** structure is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

The **CRYPTUI\_VIEWSIGNERINFO\_STRUCT** structure contains information for the [**CryptUIDlgViewSignerInfo**](cryptuidlgviewsignerinfo.md) function.

> [!Note]  
> This structure is not declared in a published header file. To use this structure, declare it in the exact format shown.

 

## Syntax


```C++
typedef struct tagCRYPTUI_VIEWSIGNERINFO_STRUCT {
  DWORD            dwSize;
  HWND             hwndParent;
  DWORD            dwFlags;
  LPCTSTR          szTitle;
  CMSG_SIGNER_INFO *pSignerInfo;
  HCRYPTMSG        hMsg;
  LPCSTR           pszOID;
  DWORD_PTR        dwReserved;
  DWORD            cStores;
  HCERTSTORE       *rghStores;
  DWORD            cPropSheetPages;
  LPCPROPSHEETPAGE rgPropSheetPages;
} CRYPTUI_VIEWSIGNERINFO_STRUCT, *PCRYPTUI_VIEWSIGNERINFO_STRUCT;
```



## Members

<dl> <dt>

**dwSize**
</dt> <dd>

The size, in bytes, of this structure.

</dd> <dt>

**hwndParent**
</dt> <dd>

The handle of the window to be the parent of the dialog box. This member can be **NULL** if the dialog box should have no parent.

</dd> <dt>

**dwFlags**
</dt> <dd>

A set of flags that modifies the behavior of the [**CryptUIDlgViewSignerInfo**](cryptuidlgviewsignerinfo.md) function. There are no flags currently defined, so this member must be zero.

</dd> <dt>

**szTitle**
</dt> <dd>

A pointer to a null-terminated string that contains the title to be displayed in the dialog box. If this member is **NULL**, a default title is used.

</dd> <dt>

**pSignerInfo**
</dt> <dd>

A pointer to a [**CMSG\_SIGNER\_INFO**](/windows/desktop/api/Wincrypt/ns-wincrypt-cmsg_signer_info) structure that contains the signer information to display.

</dd> <dt>

**hMsg**
</dt> <dd>

The handle of the message that the signer information was extracted from.

</dd> <dt>

**pszOID**
</dt> <dd>

A pointer to a null-terminated ANSI string that contains the string representation of the [*object identifier*](../secgloss/o-gly.md) (OID) that signifies what the certificate that did the signing should be validated for. For example, if this is being called to view the signature of a [*certificate trust list*](../secgloss/c-gly.md) (CTL), the **szOID\_KP\_CTL\_USAGE\_SIGNING** OID string should be passed in. If this member is **NULL**, the certificate is not validated for usages.

</dd> <dt>

**dwReserved**
</dt> <dd>

This parameter is not currently used. This member must be **NULL**.

</dd> <dt>

**cStores**
</dt> <dd>

The number of elements in the **rghStores** array.

</dd> <dt>

**rghStores**
</dt> <dd>

An array of **HCERTSTORE** values that represent the other certificate stores to search for the certificate that signed the message. If this member is **NULL**, no additional stores are searched. The **cStores** member contains the number of elements in this array.

</dd> <dt>

**cPropSheetPages**
</dt> <dd>

The number of elements in the **rgPropSheetPages** array.

</dd> <dt>

**rgPropSheetPages**
</dt> <dd>

An array of [**PROPSHEETPAGE**](/windows/win32/api/prsht/ns-prsht-propsheetpagea_v2) structure pointers that define any extra pages to display in the standard dialog box. If this member is **NULL**, no additional pages will be displayed. The **cPropSheetPages** member contains the number of elements in this array.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                      |
| Unicode and ANSI names<br/>   | **CRYPTUI\_VIEWSIGNERINFO\_STRUCTW** (Unicode) and **CRYPTUI\_VIEWSIGNERINFO\_STRUCTA** (ANSI)<br/> |



## See also

<dl> <dt>

[**CryptUIDlgViewSignerInfo**](cryptuidlgviewsignerinfo.md)
</dt> </dl>

 

 
