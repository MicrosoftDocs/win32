---
description: 'Displays a dialog box that allows a user to select a certificate.'
ms.assetid: '242c19a7-179b-4fc0-a050-a1b598566a6b'
title: CryptUIDlgSelectCertificate function
ms.topic: reference
ms.date: 05/29/2020
---

# CryptUIDlgSelectCertificate function

The **CryptUIDlgSelectCertificate** function displays a dialog box that allows a user to select a certificate.

## Syntax


```C++
PCCERT_CONTEXT WINAPI CryptUIDlgSelectCertificate(
  _In_  PCCRYPTUI_SELECTCERTIFICATE_STRUCT pcsc
);
```



## Parameters

<dl> <dt>

*pcsc* \[in\]
</dt> <dd>

A pointer to a [**CRYPTUI\_SELECTCERTIFICATE\_STRUCT**](cryptui-selectcertificate-struct.md) structure that contains information about the dialog box to display.

</dd> </dl>

## Return value

A pointer to a [**CERT\_CONTEXT**](/windows/win32/api/Wincrypt/ns-wincrypt-cert_context) structure that represents the certificate selected by the user. When you have finished using this certificate, you must pass this pointer to the [**CertFreeCertificateContext**](/windows/win32/api/wincrypt/nf-wincrypt-certfreecertificatecontext) function to decrement the reference count of the certificate context.

If the **dwFlags** member of the *pcsc* structure does not contain the **CRYPTUI\_SELECTCERT\_MULTISELECT** flag, a return value of **NULL** means that the user closed the dialog box without selecting a certificate.

If the **dwFlags** member of the *pcsc* structure does contain the **CRYPTUI\_SELECTCERT\_MULTISELECT** flag, this function always returns **NULL**. The selected certificates will be contained in the certificate store that is represented by the **hSelectedCertStore** member of *pcsc*. If the number of certificates in the store is the same before and after calling **CryptUIDlgSelectCertificate**, the user closed the dialog box without selecting any certificates.

## Remarks

If the **dwFlags** member of the [**CRYPTUI\_SELECTCERTIFICATE\_STRUCT**](cryptui-selectcertificate-struct.md) structure is set to **CRYPTUI\_SELECTCERT\_LEGACY**, the legacy dialog is displayed. Otherwise, the current certificate selection dialog is displayed.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows�XP \[desktop apps only\]<br/>                                                       |
| Minimum supported server<br/> | Windows Server�2003 \[desktop apps only\]<br/>                                              |
| End of support<br/> | Windows�7 \[desktop apps only\]<br/>                                                       |
| Library<br/>                  | <dl> <dt>Cryptui.lib</dt> </dl>            |
| DLL<br/>                      | <dl> <dt>Cryptui.dll</dt> </dl>            |
| Unicode and ANSI names<br/>   | **CryptUIDlgSelectCertificateW** (Unicode) and **CryptUIDlgSelectCertificateA** (ANSI)<br/> |



## See also

<dl> <dt>

[**CRYPTUI\_SELECTCERTIFICATE\_STRUCT**](cryptui-selectcertificate-struct.md)
</dt> </dl>






