---
description: A user-defined callback function that allows the caller of the CryptUIDlgSelectCertificate function to handle the display of certificates that the user selects to view.
ms.assetid: fdb9e9e0-02f1-42e0-9a11-204d916a1a88
title: PFNCCERTDISPLAYPROC callback function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PFNCCERTDISPLAYPROC
api_type: 
- UserDefined
api_location: 
---

# PFNCCERTDISPLAYPROC callback function

The **PFNCCERTDISPLAYPROC** function is a user-defined callback function that allows the caller of the [**CryptUIDlgSelectCertificate**](cryptuidlgselectcertificate.md) function to handle the display of certificates that the user selects to view.

## Syntax


```C++
BOOL WINAPI * PFNCCERTDISPLAYPROC(
  _In_ PCCERT_CONTEXT pCertContext,
  _In_ HWND           hWndSelCertDlg,
  _In_ void           *pvCallbackData
);
```



## Parameters

<dl> <dt>

*pCertContext* \[in\]
</dt> <dd>

A pointer to a [**CERT\_CONTEXT**](/windows/desktop/api/Wincrypt/ns-wincrypt-cert_context) structure that represents the certificate to display.

</dd> <dt>

*hWndSelCertDlg* \[in\]
</dt> <dd>

A handle to the dialog box from which the certificate was selected for viewing.

</dd> <dt>

*pvCallbackData* \[in\]
</dt> <dd>

Additional data used by the callback function.

</dd> </dl>

## Return value

This function returns **TRUE** to indicate that it handles display of the certificate and that the dialog box should not display the certificate. If this function returns **FALSE**, the dialog box displays the certificate.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |



 

 




