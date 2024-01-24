---
description: The following table lists all HRESULT values that can be returned by the methods in the XPS Digital Signature API.
ms.assetid: d20707b0-55ea-438a-8ce3-972c61678928
title: XPS Digital Signature API Errors (Xpsdigitalsignature.h)
ms.topic: reference
ms.date: 05/31/2018
---

# XPS Digital Signature API Errors

The following table lists all **HRESULT** values that can be returned by the methods in the XPS Digital Signature API. Note that not every method can return every return value listed in this table.



| Return code/value                                                                                                                                                                                                                                                                                  | Description                                                                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="S_OK"></span><span id="s_ok"></span><dl> <dt>**S\_OK**</dt> </dl>                                                                                                                                                                 | The method succeeded.<br/>                                                                                                                                                  |
| <span id="XPS_E_INVALID_SIGNATUREBLOCK_MARKUP"></span><span id="xps_e_invalid_signatureblock_markup"></span><dl> <dt>**XPS\_E\_INVALID\_SIGNATUREBLOCK\_MARKUP**</dt> <dt>0x8052038b</dt> </dl> | Encountered an error in the XML markup of the signature block while the signature markup was being read.<br/>                                                               |
| <span id="XPS_E_MARKUP_COMPATIBILITY_ELEMENTS"></span><span id="xps_e_markup_compatibility_elements"></span><dl> <dt>**XPS\_E\_MARKUP\_COMPATIBILITY\_ELEMENTS**</dt> <dt>0x80520389</dt> </dl> | The [**XPS\_SIGN\_FLAGS**](/windows/win32/api/xpsdigitalsignature/ne-xpsdigitalsignature-xps_sign_flags) value specified that no markup compatibility elements were expected; however, markup compatibility elements were found.<br/> |
| <span id="XPS_E_OBJECT_DETACHED"></span><span id="xps_e_object_detached"></span><dl> <dt>**XPS\_E\_OBJECT\_DETACHED**</dt> <dt>0x8052038a</dt> </dl>                                            | The interface is not associated with the signature manager.<br/>                                                                                                            |
| <span id="XPS_E_PACKAGE_ALREADY_OPENED"></span><span id="xps_e_package_already_opened"></span><dl> <dt>**XPS\_E\_PACKAGE\_ALREADY\_OPENED**</dt> <dt>0x80520387</dt> </dl>                      | An XPS package has already been opened in the signature manager. <br/>                                                                                                      |
| <span id="XPS_E_PACKAGE_NOT_OPENED"></span><span id="xps_e_package_not_opened"></span><dl> <dt>**XPS\_E\_PACKAGE\_NOT\_OPENED**</dt> <dt>0x80520386</dt> </dl>                                  | An XPS package has not yet been opened in the signature manager. <br/>                                                                                                      |
| <span id="XPS_E_SIGNATUREID_DUP"></span><span id="xps_e_signatureid_dup"></span><dl> <dt>**XPS\_E\_SIGNATUREID\_DUP**</dt> <dt>0x80520388</dt> </dl>                                            | Two or more signatures have the same ID.<br/>                                                                                                                               |
| <span id="XPS_E_SIGREQUESTID_DUP"></span><span id="xps_e_sigrequestid_dup"></span><dl> <dt>**XPS\_E\_SIGREQUESTID\_DUP**</dt> <dt>0x80520385</dt> </dl>                                         | The signature request ID is not unique within the signature block.<br/>                                                                                                     |



 

## Remarks

Some XPS digital signature API methods make calls to the [Packaging](/previous-versions/windows/desktop/opc/packaging) API. For information about the Packaging API return values, see [Packaging Errors](/previous-versions/windows/desktop/opc/packaging-errors).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                         |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                            |
| Header<br/>                   | <dl> <dt>Xpsdigitalsignature.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>XpsDigitalSignature.idl</dt> </dl> |



## See also

<dl> <dt>

[Error Handling in COM](../com/error-handling-in-com.md)
</dt> <dt>

[Packaging Errors](/previous-versions/windows/desktop/opc/packaging-errors)
</dt> <dt>

[Cryptography Return Values](/windows/desktop/SecCrypto/cryptography-return-values)
</dt> </dl>

 

